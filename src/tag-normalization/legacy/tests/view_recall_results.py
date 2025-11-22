#!/usr/bin/env python3
"""
View and analyze saved multi-file recall test results
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def load_latest_results():
    """Load the most recent test results"""
    results_dir = Path(__file__).parent / "results"
    
    json_files = sorted(results_dir.glob("multifile_recall_analysis_*.json"))
    if not json_files:
        print("❌ No results found!")
        return None
    
    latest = json_files[-1]
    print(f"📂 Loading: {latest.name}\n")
    
    with open(latest, 'r') as f:
        return json.load(f)

def print_summary(data):
    """Print summary statistics"""
    summary = data['summary']
    
    print("="*100)
    print("📊 SUMMARY STATISTICS")
    print("="*100)
    print(f"\nTest Type:           {data['test_type']}")
    print(f"Timestamp:           {data['timestamp']}")
    print(f"Files analyzed:      {summary['files_analyzed']}")
    print(f"Total existing tags: {summary['total_existing_tags']}")
    print(f"Re-detected:         {summary['total_re_detected']}")
    print(f"Missed:              {summary['total_missed']}")
    print(f"Average recall:      {summary['average_recall_percentage']:.1f}%")
    print(f"New suggestions:     {summary['total_new_suggestions']}")
    print()

def print_file_details(file_data):
    """Print detailed analysis for one file"""
    print(f"\n{'='*100}")
    print(f"📄 {file_data['filename']}")
    print(f"   Path: {file_data['filepath']}")
    print(f"   Size: {file_data['content_length']:,} characters")
    print(f"{'='*100}\n")
    
    # Existing tags
    print(f"EXISTING TAGS ({file_data['existing_count']}):")
    for tag in file_data['existing_tags']:
        print(f"  • {tag}")
    
    # Re-detected
    print(f"\nRE-DETECTED BY ROBOT ({file_data['re_detected_count']}/{file_data['existing_count']}):")
    if file_data['re_detected']:
        for item in file_data['re_detected']:
            print(f"  ✓ {item['tag']:<20} {item['confidence']*100:>6.0f}%")
    else:
        print(f"  [None]")
    
    # Missed
    if file_data['missed_tags']:
        print(f"\nMISSED BY ROBOT ({file_data['missed_count']}):")
        for tag in file_data['missed_tags']:
            print(f"  ✗ {tag}")
    
    # New suggestions
    print(f"\nNEW SUGGESTIONS ({file_data['new_suggestions_count']}):")
    for i, sugg in enumerate(file_data['new_suggestions'][:5], 1):
        print(f"  {i}. {sugg['tag']:<20} {sugg['confidence']*100:>6.0f}%")
    
    if file_data['new_suggestions_count'] > 5:
        print(f"  ... and {file_data['new_suggestions_count'] - 5} more")
    
    # Recall
    print(f"\nRECALL: {file_data['recall_percentage']:.1f}%")

def print_comparison_table(data):
    """Print comparison table of all files"""
    print("\n" + "="*100)
    print("📋 FILE COMPARISON TABLE")
    print("="*100 + "\n")
    
    print(f"{'File':<35} {'Existing':<12} {'Re-detected':<15} {'Missed':<12} {'Recall':<10}")
    print(f"{'-'*100}")
    
    for file_data in data['files']:
        filename = file_data['filename'][:33]
        existing = file_data['existing_count']
        detected = file_data['re_detected_count']
        missed = file_data['missed_count']
        recall = file_data['recall_percentage']
        
        print(f"{filename:<35} {existing:<12} {detected:<15} {missed:<12} {recall:<10.1f}%")
    
    print()

def main():
    data = load_latest_results()
    if not data:
        sys.exit(1)
    
    # Print summary
    print_summary(data)
    
    # Print comparison table
    print_comparison_table(data)
    
    # Print detailed analysis for each file
    if len(sys.argv) > 1 and sys.argv[1] == '--detailed':
        for file_data in data['files']:
            print_file_details(file_data)
    else:
        print("💡 Tip: Run with --detailed to see full analysis for each file")
        print("   python3 view_recall_results.py --detailed")

if __name__ == "__main__":
    main()
