#!/usr/bin/env python3
"""
Pre-generate embeddings for all canonical tags.

This script:
1. Loads all canonical tags from YAML
2. Combines label + description + aliases for each tag
3. Generates embeddings using the same model as RAG
4. Saves to JSON cache for fast loading

Result: Fast semantic matching without recalculating embeddings every run.
"""

import json
import yaml
import sys
from pathlib import Path
from typing import Dict
import logging

import numpy as np
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import RAG configuration
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
import rag_core.config as rag_config


def load_canonical_tags(tags_file: Path) -> Dict:
    """Load canonical tags from YAML file"""
    with open(tags_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_tag_embeddings(canonical_tags: Dict) -> Dict:
    """
    Generate embeddings for all canonical tags.
    
    For each tag, combines:
    - Label (e.g., "ASVS")
    - Description (e.g., "Application Security Verification Standard...")
    - Aliases (e.g., ["audit", "compliance"])
    
    Returns dict with structure:
    {
        "tag_id": {
            "label": "...",
            "description": "...",
            "aliases": [...],
            "embedding": [0.123, 0.456, ...],
            "text_used": "combined text for reference"
        }
    }
    """
    
    # Initialize embedding function
    logger.info(f"Initializing embedding model: {rag_config.EMBEDDING_MODEL}")
    embedding_fn = SentenceTransformerEmbeddingFunction(
        model_name=rag_config.EMBEDDING_MODEL
    )
    
    embeddings_cache = {}
    total_tags = len(canonical_tags)
    
    logger.info(f"Generating embeddings for {total_tags} canonical tags...")
    
    for i, (tag_id, tag_info) in enumerate(canonical_tags.items(), 1):
        # Combine all text sources for richer embedding
        label = tag_info.get('label', tag_id)
        description = tag_info.get('description', '')
        aliases = tag_info.get('aliases', [])
        
        # Build text to embed: prioritize description for semantic richness
        text_parts = [
            label,                    # "ASVS"
            description,              # Full description
            ' '.join(aliases)         # "audit compliance conformidade"
        ]
        text_to_embed = '. '.join(p for p in text_parts if p)
        
        # Generate embedding
        embedding = embedding_fn([text_to_embed])[0]
        
        # Store in cache
        embeddings_cache[tag_id] = {
            'label': label,
            'description': description,
            'aliases': aliases,
            'embedding': embedding,  # Will be converted to list for JSON
            'text_used': text_to_embed  # For debugging
        }
        
        # Progress indicator
        if i % 50 == 0:
            logger.info(f"  [{i}/{total_tags}] Generated embeddings...")
    
    logger.info(f"✅ Generated embeddings for {total_tags} tags")
    return embeddings_cache


def save_embeddings_cache(embeddings: Dict, output_file: Path):
    """
    Save embeddings to JSON file.
    
    Converts numpy arrays to lists for JSON serialization.
    """
    # Convert numpy arrays to lists
    cache_data = {}
    for tag_id, tag_data in embeddings.items():
        cache_data[tag_id] = {
            'label': tag_data['label'],
            'description': tag_data['description'],
            'aliases': tag_data['aliases'],
            'embedding': tag_data['embedding'].tolist() if isinstance(tag_data['embedding'], np.ndarray) else tag_data['embedding'],
            'text_used': tag_data['text_used']
        }
    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cache_data, f, indent=2, ensure_ascii=False)
    
    logger.info(f"✅ Embeddings saved to: {output_file}")
    logger.info(f"   File size: {output_file.stat().st_size / 1024:.1f} KB")


def main():
    print("\n" + "="*100)
    print("📊 CANONICAL TAG EMBEDDINGS GENERATOR")
    print("="*100 + "\n")
    
    # Paths
    tags_file = Path(__file__).parent / 'data' / 'canonical-tags.yml'
    output_file = Path(__file__).parent / 'data' / 'canonical-tags-embeddings.json'
    
    logger.info(f"Loading canonical tags from: {tags_file}")
    
    # Load tags
    if not tags_file.exists():
        logger.error(f"❌ Tags file not found: {tags_file}")
        sys.exit(1)
    
    canonical_tags = load_canonical_tags(tags_file)
    logger.info(f"✅ Loaded {len(canonical_tags)} canonical tags")
    
    # Generate embeddings
    embeddings = generate_tag_embeddings(canonical_tags)
    
    # Save cache
    save_embeddings_cache(embeddings, output_file)
    
    # Print summary
    print("\n" + "="*100)
    print("✅ EMBEDDINGS GENERATION COMPLETE")
    print("="*100)
    print(f"Total tags: {len(embeddings)}")
    print(f"Embedding dimension: {len(embeddings[list(embeddings.keys())[0]]['embedding'])}")
    print(f"Cache file: {output_file}")
    print(f"\nUsage: Import this cache in suggest_tags_canonical.py")
    print("="*100 + "\n")


if __name__ == '__main__':
    main()
