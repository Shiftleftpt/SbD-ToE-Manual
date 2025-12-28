#!/usr/bin/env python3
"""
Suggest canonical tags for documents using semantic similarity matching.

This script uses:
1. Chroma embeddings for RAG retrieval
2. YAML canonical tags database (with aliases, descriptions, labels)
3. Ollama/Mistral LLM for semantic analysis
4. Embedding-based similarity matching to recommend canonical tags

The process:
1. Extract content from document chunk
2. Generate keyword suggestions using LOCAL or OLLAMA
3. For each suggestion, find most similar canonical tag using embeddings
4. Return canonical tags with confidence scores
"""

import json
import yaml
import argparse
import sys
import os
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
import logging

import numpy as np
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import RAG configuration
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
import rag_core.config as rag_config

@dataclass
class CanonicalTag:
    """Represents a canonical tag from the YAML database"""
    id: str
    label: str
    description: str
    aliases: List[str]
    embedding: Optional[np.ndarray] = None


@dataclass
class TagSuggestion:
    """Represents a tag suggestion with confidence"""
    canonical_id: str
    canonical_label: str
    confidence: float
    match_reason: str


def load_canonical_tags(tags_file: Path) -> Dict[str, CanonicalTag]:
    """Load canonical tags from YAML file"""
    with open(tags_file, 'r', encoding='utf-8') as f:
        tags_data = yaml.safe_load(f)
    
    canonical_tags = {}
    for tag_id, tag_info in tags_data.items():
        canonical_tags[tag_id] = CanonicalTag(
            id=tag_id,
            label=tag_info.get('label', tag_id),
            description=tag_info.get('description', ''),
            aliases=tag_info.get('aliases', [])
        )
    
    return canonical_tags


def load_embeddings_cache(cache_file: Path) -> Dict[str, np.ndarray]:
    """Load pre-computed embeddings from cache file"""
    with open(cache_file, 'r', encoding='utf-8') as f:
        cache_data = json.load(f)
    
    embeddings = {}
    for tag_id, tag_data in cache_data.items():
        embeddings[tag_id] = {
            'embedding': np.array(tag_data['embedding']),
            'label': tag_data['label'],
            'description': tag_data['description'],
            'aliases': tag_data['aliases']
        }
    
    return embeddings


def extract_keywords_local(
    content: str,
    top_n: int = 15
) -> List[str]:
    """Extract keywords using local frequency-based analysis"""
    import re
    from collections import Counter
    
    # Clean and tokenize
    words = re.findall(r'\b\w+\b', content.lower())
    
    # Filter stop words (Portuguese + English)
    stop_words = {
        'o', 'a', 'de', 'da', 'do', 'em', 'e', 'é', 'ou', 'para', 'por',
        'que', 'um', 'uma', 'os', 'as', 'dos', 'das', 'no', 'na', 'nos', 'nas',
        'the', 'a', 'an', 'and', 'or', 'in', 'on', 'at', 'to', 'of', 'is', 'be',
        'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these',
        'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
        'who', 'when', 'where', 'why', 'how', 'as', 'if', 'with', 'from'
    }
    
    # Count word frequencies (excluding short words and stop words)
    word_counts = Counter(
        w for w in words 
        if len(w) > 3 and w not in stop_words
    )
    
    return [word for word, _ in word_counts.most_common(top_n)]


def suggest_tags_ollama(content: str) -> List[str]:
    """Get tag suggestions from Ollama/Mistral"""
    
    prompt = f"""Analyze the following content and suggest 10-15 relevant security/documentation tags.
Return ONLY a JSON array of tag strings, no markdown, no explanation.
Tags should be specific, relevant keywords that describe the content.

Content:
{content[:1000]}

Return only valid JSON array like: ["tag1", "tag2", ...]
"""
    
    try:
        response = requests.post(
            f"{rag_config.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False,
                "temperature": 0.3
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            response_text = result.get('response', '').strip()
            
            # Try to extract JSON array
            try:
                tags = json.loads(response_text)
                return tags if isinstance(tags, list) else []
            except json.JSONDecodeError:
                # Fallback: try to extract any quoted strings
                import re
                matches = re.findall(r'"([^"]+)"', response_text)
                return matches[:15]
    except Exception as e:
        logger.warning(f"Ollama error: {e}")
    
    return []


def match_keywords_to_canonical(
    keywords: List[str],
    embeddings_cache: Dict[str, Dict],
    embedding_fn: SentenceTransformerEmbeddingFunction,
    threshold: float = 0.3
) -> List[TagSuggestion]:
    """
    Match extracted keywords to canonical tags using semantic similarity.
    
    For each keyword, find the most similar canonical tag based on embeddings.
    """
    suggestions = []
    matched_tag_ids = set()  # Track to avoid duplicates
    
    for keyword in keywords:
        # Get embedding for keyword
        keyword_embedding = np.array(embedding_fn([keyword])[0])
        
        # Calculate similarity to all canonical tags
        best_match = None
        best_similarity = 0
        best_reason = ""
        
        for tag_id, tag_data in embeddings_cache.items():
            tag_embedding = tag_data['embedding']
            
            # Cosine similarity
            similarity = np.dot(keyword_embedding, tag_embedding) / (
                np.linalg.norm(keyword_embedding) * np.linalg.norm(tag_embedding) + 1e-10
            )
            
            # Also check for exact/fuzzy alias matches
            keyword_lower = keyword.lower()
            alias_match = False
            
            if keyword_lower == tag_id.lower():
                similarity = 1.0
                alias_match = True
            elif any(alias.lower() == keyword_lower for alias in tag_data['aliases']):
                similarity = 0.95
                alias_match = True
            elif any(keyword_lower in alias.lower() for alias in tag_data['aliases']):
                similarity = min(0.85, similarity + 0.2)
                alias_match = True
            
            # Track best match above threshold
            if similarity > best_similarity and similarity > threshold:
                best_similarity = similarity
                best_match = tag_id
                best_reason = "Exact alias match" if alias_match else "Semantic similarity"
        
        # Add suggestion if found and not already suggested
        if best_match and best_match not in matched_tag_ids:
            tag_data = embeddings_cache[best_match]
            suggestions.append(TagSuggestion(
                canonical_id=best_match,
                canonical_label=tag_data['label'],
                confidence=round(best_similarity, 3),
                match_reason=best_reason
            ))
            matched_tag_ids.add(best_match)
    
    # Sort by confidence
    suggestions.sort(key=lambda x: x.confidence, reverse=True)
    
    return suggestions[:12]  # Limit to 12 suggestions


def analyze_document_for_canonical_tags(
    chapter: str,
    subfolder: Optional[str] = None,
    use_ollama: bool = True,
    threshold: float = 0.3
) -> Dict:
    """Analyze documents in a chapter and suggest canonical tags"""
    
    # Load embeddings cache
    cache_file = Path(__file__).parent / 'data' / 'canonical-tags-embeddings.json'
    if not cache_file.exists():
        logger.error(f"❌ Embeddings cache not found: {cache_file}")
        logger.error("Run: python3 generate_canonical_embeddings.py")
        return {}
    
    embeddings_cache = load_embeddings_cache(cache_file)
    logger.info(f"✅ Loaded {len(embeddings_cache)} canonical tag embeddings from cache")
    
    # Initialize embedding function (for keywords)
    embedding_fn = SentenceTransformerEmbeddingFunction(
        model_name=rag_config.EMBEDDING_MODEL
    )
    
    # Load Chroma index
    try:
        import chromadb
        chroma_client = chromadb.PersistentClient(path=str(rag_config.INDEX_DIR / "chroma"))
        # Don't provide embedding function - use the one already persisted in collection
        collection = chroma_client.get_collection(name="manual")
        logger.info(f"✅ Chroma index loaded ({collection.count()} documents)")
    except Exception as e:
        logger.error(f"❌ Failed to load Chroma index: {e}")
        return {}
    
    # Build query filter
    # Try exact match first, then with suffix
    where_filter = {"chapter": {"$in": [chapter, f"{chapter}-normativo", f"{chapter}-manual"]}}
    
    # Get documents
    try:
        results = collection.get(where=where_filter, limit=10000, include=['documents', 'metadatas'])
        documents = results['documents']
        metadatas = results['metadatas']
        
        logger.info(f"📄 Found {len(documents)} documents in {chapter}")
        if subfolder:
            logger.info(f"📁 Subfolder filter: {subfolder}")
    except Exception as e:
        logger.error(f"❌ Failed to query Chroma: {e}")
        return {}
    
    # Check Ollama availability
    ollama_available = use_ollama
    try:
        requests.get(f"{rag_config.OLLAMA_BASE_URL}/api/tags", timeout=5)
        logger.info("✅ Ollama/Mistral available")
    except:
        ollama_available = False
        logger.warning("⚠️  Ollama unavailable - using LOCAL only")
    
    # Analyze each document
    analysis_results = []
    
    for i, (content, metadata) in enumerate(zip(documents[:50], metadatas[:50])):
        logger.info(f"\n[{i+1}/{min(50, len(documents))}] {metadata.get('title', 'Unknown')} ✅")
        
        # Extract keywords using both methods
        local_keywords = extract_keywords_local(content, top_n=15)
        
        ollama_keywords = []
        if ollama_available:
            ollama_keywords = suggest_tags_ollama(content)
        
        # Combine keywords
        combined_keywords = list(set(local_keywords + ollama_keywords))
        
        # Match to canonical tags
        canonical_suggestions = match_keywords_to_canonical(
            combined_keywords,
            embeddings_cache,
            embedding_fn,
            threshold=threshold
        )
        
        # Build result
        result = {
            'file_path': metadata.get('file_path', ''),
            'title': metadata.get('title', ''),
            'original_tags': metadata.get('tags', []),
            'extracted_keywords': {
                'local': local_keywords[:10],
                'ollama': ollama_keywords[:10]
            },
            'canonical_suggestions': [asdict(s) for s in canonical_suggestions]
        }
        
        analysis_results.append(result)
        
        # Print summary
        print(f"\n    Original Tags: {', '.join(result['original_tags'][:5])}")
        print(f"    Canonical Suggestions:")
        for j, sugg in enumerate(canonical_suggestions[:5], 1):
            print(f"      {j}. {sugg.canonical_label} ({sugg.confidence:.2%}) - {sugg.match_reason}")
    
    # Save results
    output_file = Path(__file__).parent / 'reports' / f'canonical_{chapter}.json'
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, indent=2, ensure_ascii=False)
    
    logger.info(f"\n✅ Report saved: {output_file}")
    
    return {
        'chapter': chapter,
        'subfolder': subfolder,
        'documents_analyzed': len(analysis_results),
        'canonical_tags_loaded': len(embeddings_cache),
        'results': analysis_results
    }


def main():
    parser = argparse.ArgumentParser(
        description='Suggest canonical tags for documents using semantic matching'
    )
    parser.add_argument('chapter', help='Chapter name (e.g., "002-cross-check")')
    parser.add_argument('--subfolder', help='Optional subfolder filter')
    parser.add_argument('--threshold', type=float, default=0.3,
                       help='Similarity threshold for matching (0-1)')
    parser.add_argument('--local-only', action='store_true',
                       help='Skip Ollama and use LOCAL keywords only')
    
    args = parser.parse_args()
    
    print("\n" + "="*100)
    print("📊 CANONICAL TAG SUGGESTION SYSTEM")
    print("="*100)
    print(f"Chapter: {args.chapter}")
    if args.subfolder:
        print(f"Subfolder: {args.subfolder}")
    print(f"Similarity Threshold: {args.threshold}")
    print(f"Strategy: {'LOCAL ONLY' if args.local_only else 'LOCAL + OLLAMA'}")
    print("="*100 + "\n")
    
    result = analyze_document_for_canonical_tags(
        chapter=args.chapter,
        subfolder=args.subfolder,
        use_ollama=not args.local_only,
        threshold=args.threshold
    )
    
    print("\n" + "="*100)
    print("✅ ANALYSIS COMPLETE")
    print("="*100)


if __name__ == '__main__':
    main()
