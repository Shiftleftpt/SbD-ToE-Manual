import json
data = json.load(open('reports/canonical_010-sbd-manual.json'))
for doc in data:
    if 'intro.md' in doc['file_path'] and '01-classificacao' in doc['file_path']:
        indexed = json.loads(doc['original_tags'])
        proposed = doc['canonical_suggestions']
        keywords = doc.get('extracted_keywords', {})
        
        print(f"{'='*80}")
        print(f"📋 {doc['file_path']}")
        print(f"{'='*80}\n")
        print(f"📌 {doc.get('title')}\n")
        
        print(f"{'='*80}\n🔴 TAGS NO INDEX RAG ({len(indexed)} tags)\n{'='*80}")
        for tag in sorted(indexed):
            print(f"• {tag}")
        
        exact = [i for i in proposed if i.get('confidence') == 1.0]
        semantic = [i for i in proposed if i.get('confidence') < 1.0]
        
        print(f"\n{'='*80}\n🟢 TAGS PROPOSTAS\n{'='*80}")
        print(f"\n✅ Exactas ({len(exact)}):")
        for i in exact:
            print(f"• {i['canonical_label']}")
        
        print(f"\n🔗 Semânticas ({len(semantic)}):")
        for i in semantic[:10]:
            print(f"• {i['canonical_label']} ({i.get('confidence', 0)*100:.0f}%)")
        
        # Intersecção
        proposed_tags = {i['canonical_label'] for i in proposed}
        indexed_set = set(indexed)
        
        common = indexed_set & proposed_tags
        only_idx = indexed_set - proposed_tags
        only_prop = proposed_tags - indexed_set
        
        print(f"\n{'='*80}\n📊 ANÁLISE\n{'='*80}")
        print(f"\n✔️ Em AMBOS ({len(common)}):")
        for t in sorted(common):
            print(f"• {t}")
        
        print(f"\n⚠️ Apenas no INDEX ({len(only_idx)}):")
        for t in sorted(only_idx):
            print(f"• {t}")
        
        print(f"\n💡 Novas Sugestões ({len(only_prop)}):")
        for t in sorted(only_prop)[:12]:
            print(f"• {t}")
        
        print(f"\n{'='*80}\n🔍 KEYWORDS\n{'='*80}")
        if keywords.get('local'):
            print(f"\n🔵 LOCAL:")
            for k in keywords['local'][:6]:
                print(f"• {k}")
        if keywords.get('ollama'):
            print(f"\n🟣 OLLAMA:")
            for k in keywords['ollama'][:6]:
                print(f"• {k}")
        break
