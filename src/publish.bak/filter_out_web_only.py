#!/usr/bin/env python3

import re
import sys
import argparse
from pathlib import Path

def remover_blocos_web_only(texto):
    # Remove blocos entre <!--web-only--> ... <!--web-only:end-->
    return re.sub(
        r'<!--\s*web-only\s*-->(.*?)<!--\s*web-only:end\s*-->',
        '',
        texto,
        flags=re.DOTALL | re.IGNORECASE
    )

def processar_ficheiro(ficheiro):
    conteudo = Path(ficheiro).read_text(encoding="utf-8")
    novo_conteudo = remover_blocos_web_only(conteudo)
    Path(ficheiro).write_text(novo_conteudo, encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove blocos web-only dos markdowns de um diretório.")
    parser.add_argument("inputdir", type=str, help="Diretório a processar")
    args = parser.parse_args()
    inputdir = args.inputdir

    print(f"[INFO] A remover blocos web-only nos ficheiros de: {inputdir}")
    for ficheiro in Path(inputdir).rglob("*.md"):
        if ficheiro.name.startswith("_") or ficheiro.name.startswith("README"):
            continue
        processar_ficheiro(ficheiro)
