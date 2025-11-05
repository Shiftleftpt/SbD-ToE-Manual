---
id: achievable-maturity
title: Mapeamento de Maturidade - Threat Modeling
description: Alinhamento entre as práticas deste capítulo e os principais frameworks de segurança
tags: [maturidade, threat-modeling, SAMM, BSIMM, SSDF, SLSA, DSOMM]
---

# 📈 Maturidade - Threat Modeling

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 03** do manual SbD-ToE e os requisitos de frameworks reconhecidas: **OWASP SAMM**, **BSIMM**, **NIST SSDF**, **SLSA** e **OWASP DSOMM**.

O Threat Modeling é uma prática estruturante do ciclo de vida seguro. Permite antecipar riscos, definir requisitos proporcionais e justificar a aplicação de controlos de segurança. Este capítulo fornece uma abordagem repetível, rastreável e proporcional baseada em STRIDE, DFDs, threat maps e critérios de validação.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento **não mede a maturidade de uma organização**, mas sim o **grau de cobertura que as práticas deste capítulo oferecem relativamente às frameworks de referência**.

### Tipos de Avaliação Utilizados

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Framework prescritiva com 3 níveis por domínio   |
| OWASP DSOMM      | `n / m` (até 4)                     | Domínios com níveis formais                      |
| NIST SSDF        | Lista de controlos cobertos         | Modelo binário, sem níveis formais               |
| BSIMM            | Lista de práticas cobertas          | Modelo observacional, não prescritivo            |
| SLSA             | Nível máximo suportado (ex: 1 de 4) | Modelo acumulativo, não gradual por domínio      |

As avaliações aqui descritas foram realizadas com base numa leitura técnico-científica de cada fonte original.

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                         | Práticas ou Objetos Cobertos                                     | Avaliação de Maturidade             |
|------------------|----------------------------------------------|------------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Design → Threat Assessment                   | Modelação estruturada com STRIDE, DFDs e análise por risco       | **2 / 3**                           |
| OWASP DSOMM      | Architecture, Requirements, Risk Analysis    | Integração no SDLC, rastreabilidade, threat maps reutilizáveis   | **2 / 3** (média dos domínios)      |
| NIST SSDF v1.1   | PW.3, RV.1                                   | Identificação e análise de ameaças como input de requisitos      | **✔️ PW.3, RV.1**                   |
| BSIMM13          | Architecture Analysis (AA1, AA2)             | Mapeamento de ameaças, mitigação e controlo                      | Contributo direto                   |
| SLSA v1.0        | Risk Awareness (Supply Chain)                | Apoio indireto à definição proporcional de controlos             | **Nível 1 / 4**                     |

---

## 🧱 OWASP SAMM – Design → Threat Assessment

| Nível | Descrição SAMM                                                            | Cobertura pelo Cap. 03                     |
|-------|---------------------------------------------------------------------------|--------------------------------------------|
| 1     | Ameaças identificadas informalmente                                       | ✅ Processo baseado em STRIDE               |
| 2     | Análise estruturada com modelos formais e critérios de rastreabilidade    | ✅ Aplicação com DFD, threat map, aceitação |
| 3     | Integração contínua e automação                                           | ❌ Fora do escopo                           |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM – Architecture, Risk Analysis, Requirements

| Domínio           | Níveis cobertos | Justificação técnica                                                   |
|-------------------|----------------|------------------------------------------------------------------------|
| Architecture      | 2 / 3          | Análise de arquitetura e dependências com mapeamento de ameaças       |
| Risk Analysis     | 2 / 3          | Integração com classificação e aceitação de risco                     |
| Requirements      | 2 / 3          | Geração e validação de requisitos a partir do threat modeling         |

> A abordagem prescrita permite a reutilização de modelos de ameaça e sua rastreabilidade a requisitos e controlos.

---

## 🧱 NIST SSDF – Identify and Review Threats

| Controlos NIST SSDF | Descrição                                        | Alinhamento com Cap. 03 |
|---------------------|--------------------------------------------------|--------------------------|
| PW.3                | Identificar e analisar ameaças                   | ✅ Totalmente coberto    |
| RV.1                | Rever artefactos de threat modeling              | ✅ Integração por artefacto |

> O threat modeling é tratado como atividade sistemática, documentada e integrada com backlog e arquitetura.

---

## 🧱 BSIMM – Architecture Analysis (AA1, AA2)

| Prática BSIMM   | Alinhamento com Cap. 03                                        |
|-----------------|----------------------------------------------------------------|
| AA1.1           | ✅ Mapeamento de ameaças por componente                        |
| AA1.2           | ✅ Definição de técnicas de ataque e mitigação                 |
| AA2.1           | ✅ Ligação com arquitetura formal e controlos selecionados     |

> As práticas do capítulo contribuem diretamente para o domínio BSIMM de análise arquitetural.

---

## 🧱 SLSA – Supply Chain Risk Awareness

| Nível | Requisitos principais                              | Cobertura pelo Cap. 03                   |
|-------|-----------------------------------------------------|------------------------------------------|
| 1     | Consciência de risco e ameaça                       | ✅ Classificação e threat modeling        |
| 2     | Requisitos formais de proveniência                  | ❌ Fora do escopo                         |
| 3+    | Controlo reforçado na cadeia de fornecimento        | ❌ Aplicado em capítulos sobre CI/CD     |

**🔐 Nível máximo suportado por este capítulo: SLSA 1 / 4**

---

## ✅ Conclusão

- O Capítulo 03 estabelece uma prática sólida de threat modeling, com artefactos formais, reutilizáveis e rastreáveis;
- Está alinhado com **SAMM 2/3**, **DSOMM média 2/3**, **BSIMM AA1 e AA2**, e **SSDF PW.3 e RV.1**;
- Permite fundamentar controlos técnicos, requisitos e decisões arquiteturais com base em análise de risco realista;
- Apoia diretamente a proporcionalidade e priorização de controlos ao longo do SDLC.

---

## 📊 Sumário Consolidado de Alinhamento por Framework

| Framework         | Domínios Relevantes                         | Práticas ou Objetos Cobertos                                     | Avaliação de Maturidade             |
|------------------|----------------------------------------------|------------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Design → Threat Assessment                   | Modelação estruturada com STRIDE, DFDs e análise por risco       | **2 / 3**                           |
| OWASP DSOMM      | Architecture, Requirements, Risk Analysis    | Integração no SDLC, rastreabilidade, threat maps reutilizáveis   | **2 / 3** (média dos domínios)      |
| NIST SSDF v1.1   | PW.3, RV.1                                   | Identificação e análise de ameaças como input de requisitos      | **✔️ PW.3, RV.1**                   |
| BSIMM13          | Architecture Analysis (AA1, AA2)             | Mapeamento de ameaças, mitigação e controlo                      | Contributo direto                   |
| SLSA v1.0        | Risk Awareness (Supply Chain)                | Apoio indireto à definição proporcional de controlos             | **Nível 1 / 4**                     |
