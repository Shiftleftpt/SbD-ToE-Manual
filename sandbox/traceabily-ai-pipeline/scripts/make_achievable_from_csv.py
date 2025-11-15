#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, re
from pathlib import Path
import pandas as pd

MD_TMPL = """---
id: achievable-maturity
title: Maturidade Atingível
description: O que a organização atinge ao aplicar integralmente este capítulo, por framework.
tags: [maturidade, alinhamento, frameworks]
sidebar_position: 10
---

# 🧭 Como interpretar este mapeamento de maturidade

Este documento resume **o nível de maturidade que é atingível** quando as práticas deste capítulo são cumpridas de forma consistente. O objetivo é dar **visibilidade objetiva** sobre o alinhamento com frameworks de referência e orientar **planos de evolução**.

## 🧩 Visão Geral de Alinhamento

| Framework | Métrica/Resumo |
|---|---|
| SAMM | {samm_summary} |
| BSIMM | {bsimm_list} |
| SSDF | {ssdf_list} |
| SLSA | {slsa_level} |
| DSOMM | {dsomm_summary} |

---

## SAMM — Detalhe
{sec_samm}

## BSIMM — Detalhe
{sec_bsimm}

## SSDF — Detalhe
{sec_ssdf}

## SLSA — Detalhe
{sec_slsa}

## DSOMM — Detalhe
{sec_dsomn}

---

## 📊 Sumário Consolidado de Alinhamento por Framework

| Framework | Conteúdo |
|---|---|
| SAMM | {samm_summary} |
| BSIMM | {bsimm_list} |
| SSDF | {ssdf_list} |
| SLSA | {slsa_level} |
| DSOMM | {dsomm_summary} |

> **Notas editoriais**  
> - Fonte: `rastreabilidade_global.csv` (consolidado).  
> - Este documento é gerado automaticamente e deve ser **revisto editorialmente** para assegurar fidelidade ao capítulo e às evidências.
"""

def _uniq(seq):
    return sorted({s for s in seq if str(s).strip()})

def _norm_token(s):
    return re.sub(r"\s+", "", str(s).strip())

def _pick_level(tokens):
    # Extrai inteiros de tokens SLSA (ex.: "2", "3") e devolve o máx.
    lv = []
    for t in tokens:
        m = re.findall(r"\d+", str(t))
        if m:
            lv.extend(int(x) for x in m)
    return max(lv) if lv else "—"

def build_sections(df_chap):
    # Seleções por framework (tolerantes à capitalização)
    def fw_mask(name):
        return df_chap["framework"].astype(str).str.upper().str.startswith(name)

    samm = _uniq(df_chap.loc[fw_mask("SAMM"), "control"])
    bsimm = _uniq(df_chap.loc[fw_mask("BSIMM"), "control"])
    ssdf = _uniq(df_chap.loc[fw_mask("SSDF"), "control"])
    slsa = _uniq(df_chap.loc[fw_mask("SLSA"), "control"])
    dsomm = _uniq(df_chap.loc[fw_mask("DSOMM"), "control"])

    # Resumos canónicos
    samm_summary = f"{len(samm)} / —" if samm else "—"
    dsomm_summary = f"{len(dsomm)} / —" if dsomm else "—"
    bsimm_list = ", ".join(s for s in bsimm) if bsimm else "—"
    ssdf_list  = ", ".join(s for s in ssdf) if ssdf else "—"
    slsa_level = _pick_level(slsa)

    # Secções detalhadas simples (listas)
    def bullets_for(name, items):
        if not items:
            return f"- —"
        return "\n".join(f"- {i}" for i in items)

    sec_samm = bullets_for("SAMM", samm)
    sec_bsimm = bullets_for("BSIMM", )
    sec_ssdf = bullets_for("SSDF", ssdf)
    sec_slsa = f"- Nível alvo evidenciado nos mapeamentos: **{slsa_level}**" if slsa_level != "—" else "- —"
    sec_dsomn = bullets_for("DSOMM", dsomm)

    return {
        "samm_summary": samm_summary,
        "bsimm_list": bsimm_list,
        "ssdf_list": ssdf_list,
        "slsa_level": slsa_level,
        "dsomm_summary": dsomm_summary,
        "sec_samm": sec_samm,
        "sec_bsimm": sec_bsimm,
        "sec_ssdf": sec_ssdf,
        "sec_slsa": sec_slsa,
        "sec_dsomn": sec_dsomn,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="rastreabilidade_global.csv consolidado")
    ap.add_argument("--repo-root", required=True, help="Raiz dos capítulos (ex.: manuals_src/docs/sbd-toe/010-sbd-manual)")
    ap.add_argument("--chapters-glob", default="*", help="Padrão para filtrar capítulos (ex.: '0[1-9]-*' ou '1[0-4]-*')")
    args = ap.parse_args()

    df = pd.read_csv(args.csv).fillna("")
    root = Path(args.repo_root)

    # Descobrir capítulos reais no repo
    chap_dirs = sorted([p for p in root.glob(args.chapters_glob) if p.is_dir() and re.match(r"^\d{2}-", p.name)])
    found = {p.name.split("-",1)[0]: p for p in chap_dirs}

    for chap, chunk in df.groupby("chapter"):
        chap = f"{int(chap):02d}"
        if chap not in found:
            print(f"[WARN] capítulo {chap} não encontrado em {root}")
            continue

        cap_dir = found[chap]
        # Se existir 'canon', usa; senão escreve na raiz do capítulo
        out_dir = cap_dir / "canon" if (cap_dir / "canon").is_dir() else cap_dir
        out_dir.mkdir(parents=True, exist_ok=True)

        sections = build_sections(chunk)
        md = MD_TMPL.format(**sections)
        out_file = out_dir / "10-achievable-maturity.md"
        out_file.write_text(md, encoding="utf-8")
        print(f"[OK] {out_file}")

if __name__ == "__main__":
    main()
