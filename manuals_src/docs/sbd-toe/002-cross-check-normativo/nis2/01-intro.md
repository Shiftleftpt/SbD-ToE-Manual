---
id: intro
title: NIS2 - Cross-check normativo
description: Como o SbD-ToE cobre, deixa em aberto deliberadamente e pode integrar rapidamente os requisitos da Diretiva NIS2 (UE 2022/2555)
tags: [cross-check, nis2, diretiva, ciberseguranca, incident-reporting, governance]
sidebar_position: 3
---

# Cross-check normativo - NIS2

## Âmbito

A **Diretiva (UE) 2022/2555 (NIS2)** (CELEX: [32022L2555](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022L2555)) atualiza o quadro europeu de cibersegurança para entidades essenciais e importantes em 18 setores, reforçando governação, medidas de gestão de risco e obrigação de reporte de incidentes. Os Estados-Membros tinham até 17 de outubro de 2024 para transpor a NIS2; a NIS1 foi revogada a 18 de outubro de 2024.

No espírito da NIS2, não chega "ter controlos" - é preciso demonstrar capacidade operacional e responsabilização da gestão. O SbD-ToE, construído top-down e atento a múltiplas referências, encaixa naturalmente neste ethos: entrega processos, políticas e artefactos técnicos reutilizáveis, deixando propositadamente algumas variáveis em aberto para preservar a universalidade do manual.

Este documento apresenta:

1. **PARTE I: ANÁLISE NORMATIVA** - mapeamento artigo a artigo dos requisitos NIS2 para capítulos SbD-ToE, identificando cobertura existente, lacunas intencionais e passos de integração.
2. **PARTE II: SÍNTESE E REFERÊNCIAS** - visão consolidada da relação NIS2/SbD-ToE e referências normativas.

---

## PARTE I: ANÁLISE NORMATIVA

### Artigo 20 - Governação e responsabilização

**Conteúdo normativo**

O Art. 20 coloca o órgão de gestão no centro: ele aprova as medidas de gestão de risco de cibersegurança, supervisiona a execução e pode ser responsabilizado por incumprimentos. Exige ainda formação regular para a gestão.

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Aprovação de medidas pelo órgão de gestão | Cap. 02, Cap. 14 | Prescreve políticas e papéis, ciclos de aprovação |
| Supervisão da execução | Cap. 12 | Métricas e evidências operacionais, monitorização contínua |
| Formação regular da gestão | Cap. 13 | Programa de formação e onboarding |

**O que o SbD-ToE cobre**

- Define políticas e papéis (Cap. 02 - Requisitos; Cap. 14 - Governança e Contratação).
- Estabelece ciclos de aprovação e monitorização com métricas e evidências operacionais (Cap. 12).
- Prescreve programa de formação e onboarding (Cap. 13).

**Lacunas intencionais**

Quem assina as políticas: o manual exige aprovação formal, mas não fixa se é equipa técnica, CISO ou board. Isto é propositado: em contextos puramente técnicos, aprovação operacional basta; para conformidade NIS2, a aprovação deve ser do órgão de gestão.

**Como cumprir**

Sugere-se registar, no Cap. 14, que as políticas do SbD-ToE foram aprovadas pelo board, com evidência de formação periódica à gestão (conforme Art. 20). A integração resume-se a formalizar a cadeia de aprovação e documentar a formação.

---

### Artigo 21 - Medidas de gestão de risco de cibersegurança

**Conteúdo normativo**

O Art. 21 pede um conjunto mínimo de medidas, num all-hazards approach: políticas de análise de risco e segurança, gestão de incidentes, continuidade/crise (backups, DR), segurança da cadeia de fornecimento, segurança em aquisição/desenvolvimento/manutenção, avaliação da eficácia dos controlos, higiene cibernética/treino, IAM, criptografia, gestão de vulnerabilidades/patching, logging e monitorização.

Em 2024/2025, a Comissão e a ENISA publicaram orientações técnicas e mapeamentos práticos com exemplos de evidência para implementar estas medidas - utilíssimos para auditoria.

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Políticas de análise de risco | Cap. 02, Cap. 03 | Requisitos de segurança, threat modeling |
| Gestão de incidentes | Cap. 12 | Deteção, resposta, pós-incidente |
| Continuidade/crise (backups, DR) | Cap. 12 | Runbooks, exercícios, backups testados |
| Segurança da cadeia de fornecimento | Cap. 05, Cap. 14 | SBOM/SCA, dependências, requisitos contratuais |
| Segurança em desenvolvimento | Cap. 06, Cap. 07, Cap. 08 | Desenvolvimento seguro, CI/CD, IaC |
| Avaliação da eficácia | Cap. 10, Cap. 12 | Testes de segurança, monitorização contínua |
| Higiene cibernética/treino | Cap. 13 | Formação e onboarding |
| IAM, criptografia | Cap. 02, Cap. 04 | Requisitos de segurança, arquitetura segura |
| Gestão de vulnerabilidades/patching | Cap. 05, Cap. 10 | Dependências, SCA, testes |
| Logging e monitorização | Cap. 12 | Observabilidade, SIEM, alertas |

**O que o SbD-ToE cobre**

- **Políticas e controlos técnicos** (Cap. 02 - Requisitos de Segurança).
- **Classificação de criticidade** e risco proporcional (Cap. 01 - Classificação de Aplicações).
- **Threat modeling** (Cap. 03).
- **Cadeia de fornecimento**: SBOM/SCA, dependências (Cap. 05).
- **CI/CD & IaC** seguros (Cap. 07, Cap. 08); containers/runtime (Cap. 09).
- **Testes** (Cap. 10) e deploy seguro (Cap. 11).
- **Monitorização, logging, resposta e melhoria contínua** (Cap. 12).
- **Governança & contratação** (Cap. 14), incluindo avaliação de terceiros.

**Lacunas intencionais**

Taxonomias/formatos "fechados": a NIS2 detalha tópicos, mas o detalhe (p. ex., lista exata de campos de logs ou templates de políticas) pode variar entre jurisdições e setores. O SbD-ToE mantém modelos genéricos, para que possam ser "plugados" aos requisitos nacionais/setoriais.

**Como cumprir**

Sugere-se usar o catálogo do Cap. 02 como base de SoA técnica e alinhar as evidências com o guia técnico da ENISA (exemplos de evidência e mapeamentos). Declarar, no Cap. 01, que a proporcionalidade segue as classes NIS2 (essencial/importante) e o impacto nos serviços.

---

### Artigo 23 - Reporte de incidentes

**Conteúdo normativo**

A NIS2 define um trilho de reporte para incidentes significativos:

- **Alerta cedo** ("early warning") até 24h após conhecimento.
- **Notificação** com avaliação inicial até 72h.
- **Relatório final** até 1 mês (podendo haver atualizações intermédias).

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Deteção e resposta | Cap. 12 | Processo de deteção, resposta, pós-incidente |
| Escalonamento e responsabilidades | Cap. 14 | Papéis e responsabilidades |
| Classificação de severidade | Cap. 01, Cap. 12 | Critérios de impacto, classificação de incidentes |

**O que o SbD-ToE cobre**

- Processo de deteção e resposta, com pós-incidente (Cap. 12).
- Papéis de escalonamento e responsabilidades (Cap. 14).
- Critérios de impacto (Cap. 01) que suportam a classificação de severidade.

**Lacunas intencionais**

O SbD-ToE não fixa um modelo canónico de dados para incidentes, nem uma taxonomia P0–P3 "oficial", nem os templates de submissão. Isto é intencional: DORA, NIS2, HIPAA pedem conjuntos diferentes de campos e formatos. O manual diz "registar o incidente com campos obrigatórios", e o conjunto final de campos vem do normativo aplicável (no caso NIS2, das orientações nacionais e do Art. 23).

**Como cumprir**

Sugere-se, no Cap. 12, adotar um schema mínimo (`incident.json/csv`) e parametrizar os campos em função da NIS2 (p. ex., causa provável, severidade, consequências, IOCs, medidas; cf. guias ENISA). Configurar exportadores do SIEM/ITSM → ficheiros prontos a submeter nos prazos (24h/72h/1 mês).

---

### Segurança da cadeia de fornecimento e terceiros

**Conteúdo normativo**

A NIS2 enfatiza segurança da cadeia de fornecimento e de aquisição/desenvolvimento/manutenção (Art. 21), incluindo verificação dos fornecedores críticos e medidas técnicas verificáveis.

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Inventário de dependências e SBOM | Cap. 05 | SBOM, SCA, políticas de atualização |
| Requisitos contratuais técnicos | Cap. 14 | Governança e contratação, práticas de avaliação |
| Arquiteturas portáveis e planos de saída | Cap. 04, Cap. 08 | Arquitetura segura, IaC |

**O que o SbD-ToE cobre**

- Inventário de dependências e SBOM, SCA, políticas de atualização (Cap. 05).
- Requisitos contratuais técnicos (Cap. 14) e práticas de avaliação.
- Arquiteturas portáveis e planos de saída (técnicos).

**Lacunas intencionais**

Listas nacionais de entidades a registar, procedimentos de designação e requisitos jurídicos de contrato (variam entre Estados-Membros). Campos normativos específicos de registos nacionais.

**Como cumprir**

Sugere-se estender o registo de fornecedores do Cap. 05 com os campos exigidos pela autoridade nacional (seguindo guias/portais locais e as notas da ENISA).

---

### Continuidade, crise e operação

**Conteúdo normativo**

A NIS2 pede continuidade de negócio, gestão de crise, backups e DR testados, e monitorização/logging eficazes (Art. 21).

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Runbooks e exercícios de resposta/recuperação | Cap. 12 | Runbooks, exercícios, testes |
| Backups com testes de restauração | Cap. 12 | Backups testados, validação |
| Logging/observabilidade "by design" | Cap. 12 | Logging, observabilidade, retenção |

**O que o SbD-ToE cobre**

- Runbooks e exercícios de resposta/recuperação (Cap. 12).
- Backups com testes de restauração e validação (Cap. 12).
- Logging/observabilidade "by design" (Cap. 12), com orientação para retenção alinhável a normas.

**Lacunas intencionais**

Períodos de retenção e campos exactos de logs: variam entre NIS2, DORA e regimes setoriais; o manual define "logs com campos obrigatórios" e deixa os campos finais para serem plugados segundo o normativo aplicável (NIS2 aqui).

**Como cumprir**

Sugere-se alinhar a matriz de fontes (app, IAM, rede, cloud audit, EDR) e retenção com as orientações ENISA, colhendo exemplos de evidência para auditoria.

---

## PARTE II: SÍNTESE E REFERÊNCIAS

### Síntese da cobertura NIS2/SbD-ToE

A NIS2 pede gestão com responsabilidade, medidas com substância e reportes com prazos. O SbD-ToE oferece o coração técnico-operacional: políticas, processos, testes, inventários, automação e evidências.

As aparentes lacunas do manual - quem aprova políticas, campos rígidos de logs/incidentes, templates e formatos de submissão, pormenores jurídicos de contratos - são lacunas deliberadas: detalhes específicos que mudam entre normas e países e que, por isso, o SbD-ToE deixa configuráveis.

O resultado é elegante:

- **Hoje**, o SbD-ToE permite a qualquer equipa praticar segurança por desenho com qualidade.
- **Amanhã**, quando a organização quiser cumprir NIS2, basta ligar os detalhes - aprovação pelo board (Art. 20), campos e prazos de incidente (Art. 23), mapeamento das medidas (Art. 21) e, quando necessário, requisitos nacionais.

Assim, o SbD-ToE mantém-se universal e quente na prática diária, e a NIS2 acrescenta a camada de formalidade e supervisão. Juntos, constroem uma conformidade sustentável - não por check-box, mas por construção.

### Setor, âmbito e sanções

A NIS2 alarga o âmbito para 18 setores (Anexos I/II) e reforça a distinção entre essenciais e importantes. Em muitos países, há registos nacionais e prazos de autoregisto para entidades abrangidas; acompanhar trackers oficiais ajuda a implementar as especificidades locais.

Em termos sancionatórios, a Diretiva estabelece patamares que os Estados-Membros transpõem: até 10M€ ou 2% do volume de negócios mundial para essenciais e até 7M€ ou 1,4% para importantes (o que for mais elevado).

### Referências

- **Diretiva NIS2**: Diretiva (UE) 2022/2555 (CELEX: [32022L2555](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022L2555))
- **Art. 20** - Responsabilidade do órgão de gestão e obrigação de formação.
- **Art. 21** - Medidas mínimas de gestão de risco (abordagem "all-hazards").
- **Art. 23** - Prazos de reporte de incidentes (24h/72h/1 mês) e relatórios intermédios.
- **Art. 34** - Sanções administrativas máximas (10M€ ou 2%; 7M€ ou 1,4%).
- **ENISA & Comissão Europeia (2024/2025)** - Orientações técnicas e mapeamentos práticos com exemplos de evidência para Art. 21.
- **ENISA** - *Technical implementation guidance for NIS2 risk-management measures* (exemplos de evidência e mapeamentos).
- **Autoridades nacionais NIS2** - Guias/portais de registo e requisitos locais (exemplos: NCSC nacionais).

---

:::note Exceções e evidência de controlo

A NIS2, tal como a DORA, beneficia de um processo formal de exceções à conformidade. Casos onde um requisito específico não é aplicável ou onde se aceita um risco temporário devem ser documentados, aprovados pelo órgão de gestão e revistos periodicamente.

O Cap. 14 (Governança e Contratação) do SbD-ToE fornece os artefactos necessários: registo de exceções, critérios de aceitação de risco, cadeia de aprovação e plano de remediação. A existência deste processo não é sinal de fragilidade - é evidência de governação madura e de controlo consciente sobre o perfil de risco da organização.

:::
