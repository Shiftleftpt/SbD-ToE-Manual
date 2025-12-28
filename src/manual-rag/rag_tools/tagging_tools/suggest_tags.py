#!/usr/bin/env python3
"""
Tagging Tools - Suggest Tags using Ollama
Analisa documentos do RAG e sugere 10-15 tags por documento
Ignora tags existentes no metadata - foca em sugestões novas baseadas no conteúdo

Processo:
1. Carrega capítulo do RAG
2. Para cada documento:
   - Envia conteúdo para Ollama/Mistral
   - Pede 10-15 tags sugestões
   - Retorna com contexto e confiança
3. Gera relatório com sugestões vs tags originais
"""

import json
import sys
import re
import argparse
from pathlib import Path
from typing import Dict, List
from collections import Counter
import chromadb
import requests

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from rag_core.config import INDEX_DIR, OLLAMA_BASE_URL


def extract_keywords_from_text(text: str, top_n: int = 15) -> List[str]:
    """
    Extract keywords from text using simple heuristics + TF-IDF-like approach
    
    Usa análise local para sugerir tags quando Ollama não está disponível
    """
    
    # Common stop words em português e inglês
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
    
    # Tokenize and clean
    words = re.findall(r'\b[a-záéíóúàâãêôçñ]+\b', text.lower(), re.UNICODE)
    
    # Filter
    candidates = [w for w in words if len(w) > 2 and w not in stop_words]
    
    # Count frequency
    freq = Counter(candidates)
    
    # Get top candidates
    top_candidates = [w for w, _ in freq.most_common(top_n * 2)]
    
    return top_candidates[:top_n]


def call_ollama_for_tags(title: str, content: str, similar_titles: List[str], top_n: int = 15) -> List[str]:
    """
    Chamar Ollama/Mistral para sugerir tags baseado no conteúdo
    Se Ollama não estiver disponível, usa análise local
    
    Ignora completamente tags existentes - apenas analisa o documento
    """
    
    # Limitar conteúdo para não sobrecarregar
    content_preview = content[:2000] if content else ""
    similar_context = "\n".join(similar_titles[:3]) if similar_titles else ""
    
    prompt = f"""Você é um especialista em classificação de documentação técnica de segurança.

Analise o seguinte documento APENAS pelo seu conteúdo e contexto. Não use nenhuma informação de tags anteriores.

TÍTULO:
{title}

CONTEÚDO:
{content_preview}

DOCUMENTOS SIMILARES (para contexto):
{similar_context}

TAREFA: Gere exatamente {top_n} palavras-chave/tags que descrevem este documento.

REGRAS:
1. Cada tag: 1-3 palavras máximo
2. Português se documento é PT, inglês se é EN
3. Substantivos e conceitos técnicos
4. Ignore: "documento", "manual", "seção", "capítulo", "página"
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
            # Fallback to local extraction
            return extract_keywords_from_text(content, top_n)
        
        result = response.json()
        response_text = result.get('response', '')
        
        # Extract JSON
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
        
        # Fallback to local extraction
        return extract_keywords_from_text(content, top_n)
        
    except requests.exceptions.RequestException as e:
        # Ollama not available - use local extraction
        return extract_keywords_from_text(content, top_n)


def analyze_chapter_for_tags(chapter_name: str, top_n: int = 15, max_docs: int = None, subfolder: str = None):
    """
    Analisar capítulo inteiro e sugerir tags para cada documento
    
    Args:
        chapter_name: Nome do capítulo (partial match OK)
        top_n: Número de tags a sugerir por documento
        max_docs: Máximo de documentos a processar (None = todos)
        subfolder: Filtrar por subfolder específico (ex: "01-classificacao-aplicacoes")
    """
    
    print("\n" + "=" * 160)
    print(f"🏷️  TAGGING TOOLS - Fresh tag suggestions from Ollama")
    print("=" * 160)
    print(f"Strategy: Analyze document content → Call Ollama → Suggest {top_n} tags per document")
    print(f"Note: Ignoring existing tags in metadata - fresh analysis only\n")
    
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
        print(f"\n📂 Available chapters:")
        for ch in sorted(chapters.keys()):
            print(f"   • {ch} ({len(chapters[ch])} documents)")
        return
    
    chapter_key = matching_chapters[0]
    chapter_docs = chapters[chapter_key]
    
    # Filter by subfolder if specified
    if subfolder:
        subfolder_lower = subfolder.lower()
        chapter_docs = [d for d in chapter_docs 
                       if subfolder_lower in d['metadata'].get('file_path', '').lower()]
        print(f"✅ Found chapter: {chapter_key}")
        print(f"📁 Subfolder filter: {subfolder}")
        print(f"📄 Documents: {len(chapter_docs)}")
    else:
        print(f"✅ Found chapter: {chapter_key}")
        print(f"📄 Documents: {len(chapter_docs)}")
    if max_docs:
        chapter_docs = chapter_docs[:max_docs]
        print(f"   (analyzing first {max_docs} documents)\n")
    else:
        print()
    
    # Analyze each document
    results = []
    all_suggested_tags = []
    
    # Build a lookup for all document titles (for similarity context)
    all_titles = {}
    if all_docs and all_docs['ids']:
        for idx, doc_id in enumerate(all_docs['ids']):
            metadata = all_docs['metadatas'][idx] if all_docs['metadatas'] else {}
            title = metadata.get('title', '')
            if title:
                all_titles[doc_id] = title
    
    for idx, doc_info in enumerate(chapter_docs, 1):
        doc_id = doc_info['doc_id']
        metadata = doc_info['metadata']
        
        file_path = metadata.get('file_path', '???')
        title = metadata.get('title', '???')
        content = metadata.get('content_preview', '')
        existing_tags = json.loads(metadata.get('tags', '[]') or '[]')
        
        print(f"[{idx}/{len(chapter_docs)}] {Path(file_path).name}", end='')
        sys.stdout.flush()
        
        # Get similar documents for context
        similar_titles = []
        try:
            # Get document embedding to find similar docs
            results_similar = collection.query(
                query_texts=[content[:500]],
                n_results=3,
                include=['metadatas']
            )
            if results_similar and results_similar['metadatas']:
                similar_titles = [m.get('title', '')[:50] for m in results_similar['metadatas'][0]]
        except:
            pass
        
        # Call Ollama (or fallback to local extraction) for suggestions
        suggested_tags = call_ollama_for_tags(title, content, similar_titles, top_n=top_n)
        
        if suggested_tags:
            print(f" ✅ ({len(suggested_tags)} tags suggested)")
        else:
            print(f" ⚠️  No tags suggested")
            continue
        
        # Display results
        print(f"   📍 {title[:70]}")
        print(f"   🔖 Existing tags ({len(existing_tags)}): {', '.join(existing_tags[:3])}{'...' if len(existing_tags) > 3 else ''}")
        print(f"   ✨ Suggested tags ({len(suggested_tags)}):")
        
        for rank, tag in enumerate(suggested_tags, 1):
            # Check if tag is already in existing tags
            status = "✓ EXISTS" if tag.lower() in [t.lower() for t in existing_tags] else "○ NEW"
            print(f"      {rank:2d}. {tag:40s} [{status}]")
        
        print()
        
        # Store result
        results.append({
            'file_path': file_path,
            'title': title,
            'existing_tags': existing_tags,
            'suggested_tags': suggested_tags,
            'new_tags': [t for t in suggested_tags if t.lower() not in [x.lower() for x in existing_tags]]
        })
        
        all_suggested_tags.extend(suggested_tags)
    
    # Summary
    print("\n" + "=" * 160)
    print("📊 SUMMARY")
    print("=" * 160)
    
    total_docs = len(results)
    total_suggestions = sum(len(r['suggested_tags']) for r in results)
    total_new_tags_proposed = sum(len(r['new_tags']) for r in results)
    unique_suggestions = len(set(t.lower() for t in all_suggested_tags))
    
    print(f"Documents analyzed: {total_docs}")
    print(f"Total tag suggestions: {total_suggestions}")
    print(f"New tags proposed (not in existing): {total_new_tags_proposed}")
    print(f"Unique suggested tags: {unique_suggestions}")
    
    # Most suggested tags
    tag_freq = Counter(t.lower() for t in all_suggested_tags)
    
    print(f"\n🏆 Most suggested tags (across {total_docs} documents):")
    for tag, count in tag_freq.most_common(20):
        pct = count / total_docs * 100
        print(f"   • {tag:40s} ({count:2d} docs, {pct:5.1f}%)")
    
    # Comparison: existing vs new
    total_existing_tags = sum(len(r['existing_tags']) for r in results)
    print(f"\n📊 Tags Comparison:")
    print(f"   Total existing tags in metadata: {total_existing_tags}")
    print(f"   Average per doc: {total_existing_tags / total_docs:.1f}")
    print(f"   Total suggestions: {total_suggestions}")
    print(f"   Average per doc: {total_suggestions / total_docs:.1f}")
    
    # Save detailed report
    report_file = Path(__file__).parent / "reports" / f"chapter_{chapter_key.replace('/', '_')}_tags_top{top_n}.json"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump({
            'chapter': chapter_key,
            'documents_analyzed': total_docs,
            'tags_per_document': top_n,
            'results': results,
            'summary': {
                'total_existing_tags': total_existing_tags,
                'total_suggestions': total_suggestions,
                'total_new_proposed': total_new_tags_proposed,
                'unique_suggested': unique_suggestions,
                'tag_frequency': dict(tag_freq.most_common(50))
            }
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Report saved: {report_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Suggest tags for documents using Ollama',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 suggest_tags.py "cross-check" --top-n 15
  python3 suggest_tags.py "010-sbd" --top-n 12 --max-docs 50
  python3 suggest_tags.py "010-sbd" --top-n 12 --subfolder "01-classificacao-aplicacoes"
  python3 suggest_tags.py "010-sbd" --top-n 12 --subfolder "02-requisitos" --max-docs 20
        """
    )
    parser.add_argument('chapter', help='Chapter name (partial match OK)')
    parser.add_argument('--top-n', type=int, default=15, help='Number of tags to suggest per document (default: 15)')
    parser.add_argument('--max-docs', type=int, default=None, help='Maximum number of documents to analyze (default: all)')
    parser.add_argument('--subfolder', type=str, default=None, help='Filter by subfolder (for 010-sbd-manual sections)')
    
    args = parser.parse_args()
    
    analyze_chapter_for_tags(args.chapter, top_n=args.top_n, max_docs=args.max_docs, subfolder=args.subfolder)
