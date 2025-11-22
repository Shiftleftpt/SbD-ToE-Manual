#!/usr/bin/env python3
"""Test chapter-aware search improvements"""

from manual_rag.tagging import AutoTagger
from manual_rag.query import SemanticSearch

def test_chapter_context():
    """Compare search results with and without chapter context"""
    
    tagger = AutoTagger()
    searcher = SemanticSearch()
    
    # Test 1: CI/CD in different chapters
    test_cases = [
        {
            "file": "010-sbd-manual/06-desenvolvimento-seguro/cicd-example.md",
            "content": "CI/CD pipeline automation, continuous integration, testing gates, approval workflows",
            "chapter": "010-sbd-manual/06-desenvolvimento-seguro",
        },
        {
            "file": "010-sbd-manual/07-cicd-seguro/intro.md",
            "content": "CI/CD security, pipeline configuration, secure deployments, artifact scanning",
            "chapter": "010-sbd-manual/07-cicd-seguro",
        },
        {
            "file": "010-sbd-manual/08-iac-infraestrutura/cicd-integration.md",
            "content": "CI/CD integration with infrastructure as code, deployment automation",
            "chapter": "010-sbd-manual/08-iac-infraestrutura",
        },
    ]
    
    print("=" * 80)
    print("CHAPTER-AWARE SEARCH TEST")
    print("=" * 80)
    
    for test_case in test_cases:
        file_path = test_case["file"]
        content = test_case["content"]
        
        print(f"\n📄 File: {file_path}")
        print(f"   Chapter: {test_case['chapter']}")
        print(f"\n   Content preview: {content[:60]}...\n")
        
        # Search WITHOUT chapter context
        print("   ❌ WITHOUT chapter context (old behavior):")
        results_no_context = searcher.search(content[:500], top_k=5, context_file=None)
        for i, result in enumerate(results_no_context[:3], 1):
            result_chapter = result['path'].split('/')[0]
            same_chapter = "✓" if result_chapter == test_case['chapter'].split('/')[0] else "✗"
            print(f"      {same_chapter} {i}. {result['path'][:60]}")
            print(f"         Tags: {result['tags'][:3]}")
            print(f"         Similarity: {result['similarity']:.1%}")
        
        # Search WITH chapter context
        print("\n   ✅ WITH chapter context (new behavior):")
        results_with_context = searcher.search(content[:500], top_k=5, context_file=file_path)
        for i, result in enumerate(results_with_context[:3], 1):
            result_chapter = result['path'].split('/')[0]
            same_chapter = "✓" if result_chapter == test_case['chapter'].split('/')[0] else "✗"
            print(f"      {same_chapter} {i}. {result['path'][:60]}")
            print(f"         Tags: {result['tags'][:3]}")
            print(f"         Similarity: {result['similarity']:.1%}")
        
        # Check if chapter-aware improved same-chapter ranking
        first_result_no_context = results_no_context[0]['path'].split('/')[0]
        first_result_with_context = results_with_context[0]['path'].split('/')[0]
        context_chapter = test_case['chapter'].split('/')[0]
        
        improved = (first_result_no_context != context_chapter and 
                   first_result_with_context == context_chapter)
        
        if improved:
            print(f"\n   📈 Chapter awareness improved ranking!")
        else:
            print(f"\n   ℹ️  Top result already in same chapter")
    
    print("\n" + "=" * 80)
    print("TEST COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    test_chapter_context()
