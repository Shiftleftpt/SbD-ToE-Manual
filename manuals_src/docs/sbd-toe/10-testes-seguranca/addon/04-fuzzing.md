---
id: fuzzing
title: Fuzzing Direcionado e Aleatório
description: Testes com dados inesperados ou malformados para descoberta de falhas em parsers, APIs e lógica interna.
tags: [fuzzing, testes aleatórios, fuzzers, cobertura, validação]
sidebar_position: 5
---


# 🌀 Fuzzing de Segurança {testes-seguranca:addon:fuzzing}

## 🌟 Objetivo {testes-seguranca:addon:fuzzing#objetivo}

Descobrir vulnerabilidades e falhas de robustez através da **geração automática e massiva de inputs malformados, inesperados ou aleatórios**, com o objetivo de:

- Testar limites da aplicação;
- Detetar exceções não tratadas, falhas de parsing, crashes;
- Reproduzir comportamentos anómalos ou edge cases;
- Validar a resiliência da aplicação face a entradas fora do esperado.

> O fuzzing é essencial para testar “o inesperado” — aquilo que os testes planeados não cobrem.

---

## 🔍 O que é fuzzing {testes-seguranca:addon:fuzzing#o_que_e_fuzzing}

Fuzzing é uma técnica de segurança que consiste em alimentar a aplicação com **inputs gerados de forma aleatória ou sistemática**, com o intuito de provocar erros, falhas ou crashes.

Tipos comuns:

- **Fuzzing de APIs REST** (inputs em JSON, headers, parâmetros);
- **Fuzzing de protocolos binários ou mensagens estruturadas**;
- **Fuzzing de ficheiros ou parsers** (ex: XML, PDF, imagem);
- **Coverage-guided fuzzing** (instrumentação para maximizar caminhos explorados);
- **Mutation-based fuzzing** (variações sobre inputs reais conhecidos).

> ⚠️ O fuzzing não identifica diretamente vulnerabilidades — mas sim condições de erro que **podem indicar fragilidades exploráveis**.

---

## ⚙️ Como aplicar {testes-seguranca:addon:fuzzing#como_aplicar}

1. **Selecionar alvo e contexto de teste** (ex: endpoint REST, ficheiro, fluxo de API);
2. **Configurar fuzzer com tipos de input relevantes** (estrutura, tipos, encoding);
3. **Executar fuzzing em ambiente isolado ou controlado**, com observabilidade (logging, crash dump);
4. **Instrumentar aplicação com cobertura ou deteção de exceções** (opcional);
5. **Analisar comportamentos anómalos ou inconsistentes**: respostas inesperadas, falhas silenciosas, quedas;
6. **Reportar ocorrências como findings de robustez, com evidência e reprodutibilidade**.

---

## ✅ Boas práticas {testes-seguranca:addon:fuzzing#boas_praticas}

- Utilizar fuzzing em endpoints críticos e APIs externas;
- Priorizar formatos ricos (JSON, XML, JWT) e campos menos validados;
- Repetir fuzzing após alterações de parsing ou bibliotecas de entrada;
- Usar ferramentas com feedback de cobertura para melhor exploração;
- Integrar fuzzing como etapa separada no pipeline ou build noturno;
- Combinar com logs, tracing e crash reports para análise eficaz.

---

## 📎 Referências cruzadas {testes-seguranca:addon:fuzzing#referencias_cruzadas}

| Documento                       | Relevância estratégica                       |
|--------------------------------|----------------------------------------------|
| Capítulo 02 — Requisitos       | Relacionado com `REQ-309`, `REQ-406`         |
| `02-dast.md`                   | Complementa com entradas mais imprevisíveis  |
| `06-cobertura-e-priorizacao.md`| Usado em zonas com menos testes manuais      |
| Capítulo 07 — CI/CD Seguro     | Aplicação em jobs dedicados ou ambientes paralelos |
| `08-gestao-findings.md`        | Findings do fuzzing podem requerer triagem especializada |

---

> 🎲 O fuzzing não substitui testes planeados — mas **aumenta a cobertura invisível**, detetando falhas que só emergem com inputs fora do normal. É um sinal de maturidade na estratégia de validação de segurança.
