#!/usr/bin/env python3
"""
Compare Tag Suggestions - Local vs Ollama/LLM
Compara sugestões de tags usando análise local vs LLM (Ollama)
Gera relatório detalhado mostrando:
- Tags originais (no índice)
- Tags no documento (metadata atual)
- Tags sugeridas (análise local)
- Tags sugeridas (Ollama/LLM)
- Comparativos: matches, novos, removidos
- Estatísticas de qualidade
"""

import json
import sys
import re
import argparse
from pathlib import Path
from typing import Dict, List, Set
from collections import Counter
import chromadb
import requests

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from rag_core.config import INDEX_DIR, OLLAMA_BASE_URL


def extract_keywords_local(text: str, top_n: int = 10) -> List[str]:
    """Análise local: keyword extraction"""
    
    stop_words = {
        'o', 'a', 'de', 'para', 'com', 'sem', 'por', 'que', 'um', 'uma', 
        'e', 'ou', 'é', 'em', 'do', 'da', 'dos', 'das', 'ao', 'à', 'este',
        'esse', 'aquele', 'este', 'foi', 'ser', 'está', 'são', 'tem', 'tinha',
        'sido', 'há', 'pelo', 'pela', 'pelos', 'pelas', 'seu', 'sua', 'seus',
        'suas', 'nosso', 'nossa', 'nossos', 'nossas', 'vosso', 'vossa',
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'should', 'would',
        'could', 'can', 'may', 'might', 'must', 'shall', 'will', 'document',
        'manual', 'seção', 'section', 'capítulo', 'chapter', 'página', 'page',
        'tabela', 'table', 'figura', 'figure', 'exemplo', 'example'
    }
    
    words = re.findall(r'\b[a-záéíóúàâãêôçñ]+\b', text.lower(), re.UNICODE)
    candidates = [w for w in words if len(w) > 2 and w not in stop_words]
    freq = Counter(candidates)
    
    return [w for w, _ in freq.most_common(top_n * 2)][:top_n]


def suggest_tags_ollama(title: str, content: str, top_n: int = 10) -> List[str]:
    """Usar Ollama/Mistral para sugerir tags"""
    
    content_preview = content[:2000] if content else ""
    
    prompt = f"""Você é um especialista em classificação de documentação técnica de segurança.

Analise o seguinte documento APENAS pelo seu conteúdo. Não use nenhuma informação de tags anteriores.

TÍTULO:
{title}

CONTEÚDO:
{content_preview}

TAREFA: Gere exatamente {top_n} palavras-chave/tags que descrevem este documento.

REGRAS:
1. Cada tag: 1-3 palavras máximo
2. Português se documento é PT, inglês se é EN
3. Substantivos e conceitos técnicos
4. Ignore: "documento", "manual", "seção", "capítulo"
5. Seja específico
6. Retorne EXATAMENTE {top_n} tags

Responda APENAS com JSON:
{{"tags": ["tag1", "tag2", ... ({top_n} tags)]}}"""

    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False,
                "temperature": 0.3,
            },
            timeout=60
        )
        
        if response.status_code != 200:
            return []
        
        result = response.json()
        response_text = result.get('response', '')
        
        try:
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                parsed = json.loads(json_str)
                
                if 'tags' in parsed and isinstance(parsed['tags'], list):
                    tags = parsed['tags'][:top_n]
                    if tags:
                        return tags
        except (json.JSONDecodeError, Exception):
            pass
        
        return []
        
    except requests.exceptions.RequestException:
        return []


def compare_tag_sets(original: List[str], local: List[str], ollama: List[str]) -> Dict:
    """Comparar três conjuntos de tags"""
    
    orig_set = set(t.lower() for t in original)
    local_set = set(t.lower() for t in local)
    ollama_set = set(t.lower() for t in ollama)
    
    return {
        'original_count': len(orig_set),
        'local_count': len(local_set),
        'ollama_count': len(ollama_set),
        
        # Local vs Original
        'local_matches_original': len(local_set & orig_set),
        'local_new': list(local_set - orig_set),
        'local_new_count': len(local_set - orig_set),
        'local_removed': list(orig_set - local_set),
        'local_removed_count': len(orig_set - local_set),
        
        # Ollama vs Original
        'ollama_matches_original': len(ollama_set & orig_set),
        'ollama_new': list(ollama_set - orig_set),
        'ollama_new_count': len(ollama_set - orig_set),
        'ollama_removed': list(orig_set - ollama_set),
        'ollama_removed_count': len(orig_set - ollama_set),
        
        # Local vs Ollama
        'local_vs_ollama_matches': len(local_set & ollama_set),
        'local_unique': list(local_set - ollama_set),
        'ollama_unique': list(ollama_set - local_set),
        
        # Overlap
        'all_three_overlap': len(local_set & ollama_set & orig_set),
    }


def analyze_single_chapter(chapter_name: str, subfolder: str = None, max_docs: int = None):
    """Analisar um capítulo completo e comparar estratégias"""
    
    print("\n" + "=" * 180)
    print(f"📊 TAG SUGGESTIONS COMPARISON - Local vs Ollama")
    print("=" * 180)
    print(f"Chapter: {chapter_name}")
    if subfolder:
        print(f"Subfolder: {subfolder}")
    print(f"Strategy: Analyze each document with LOCAL and OLLAMA, compare results\n")
    
    # Load Chroma
    print(f"🔄 Loading Chroma index...")
    client = chromadb.PersistentClient(path=str(INDEX_DIR / "chroma"))
    collection = client.get_collection("manual")
    print(f"   ✅ Index loaded ({collection.count()} documents)\n")
    
    # Get all documents and discover chapters
    all_docs = collection.get(include=['metadatas'])
    chapters = {}
    
    if all_docs and all_docs['ids']:
        for idx, doc_id in enumerate(all_docs['ids']):
            metadata = all_docs['metadatas'][idx] if all_docs['metadatas'] else {}
            chapter = metadata.get('chapter', '')
            if chapter:
                if chapter not in chapters:
                    chapters[chapter] = []
                chapters[chapter].append({
                    'doc_id': doc_id,
                    'metadata': metadata
                })
    
    # Match chapter
    chapter_lower = chapter_name.lower()
    matching_chapters = [k for k in chapters.keys() if chapter_lower in k.lower()]
    
    if not matching_chapters:
        print(f"❌ Chapter '{chapter_name}' not found")
        return
    
    chapter_key = matching_chapters[0]
    chapter_docs = chapters[chapter_key]
    
    # Filter by subfolder if specified
    if subfolder:
        subfolder_lower = subfolder.lower()
        chapter_docs = [d for d in chapter_docs 
                       if subfolder_lower in d['metadata'].get('file_path', '').lower()]
    
    print(f"✅ Found chapter: {chapter_key}")
    if subfolder:
        print(f"📁 Subfolder: {subfolder}")
    print(f"📄 Total documents: {len(chapter_docs)}")
    
    if max_docs:
        chapter_docs = chapter_docs[:max_docs]
        print(f"   (analyzing first {max_docs})\n")
    else:
        print()
    
    # Check Ollama availability
    ollama_available = False
    try:
        requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        ollama_available = True
        print("✅ Ollama/Mistral available - will use both strategies\n")
    except:
        print("⚠️  Ollama not available - local analysis only\n")
    
    # Analyze documents
    results = []
    all_comparisons = {
        'local_matches_original': [],
        'local_new': [],
        'ollama_matches_original': [],
        'ollama_new': [],
        'local_vs_ollama_matches': [],
        'local_unique': [],
        'ollama_unique': [],
    }
    
    for idx, doc_info in enumerate(chapter_docs, 1):
        metadata = doc_info['metadata']
        file_path = metadata.get('file_path', '???')
        title = metadata.get('title', '???')
        content = metadata.get('content_preview', '')
        original_tags = json.loads(metadata.get('tags', '[]') or '[]')
        
        print(f"[{idx}/{len(chapter_docs)}] {Path(file_path).name}", end='', flush=True)
        
        # Local analysis
        local_tags = extract_keywords_local(content, top_n=10)
        
        # Ollama analysis (if available)
        ollama_tags = []
        if ollama_available:
            ollama_tags = suggest_tags_ollama(title, content, top_n=10)
        
        # Compare
        comparison = compare_tag_sets(original_tags, local_tags, ollama_tags)
        
        print(f" ✅")
        
        # Store result
        result = {
            'file_path': file_path,
            'title': title,
            'original_tags': original_tags,
            'local_tags': local_tags,
            'ollama_tags': ollama_tags,
            'comparison': comparison
        }
        results.append(result)
        
        # Aggregate stats
        all_comparisons['local_matches_original'].append(comparison['local_matches_original'])
        all_comparisons['local_new'].extend(comparison['local_new'][:3])
        if ollama_available:
            all_comparisons['ollama_matches_original'].append(comparison['ollama_matches_original'])
            all_comparisons['ollama_new'].extend(comparison['ollama_new'][:3])
            all_comparisons['local_vs_ollama_matches'].append(comparison['local_vs_ollama_matches'])
            all_comparisons['local_unique'].extend(comparison['local_unique'][:2])
            all_comparisons['ollama_unique'].extend(comparison['ollama_unique'][:2])
    
    # Print detailed report
    print("\n" + "=" * 180)
    print("📋 DETAILED DOCUMENT COMPARISON")
    print("=" * 180)
    
    for idx, result in enumerate(results, 1):
        print(f"\n[{idx}] {result['file_path']}")
        print(f"    Title: {result['title'][:70]}")
        
        comp = result['comparison']
        print(f"\n    Original Tags ({comp['original_count']}): {', '.join(result['original_tags'][:5])}{'...' if len(result['original_tags']) > 5 else ''}")
        print(f"    LOCAL Tags ({comp['local_count']}): {', '.join(result['local_tags'][:5])}")
        if ollama_available and result['ollama_tags']:
            print(f"    OLLAMA Tags ({comp['ollama_count']}): {', '.join(result['ollama_tags'][:5])}")
        
        print(f"\n    Comparisons:")
        print(f"      LOCAL vs Original:")
        print(f"        ✓ Matches: {comp['local_matches_original']}/{comp['original_count']} ({100*comp['local_matches_original']/max(comp['original_count'],1):.0f}%)")
        print(f"        ⊕ New: {comp['local_new_count']} - {', '.join(comp['local_new'][:3])}")
        print(f"        ⊖ Removed: {comp['local_removed_count']}")
        
        if ollama_available and result['ollama_tags']:
            print(f"      OLLAMA vs Original:")
            print(f"        ✓ Matches: {comp['ollama_matches_original']}/{comp['original_count']} ({100*comp['ollama_matches_original']/max(comp['original_count'],1):.0f}%)")
            print(f"        ⊕ New: {comp['ollama_new_count']} - {', '.join(comp['ollama_new'][:3])}")
            print(f"        ⊖ Removed: {comp['ollama_removed_count']}")
            
            print(f"      LOCAL vs OLLAMA:")
            print(f"        ✓ Both suggest: {comp['local_vs_ollama_matches']}")
            print(f"        ⊕ Only LOCAL: {len(comp['local_unique'])}")
            print(f"        ⊕ Only OLLAMA: {len(comp['ollama_unique'])}")
    
    # Summary statistics
    print("\n" + "=" * 180)
    print("📊 SUMMARY STATISTICS")
    print("=" * 180)
    
    local_matches = sum(all_comparisons['local_matches_original'])
    total_original = sum(comp['comparison']['original_count'] for comp in results)
    
    print(f"\nDocuments analyzed: {len(results)}")
    print(f"\nLOCAL Strategy:")
    print(f"  Average matches with original: {local_matches/len(results):.1f} tags")
    print(f"  Average new tags proposed: {sum(comp['comparison']['local_new_count'] for comp in results)/len(results):.1f}")
    print(f"  Total unique new tags: {len(set(tag.lower() for tags in all_comparisons['local_new'] for tag in tags))}")
    
    if ollama_available:
        ollama_matches = sum(all_comparisons['ollama_matches_original'])
        print(f"\nOLLAMA Strategy:")
        print(f"  Average matches with original: {ollama_matches/len(results):.1f} tags")
        print(f"  Average new tags proposed: {sum(comp['comparison']['ollama_new_count'] for comp in results)/len(results):.1f}")
        print(f"  Total unique new tags: {len(set(tag.lower() for tags in all_comparisons['ollama_new'] for tag in tags))}")
        
        print(f"\nComparison (LOCAL vs OLLAMA):")
        print(f"  Average agreement: {sum(all_comparisons['local_vs_ollama_matches'])/len(results):.1f} tags both suggest")
        print(f"  LOCAL unique insights: {len(set(tag.lower() for tags in all_comparisons['local_unique'] for tag in tags))}")
        print(f"  OLLAMA unique insights: {len(set(tag.lower() for tags in all_comparisons['ollama_unique'] for tag in tags))}")
    
    # Save report
    report_file = Path(__file__).parent / "reports" / f"comparison_{chapter_key.replace('/', '_')}"
    if subfolder:
        report_file = report_file.parent / f"comparison_{chapter_key.replace('/', '_')}_{subfolder.replace('/', '_')}.json"
    else:
        report_file = report_file.parent / f"comparison_{chapter_key.replace('/', '_')}.json"
    
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump({
            'chapter': chapter_key,
            'subfolder': subfolder,
            'documents_analyzed': len(results),
            'ollama_available': ollama_available,
            'results': results,
            'summary': {
                'local_avg_matches': local_matches / len(results) if results else 0,
                'ollama_avg_matches': sum(all_comparisons['ollama_matches_original']) / len(results) if results and ollama_available else 0,
                'ollama_available': ollama_available,
            }
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Report saved: {report_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compare tag suggestions: Local vs Ollama',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 compare_tags.py "002-cross-check" --max-docs 5
  python3 compare_tags.py "010-sbd" --subfolder "01-classificacao" --max-docs 10
  python3 compare_tags.py "010-sbd" --subfolder "02-requisitos" --max-docs 5
        """
    )
    parser.add_argument('chapter', help='Chapter name (partial match OK)')
    parser.add_argument('--subfolder', type=str, default=None, help='Filter by subfolder')
    parser.add_argument('--max-docs', type=int, default=None, help='Maximum documents to analyze')
    
    args = parser.parse_args()
    
    analyze_single_chapter(args.chapter, subfolder=args.subfolder, max_docs=args.max_docs)
