---
id: achievable-maturity
title: Mapeamento de Maturidade – Capítulo 13
sidebar_position: 10
tags: [canon, maturidade, SAMM, BSIMM, SSDF, DSOMM]
---

# 📈 Maturidade — Formação e Onboarding Seguro

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 13 — Formação e Onboarding Seguro**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **OWASP DSOMM**

> ℹ️ Nota: **SLSA não se aplica diretamente** a este domínio, dado que não trata práticas humanas ou formativas.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este mapeamento avalia a completude, rastreabilidade e sofisticação das práticas formativas de acordo com os mecanismos nativos de avaliação de cada framework:

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Três níveis por domínio                          |
| OWASP DSOMM      | `n / m`                             | Maturidade progressiva por domínio técnico       |
| NIST SSDF        | Lista de controlos cobertos         | Avaliação objetiva e binária                     |
| BSIMM            | Práticas observadas                 | Enfoque empírico e descritivo                    |

---

## 🧭 Visão Geral de Alinhamento

| Framework     | Domínios Relevantes                      | Práticas Cobertas                                                  | Avaliação de Maturidade         |
|---------------|-------------------------------------------|----------------------------------------------------------------------|---------------------------------|
| **SAMM v2.1** | Governance → Education & Guidance         | Trilhos formativos por função e risco, rastreabilidade, champions   | **2 / 3**                       |
| **BSIMM13**   | Training (T1, T2), Software Mgmt (SM1)    | Awareness, labs práticos, cultura formativa, rastreio               | **Contributo direto**           |
| **SSDF v1.1** | PS.2.1, PS.2.2, PS.2.3                    | Formação proporcional, auditoria, atualizações frequentes           | **Completamente cumprido**      |
| **DSOMM**     | Education & Training                      | Formação adaptativa, feedback contínuo, integração com maturidade   | **3 / 3**                       |

---

## 🧱 OWASP SAMM — Governance → Education & Guidance

| Nível | Descrição SAMM                                             | Implementação no Cap. 13                               |
|-------|-------------------------------------------------------------|--------------------------------------------------------|
| 1     | Formação básica disponível                                   | ✅ Formação de awareness para todos os perfis           |
| 2     | Formação direcionada e rastreável                            | ✅ Trilhos por função e nível de risco, KPIs            |
| 3     | Integração com governance e melhoria contínua               | ❌ Parcial — não é ainda integrada com ciclos de gestão |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM – Education & Training

| Domínio             | Nível | Justificação técnica                                                      |
|---------------------|-------|---------------------------------------------------------------------------|
| Education & Training| 3 / 3 | Formação adaptada, prática, feedback contínuo, integração com rastreio    |

---

## 🧱 NIST SSDF – PS.2.x

| Controlos NIST SSDF | Descrição                                           | Alinhamento com Cap. 13                      |
|---------------------|-----------------------------------------------------|----------------------------------------------|
| PS.2.1              | Sensibilizar com conteúdo relevante                 | ✅ Formação awareness e conteúdos customizados|
| PS.2.2              | Atualizar conteúdos regularmente                    | ✅ Revisão e versionamento do material        |
| PS.2.3              | Rastrear e validar participação                     | ✅ Matrículas, KPIs e validação por equipa    |

---

## 🧱 BSIMM – Training e Gestão de Software

| Prática BSIMM | Alinhamento com Cap. 13                                   |
|---------------|------------------------------------------------------------|
| T1            | Sensibilização estruturada                                 |
| T2            | Formação avançada e gamificada (labs, exercícios)          |
| SM1           | Integração de formação com processos de gestão de software |

---

## ✅ Conclusão

- Este capítulo permite atingir **maturidade elevada e sustentável** em **DSOMM, SSDF e BSIMM**, com rastreabilidade e proporcionalidade formativa;
- O nível SAMM é sólido (2/3), com possibilidade de progressão mediante integração da formação com governance e avaliação contínua;
- As práticas aqui descritas são essenciais para dar suporte a todos os restantes capítulos do SbD-ToE.
