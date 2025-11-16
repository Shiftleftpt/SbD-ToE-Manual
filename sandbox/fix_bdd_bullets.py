#!/usr/bin/env python3
"""
Corrige estrutura de bullets em blocos BDD.

FORMATO CORRETO (Cap 08):
**Critérios de aceitação (BDD).**
- **Dado** texto...  
  **Quando** continua...  
  **Então** resultado...

FORMATO ATUAL (errado):
**Critérios de aceitação (BDD).**
- **Dado** texto...  
- **Quando** continua...  
- **Então** resultado...

FIX: Remover bullet de linhas Quando/Então, adicionar 2 espaços.
"""

import re
import sys
from pathlib import Path


def fix_bdd_bullets(content: str) -> tuple[str, int]:
    """
    Corrige bullets em blocos BDD.
    
    Returns:
        (fixed_content, num_fixes)
    """
    
    lines = content.split('\n')
    fixed_lines = []
    in_bdd_block = False
    num_fixes = 0
    
    for i, line in enumerate(lines):
        # Detectar início de bloco BDD
        if '**Critérios de aceitação (BDD).**' in line:
            in_bdd_block = True
            fixed_lines.append(line)
            continue
        
        # Detectar fim de bloco BDD
        if in_bdd_block:
            # Fim se linha vazia, nova seção, ou checklist DoD
            if (line.strip() == '' or 
                (line.startswith('**') and 'Critérios' not in line) or
                line.startswith(':::') or
                re.match(r'^\s*-\s*\[\s*\]', line)):  # checklist
                in_bdd_block = False
        
        # Se estamos num bloco BDD, processar
        if in_bdd_block:
            # Linha com "Dado" → MANTER bullet
            if re.match(r'^\s*-\s+\*\*Dado\*\*\s+', line):
                fixed_lines.append(line)
                continue
            
            # Linha com "Quando" → REMOVER bullet, adicionar 2 espaços
            match_quando = re.match(r'^\s*-\s+(\*\*Quando\*\*.+)$', line)
            if match_quando:
                fixed_line = f'  {match_quando.group(1)}'
                fixed_lines.append(fixed_line)
                num_fixes += 1
                continue
            
            # Linha com "Então" → REMOVER bullet, adicionar 2 espaços
            match_entao = re.match(r'^\s*-\s+(\*\*Então\*\*.+)$', line)
            if match_entao:
                fixed_line = f'  {match_entao.group(1)}'
                fixed_lines.append(fixed_line)
                num_fixes += 1
                continue
        
        # Linha normal
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), num_fixes


def process_file(filepath: Path) -> tuple[bool, int]:
    """
    Processa um ficheiro.
    
    Returns:
        (changed, num_fixes)
    """
    
    try:
        original_content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"❌ Erro ao ler {filepath}: {e}", file=sys.stderr)
        return False, 0
    
    fixed_content, num_fixes = fix_bdd_bullets(original_content)
    
    if num_fixes == 0:
        return False, 0
    
    try:
        filepath.write_text(fixed_content, encoding='utf-8')
        return True, num_fixes
    except Exception as e:
        print(f"❌ Erro ao escrever {filepath}: {e}", file=sys.stderr)
        return False, 0


def main():
    """Processa todos os ficheiros aplicacao-lifecycle.md."""
    
    base_dir = Path(__file__).parent.parent / 'manuals_src' / 'docs' / 'sbd-toe' / '010-sbd-manual'
    
    if not base_dir.exists():
        print(f"❌ Diretório base não encontrado: {base_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Excluir Cap 08 e 09 (já corretos)
    exclude_chapters = {'08-iac-infraestrutura', '09-containers-imagens'}
    
    lifecycle_files = []
    for chapter_dir in sorted(base_dir.iterdir()):
        if not chapter_dir.is_dir():
            continue
        if chapter_dir.name in exclude_chapters:
            continue
            
        lifecycle_file = chapter_dir / 'aplicacao-lifecycle.md'
        if lifecycle_file.exists():
            lifecycle_files.append(lifecycle_file)
    
    if not lifecycle_files:
        print("⚠️  Nenhum ficheiro encontrado", file=sys.stderr)
        sys.exit(0)
    
    print(f"🔍 Processando {len(lifecycle_files)} ficheiros\n")
    
    total_changed = 0
    total_fixes = 0
    
    for filepath in lifecycle_files:
        chapter_name = filepath.parent.name
        changed, num_fixes = process_file(filepath)
        
        if changed:
            print(f"✅ {chapter_name}: {num_fixes} bullets corrigidos")
            total_changed += 1
            total_fixes += num_fixes
        else:
            print(f"⏭️  {chapter_name}: já correto")
    
    print(f"\n📊 Resumo:")
    print(f"   - Ficheiros alterados: {total_changed}/{len(lifecycle_files)}")
    print(f"   - Total de bullets corrigidos: {total_fixes}")


if __name__ == '__main__':
    main()
