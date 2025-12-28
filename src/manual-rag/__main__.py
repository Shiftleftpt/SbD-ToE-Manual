#!/usr/bin/env python3
"""CLI interface for Manual RAG system"""

import argparse
import json
import sys
from pathlib import Path

from rag_core import SemanticSearch, ManualIndexer, OllamaClient
from rag_core.config import MANUAL_ROOT, INDEX_DIR


def cmd_index(args):
    """Build the manual index"""
    from rag_core.indexing.build import main as build_index
    
    # Pass rebuild flag as sys.argv for the build script
    sys.argv = ["index", "--rebuild"] if args.rebuild else ["index"]
    return build_index()


def cmd_search(args):
    """Search for similar documents"""
    searcher = SemanticSearch(INDEX_DIR)
    results = searcher.search(args.query, top_k=args.top_k)
    
    if not results:
        print("No results found")
        return
    
    if args.json:
        print(json.dumps([{
            "path": r["path"],
            "title": r["title"],
            "similarity": r["similarity"],
            "tags": r["tags"],
        } for r in results], indent=2))
    else:
        print(f"Found {len(results)} related documents:\n")
        for r in results:
            print(f"  {r['path']}")
            print(f"    Similarity: {r['similarity']:.1%}")
            print(f"    Tags: {', '.join(r['tags']) or 'none'}")
            print(f"    Preview: {r['content'][:100]}...")
            print()


def cmd_tag(args):
    """Suggest tags for a file (REMOVED - use rag_tools.tagging.AutoTagger instead)"""
    print("❌ Tag suggestion has been moved to rag_tools.tagging.AutoTagger")
    print("   Use: from rag_tools.tagging import AutoTagger")
    sys.exit(1)


def cmd_gaps(args):
    """Analyze gaps in document (REMOVED - analysis functions moved to separate module)"""
    print("❌ Gap analysis is not part of the core RAG module")
    print("   SemanticSearch.search() provides the query functionality")
    sys.exit(1)


def cmd_xref(args):
    """Find cross-references for a topic (REMOVED - use SemanticSearch.search() directly)"""
    print("❌ Cross-reference analysis is not part of the core RAG module")
    print("   Use: SemanticSearch.search(topic, top_k=10)")
    sys.exit(1)


def cmd_health(args):
    """Check system health"""
    print("Checking Manual RAG system health...\n")
    
    # Check LLM
    llm = OllamaClient()
    llm_ok = llm.health_check()
    print(f"  Ollama: {'✓' if llm_ok else '✗'}")
    
    # Check index
    index_path = Path(__file__).parent / "index" / "chroma"
    index_ok = index_path.exists()
    print(f"  Index: {'✓' if index_ok else '✗'}")
    
    if not llm_ok or not index_ok:
        print("\nSetup needed:")
        if not llm_ok:
            print("  1. Install Ollama: brew install ollama")
            print("  2. Start Ollama: ollama serve")
            print("  3. Pull model: ollama pull mistral")
        if not index_ok:
            print("  - Build index: python3 build_index.py")
        sys.exit(1)
    
    print("\n✓ System ready")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Manual RAG System - Query the SbD-ToE manual"
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Index command
    index_parser = subparsers.add_parser("index", help="Build the manual index")
    index_parser.add_argument("--rebuild", action="store_true", help="Rebuild from scratch")
    index_parser.set_defaults(func=cmd_index)
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search for similar documents")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--top-k", type=int, default=5, help="Number of results")
    search_parser.set_defaults(func=cmd_search)
    
    # Tag command (REMOVED - functionality moved to rag_tools.tagging)
    tag_parser = subparsers.add_parser("tag", help="[DEPRECATED] Use rag_tools.tagging.AutoTagger")
    tag_parser.add_argument("file", help="File path")
    tag_parser.add_argument("--query", help="Optional query")
    tag_parser.set_defaults(func=cmd_tag)
    
    # Gaps command (REMOVED - not part of core RAG)
    gaps_parser = subparsers.add_parser("gaps", help="[DEPRECATED] Gap analysis removed")
    gaps_parser.add_argument("file", help="File path to analyze")
    gaps_parser.set_defaults(func=cmd_gaps)
    
    # Cross-reference command (REMOVED - use search() directly)
    xref_parser = subparsers.add_parser("xref", help="[DEPRECATED] Use SemanticSearch.search()")
    xref_parser.add_argument("topic", help="Topic to find references for")
    xref_parser.set_defaults(func=cmd_xref)
    
    # Health command
    health_parser = subparsers.add_parser("health", help="Check system health")
    health_parser.set_defaults(func=cmd_health)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
