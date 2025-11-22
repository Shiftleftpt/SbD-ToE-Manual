# 🎯 Demo - Sistema de Validação e Recomendação

Este ficheiro demonstra como funciona o sistema automático de validação e recomendação de tags.

## Como Executar

```bash
cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/tag-normalization
source .venv/bin/activate
python3 demo.py
```

## O que o Demo Mostra

### DEMO 1: Ficheiro COM Tags Válidas

**Ficheiro**: `DEMO-SAMPLE.md`

**Tags definidas**: `[cicd, sbom, sast, dast, design, arquitetura]`

**Resultado da Validação**:
- ✅ Todas as 6 tags são válidas
- ✅ Sem problemas detectados

**Recomendações Automáticas**:
- compliance (40%)
- dashboards (40%)
- logging (40%) → aliases: logs
- pipeline (40%)
- segurança (40%) → aliases: security, seguranca
- validação (40%)
- threat modeling (40%)
- alertas (40%)

---

### DEMO 2: Ficheiro SEM Tags

**Ficheiro**: `DEMO-NO-TAGS.md` (gerado dinamicamente)

**Tags definidas**: (nenhuma)

**Resultado da Validação**:
- ⚠️ Nenhuma tag encontrada
- ✅ Sem problemas de sintaxe

**Recomendações Automáticas**:
- arquitetura (40%) → aliases: architecture, design
- controlo (40%) → aliases: control, mitigação
- integração (40%)
- pipeline (40%)
- segurança (40%) → aliases: security, seguranca
- testes (40%) → aliases: testing, test
- validação (40%)
- threat modeling (40%)

---

## Componentes do Sistema

### 1️⃣ Validação (ValidationEngine)

Analisa tags **existentes** num ficheiro e detecta:

- **Unknown Tag**: Tag não reconhecida no canonical
- **Alias Found**: Tag que é um alias de outra (sugestão de correção)
- **Case Mismatch**: Diferença de capitalização
- **Duplicate Tag**: Tag duplicada
- **Formatting Error**: Erro de sintaxe

### 2️⃣ Recomendações (RecommendationEngine)

Analisa **conteúdo** do ficheiro e sugere tags automáticamente baseado em:

- **Título**: Palavras-chave no título
- **Descrição**: Conteúdo da descrição
- **Conteúdo**: Texto do documento
- **Contexto**: Ficheiros relacionados na hierarquia
- **Relações**: Tags semanticamente relacionadas

### 3️⃣ Análise Semântica

Mostra **relações entre tags** existentes:

- `sbom` ↔ supply-chain, sca, dependencias
- `cicd` ↔ pipeline, deployment, iac, testing
- `testing` ↔ sast, dast, fuzzing, cicd
- etc.

---

## Fluxo de Validação e Recomendação

```
1. Ler ficheiro markdown
   ↓
2. Extrair YAML frontmatter
   ├─ Título
   ├─ Descrição
   ├─ Tags existentes
   └─ Contexto

3. VALIDAÇÃO (tags existentes)
   ├─ Verificar se tags existem no canonical
   ├─ Procurar aliases
   ├─ Detectar case mismatches
   └─ Reportar problemas

4. RECOMENDAÇÕES (tags sugeridas)
   ├─ Analisar keywords no conteúdo
   ├─ Verificar relações semânticas
   ├─ Considerar contexto (parent chapter)
   ├─ Calcular confidence score
   └─ Ordena por score (maior → menor)

5. ANÁLISE SEMÂNTICA (relações)
   └─ Mostrar tags relacionadas

6. RESUMO
   ├─ Total de tags válidas
   ├─ Problemas detectados
   └─ Recomendações
```

---

## Casos de Uso

### Caso 1: Validar um Ficheiro com Tags

```bash
cd tag_system
make validate BASE_PATH=../../../manuals_src/docs/sbd-toe LIMIT=1
```

**Resultado**:
- Lista todas as tags do ficheiro
- Mostra problemas encontrados
- Sugere correções

### Caso 2: Obter Recomendações para um Ficheiro

```bash
cd tag_system
make recommend BASE_PATH=../../../manuals_src/docs/sbd-toe LIMIT=5
```

**Resultado**:
- Analisa ficheiros sem tags (ou com tags insuficientes)
- Sugere novas tags com confidence scores
- Ordena por relevância

### Caso 3: Audit Completo

```bash
cd tag_system
make audit BASE_PATH=../../../manuals_src/docs/sbd-toe
```

**Resultado**:
- Validação + Recomendações para todos os ficheiros
- Relatório consolidado
- Sugestões de correção em massa

---

## Interpretando Resultados

### Validation Severity Levels

| Nível | Significado |
|-------|-------------|
| ERROR | Problema crítico (tag desconhecida, erro de sintaxe) |
| WARNING | Problema não-crítico (alias, case mismatch) |
| INFO | Informação útil (sugestão de tag relacionada) |

### Recommendation Confidence

| Intervalo | Interpretação |
|-----------|---------------|
| 0-30% | Baixa confiança, revisar manualmente |
| 30-60% | Confiança média, revisar e considerar |
| 60-80% | Boa confiança, considerar adicionar |
| 80%+ | Alta confiança, recomendado adicionar |

---

## Exemplo Prático

**Ficheiro**: `intro.md`

```yaml
---
id: intro
title: "Introdução ao SbD-ToE"
description: "Overview do manual Security by Design"
tags: []  # ← Sem tags!
---

# Introdução

Este manual cobre segurança em arquitetura, threat modeling,
testing (SAST, DAST), CI/CD pipelines e containers.
```

**Sistema Detecta**:

1. ✅ Ficheiro tem 0 tags
2. 📋 Escaneia conteúdo:
   - "arquitetura" → tag `arquitetura`
   - "threat modeling" → tag `threat-modeling`
   - "testing, SAST, DAST" → tag `testing`
   - "CI/CD" → tag `cicd`
   - "containers" → tag `containers`

3. 💡 Recomenda (ordenado por score):
   - cicd (90%) - keyword "CI/CD"
   - testing (85%) - keyword "SAST, DAST"
   - arquitetura (80%) - keyword "arquitetura"
   - threat-modeling (75%) - keyword "threat modeling"
   - containers (70%) - keyword "containers"

4. ✨ Utilizador revê e aprova as top 3

---

## Próximos Passos

1. **Validar** ficheiros existentes
2. **Obter recomendações** para ficheiros sem tags
3. **Revisar** e **aprovar** as sugestões
4. **Aplicar** as tags via script de batch ou manual

