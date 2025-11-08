#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, re, json
from pathlib import Path
import pandas as pd

BADGES_TMPL = """<!--AUTO:BADGES:START-->
<div class="badges">
  <Badge color="info">SAMM: {samm_summary}</Badge>
  <Badge color="info">BSIMM: {bsimm_list}</Badge>
  <Badge color="info">SSDF: {ssdf_list}</Badge>
  <Badge color="info">SLSA: {slsa_level}</Badge>
  <Badge color="info">DSOMM: {dsomm_summary}</Badge>
</div>
<!--AUTO:BADGES:END-->
"""

def _summarize_list(items, max_len=12):
    uniq = sorted(set(items))
    return ", ".join(uniq[:max_len]) + ("…" if len(uniq) > max_len else "") if uniq else "—"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--repo-root", required=True, help="Raiz dos capítulos (ex.: manuals_src/docs/sbd-toe)")
    ap.add_argument("--inject", action="store_true", help="Se definido, tenta injetar no intro.md entre marcadores.")
    ap.add_argument("--dump-json", default=None, help="Se definido, exporta JSON com badges por capítulo.")
    args = ap.parse_args()

    df = pd.read_csv(args.csv).fillna("")
    badges_by_chap = {}

    for chap, chunk in df.groupby("chapter"):
        chap = f"{int(chap):02d}"
        get = lambda fw: [c for f,c in zip(chunk["framework"], chunk["control"]) if str(f).upper().startswith(fw)]
        samm = get("SAMM"); bsimm = get("BSIMM"); ssdf = get("SSDF"); slsa = get("SLSA"); dsomm = get("DSOMM")

        samm_summary = f"{len(set(samm))} / —" if samm else "—"
        dsomm_summary = f"{len(set(dsomm))} / —" if dsomm else "—"
        nums = []
        import re
        for s in slsa:
            m = re.findall(r"(\\d+)", s)
            if m: nums.append(int(m[0]))
        slsa_level = max(nums) if nums else "—"

        bsimm_list = _summarize_list(bsimm)
        ssdf_list = _summarize_list(ssdf)

        badges_by_chap[chap] = {"SAMM": samm_summary, "BSIMM": bsimm_list, "SSDF": ssdf_list, "SLSA": slsa_level, "DSOMM": dsomm_summary}

        if args.inject:
            repo = Path(args.repo_root)
            cap_dir = next(iter(sorted(repo.glob(f"{chap}-*"))), None)
            if not cap_dir:
                print(f"[WARN] cap {chap}: sem diretório em {repo}")
                continue
            intro = cap_dir / "intro.md"
            if not intro.exists():
                print(f"[WARN] cap {chap}: sem intro.md")
                continue
            block = BADGES_TMPL.format(
                samm_summary=samm_summary, bsimm_list=bsimm_list, ssdf_list=ssdf_list, slsa_level=slsa_level, dsomm_summary=dsomm_summary
            )
            txt = intro.read_text(encoding="utf-8", errors="ignore")
            if "<!--AUTO:BADGES:START-->" in txt and "<!--AUTO:BADGES:END-->" in txt:
                new = re.sub(r"<!--AUTO:BADGES:START-->(?s).*?<!--AUTO:BADGES:END-->", block, txt, flags=re.S)
            else:
                new = block + "\n\n" + txt
            intro.write_text(new, encoding="utf-8")
            print(f"[OK] injetado badges em {intro}")

    if args.dump_json:
        Path(args.dump_json).write_text(json.dumps(badges_by_chap, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[OK] JSON: {args.dump_json}")
    elif not args.inject:
        for chap in sorted(badges_by_chap):
            print(chap, "=>", badges_by_chap[chap])

if __name__ == "__main__":
    main()
