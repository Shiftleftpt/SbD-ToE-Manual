---
id: ameacas-mitigadas
title: Ameaças Mitigadas
sidebar_position: 50
---

# 🔐 Ameaças Mitigadas — Capítulo 03: Threat Modeling

Este capítulo define práticas formais para **identificar, modelar, documentar e priorizar ameaças** ao longo do ciclo de vida de software.  
As ameaças mitigadas por este capítulo são maioritariamente de natureza **estrutural, de antecipação, visibilidade e cobertura** — e muitas não podem ser mitigadas sem threat modeling formal.

> ✅ O Threat Modeling atua como **mecanismo de antecipação e ativação de requisitos e controlos**, sendo essencial no SbD-ToE para quebrar o ciclo reativo de segurança.

---

## 🧠 Categoria 1 – Ausência de identificação sistemática de ameaças

| Ameaça                                      | Fonte                             | Como surge                                          | Como a prática mitiga                                                    | Controlos associados                     | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------|----------------------------------------|
| Ameaças desconhecidas e não tratadas        | STRIDE / CAPEC-137                 | Nenhuma análise formal de segurança ao design       | Modelação sistemática por tipo de ameaça e zona de ataque                 | `addon/01-metodologias-e-ferramentas.md`| ✅                                     |
| Prioridades de segurança mal definidas      | MITRE / BSIMM AA1.3               | Equipa não conhece os riscos prioritários           | Identificação e classificação de ameaças com impacto por risco            | `addon/07-mapeamento-threats-requisitos.md` | ✅                                  |
| Requisitos definidos sem base em ameaças    | SSDF PW.1 / ISO 27034 / DSOMM – Design & Development             | Requisitos genéricos ou não relacionados com riscos | Mapeamento direto entre ameaças e requisitos                              | `addon/07-mapeamento-threats-requisitos.md` | ✅                                  |
| Ameaças a privacidade ignoradas             | LINDDUN / ENISA Privacy Threats    | Dados pessoais tratados sem avaliação de risco      | Threat modeling específico de privacidade (ex: LINDDUN)                   | `addon/08-exemplo-privacidade.md`       | ✅                                     |
| Falta de cobertura de ameaças não técnicas  | ENISA SDLC / OSC&R / DSOMM – Design & Development                 | Foco apenas em exploits ou CVEs                     | Modelos incluem sociais, organizacionais, insiders                         | `addon/01-metodologias-e-ferramentas.md`| ✅                                     |

---

## 🔎 Categoria 2 – Falhas na modelação e revisão de arquitetura

| Ameaça                                      | Fonte                             | Como surge                                          | Como a prática mitiga                                                    | Controlos associados                       | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------|----------------------------------------|
| Arquitetura insegura não identificada       | CAPEC-122 / BSIMM AA1             | Equipa não vê falhas de fluxo, trust boundaries     | Modelação por diagrama, análise de zonas e pontos de entrada              | `addon/09-validacao-arquitetura.md`       | ❌ Cap. 04                             |
| Validação superficial em design reviews     | OWASP SAMM / ISO 27034             | Revisão apenas visual ou checklist simplista        | Integração de threat modeling em revisão técnica formal                    | `15-aplicacao-lifecycle.md`         | ❌ Cap. 04                             |
| Controles aplicados sem base em arquitetura | OSC&R Design / SSDF PW.4          | Controlos não contextualizados                      | Requisitos e testes derivados da arquitetura modelada                      | `addon/07-mapeamento-threats-requisitos.md` | ✅                                  |
| Ausência de revisão em interfaces críticas  | STRIDE / MITRE ATT&CK             | APIs, integrações, UIs não revistas                 | Modelagem dirigida por ativos e fronteiras técnicas                       | `addon/01-metodologias-e-ferramentas.md`  | ✅                                     |

---

## 🔄 Categoria 3 – Integração deficiente no ciclo de vida

| Ameaça                                      | Fonte                             | Como surge                                              | Como a prática mitiga                                                        | Controlos associados                         | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|------------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------|
| Ameaças descobertas demasiado tarde         | SSDF PW.4 / NIST 800-64            | Detetadas apenas em teste ou produção                   | Threat modeling obrigatório em early design e por marcos do SDLC             | `15-aplicacao-lifecycle.md`           | ✅                                     |
| Mudanças críticas sem nova modelação        | CAPEC-137 / OSC&R Lifecycle        | Funcionalidade nova sem reanálise de ameaças            | Integração no ciclo de vida e reativação por evento                           | `addon/09-validacao-arquitetura.md`         | ✅                                     |
| Descontinuidade entre equipas e fases       | ENISA DevSecOps                    | Ameaças não transitam entre equipas                     | Threat modeling documentado e versionado como artefacto                       | `addon/07-mapeamento-threats-requisitos.md` | ✅                                     |
| Ameaças não visíveis na pipeline CI/CD      | SLSA / OWASP CI/CD / OSC&R CI Flow | Pipelines não são modelados como software               | Threat modeling de CI/CD como projeto (runners, triggers, provenance)         | `addon/06-threat-modeling-ci.md`            | ✅                                     |

---

## 🧰 Categoria 4 – Ferramentas, automação e gestão de conhecimento

| Ameaça                                      | Fonte                             | Como surge                                          | Como a prática mitiga                                                    | Controlos associados                       | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------|----------------------------------------|
| Conhecimento de ameaças não acumulado       | BSIMM13 / ISO 27005 Sec.10        | Cada projeto parte do zero                          | Integração com ferramentas como IriusRisk, reuse de modelos e templates    | `addon/10-integracao-iriusrisk.md`         | ✅                                     |
| Inconsistência entre projetos e equipas     | OWASP SAMM / ENISA                 | Metodologias ou escopos diferentes                  | Frameworks e abordagens normalizadas por tipo de sistema                   | `addon/01-metodologias-e-ferramentas.md`   | ✅                                     |
| Ferramentas desconectadas do ciclo          | SSDF PW.3 / RM.1                   | Modelação feita isoladamente sem ligação a backlog  | Ligação entre ameaça, requisito, teste e owner funcional                    | `addon/07-mapeamento-threats-requisitos.md`| ❌ Cap. 02                             |

---

## ✅ Conclusão

As práticas de threat modeling formal descritas neste capítulo mitigam um conjunto de ameaças críticas **impossíveis de abordar apenas com testes, checklists ou controlos reativos**.  
Este capítulo permite:

- Antecipar ameaças antes de se manifestarem;
- Ligar ameaças a requisitos e controlos;
- Integrar segurança ao raciocínio de arquitetura e negócio;
- Tornar visível o que não é coberto por scans ou automações.

> ✅ Pelo menos **12 ameaças aqui mapeadas são exclusivamente mitigadas** por threat modeling estruturado — e são aquelas que **mais frequentemente passam despercebidas** em auditorias técnicas.

> 📌 O threat modeling é o **cérebro do SbD-ToE**: sem ele, os restantes controlos não sabem quando ou onde atuar.
