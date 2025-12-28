"""Quality validation and analysis for auto-tagged files"""

import json
from pathlib import Path
from typing import Dict, List
from collections import defaultdict
import yaml

from manual_rag.tagging import FileTagUpdater, CanonicalTags
from rag_core.config import MANUAL_ROOT


class TagQualityAnalyzer:
    """Analyze quality of tags across the corpus"""
    
    def __init__(self):
        self.canonical = CanonicalTags()
        self.stats = {
            'total_files': 0,
            'files_with_tags': 0,
            'total_tags': 0,
            'invalid_tags': [],
            'tag_distribution': defaultdict(int),
            'files_by_tag_count': defaultdict(list),
            'problematic_files': []
        }
    
    def analyze_corpus(self) -> Dict:
        """Analyze all files for tag quality"""
        md_files = sorted(MANUAL_ROOT.rglob("*.md"))
        md_files = [f for f in md_files if not f.name.endswith(".2review")]
        
        self.stats['total_files'] = len(md_files)
        
        for file_path in md_files:
            frontmatter, _ = FileTagUpdater.read_frontmatter(file_path)
            tags = frontmatter.get('tags', [])
            
            if tags:
                self.stats['files_with_tags'] += 1
                self.stats['total_tags'] += len(tags)
                
                relative_path = str(file_path.relative_to(MANUAL_ROOT))
                tag_count = len(tags)
                self.stats['files_by_tag_count'][tag_count].append(relative_path)
                
                for tag in tags:
                    normalized = self.canonical.normalize(tag)
                    if not normalized:
                        self.stats['invalid_tags'].append({
                            'file': relative_path,
                            'tag': tag
                        })
                    else:
                        self.stats['tag_distribution'][normalized] += 1
        
        # Identify problematic files
        for tag_count, files in self.stats['files_by_tag_count'].items():
            if tag_count > 15:  # Too many tags
                for f in files:
                    self.stats['problematic_files'].append({
                        'file': f,
                        'issue': f'Too many tags ({tag_count})',
                        'severity': 'medium'
                    })
            elif tag_count == 0:  # No tags
                for f in files:
                    self.stats['problematic_files'].append({
                        'file': f,
                        'issue': 'No tags',
                        'severity': 'low'
                    })
        
        return self.stats
    
    def print_report(self):
        """Print analysis report"""
        print("\n" + "="*70)
        print("TAG QUALITY ANALYSIS REPORT")
        print("="*70)
        
        print(f"\nCORPUS STATS:")
        print(f"  Total files:       {self.stats['total_files']}")
        print(f"  Files with tags:   {self.stats['files_with_tags']} ({self.stats['files_with_tags']*100//max(self.stats['total_files'],1)}%)")
        print(f"  Total tags:        {self.stats['total_tags']}")
        print(f"  Avg tags/file:     {self.stats['total_tags']//max(self.stats['files_with_tags'],1)}")
        
        if self.stats['invalid_tags']:
            print(f"\nINVALID TAGS: {len(self.stats['invalid_tags'])}")
            for issue in self.stats['invalid_tags'][:10]:
                print(f"  {issue['file']}: {issue['tag']}")
            if len(self.stats['invalid_tags']) > 10:
                print(f"  ... and {len(self.stats['invalid_tags'])-10} more")
        
        print(f"\nTAG DISTRIBUTION (Top 15):")
        sorted_tags = sorted(self.stats['tag_distribution'].items(), key=lambda x: x[1], reverse=True)
        for tag, count in sorted_tags[:15]:
            pct = count * 100 // max(self.stats['total_tags'], 1)
            bar = '█' * (pct // 5)
            print(f"  {tag:20} {count:4} ({pct:3}%) {bar}")
        
        print(f"\nFILE TAG COUNT DISTRIBUTION:")
        for count in sorted(self.stats['files_by_tag_count'].keys()):
            files = len(self.stats['files_by_tag_count'][count])
            print(f"  {count:2} tags: {files:3} files")
        
        if self.stats['problematic_files']:
            print(f"\nPROBLEMATIC FILES: {len(self.stats['problematic_files'])}")
            for issue in self.stats['problematic_files'][:10]:
                print(f"  [{issue['severity']}] {issue['file']}: {issue['issue']}")
            if len(self.stats['problematic_files']) > 10:
                print(f"  ... and {len(self.stats['problematic_files'])-10} more")
        
        print("\n" + "="*70)
    
    def save_report(self, output_path: Path):
        """Save report to JSON"""
        report = {
            'corpus_stats': {
                'total_files': self.stats['total_files'],
                'files_with_tags': self.stats['files_with_tags'],
                'total_tags': self.stats['total_tags'],
                'average_tags_per_file': self.stats['total_tags'] // max(self.stats['files_with_tags'], 1)
            },
            'invalid_tags': self.stats['invalid_tags'][:100],
            'tag_distribution': dict(sorted(self.stats['tag_distribution'].items(), 
                                           key=lambda x: x[1], reverse=True)[:50]),
            'problematic_files': self.stats['problematic_files'][:100]
        }
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Report saved to {output_path}")


if __name__ == '__main__':
    analyzer = TagQualityAnalyzer()
    analyzer.analyze_corpus()
    analyzer.print_report()
    analyzer.save_report(Path('tag-quality-report.json'))
