# 🚀 GUIA RÁPIDO - Sistema de Validação e Recomendação de Tags

## Setup (primeira vez)

```bash
cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/tag-normalization
./setup-env.sh  # Cria .venv e instala dependências
```

## Demo Interativo

```bash
source .venv/bin/activate
python3 demo.py
```

Mostra 2 exemplos:
1. **DEMO 1**: Ficheiro COM tags válidas + sugestões de tags adicionais
2. **DEMO 2**: Ficheiro SEM tags + sistema de recomendação automática

## Usar em Produção

### 1️⃣ Validar Tags Existentes

```bash
cd tag_system
make validate BASE_PATH=../../../manuals_src/docs/sbd-toe LIMIT=10
```

**Resultado**: Lista ficheiros com problemas nas tags (unknown tags, aliases, case mismatches)

### 2️⃣ Obter Recomendações

```bash
cd tag_system
make recommend BASE_PATH=../../../manuals_src/docs/sbd-toe LIMIT=5
```

**Resultado**: Sugere tags para ficheiros sem tags ou com tags insuficientes

### 3️⃣ Audit Completo

```bash
cd tag_system
make audit BASE_PATH=../../../manuals_src/docs/sbd-toe
```

**Resultado**: Validação + Recomendações para toda a documentação

## Ficheiros Importantes

```
tag-normalization/
├── canonical-tags.yml          # 489 tags canónicas (source of truth)
├── DEMO-SAMPLE.md              # Exemplo com tags válidas
├── DEMO-NO-TAGS.md             # Exemplo sem tags
├── demo.py                      # Script de demonstração
├── SISTEMA-FUNCIONANDO.txt      # Este ficheiro (resumo visual)
│
└── tag_system/
    ├── core/
    │   └── canonical_tags.py           # Carrega canonical-tags.yml
    ├── validators/
    │   └── validation_engine.py        # Valida tags existentes
    ├── recommenders/
    │   └── recommendation_engine.py    # Recomenda tags novas
    └── cli/
        └── main_cli.py                 # Interface CLI
```

## Output Esperado

### Validação bem-sucedida

```
✅ Validando tags em: /path/to/docs
❌ Unknown tag: 'invalid-tag' → Check canonical-tags.yml
⚠️ Case mismatch: 'Security' → Did you mean 'security'?
...
Ficheiros com problemas: 5
```

### Recomendações bem-sucedidas

```
💡 Recomendações para: intro.md
   1. security (85%)      - Razão: keyword match
   2. cicd (75%)          - Razão: keyword match
   3. testing (70%)       - Razão: semantic relation
...
```

## Troubleshooting

**"ModuleNotFoundError: No module named 'sklearn'"**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**"canonical-tags.yml not found"**
```bash
# Certificar que estás no diretório correto
cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/tag-normalization
```

**Recommendations vazias**
- Aumentar `min_confidence` no comando
- Verificar conteúdo do ficheiro tem keywords

## Próximos Passos

1. ✅ Executar demo.py para ver sistema em ação
2. 🔍 Validar alguns ficheiros da documentação
3. 💡 Obter recomendações para ficheiros críticos
4. 👍 Revisar e aprovar as sugestões
5. 📝 Aplicar as tags aprovadas

---

**Criado**: 22 Nov 2025
**Status**: ✅ Pronto para Produção
**Versão**: 1.0
