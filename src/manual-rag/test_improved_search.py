#!/usr/bin/env python3
"""Test improved search with chunking + metadata"""

import json
from manual_rag.query import SemanticSearch

def test_improved_search():
    """Test search with new chunked index"""
    
    searcher = SemanticSearch()
    
    # Test cases showing chapter-sensitive searches
    test_cases = [
        {
            "name": "CI/CD Security",
            "query": "CI/CD pipeline security deployment automation",
            "context_file": "010-sbd-manual/07-cicd-seguro/intro.md",
            "expected_chapter": "010-sbd-manual",
        },
        {
            "name": "Authentication Requirements",
            "query": "authentication authorization access control requirements",
            "context_file": "010-sbd-manual/02-requisitos-seguranca/intro.md",
            "expected_chapter": "010-sbd-manual",
        },
        {
            "name": "Threat Modeling",
            "query": "threat analysis STRIDE data flow attack scenarios",
            "context_file": "010-sbd-manual/03-threat-modeling/intro.md",
            "expected_chapter": "010-sbd-manual",
        },
    ]
    
    print("=" * 100)
    print("IMPROVED SEARCH TEST: Chunking + Chapter Awareness")
    print("=" * 100)
    
    for test in test_cases:
        print(f"\n📋 Test: {test['name']}")
        print(f"   Query: {test['query']}")
        print(f"   Context File: {test['context_file']}")
        print(f"   Expected Chapter: {test['expected_chapter']}\n")
        
        # Search WITH chapter context (new behavior)
        results = searcher.search(test['query'], top_k=5, context_file=test['context_file'])
        
        same_chapter_count = 0
        print("   Results:")
        
        for i, result in enumerate(results[:5], 1):
            # Extract chapter from metadata
            metadata = result.get('metadata', {})
            chapter = metadata.get('chapter', 'UNKNOWN')
            domain = metadata.get('domain', '')
            section = metadata.get('section', '')
            chunk_idx = metadata.get('chunk_index', 0)
            total_chunks = metadata.get('total_chunks', 1)
            
            same_chapter = chapter == test['expected_chapter']
            if same_chapter:
                same_chapter_count += 1
            
            marker = "✓" if same_chapter else "✗"
            
            print(f"      {marker} {i}. [{chapter}]")
            if domain:
                print(f"         Domain: {domain}")
            print(f"         Chunk: {chunk_idx + 1}/{total_chunks}")
            print(f"         Similarity: {result['similarity']:.1%}")
            
            # Show snippet
            content = result.get('content', '')[:80]
            print(f"         Preview: {content.replace(chr(10), ' ')}...")
        
        percentage = (same_chapter_count / min(5, len(results))) * 100 if results else 0
        print(f"\n   📊 Same-chapter results: {same_chapter_count}/5 ({percentage:.0f}%)")
        
        if same_chapter_count >= 3:
            print(f"   ✅ EXCELLENT chapter-aware ranking!")
        elif same_chapter_count >= 1:
            print(f"   ✓ GOOD - some same-chapter results")
        else:
            print(f"   ⚠️  No same-chapter results in top 5")
    
    print("\n" + "=" * 100)
    print("TEST COMPLETE")
    print("=" * 100)

if __name__ == "__main__":
    test_improved_search()
