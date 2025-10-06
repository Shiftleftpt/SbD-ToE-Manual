#!/usr/bin/env python3
"""
Concatena os conteúdos Markdown definidos em book.yml e gera um ficheiro .md unificado para Eisvogel.
"""

import yaml
from pathlib import Path
import re
import argparse

def load_book(yml):
    with open(yml, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def sanitize_title(name):
    return name.replace('-', ' ').title()

def escape_yaml(s):
    return str(s).replace('"', '\\"') if s else ""

def fix_triple_dash_lines(md_text):
    lines = md_text.splitlines()
    fixed_lines = []
    n = len(lines)
    for i, line in enumerate(lines):
        if re.match(r'^\s*---\s*$', line):
            # Inserir linha vazia antes se não existir
            if i == 0 or lines[i-1].strip() != '':
                fixed_lines.append('')
            fixed_lines.append(line)
            # Inserir linha vazia depois se não existir
            if i == n-1 or lines[i+1].strip() != '':
                fixed_lines.append('')
        else:
            fixed_lines.append(line)
    return '\n'.join(fixed_lines)

def remove_frontmatter(md_text):
    return re.sub(r'^---\s*\n.*?\n---\s*\n', '', md_text, flags=re.DOTALL)

import yaml

def write_yaml_frontmatter(book, out):
    yaml_block = book.get('pandoc_yaml', {})
    out.write("---\n")
    # Dump YAML (preserva listas, etc.)
    yaml.dump(yaml_block, out, allow_unicode=True, sort_keys=False)
    out.write("---\n\n")

def main():
    parser = argparse.ArgumentParser(description="Concatena Markdown segundo book.yml para Eisvogel.")
    parser.add_argument('--book', type=str, default="book.yml", help="Caminho para o book.yml")
    parser.add_argument('--outdir', type=str, default="../BOOK/pdf", help="Diretório para o output do markdown")
    args = parser.parse_args()

    BOOK_FILE = args.book
    OUT_DIR = args.outdir
    OUT_MD = Path(OUT_DIR) / "manual-sbd-toe.md"

    src_dir = Path(BOOK_FILE).parent
    print(f"[INFO] A gerar markdown unificado para Eisvogel usando {BOOK_FILE}")
    book = load_book(BOOK_FILE)
    structure = book.get("structure", [])

    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

    with open(OUT_MD, 'w', encoding='utf-8') as out:
        # YAML header para Eisvogel
        write_yaml_frontmatter(book, out)
        for section in structure:
            if not section.get("include", True):
                continue
            section_title = section.get("section", "")
            out.write(f"# {section_title}\n\n")

            for chapter in section.get("chapters", []):
                if "file" in chapter:
                    full_path = Path(chapter["file"])
                    if not full_path.is_absolute():
                        full_path = src_dir / full_path
                    if full_path.exists():
                        out.write(f"# {sanitize_title(full_path.stem)}\n\n")
                        with open(full_path, 'r', encoding='utf-8') as f:
                            raw = f.read()
                            cleaned = remove_frontmatter(raw)
                            cleaned = fix_triple_dash_lines(cleaned)
                            out.write(cleaned.strip() + "\n\n\\newpage\n\n")
                    else:
                        print(f"[⚠️ AVISO] Ficheiro não encontrado: {full_path}")
                    continue

                chapter_id = chapter.get("id", "")
                chapter_title = chapter.get("title", sanitize_title(chapter_id))
                chapter_dir = src_dir / chapter_id

                out.write(f"# {chapter_title}\n\n")

                for pattern in chapter.get("files", []):
                    for path in sorted(chapter_dir.glob(pattern)):
                        out.write(f"## {sanitize_title(path.stem)}\n\n")
                        with open(path, 'r', encoding='utf-8') as f:
                            raw = f.read()
                            cleaned = remove_frontmatter(raw)
                            cleaned = fix_triple_dash_lines(cleaned)
                            out.write(cleaned.strip() + "\n\n\\newpage\n\n")
        # Insere o índice (TOC) no final do documento
        out.write("\n# Índice\n\n")
        out.write("\\tableofcontents\n\n")

    print(f"[✓] Markdown unificado gerado em: {OUT_MD}")
    print("[INFO] Para gerar o PDF, correr manualmente: pandoc manual-sbd-toe.md --from markdown --template eisvogel --pdf-engine=xelatex -o manual-sbd-toe.pdf")

if __name__ == "__main__":
    main()
