"""Tag System - Validation & Recommendation Engine.

A modular, professional-grade system for validating, auditing, and recommending
tags in markdown documentation.

Modules:
- core: Canonical tags management
- validators: Tag validation engine
- recommenders: Tag recommendation engine
- cli: Command-line interface
- reports: Report generation
"""

from tag_system.core import CanonicalTagsManager
from tag_system.validators import ValidationEngine
from tag_system.recommenders import RecommendationEngine

__version__ = "1.0.0"
__all__ = [
    'CanonicalTagsManager',
    'ValidationEngine',
    'RecommendationEngine',
]
