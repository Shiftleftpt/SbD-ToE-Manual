---
id: nis2
title: NIS2 — Cross-check normativo
description: Como o SbD-ToE cobre, deixa em aberto deliberadamente e pode integrar rapidamente os requisitos da Diretiva NIS2 (UE 2022/2555)
tags: [cross-check, nis2, diretiva, ciberseguranca, incident-reporting, governance]
sidebar_position: 3
---

# Cross-check normativo — NIS2

## Enquadramento geral

A **Diretiva (UE) 2022/2555 — NIS2** atualiza o quadro europeu de cibersegurança para **entidades essenciais e importantes** em 18 setores, reforçando **governação**, **medidas de gestão de risco**, e **obrigação de reporte de incidentes**. Os Estados-Membros tinham até **17 de outubro de 2024** para transpor a NIS2 e a NIS1 foi revogada a **18 de outubro de 2024**. [^1]

No espírito da NIS2, não chega “ter controlos”; é preciso demonstrar **capacidade operacional** e **responsabilização da gestão**. O SbD-ToE, construído **top-down** e atento a múltiplas referências, encaixa naturalmente neste ethos: entrega **processos, políticas e artefactos técnicos** reutilizáveis, deixando propositadamente algumas variáveis em aberto para preservar a **universalidade** do manual.

---

## Governação (Art. 20): responsabilidade clara… e intencionalmente configurável

A NIS2 coloca o **órgão de gestão** no centro: ele **aprova** as medidas de gestão de risco de cibersegurança, **supervisiona a execução** e **pode ser responsabilizado** por incumprimentos. Exige ainda **formação** regular para a gestão. [^2]

**O que o SbD-ToE já cobre por omissão**  
- Prescreve **políticas** e **papéis** (Cap. 02 — Requisitos; Cap. 14 — Governança e Contratação).  
- Define **ciclos de aprovação** e **monitorização** (com métricas e evidências operacionais).  

**O que deixa em aberto (deliberadamente)**  
- **Quem assina** as políticas: o manual exige aprovação formal, mas **não fixa** se é equipa técnica, CISO ou **board**. Isto é propositado: em contextos puramente técnicos, **aprovação operacional** basta; para **conformidade NIS2**, a aprovação deve ser do **órgão de gestão**. [^3]

**Como integrar facilmente para NIS2**  
- Registar, no **Cap. 14**, que as políticas do SbD-ToE foram **aprovadas pelo board**, com evidência de formação periódica à gestão (conforme Art. 20). [^4]

---

## Medidas de gestão de risco (Art. 21): o núcleo técnico do SbD-ToE

O Art. 21 pede um conjunto **mínimo** de medidas, num **all-hazards approach**: políticas de análise de risco e segurança, **gestão de incidentes**, **continuidade/crise** (backups, DR), **segurança da cadeia de fornecimento**, **segurança em aquisição/desenvolvimento/manutenção**, **avaliação da eficácia dos controlos**, **higiene cibernética/treino**, **IAM**, **criptografia**, **gestão de vulnerabilidades/patching**, **logging e monitorização**, entre outras. [^5]

Em 2024/2025, a Comissão e a ENISA publicaram **orientações técnicas** e mapeamentos práticos com **exemplos de evidência** para implementar estas medidas — utilíssimos para auditoria. [^6]

**O que o SbD-ToE já cobre por omissão**  
- **Políticas e controlos técnicos** (Cap. 02).  
- **Classificação de criticidade** & risco proporcional (Cap. 01).  
- **Threat modeling** (Cap. 03).  
- **Cadeia de fornecimento**: SBOM/SCA, dependências (Cap. 05).  
- **CI/CD & IaC** seguros (Cap. 07 e Cap. 08); **containers/runtime** (Cap. 09).  
- **Testes** (Cap. 10) e **deploy seguro** (Cap. 11).  
- **Monitorização, logging, resposta e melhoria contínua** (Cap. 12).  
- **Governança & contratação** (Cap. 14), incluindo avaliação de terceiros.

**O que deixa em aberto (deliberadamente)**  
- **Taxonomias/formatos “fechados”**: a NIS2 detalha tópicos, mas o **detalhe** (p. ex., **lista exata de campos** de logs ou **templates** de políticas) pode variar entre jurisdições e setores. O SbD-ToE mantém **modelos genéricos**, para que possam ser “plugados” aos requisitos nacionais/sectoriais. [^7]

**Como integrar facilmente para NIS2**  
- Usar o catálogo do Cap. 02 como **base de SoA técnica** e alinhar as evidências com o **guia técnico da ENISA** (exemplos de evidência e mapeamentos). [^8]  
- Declarar, no Cap. 01, que a **proporcionalidade** segue as classes NIS2 (essencial/important) e o **impacto nos serviços**.

---

## Incidentes e reporte (Art. 23): prazos claros, detalhes configuráveis

A NIS2 define um **trilho de reporte** para incidentes **significativos**:  
- **Alerta cedo** (“early warning”) **até 24h** após conhecimento.  
- **Notificação** com avaliação inicial **até 72h**.  
- **Relatório final** **até 1 mês** (podendo haver atualizações intermédias). [^9]

**O que o SbD-ToE já cobre por omissão**  
- Processo de **deteção e resposta**, com **pós-incidente** (Cap. 12).  
- Papéis de **escalonamento** e **responsabilidades** (Cap. 14).  
- **Critérios de impacto** (Cap. 01) que suportam a **classificação de severidade**.

**O que deixa em aberto (deliberadamente)**  
- O SbD-ToE **não fixa** um **modelo canónico de dados** para incidentes, **nem** uma **taxonomia P0–P3 “oficial”**, **nem** os **templates de submissão**. Isto é intencional: **DORA, NIS2, HIPAA** pedem conjuntos **diferentes** de campos e formatos.  
- O manual diz “**registar o incidente com campos obrigatórios**”, e **o conjunto final de campos vem do normativo aplicável** (no caso NIS2, das orientações nacionais e do Art. 23). [^10]

**Como integrar facilmente para NIS2**  
- No **Cap. 12**, adotar um **schema mínimo** (`incident.json/csv`) e **parametrizar** os campos em função da NIS2 (p. ex., causa provável, severidade, consequências, IOCs, medidas; cf. guias ENISA). [^11]  
- Configurar exportadores do **SIEM/ITSM → ficheiros** prontos a submeter **nos prazos (24h/72h/1 mês)**. [^12]

---

## Cadeia de fornecimento e terceiros: foco onde o SbD-ToE é forte

A NIS2 enfatiza **segurança da cadeia de fornecimento** e de **aquisição/desenvolvimento/manutenção** (Art. 21), incluindo verificação dos **fornecedores críticos** e **medidas técnicas verificáveis**. [^13]

**O que o SbD-ToE já cobre por omissão**  
- **Inventário de dependências e SBOM**, SCA, políticas de atualização (Cap. 05).  
- **Requisitos contratuais técnicos** (Cap. 14) e práticas de avaliação.  
- **Arquiteturas portáveis** e **planos de saída** (técnicos).

**O que deixa em aberto (deliberadamente)**  
- **Listas nacionais** de entidades a registar, **procedimentos de designação** e **requisitos jurídicos** de contrato (variam entre Estados-Membros).  
- **Campos normativos específicos** de registos nacionais.

**Como integrar facilmente para NIS2**  
- Estender o registo de fornecedores do **Cap. 05** com os **campos exigidos** pela autoridade nacional (seguindo guias/portais locais e as notas da ENISA). [^14]

---

## Continuidade, crise e operação: sobriedade com evidências

A NIS2 pede **continuidade de negócio**, **gestão de crise**, **backups e DR testados**, e **monitorização/logging** eficazes (Art. 21). [^15]

**O que o SbD-ToE já cobre por omissão**  
- **Runbooks** e **exercícios** de resposta/recuperação (Cap. 12).  
- **Backups** com **testes de restauração** e **validação** (Cap. 12).  
- **Logging/observabilidade** “by design” (Cap. 12), com orientação para **retenção** alinhável a normas.

**O que deixa em aberto (deliberadamente)**  
- **Períodos de retenção** e **campos exactos** de logs: variam entre NIS2, DORA e regimes setoriais; o manual define “**logs com campos obrigatórios**” e deixa os **campos finais** para serem **plugados** segundo o normativo aplicável (NIS2 aqui). [^16]

**Como integrar facilmente para NIS2**  
- Alinhar a **matriz de fontes** (app, IAM, rede, cloud audit, EDR) e **retenção** com as orientações ENISA, colhendo **exemplos de evidência** para auditoria. [^17]

---

## Setor, escopo e sanções: o pano de fundo que orienta o detalhe

A NIS2 **alarga o escopo** para 18 setores e reforça a distinção entre **essenciais** e **importantes**. Em muitos países, há **registos nacionais** e prazos de **autoregisto** para entidades abrangidas; acompanhar **trackers oficiais** ajuda a implementar as especificidades locais. [^18]

Em termos sancionatórios, a Diretiva estabelece patamares que os Estados-Membros transpõem: **até 10M€ ou 2%** do volume de negócios mundial para **essenciais** e **até 7M€ ou 1,4%** para **importantes** (o que for mais elevado). [^19]

---

## Conclusão — calor, rigor e pragmatismo

A NIS2 pede **gestão** com responsabilidade, **medidas** com substância e **reportes** com prazos. O SbD-ToE oferece o **coração técnico-operacional**: políticas, processos, testes, inventários, automação e evidências.  
As aparentes lacunas do manual — **quem aprova** políticas, **campos** rígidos de logs/incidentes, **templates** e **formatos** de submissão, **pormenores jurídicos** de contratos — são **lacunas deliberadas**: **detalhes específicos** que mudam entre normas e países e que, por isso, o SbD-ToE deixa **configuráveis**.

O resultado é elegante:  
- **Hoje**, o SbD-ToE permite a qualquer equipa **praticar segurança por desenho** com qualidade.  
- **Amanhã**, quando a organização quiser **cumprir NIS2**, basta **ligar** os detalhes — aprovação pelo board (Art. 20), campos e prazos de incidente (Art. 23), mapeamento das medidas (Art. 21) e, quando necessário, requisitos nacionais. [^20]

Assim, o SbD-ToE mantém-se **universal e quente na prática diária**, e a NIS2 acrescenta a **camada de formalidade e supervisão**. Juntos, constroem uma **conformidade sustentável** — não por check-box, mas **por construção**.

---

## Referências

[^1]: Diretiva (UE) 2022/2555 (“NIS2”), prazos de transposição e revogação da NIS1 (Art. 41 e 44). Texto oficial: EUR-Lex — *eli/dir/2022/2555/oj*.  
[^2]: NIS2, Art. 20 — Responsabilidade do órgão de gestão e obrigação de formação.  
[^3]: NIS2, Art. 20 — Aprovação ao nível do órgão de gestão.  
[^4]: NIS2, Art. 20(2) — Formação periódica da gestão.  
[^5]: NIS2, Art. 21 — Medidas mínimas de gestão de risco (abordagem “all-hazards”).  
[^6]: ENISA & Comissão Europeia (2024/2025) — Orientações técnicas e mapeamentos práticos com exemplos de evidência para Art. 21.  
[^7]: ENISA — Notas de implementação: variação setorial/nacional de taxonomias e formatos.  
[^8]: ENISA — *Technical implementation guidance for NIS2 risk-management measures* (exemplos de evidência e mapeamentos).  
[^9]: NIS2, Art. 23 — Prazos de reporte de incidentes (24h/72h/1 mês) e relatórios intermédios.  
[^10]: NIS2, Art. 23 — Conteúdos mínimos; especificação final por autoridade nacional/sectorial.  
[^11]: ENISA — Campos recomendados para registo de incidentes e exemplos de evidência (schema parametrizável).  
[^12]: NIS2, Art. 23 — Cumprimento de prazos operacionais com exportadores SIEM/ITSM.  
[^13]: NIS2, Art. 21 — Segurança da cadeia de fornecimento; requisitos em aquisição/desenvolvimento/manutenção.  
[^14]: Autoridades nacionais NIS2 — Guias/portais de registo e requisitos locais (exemplos: NCSC nacionais).  
[^15]: NIS2, Art. 21 — Continuidade/gestão de crise, backups/DR, logging/monitorização.  
[^16]: ENISA — Alinhamento de retenções e conteúdos de log com regimes NIS2/DORA/setoriais.  
[^17]: ENISA — Matriz de fontes de log/observabilidade e *examples of evidence*.  
[^18]: NIS2 — Âmbito setorial (Anexos I/II) e distinção entre “essenciais” e “importantes”.  
[^19]: NIS2, Art. 34 — Sanções administrativas máximas (10 M€ ou 2%; 7 M€ ou 1,4%).  
[^20]: Síntese de governação (Art. 20), medidas (Art. 21) e reporte (Art. 23) com apoio das orientações ENISA.
