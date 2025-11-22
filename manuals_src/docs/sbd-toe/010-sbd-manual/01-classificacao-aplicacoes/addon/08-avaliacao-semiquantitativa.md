---

id: avaliacao-semiquantitativa
title: Alternativa - Avaliação Semiquantitativa do Risco
sidebar_position: 8
tags: [criticidade, metodologia, tema:risco, tipo:avaliacao]
---

# 🛠️ Modelo Alternativo : Avaliação Semiquantitativa

A avaliação de risco semiquantitativa permite ultrapassar as limitações da abordagem meramente qualitativa, ao fornecer um modelo mais estruturado, mensurável e comparável - sem exigir dados estatísticos completos como nos modelos puramente quantitativos.

Este modelo é recomendado como alternativa ligeiramente mais avançada, mas acessível, ao modelo qualitativo descrito nos restantes ficheiros deste capítulo.

## 📌 Nota Técnica - Comparação com a Metodologia OWASP Risk Rating

A abordagem semiquantitativa aqui descrita visa fornecer uma alternativa prática ao modelo qualitativo baseado em eixos (ver `01-modelo-classificacao-eixos.md`), mantendo um nível de estruturação suficiente para justificar decisões técnicas, sem exigir dados estatísticos nem competências avançadas de análise de risco.

Embora simplificada, esta abordagem permite:

* Quantificação básica do risco, através de escalas discretas de impacto e probabilidade;
* Categorização objetiva e rastreável dos riscos, com thresholds explícitos por nível L1–L3;
* Decisões proporcionais sobre mitigação e controlo, integradas com os restantes capítulos do manual SbD-ToE.

Contudo, existem metodologias mais completas e rigorosas, como a **OWASP Risk Rating Methodology (ORRM)**, que:

* Decompõe o risco em múltiplos fatores técnicos (ex: *skill level*, *exploitability*, *business impact*);
* Utiliza médias ponderadas para cálculo de *likelihood* e *impacto*, aumentando a granularidade e precisão;
* É amplamente utilizada para análise de vulnerabilidades técnicas específicas, como parte de processos de pentest, gestão de findings ou triagem de bugs.

A metodologia OWASP Risk Rating pode e deve ser adotada quando a organização possuir maturidade suficiente, ferramentas de suporte, e necessidade de avaliação mais fina.

O modelo semiquantitativo aqui apresentado não pretende substituir modelos mais detalhados, mas sim servir como base mínima estruturada e compatível com os restantes elementos do SbD-ToE - nomeadamente na definição de proporcionalidade de controlos, testes, requisitos e validações em função do risco.

A decisão entre modelos deve considerar a maturidade da organização, a capacidade de adoção prática e o objetivo da análise de risco (macroclassificação vs. triagem granular de vulnerabilidades).

## 🌟 Objetivos da Avaliação Semiquantitativa

* Priorizar riscos com maior precisão e objetividade.
* Justificar decisões de mitigação baseadas em pontuação.
* Suportar análises de custo-benefício de controlos.
* Permitir integração com ferramentas de GRC ou SAST/DAST.

---

## 📊 Modelo de Scoring Mínimo Recomendado

A fórmula base:

```
Risco = Impacto × Probabilidade
```

Cada fator é avaliado numa escala discreta (ex.: 1–5), com definição clara dos critérios.

| Escala | Impacto (I)                        | Probabilidade (P)                     |
| ------ | ---------------------------------- | ------------------------------------- |
| 1      | Impacto negligenciável             | Muito improvável (1×/ano)             |
| 2      | Impacto limitado (interno)         | Pouco provável (1×/trimestre)         |
| 3      | Impacto moderado (operacional)     | Possível (1×/mês)                     |
| 4      | Impacto elevado (legal/cliente)    | Provável (1×/semana)                  |
| 5      | Impacto crítico (negócio em risco) | Quase certo (constante/automatizável) |

O resultado `Risco = I × P` pode depois ser mapeado para categorias:

| Risco Total | Categoria |
| ----------- | --------- |
| 1–4         | Baixo     |
| 5–9         | Médio     |
| 10–15       | Alto      |
| 16–25       | Crítico   |

---

## 📈 Exemplo Aplicado

**Cenário:** API de autenticação exposta na internet

| Fator                            | Avaliação | Justificação                                        |
| -------------------------------- | --------- | --------------------------------------------------- |
| Impacto (I)                      | 5         | Comprometimento total de identidade de utilizadores |
| Probabilidade (P)                | 4         | Exposição contínua + alvo comum de ataque           |
| **Risco = 5 × 4 = 20 → Crítico** |           |                                                     |

---

## 🌟 Interpretação segundo Níveis L1–L2–L3

Para manter coerência com o modelo de três níveis de criticidade de aplicação (L1–L3) adotado em todo o manual SbD-ToE, propõe-se o seguinte enquadramento na interpretação dos resultados de risco:

| Nível da aplicação         | Risco aceitável sem mitigação | Exige mitigação imediata se ≥ |
| -------------------------- | ----------------------------- | ----------------------------- |
| **L1 (Baixa criticidade)** | até 9 (risco médio)           | ≥ 15                          |
| **L2 (Criticidade média)** | até 6                         | ≥ 10                          |
| **L3 (Alta criticidade)**  | até 4                         | ≥ 6                           |

> ⚠️ **Nota:** Estes valores representam uma interpretação prescritiva do modelo para fins de segurança aplicacional. Podem divergir de alguns frameworks normativos, mas têm por base uma abordagem pragmática e alinhada com o princípio de proporcionalidade do SbD-ToE.

---

## ✅ Vantagens do Modelo Semiquantitativo

* Mais objetivo e comparável que modelos apenas verbais (baixo/médio/alto).
* Permite priorização automatizável (ex.: dashboards).
* Apoia decisões de investimento em segurança baseadas em impacto.

---

## ⚠️ Riscos de Má Adoção

* ❌ **Arbitrariedade** na atribuição de pontuações, sem critérios objetivos claros.
* ❌ **Inflacionamento artificial** de scores para justificar controlos desejados.
* ❌ **Desalinhamento entre equipas técnicas e de negócio** sobre o que representa “impacto” ou “probabilidade”.
* ❌ **Estagnação** do scoring se não for revisto ao longo do tempo.

---

## 🤣 Conformidade com Modelos Avançados

Esta abordagem está alinhada com frameworks como:

* **ISO/IEC 27005**: Recomenda avaliação semiquantitativa como boa prática em análise de risco.
* **OWASP Risk Rating Methodology**: Usa scoring semelhante com fatores adicionais (facilidade de exploração, exposição, etc.).
* **NIST SP 800-30**: Incentiva uso de escalas normalizadas para impacto e likelihood.

---

## 🛠️ Sugestões de Adoção

* Definir escalas e critérios antes da aplicação.
* Envolver stakeholders de negócio na definição de impacto.
* Rever periodicamente os scores (ver xref\:cap01#ciclo-vida-risco).
* Usar planilhas rastreáveis ou ferramentas de GRC.
