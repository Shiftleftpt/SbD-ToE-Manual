"""Validation engine - analyzes existing tags and identifies issues."""

from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass, field
from enum import Enum

from ..core import CanonicalTagsManager


class IssueSeverity(Enum):
    """Issue severity levels."""
    ERROR = "error"        # Invalid tag not in canonical
    WARNING = "warning"    # Variation/alias that should be normalized
    INFO = "info"          # Minor consistency issue


class IssueType(Enum):
    """Types of issues detected."""
    UNKNOWN_TAG = "unknown_tag"
    ALIAS_FOUND = "alias_found"
    CASE_MISMATCH = "case_mismatch"
    DUPLICATE_TAG = "duplicate_tag"
    FORMATTING_ERROR = "formatting_error"


@dataclass
class ValidationIssue:
    """A single validation issue."""
    filepath: str
    issue_type: IssueType
    severity: IssueSeverity
    tag: str
    message: str
    suggestion: str = ""
    line_number: int = 0


@dataclass
class ValidationResult:
    """Complete validation result for a file."""
    filepath: str
    title: str
    existing_tags: List[str] = field(default_factory=list)
    valid_tags: List[str] = field(default_factory=list)
    issues: List[ValidationIssue] = field(default_factory=list)
    
    @property
    def is_valid(self) -> bool:
        """True if no ERROR issues."""
        return not any(i.severity == IssueSeverity.ERROR for i in self.issues)
    
    @property
    def error_count(self) -> int:
        return len([i for i in self.issues if i.severity == IssueSeverity.ERROR])
    
    @property
    def warning_count(self) -> int:
        return len([i for i in self.issues if i.severity == IssueSeverity.WARNING])


class ValidationEngine:
    """Validates existing tags in markdown files."""
    
    def __init__(self, canonical: CanonicalTagsManager):
        self.canonical = canonical
    
    def extract_frontmatter_tags(self, filepath: str) -> tuple[str, List[str]]:
        """Extract title and tags from frontmatter."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            import re
            match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            if not match:
                return "", []
            
            frontmatter = match.group(1)
            title = ""
            tags = []
            
            for line in frontmatter.split('\n'):
                if line.startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('"\'')
                elif line.startswith('tags:'):
                    tags_str = line.split(':', 1)[1].strip()
                    tags_str = tags_str.strip('[]')
                    if tags_str:
                        tags = [t.strip() for t in tags_str.split(',')]
            
            return title, tags
        except Exception:
            return "", []
    
    def validate_file(self, filepath: str) -> ValidationResult:
        """Validate all tags in a file."""
        title, tags = self.extract_frontmatter_tags(filepath)
        result = ValidationResult(filepath=filepath, title=title, existing_tags=tags)
        
        if not tags:
            return result
        
        seen = set()
        for tag in tags:
            # Check for duplicates
            if tag in seen:
                result.issues.append(ValidationIssue(
                    filepath=filepath,
                    issue_type=IssueType.DUPLICATE_TAG,
                    severity=IssueSeverity.WARNING,
                    tag=tag,
                    message=f"Duplicate tag: {tag}",
                    suggestion=f"Remove duplicate"
                ))
                continue
            seen.add(tag)
            
            # Check if tag exists in canonical
            canonical_tag = self.canonical.get_tag(tag)
            if canonical_tag:
                result.valid_tags.append(tag)
                continue
            
            # Check for aliases
            alias_match = self.canonical.find_by_alias(tag)
            if alias_match:
                result.issues.append(ValidationIssue(
                    filepath=filepath,
                    issue_type=IssueType.ALIAS_FOUND,
                    severity=IssueSeverity.WARNING,
                    tag=tag,
                    message=f"Tag '{tag}' is an alias",
                    suggestion=f"Use canonical form: '{alias_match}'"
                ))
                continue
            
            # Check for case mismatch
            similar = self.canonical.find_similar_tag(tag, threshold=0.9)
            if similar:
                result.issues.append(ValidationIssue(
                    filepath=filepath,
                    issue_type=IssueType.CASE_MISMATCH,
                    severity=IssueSeverity.WARNING,
                    tag=tag,
                    message=f"Tag '{tag}' has case/format mismatch",
                    suggestion=f"Use: '{similar}'"
                ))
                continue
            
            # Unknown tag
            result.issues.append(ValidationIssue(
                filepath=filepath,
                issue_type=IssueType.UNKNOWN_TAG,
                severity=IssueSeverity.ERROR,
                tag=tag,
                message=f"Unknown tag: '{tag}'",
                suggestion=f"Check canonical-tags.yml or add to canonical"
            ))
        
        return result
    
    def validate_batch(self, base_path: str) -> List[ValidationResult]:
        """Validate all markdown files in a directory."""
        results = []
        base = Path(base_path)
        
        for md_file in sorted(base.rglob('*.md')) + sorted(base.rglob('*.mdx')):
            result = self.validate_file(str(md_file))
            if result.issues:  # Only include files with issues
                results.append(result)
        
        return results
