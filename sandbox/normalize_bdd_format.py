#!/usr/bin/env python3
"""
Normaliza formato BDD em user stories dos capítulos.

Padrão alvo (Cap 08 - IaC):
**Critérios de aceitação (BDD).**
- **Dado** um projeto IaC novo  
  **Quando** é inicializado  
  **Então** usa backend remoto...

Variações encontradas a corrigir:
- **BDD.** → **Critérios de aceitação (BDD).**
- Dado/Quando/Então sem bold → **Dado**/**Quando**/**Então**
- Bullets sem estrutura uniforme
"""

import re
import sys
from pathlib import Path


def normalize_bdd_section(content: str) -> str:
    """
    Normaliza seções BDD para formato padronizado.
    
    Formato correto (Cap 08):
    - **Dado** um texto...  
      **Quando** continua...  
      **Então** resultado...
    
    Ou seja:
    - Primeira linha (Dado): com bullet e bold
    - Linhas seguintes (Quando/Então): SEM bullet, 2 espaços indentação, bold
    """
    
    # Padrão 1: **BDD.** → **Critérios de aceitação (BDD).**
    content = re.sub(
        r'\*\*BDD\.\*\*',
        '**Critérios de aceitação (BDD).**',
        content
    )
    
    # Padrão 2: Normalizar estrutura de bullets BDD
    lines = content.split('\n')
    normalized_lines = []
    in_bdd_block = False
    
    for i, line in enumerate(lines):
        # Detectar início de bloco BDD
        if '**Critérios de aceitação (BDD).**' in line:
            in_bdd_block = True
            normalized_lines.append(line)
            continue
        
        # Detectar fim de bloco BDD (linha vazia, nova seção, ou DoD)
        if in_bdd_block and (
            line.strip() == '' or 
            line.startswith('**') and 'BDD' not in line or
            line.startswith(':::')
        ):
            in_bdd_block = False
        
        # Se estamos num bloco BDD, normalizar
        if in_bdd_block:
            # Linha com "Dado" → deve ter bullet
            if re.match(r'^\s*-?\s*\*?\*?Dado\s+', line):
                # Remover bullet e bold existentes, reconstruir
                clean_text = re.sub(r'^\s*-?\s*\*?\*?Dado\*?\*?\s+', '', line)
                normalized_lines.append(f'- **Dado** {clean_text}')
                continue
            
            # Linha com "Quando" → SEM bullet, 2 espaços
            elif re.match(r'^\s*-?\s*\*?\*?Quando\s+', line):
                clean_text = re.sub(r'^\s*-?\s*\*?\*?Quando\*?\*?\s+', '', line)
                normalized_lines.append(f'  **Quando** {clean_text}')
                continue
            
            # Linha com "Então" → SEM bullet, 2 espaços
            elif re.match(r'^\s*-?\s*\*?\*?Então\s+', line):
                clean_text = re.sub(r'^\s*-?\s*\*?\*?Então\*?\*?\s+', '', line)
                normalized_lines.append(f'  **Então** {clean_text}')
                continue
        
        # Linha normal, manter como está
        normalized_lines.append(line)
    
    return '\n'.join(normalized_lines)


def normalize_dod_section(content: str) -> str:
    """Normaliza seções DoD para formato padronizado."""
    
    # Padrão: **DoD.** → **Critérios de aceitação (DoD).**
    # (alguns capítulos usam DoD em vez de BDD)
    content = re.sub(
        r'\*\*DoD\.\*\*',
        '**Critérios de aceitação (DoD).**',
        content
    )
    
    return content


def process_file(filepath: Path) -> tuple[bool, int]:
    """
    Processa um ficheiro aplicando normalizações.
    
    Returns:
        (changed, num_replacements): Se houve alterações e quantas
    """
    
    try:
        original_content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"❌ Erro ao ler {filepath}: {e}", file=sys.stderr)
        return False, 0
    
    # Aplicar normalizações
    normalized_content = normalize_bdd_section(original_content)
    normalized_content = normalize_dod_section(normalized_content)
    
    # Verificar se houve mudanças
    if normalized_content == original_content:
        return False, 0
    
    # Contar substituições (aproximado)
    num_bdd = original_content.count('**BDD.**')
    num_dod = original_content.count('**DoD.**')
    num_dado = len(re.findall(r'^\s*-\s+Dado\s+', original_content, re.MULTILINE))
    num_quando = len(re.findall(r'^\s*-\s+Quando\s+', original_content, re.MULTILINE))
    num_entao = len(re.findall(r'^\s*-\s+Então\s+', original_content, re.MULTILINE))
    
    total_replacements = num_bdd + num_dod + num_dado + num_quando + num_entao
    
    # Escrever ficheiro normalizado
    try:
        filepath.write_text(normalized_content, encoding='utf-8')
        return True, total_replacements
    except Exception as e:
        print(f"❌ Erro ao escrever {filepath}: {e}", file=sys.stderr)
        return False, 0


def main():
    """Processa todos os ficheiros aplicacao-lifecycle.md dos capítulos."""
    
    base_dir = Path(__file__).parent.parent / 'manuals_src' / 'docs' / 'sbd-toe' / '010-sbd-manual'
    
    if not base_dir.exists():
        print(f"❌ Diretório base não encontrado: {base_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Excluir Cap 08 (já está correto - é o modelo)
    exclude_chapters = {'08-iac-infraestrutura'}
    
    # Encontrar todos os aplicacao-lifecycle.md
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
        print("⚠️  Nenhum ficheiro aplicacao-lifecycle.md encontrado", file=sys.stderr)
        sys.exit(0)
    
    print(f"🔍 Encontrados {len(lifecycle_files)} ficheiros para processar\n")
    
    total_changed = 0
    total_replacements = 0
    
    for filepath in lifecycle_files:
        chapter_name = filepath.parent.name
        changed, num_replacements = process_file(filepath)
        
        if changed:
            print(f"✅ {chapter_name}: {num_replacements} normalizações")
            total_changed += 1
            total_replacements += num_replacements
        else:
            print(f"⏭️  {chapter_name}: já normalizado")
    
    print(f"\n📊 Resumo:")
    print(f"   - Ficheiros alterados: {total_changed}/{len(lifecycle_files)}")
    print(f"   - Total de normalizações: {total_replacements}")
    
    if total_changed > 0:
        print(f"\n✅ Normalização concluída com sucesso!")
    else:
        print(f"\n⏭️  Nenhuma alteração necessária")


if __name__ == '__main__':
    main()
