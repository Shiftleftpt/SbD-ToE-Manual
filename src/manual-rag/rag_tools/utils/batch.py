"""Auto-tagging batch processor for all manual files"""

import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime
import yaml

from .tagging import AutoTagger, FileTagUpdater
from .config import MANUAL_ROOT, INDEX_DIR


class BatchAutoTagger:
    """Process auto-tagging for entire manual corpus"""
    
    def __init__(self):
        self.tagger = AutoTagger()
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'updated': 0,
            'skipped': 0,
            'errors': 0,
            'tags_added': 0,
            'tags_removed': 0,
            'files_updated': []
        }
    
    def find_all_files(self) -> List[Path]:
        """Find all markdown files excluding .2review files"""
        md_files = list(MANUAL_ROOT.rglob("*.md"))
        md_files = [f for f in md_files if not f.name.endswith(".2review")]
        return sorted(md_files)
    
    def process_file(self, file_path: Path, strategy: str = 'balanced', 
                     dry_run: bool = False, verbose: bool = False) -> Dict:
        """Process single file
        
        Args:
            file_path: Path to markdown file
            strategy: 'conservative', 'balanced', or 'aggressive'
            dry_run: Don't write changes
            verbose: Print details
        
        Returns:
            Processing result
        """
        try:
            relative_path = file_path.relative_to(MANUAL_ROOT)
            
            # Read file
            frontmatter, content = FileTagUpdater.read_frontmatter(file_path)
            existing_tags = frontmatter.get('tags', [])
            title = frontmatter.get('title', file_path.stem)
            
            # Get suggestions
            suggestions = self.tagger.suggest_tags(
                str(relative_path),
                content,
                title,
                existing_tags,
                min_confidence=0.35
            )
            
            # Merge tags
            merged_tags, new_tags = self.tagger.merge_tags(
                existing_tags,
                suggestions,
                strategy=strategy
            )
            
            # Update file
            changes = FileTagUpdater.update_tags(file_path, merged_tags, dry_run=dry_run)
            
            result = {
                'file': str(relative_path),
                'status': 'updated' if changes['updated'] else 'unchanged',
                'existing_tags': existing_tags,
                'new_tags': merged_tags,
                'added': changes['added'],
                'removed': changes['removed'],
                'suggestions_count': len(suggestions),
                'top_suggestion': suggestions[0].tag if suggestions else None
            }
            
            # Update stats
            self.stats['processed'] += 1
            if changes['updated']:
                self.stats['updated'] += 1
                self.stats['tags_added'] += len(changes['added'])
                self.stats['tags_removed'] += len(changes['removed'])
                self.stats['files_updated'].append(result)
                
                if verbose:
                    print(f"✓ {relative_path}")
                    if changes['added']:
                        print(f"  + Added: {', '.join(changes['added'])}")
                    if changes['removed']:
                        print(f"  - Removed: {', '.join(changes['removed'])}")
            else:
                self.stats['skipped'] += 1
                if verbose and suggestions:
                    print(f"~ {relative_path} (no changes, but {len(suggestions)} suggestions available)")
            
            return result
        
        except Exception as e:
            self.stats['errors'] += 1
            print(f"✗ Error processing {file_path}: {e}")
            return {'file': str(file_path), 'status': 'error', 'error': str(e)}
    
    def process_all(self, strategy: str = 'balanced', dry_run: bool = False,
                   verbose: bool = False, sample_size: int = None) -> Dict:
        """Process all manual files
        
        Args:
            strategy: 'conservative', 'balanced', or 'aggressive'
            dry_run: Don't write changes
            verbose: Print progress
            sample_size: Process only N files (for testing)
        
        Returns:
            Summary statistics
        """
        files = self.find_all_files()
        
        if sample_size:
            files = files[:sample_size]
        
        self.stats['total_files'] = len(files)
        
        print(f"Processing {len(files)} files with {strategy} strategy...")
        if dry_run:
            print("(DRY RUN - no files will be modified)")
        print()
        
        results = []
        for i, file_path in enumerate(files, 1):
            if verbose or i % 10 == 0:
                print(f"[{i}/{len(files)}] Processing {file_path.relative_to(MANUAL_ROOT)}...")
            
            result = self.process_file(file_path, strategy, dry_run, verbose=False)
            results.append(result)
        
        self.stats['results'] = results
        return self.stats
    
    def save_report(self, output_path: Path):
        """Save processing report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_files': self.stats['total_files'],
                'processed': self.stats['processed'],
                'updated': self.stats['updated'],
                'skipped': self.stats['skipped'],
                'errors': self.stats['errors'],
                'tags_added': self.stats['tags_added'],
                'tags_removed': self.stats['tags_removed']
            },
            'updated_files': self.stats['files_updated'][:100]  # Top 100
        }
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Report saved to {output_path}")
    
    def print_summary(self):
        """Print summary statistics"""
        print("\n" + "="*60)
        print("AUTO-TAGGING SUMMARY")
        print("="*60)
        print(f"Total files:     {self.stats['total_files']}")
        print(f"Processed:       {self.stats['processed']}")
        print(f"Updated:         {self.stats['updated']} ({self.stats['updated']*100//max(self.stats['processed'],1)}%)")
        print(f"Skipped:         {self.stats['skipped']}")
        print(f"Errors:          {self.stats['errors']}")
        print(f"Tags added:      {self.stats['tags_added']}")
        print(f"Tags removed:    {self.stats['tags_removed']}")
        print("="*60)
