"""
Workflows Module - High-Level RAG-Based Operations

Responsible for:
- Building chunked JSONL index with metadata
- Generating review reports for tag suggestions
- Applying approved tag changes to files

Scripts (Entry Points):
- build_chunked_index.py: Builds vector index
- generate_review_report.py: Analyzes files, generates CSV review
- apply_review_decisions.py: Applies approved tags from CSV
"""

__all__ = [
    "build_chunked_index",
    "generate_review_report",
    "apply_review_decisions",
]
