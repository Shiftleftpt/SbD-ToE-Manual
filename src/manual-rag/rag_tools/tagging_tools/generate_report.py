#!/usr/bin/env python3
"""
Generate Markdown Report from Comparison
Converte o JSON de comparação num relatório Markdown legível
"""

import json
import sys
from pathlib import Path
from typing import Dict, List

def generate_markdown_report(comparison_json_file: str, output_file: str = None):
    """Gerar relatório Markdown a partir do JSON de comparação"""
    
    # Read JSON
    with open(comparison_json_file, 'r') as f:
        data = json.load(f)
    
    # Default output filename
    if not output_file:
        input_path = Path(comparison_json_file)
        output_file = input_path.parent / input_path.stem.replace('comparison_', 'report_') / '.md'
    
    # Build markdown
    md = []
    
    md.append(f"# 📊 Tag Comparison Report")
    md.append(f"\n**Chapter**: {data['chapter']}")
    if data.get('subfolder'):
        md.append(f"  \n**Subfolder**: {data['subfolder']}")
    md.append(f"  \n**Documents Analyzed**: {data['documents_analyzed']}")
    md.append(f"  \n**Ollama Available**: {'✅ Yes' if data['ollama_available'] else '❌ No'}")
    
    md.append(f"\n---\n")
    md.append(f"## 📋 Detailed Comparison\n")
    
    for idx, result in enumerate(data['results'], 1):
        md.append(f"\n### [{idx}] {result['file_path']}")
        md.append(f"\n**Title**: {result['title']}")
        
        comp = result['comparison']
        
        md.append(f"\n#### Tags Overview")
        md.append(f"\n| Source | Count | Tags |")
        md.append(f"|--------|-------|------|")
        md.append(f"| Original (Index) | {comp['original_count']} | {', '.join(result['original_tags'][:3])}{'...' if len(result['original_tags']) > 3 else ''} |")
        md.append(f"| LOCAL Analysis | {comp['local_count']} | {', '.join(result['local_tags'][:3])}{'...' if len(result['local_tags']) > 3 else ''} |")
        
        if data['ollama_available'] and result['ollama_tags']:
            md.append(f"| OLLAMA Analysis | {comp['ollama_count']} | {', '.join(result['ollama_tags'][:3])}{'...' if len(result['ollama_tags']) > 3 else ''} |")
        
        md.append(f"\n#### Comparison Results")
        
        md.append(f"\n**LOCAL vs Original:**")
        md.append(f"- ✓ Matches: **{comp['local_matches_original']}/{comp['original_count']}** ({100*comp['local_matches_original']/max(comp['original_count'],1):.0f}%)")
        md.append(f"- ⊕ New tags: **{comp['local_new_count']}** - {', '.join(comp['local_new'][:5])}")
        md.append(f"- ⊖ Removed: **{comp['local_removed_count']}**")
        
        if data['ollama_available'] and result['ollama_tags']:
            md.append(f"\n**OLLAMA vs Original:**")
            md.append(f"- ✓ Matches: **{comp['ollama_matches_original']}/{comp['original_count']}** ({100*comp['ollama_matches_original']/max(comp['original_count'],1):.0f}%)")
            md.append(f"- ⊕ New tags: **{comp['ollama_new_count']}** - {', '.join(comp['ollama_new'][:5])}")
            md.append(f"- ⊖ Removed: **{comp['ollama_removed_count']}**")
            
            md.append(f"\n**LOCAL vs OLLAMA Agreement:**")
            md.append(f"- ✓ Both suggest: **{comp['local_vs_ollama_matches']}**")
            md.append(f"- ⊕ Only LOCAL: **{len(comp['local_unique'])}** - {', '.join(comp['local_unique'][:3])}")
            md.append(f"- ⊕ Only OLLAMA: **{len(comp['ollama_unique'])}** - {', '.join(comp['ollama_unique'][:3])}")
    
    md.append(f"\n---\n")
    md.append(f"## 📊 Summary Statistics\n")
    
    summary = data.get('summary', {})
    
    md.append(f"\n### LOCAL Strategy Performance:")
    md.append(f"- Average matches with original: **{summary.get('local_avg_matches', 0):.1f}** tags")
    md.append(f"- Average new tags proposed: **{data['documents_analyzed'] - summary.get('local_avg_matches', 0):.1f}**")
    
    if data['ollama_available']:
        md.append(f"\n### OLLAMA Strategy Performance:")
        md.append(f"- Average matches with original: **{summary.get('ollama_avg_matches', 0):.1f}** tags")
        md.append(f"- Average new tags proposed: **{data['documents_analyzed'] - summary.get('ollama_avg_matches', 0):.1f}**")
        
        md.append(f"\n### Comparison (LOCAL vs OLLAMA):")
        md.append(f"- **LOCAL** and **OLLAMA** agreement: Low")
        md.append(f"- This suggests original tags may be incomplete or outdated")
        md.append(f"- **Recommendation**: Use both strategies to validate suggestions")
    
    # Write file
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(md))
    
    print(f"✅ Markdown report generated: {output_path}")
    return output_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 generate_report.py <comparison_json_file> [output_markdown_file]")
        sys.exit(1)
    
    json_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    generate_markdown_report(json_file, output_file)
