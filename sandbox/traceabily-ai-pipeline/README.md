# SbD-ToE — Pipeline de Apoio com IA (Rastreabilidade → MD + Prompts + Tags)

Este kit ajuda a **documentar e operacionalizar** o uso de IA no manual SbD-ToE:

1. **Fonte única (CSV):** tabela `rastreabilidade_global.csv` com mapeamentos (framework ↔ prática/capítulo).
2. **`csv_split_chapters.py`:** gera, por capítulo, o **esqueleto base** de `canon/25-rastreabilidade.md` e CSV por capítulo.
3. **`make_prompts_from_csv.py`:** cria **prompts** por capítulo para pedir a uma IA o enriquecimento/redação final do ficheiro.
4. **`extract_framework_tags.py`:** agrega por capítulo e gera o **bloco de badges/tags** para `intro.md` (com opção de injeção entre marcadores).

> O objetivo é: *“andar para trás”* a partir da rastreabilidade central, **registar o uso de IA** (ficam guardados os prompts e entradas), e manter um **pipeline determinístico**.

> o Projeto adicional SbD-ToE-RAG constroi um modelo RAG que permite suportar a criaçao consistente de "brack trace" para as referencias usadas criando uma base solida para o rastreabilidade_global.csv. O processo ainda não está totalmente automatizado, só a indexação e chunking deste manual e a criaçao de embeds. Existem scripts que usam, ou localmente ou via OpenIA API, esses embed para derivar a rastreabilidade global.

## Estrutura 
```
sbdtoe-ai-pipeline/
├── schemas/
│   └── rastreabilidade_global.csv      # CSV global (ver cabeçalho abaixo)
└── scripts/
    ├── csv_split_chapters.py
    ├── make_prompts_from_csv.py
    └── extract_framework_tags.py
```

## CSV — Cabeçalho (obrigatório)
```csv
framework,control,chapter,chapter_name,practice_id,practice_name,how_it_maps,notes,source_ref
```
- `framework`: SAMM | BSIMM | SSDF | SLSA | DSOMM | ISO27001 | CIS | ENISA | etc.
- `control`: ex.: SAMM-SM.2-A, BSIMM-SR1.5, SSDF-RM.1, SLSA-3, DSOMM-Design-2
- `chapter`: ex.: 02, 05, 07 (sempre 2 dígitos)
- `chapter_name`: nome curto do capítulo (opcional, mas recomendado)
- `practice_id`: ID interno da prática do capítulo (ex.: REQ-XXX, ARC-YYY)
- `practice_name`: descrição curta da prática
- `how_it_maps`: explicação objetiva de como a prática satisfaz o controlo
- `notes`: observações (limites, pressupostos, cobertura parcial)
- `source_ref`: referência (link interno/externo) que fundamenta o mapeamento

## Instalação rápida
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install pandas numpy
```

## 1) Gerar base markdowns e CSV por capítulo
```bash
python scripts/csv_split_chapters.py   --csv schemas/rastreabilidade_global.csv   --out-root /caminho/para/manuals_src/docs/sbd-toe   --emit-md
```
- Cria `XX-*/canon/25-rastreabilidade.md` com **tabela base** e notas.
- Cria também `XX-*/canon/25-rastreabilidade.csv` para auditoria.

## 2) Gerar prompts por capítulo (para uso com IA)
```bash
python scripts/make_prompts_from_csv.py   --csv schemas/rastreabilidade_global.csv   --prompts-out prompts   --repo-root /caminho/para/manuals_src/docs/sbd-toe
```
- Emite `prompts/XX_rastreabilidade_prompt.md` com contexto + instruções + tabela capítulo.

## 3) Extrair badges/tags para o `intro.md`
```bash
python scripts/extract_framework_tags.py   --csv schemas/rastreabilidade_global.csv   --repo-root /caminho/para/manuals_src/docs/sbd-toe   --inject
```
- Sem `--inject`, imprime no stdout. Com `--dump-json badges.json`, também exporta JSON.

## Nota sobre “uso de IA”
- Os **prompts** ficam versionados em `prompts/` e podem incluir o *hash* do CSV de origem.
- Inclui-se um *front-matter* no `25-rastreabilidade.md` com `ai_generated: true` e link para o prompt usado.
- Mantém-se CSVs por capítulo como **evidência de completude**.
