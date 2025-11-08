#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, hashlib
from pathlib import Path
import pandas as pd

HEADER = ["framework","control","chapter","chapter_name","practice_id","practice_name","how_it_maps","notes","source_ref"]

MD_TEMPLATE = """---
id: rastreabilidade
title: Rastreabilidade (Top-Down)
description: Como as práticas deste capítulo mapeiam para frameworks e controlos.
tags: [rastreabilidade, conformidade, evidência]
sidebar_position: 25
ai_generated: false
ai_prompt_ref: {prompt_ref}
---

# 🔗 Rastreabilidade — {chapter} {chapter_name}

> Esta secção mostra como as práticas prescritas **respondem** aos controlos das frameworks. A tabela abaixo é gerada a partir de uma fonte única (CSV) e serve de **evidência de completude**.

| Framework | Controlo | Prática (ID) | Prática (nome) | Como mapeia | Notas |
|---|---|---|---|---|---|
{rows}

<!-- Notas editoriais -->
- Fonte: `{csv_src}` (hash: `{csv_hash}`)
- Manter consistência com `intro.md` e `20-checklist-revisao.md`.
- Esta versão é a base *pré-edição*. O enriquecimento textual pode ser feito com IA, usando o prompt em `{prompt_ref}`.
"""

def emit_table_rows(df):
    def esc(x):
        return str(x).replace("|","\\|").replace("\n"," ").strip()
    lines = []
    for _, r in df.iterrows():
        lines.append(f"| {esc(r.framework)} | {esc(r.control)} | {esc(r.practice_id)} | {esc(r.practice_name)} | {esc(r.how_it_maps)} | {esc(r.notes)} |")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--out-root", required=True, help="Raiz dos capítulos (ex. manuals_src/docs/sbd-toe)")
    ap.add_argument("--emit-md", action="store_true", help="Gerar 25-rastreabilidade.md base por capítulo")
    args = ap.parse_args()

    src = Path(args.csv)
    df = pd.read_csv(src).fillna("")
    if set(HEADER) - set(df.columns):
        missing = sorted(set(HEADER) - set(df.columns))
        raise SystemExit(f"CSV sem colunas obrigatórias: {missing}")

    csv_hash = hashlib.sha1(src.read_bytes()).hexdigest()[:12]
    out_root = Path(args.out_root)

    for chap, chunk in df.groupby("chapter"):
        chap = f"{int(chap):02d}"
        # procurar diretório do capítulo
        matchs = sorted(p for p in out_root.glob(f"{chap}-*") if p.is_dir())
        if not matchs:
            print(f"[WARN] Capítulo {chap} sem diretório encontrado em {out_root}")
            continue
        cap_dir = matchs[0]
        canon = cap_dir / "canon"
        canon.mkdir(exist_ok=True)

        # escrever CSV por capítulo (audit trail)
        out_csv = canon / "25-rastreabilidade.csv"
        chunk.to_csv(out_csv, index=False)

        if args.emit_md:
            prompt_ref = f"/prompts/{chap}_rastreabilidade_prompt.md"
            # construir tabela do MD
            rows = emit_table_rows(chunk)
            md = MD_TEMPLATE.format(
                chapter=chap,
                chapter_name=chunk["chapter_name"].iloc[0] or "",
                rows=rows,
                csv_src=str(src),
                csv_hash=csv_hash,
                prompt_ref=prompt_ref
            )
            (canon / "25-rastreabilidade.md").write_text(md, encoding="utf-8")
            print(f"[OK] {cap_dir}/canon/25-rastreabilidade.md")

if __name__ == "__main__":
    main()
