"""Main CLI - unified interface for tag system."""

import sys
import argparse
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tag_system.core import CanonicalTagsManager
from tag_system.validators import ValidationEngine
from tag_system.recommenders import RecommendationEngine


class TagSystemCLI:
    """Unified CLI for tag validation and recommendations."""
    
    def __init__(self):
        self.canonical_path = Path(__file__).parent.parent.parent / "canonical-tags.yml"
        self.canonical = CanonicalTagsManager(str(self.canonical_path))
        self.validator = ValidationEngine(self.canonical)
        self.recommender = RecommendationEngine(self.canonical)
    
    def cmd_validate(self, args):
        """Validate tags in files."""
        base_path = args.base_path or Path.cwd()
        
        print(f"📋 Validating tags in: {base_path}\n")
        
        results = self.validator.validate_batch(str(base_path))
        
        if not results:
            print("✅ No validation issues found!")
            return
        
        error_count = 0
        warning_count = 0
        
        for result in results:
            if result.error_count > 0:
                error_count += result.error_count
                print(f"❌ {result.filepath}")
            else:
                print(f"⚠️  {result.filepath}")
            
            for issue in result.issues:
                icon = "❌" if issue.severity.value == "error" else "⚠️"
                print(f"  {icon} {issue.message}")
                if issue.suggestion:
                    print(f"     → {issue.suggestion}")
            
            warning_count += result.warning_count
        
        print(f"\n📊 Summary: {error_count} errors, {warning_count} warnings")
    
    def cmd_recommend(self, args):
        """Recommend tags for files."""
        base_path = args.base_path or Path.cwd()
        
        print(f"💡 Recommending tags for: {base_path}\n")
        
        base = Path(base_path)
        md_files = sorted(base.rglob('*.md')) + sorted(base.rglob('*.mdx'))
        
        if args.limit:
            md_files = md_files[:args.limit]
        
        for md_file in md_files:
            recommendations = self.recommender.recommend_tags(str(md_file))
            
            if not recommendations:
                continue
            
            title = md_file.stem
            print(f"📄 {md_file.name}")
            
            for rec in recommendations:
                print(f"  💬 {rec.tag:<25} ({rec.confidence:.1%}) - {rec.reason}")
            print()
    
    def cmd_audit(self, args):
        """Full audit: validate + recommend."""
        print("🔍 Starting full audit...\n")
        
        self.cmd_validate(args)
        print("\n" + "="*70 + "\n")
        self.cmd_recommend(args)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Tag Validation & Recommendation System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  tag-system validate --base-path ./docs
  tag-system recommend --base-path ./docs --limit 10
  tag-system audit --base-path ./docs
        """
    )
    
    parser.add_argument('--base-path', help='Base path for analysis (default: current dir)')
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # validate command
    sub_validate = subparsers.add_parser('validate', help='Validate existing tags')
    
    # recommend command
    sub_recommend = subparsers.add_parser('recommend', help='Recommend tags')
    sub_recommend.add_argument('--limit', type=int, help='Limit number of files')
    
    # audit command
    sub_audit = subparsers.add_parser('audit', help='Full audit: validate + recommend')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    cli = TagSystemCLI()
    
    if args.command == 'validate':
        cli.cmd_validate(args)
    elif args.command == 'recommend':
        cli.cmd_recommend(args)
    elif args.command == 'audit':
        cli.cmd_audit(args)


if __name__ == '__main__':
    main()
