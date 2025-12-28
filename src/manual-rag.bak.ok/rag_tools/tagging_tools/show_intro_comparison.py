#!/usr/bin/env python3
import json

with open('reports/canonical_010-sbd-manual.json', 'r') as f:
    data = json.load(f)

# Encontrar o intro.md
for doc in data:
    if 'intro.md' in doc['file_path'] and '01-classificacao' in doc['file_path']:
        indexed = json.loads(doc['original_tags']) if isinstance(doc['original_tags'], str) else doc['original_tags']
        proposed = doc.get('canonical_suggestions', [])
        keywords = doc.get('extracted_keywords', {})
        
        print(f"{'='*80}")
        print(f"📋 Ficheiro: {doc['file_path']}")
        print(f"{'='*80}\n")
        
        print(f"📌 Título: {doc.get('title', 'N/A')}\n")
        
        print(f"{'='*80}")
        print("🔴 TAGS ATUALMENTE NO INDEX RAG")
        print(f"{'='*80}")
        print(f"Total: {len(indexed)} tags\n")
        for tag in sorted(indexed):
            print(f"   • {tag}")
        
        print(f"\n{'='*80}")
        print("🟢 TAGS PROPOSTAS (Canónicas - Semantic Matching)")
        print(f"{'='*80}")
        
        # Separar por tipo de match
        exact_matches = [item for item in proposed if item.get('confidence', 0) == 1.0]
        semantic_matches = [item for item in proposed if item.get('confidence', 0) < 1.0]
        
        print(f"\n✅ Correspondências Exatas (100%):")
        for i, item in enumerate(exact_matches, 1):
            print(f"   {i}. {item['canonical_label']}")
        
        print(f"\n🔗 Correspondências Semânticas:")
        for i, item in enumerate(semantic_matches[:10], 1):
            conf = item.get('confidence', 0) * 100
            print(f"   {i}. {item['canonical_label']} ({conf:.1f}%)")
        
        print(f"\n{'='*80}")
        print("📊 ANÁLISE COMPARATIVA")
        print(f"{'='*80}")
        print(f"Total de propostas: {len(proposed)}")
        print(f"Exactas (100%): {len(exact_matches)}")
        print(f"Semânticas (<100%): {len(semantic_matches)}")
        
        # Verificar intersecção
        proposed_tags = [item['canonical_label'] for item in proposed]
        indexed_set = set(indexed)
        proposed_set = set(proposed_tags)
        
        intersect = indexed_set & proposed_set
        only_indexed = indexed_set - proposed_set
        only_proposed = proposed_set - indexed_set
        
        print(f"\n✔️  Em AMBOS (index + propostas): {len(intersect)}")
        for tag in sorted(intersect):
            print(f"   • {tag}")
        
        if only_indexed:
            print(f"\n⚠️  APENAS NO INDEX (não foram propostas): {len(only_indexed)}")
            for tag in sorted(only_indexed):
                print(f"   • {tag}")
        
        if only_proposed:
            print(f"\n💡 NOVAS SUGESTÕES (propostas mas não no index): {len(only_proposed)}")
            for tag in sorted(only_proposed)[:15]:
                print(f"   • {tag}")
        
        print(f"\n{'='*80}")
        print("🔍 KEYWORDS EXTRAÍDAS")
        print(f"{'='*80}")
        
        if keywords:
            if keywords.get('local'):
                print(f"\n🔵 LOCAL (frequency-based):")
                for kw in keywords['local'][:8]:
                    print(f"   • {kw}")
            
            if keywords.get('ollama'):
                print(f"\n🟣 OLLAMA (LLM-based):")
                for kw in keywords['ollama'][:8]:
                    print(f"   • {kw}")
        
        break
