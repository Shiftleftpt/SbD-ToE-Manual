"""
Tagging Module - Tag Management and Auto-Tagging

Responsible for:
- Loading and managing canonical tags (CanonicalTags)
- Suggesting tags using RAG + patterns (AutoTagger)
- Reading/writing file frontmatter with tags (FileTagUpdater)

Key Classes:
- CanonicalTags: Load and validate canonical tag vocabulary
- AutoTagger: Combine RAG + regex patterns for suggestions
- FileTagUpdater: Read/write markdown frontmatter
- TagSuggestion: Data class for tag suggestions
"""

from ._tags import CanonicalTags
from ._auto_tagger import AutoTagger, TagSuggestion
from ._file_updater import FileTagUpdater

__all__ = [
    "CanonicalTags",
    "AutoTagger",
    "TagSuggestion",
    "FileTagUpdater",
]
