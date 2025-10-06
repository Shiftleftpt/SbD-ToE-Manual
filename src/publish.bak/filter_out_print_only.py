# filter_out_print_only.py
import re
import sys
import argparse
from pathlib import Path

def remover_blocos_print_only(texto):
    return re.sub(
        r'<!--\s*print-only\s*-->(.*?)<!--\s*print-only:end\s*-->',
        '',
        texto,
        flags=re.DOTALL | re.IGNORECASE
    )

def processar_ficheiro(ficheiro):
    conteudo = Path(ficheiro).read_text(encoding="utf-8")
    novo_conteudo = remover_blocos_print_only(conteudo)
    Path(ficheiro).write_text(novo_conteudo, encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processa os ficheiros Markdown.")
    parser.add_argument("--inputdir", "--input-dir", dest="inputdir", default="docs",
                        help="Diretório de entrada com ficheiros .md")
    args = parser.parse_args()
    inputdir = Path(args.inputdir).resolve()
    print(f"[INFO] A processar ficheiros em: {inputdir}")
    for ficheiro in Path(inputdir).rglob("*.md"):
        if ficheiro.name.startswith("_") or ficheiro.name.startswith("README"):
            continue
        processar_ficheiro(ficheiro)
