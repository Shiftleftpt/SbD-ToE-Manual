#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, hashlib
from pathlib import Path
import pandas as pd

PROMPT_TMPL = """És um assistente técnico-editorial a escrever em **Português (Portugal)**, com **rigor técnico-científico**.
Tarefa: redigir o ficheiro `canon/25-rastreabilidade.md` do capítulo **{chapter} {chapter_name}**, seguindo o **modelo canónico** do SbD-ToE.

Instruções (obrigatórias):
- Mantém o título, o frontmatter e a estrutura da tabela **exactamente como no exemplo**.
- Escreve uma **introdução breve** (2–4 frases) que explique o papel da rastreabilidade como **evidência de completude**.
- Usa a **tabela abaixo** para preencher os mapeamentos (não acrescentes colunas).
- Acrescenta uma **secção final** “Notas por framework” com 1–2 pontos por framework presente neste capítulo.
- **Não alteres** a taxonomia dos controlos.
- Regista o uso de IA no frontmatter: `ai_generated: true` e inclui `ai_source_csv_hash: '{csv_hash}'`.

Dados do capítulo (CSV → tabela):
{table}

Estilo e consistência:
- Linguagem prescritiva, objectiva e concisa.
- Alinha com `intro.md` (badges) e `20-checklist-revisao.md`.
- Só introduz proporcionalidade L1–L3 quando estiver **explicitamente** prevista nas práticas.

Devolve **apenas** o conteúdo markdown final de `25-rastreabilidade.md`, pronto a colar.
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--prompts-out", required=True)
    ap.add_argument("--repo-root", required=True, help="Raiz dos capítulos para localizar nomes")
    args = ap.parse_args()

    src = Path(args.csv)
    df = pd.read_csv(src).fillna("")
    import hashlib
    csv_hash = hashlib.sha1(src.read_bytes()).hexdigest()[:12]

    out = Path(args.prompts_out); out.mkdir(parents=True, exist_ok=True)
    repo = Path(args.repo_root)

    for chap, chunk in df.groupby("chapter"):
        chap = f"{int(chap):02d}"
        cap_dir = next(iter(sorted(repo.glob(f"{chap}-*"))), None)
        chapter_name = chunk["chapter_name"].iloc[0] if "chapter_name" in chunk.columns else (cap_dir.name.split("-",1)[1] if cap_dir else "")
        # construir tabela markdown a partir do CSV filtrado
        cols = ["framework","control","practice_id","practice_name","how_it_maps","notes"]
        table_header = "| Framework | Controlo | Prática (ID) | Prática | Como mapeia | Notas |\n|---|---|---|---|---|---|"
        lines = [table_header]
        for _, r in chunk.iterrows():
            row = [str(r.get(c,"")).replace("|","\\|").replace("\n"," ") for c in cols]
            lines.append("| " + " | ".join(row) + " |")
        prompt = PROMPT_TMPL.format(chapter=chap, chapter_name=chapter_name, table="\n".join(lines), csv_hash=csv_hash)
        out_file = out / f"{chap}_rastreabilidade_prompt.md"
        out_file.write_text(prompt, encoding="utf-8")
        print(f"[OK] {out_file}")

if __name__ == "__main__":
    main()
