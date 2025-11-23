#!/usr/bin/env python3
"""
Smart tag filtering strategy for Docusaurus rendering
- Keep mandatory tags (tipo:*, tema:* only - cat_* and grp_* are in categoria/group fields)
- Limit total to ~7 tags max (configurable)
- Select highest confidence tags within limit
"""

from typing import Dict, List
import sys
from pathlib import Path


def select_tags_for_display(all_tags: List[str], suggested_tags: Dict, 
                           max_total: int = 7, existing_tags: List[str] = None) -> Dict:
    """
    Select tags for Docusaurus display
    
    Strategy:
    1. Keep mandatory tags (tipo:*, tema:*)
    2. Keep important existing tags
    3. Add highest-confidence suggestions to reach ~max_total
    
    Returns dict with:
    - selected_tags: Final list for display
    - rationale: Why each tag was kept
    - stats: Selection statistics
    """
    
    if existing_tags is None:
        existing_tags = []
    
    selected = {}
    remaining_slots = max_total
    
    # Step 1: Keep mandatory tags (tipo:*, tema:* only - cat_* and grp_* are now in categoria/group fields)
    mandatory = [t for t in existing_tags if ':' in t]
    for tag in mandatory:
        selected[tag] = {
            'reason': 'MANDATORY (tipo:*, tema:*)',
            'confidence': 1.0,
            'source': 'mandatory'
        }
        remaining_slots -= 1
    
    if remaining_slots <= 0:
        return {
            'selected_tags': list(selected.keys()),
            'rationale': selected,
            'stats': {
                'total_selected': len(selected),
                'mandatory_count': len(mandatory),
                'suggested_count': 0,
                'max_total': max_total,
                'note': f'Reached max with mandatory tags only ({len(mandatory)} tags)'
            }
        }
    
    # Step 2: Keep existing non-mandatory tags (they have user intent)
    existing_non_mandatory = [t for t in existing_tags if t not in mandatory and t not in selected]
    for tag in existing_non_mandatory[:remaining_slots]:
        selected[tag] = {
            'reason': 'EXISTING (preserved)',
            'confidence': 1.0,
            'source': 'existing'
        }
        remaining_slots -= 1
    
    # Step 3: Add highest-confidence suggestions
    # Sort suggested tags by confidence
    sorted_suggestions = sorted(
        suggested_tags.items(),
        key=lambda x: x[1].get('confidence', 0),
        reverse=True
    )
    
    for tag, suggestion in sorted_suggestions:
        if remaining_slots <= 0:
            break
        
        if tag not in selected:
            selected[tag] = {
                'reason': f"SUGGESTED ({suggestion.get('source', 'rag')} confidence)",
                'confidence': suggestion.get('confidence', 0),
                'source': suggestion.get('source', 'rag')
            }
            remaining_slots -= 1
    
    return {
        'selected_tags': list(selected.keys()),
        'rationale': selected,
        'stats': {
            'total_selected': len(selected),
            'mandatory_count': len(mandatory),
            'existing_count': len([t for t in existing_non_mandatory if t in selected]),
            'suggested_count': len([s for s in selected.keys() if selected[s]['source'] != 'mandatory' and selected[s]['source'] != 'existing']),
            'max_total': max_total,
            'remaining_slots': remaining_slots
        }
    }


__all__ = ['select_tags_for_display']
