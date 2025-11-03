---
id: dora
title: DORA — Cross-check normativo
description: Como o SbD-ToE cobre, deixa em aberto de forma deliberada, e pode ser ajustado para alinhar-se com o Regulamento DORA (UE 2022/2554)
tags: [cross-check, dora, regulamentacao, ict-risk, resiliencia, finanças]
sidebar_position: 1
---



# Cross-check normativo — DORA

## Enquadramento geral

O **Digital Operational Resilience Act (DORA)** — Regulamento (UE) 2022/2554 — representa uma viragem histórica na forma como a União Europeia encara a **resiliência digital** no setor financeiro.  
A partir de janeiro de 2025, não basta às entidades financeiras protegerem dados ou cumprirem boas práticas gerais: exige-se que demonstrem, com evidências e mecanismos consistentes, que **sabem identificar, prevenir, detetar, responder e aprender com riscos tecnológicos**.

O DORA é abrangente, mas pragmático. Divide-se em cinco blocos centrais: gestão de risco TIC, gestão de incidentes e reporte, testes de resiliência, gestão de terceiros críticos e partilha de informação.  
O SbD-ToE, apesar de não ter sido escrito “a pensar” no DORA, cobre muitos destes pontos **por omissão**, graças à sua génese **top-down** e à integração de múltiplas referências normativas e técnicas.  
O que aqui fazemos é mostrar, de forma rigorosa e descritiva, **como o SbD-ToE se cruza com cada pilar da DORA, o que cobre já hoje, o que deixa de fora de forma deliberada, e como pequenas integrações podem bastar para cumprir plenamente o regulamento**.

---

## Gestão de risco TIC

O primeiro pilar da DORA reforça a ideia de que a **resiliência digital é responsabilidade última do órgão de gestão**. O Artigo 5 é claro: cabe ao board aprovar a estratégia, supervisionar a sua execução e garantir que existe capacidade de resposta. A norma exige ainda inventários de funções críticas, políticas de proteção, deteção, resposta e recuperação, planos de comunicação de crise e revisões regulares.

Aqui, o SbD-ToE já fornece uma base sólida:  
- O **Capítulo 01** estabelece a **classificação de criticidade aplicacional**, permitindo identificar quais as funções críticas e qual o seu peso no risco global.  
- O **Capítulo 02** traz um **catálogo prescritivo de requisitos de segurança**, que se traduzem diretamente em políticas técnicas.  
- O **Capítulo 03**, dedicado ao **Threat Modeling**, apoia a identificação de cenários de risco e vulnerabilidades.  
- O **Capítulo 12** cobre a **deteção, resposta e melhoria contínua** nas operações.  
- O **Capítulo 14** detalha a **governação e a aprovação de políticas**.

O que não aparece, e não por falha mas por escolha metodológica, é a definição de **quem aprova** essas políticas. O SbD-ToE exige que sejam aprovadas e monitorizadas, mas não fixa se a assinatura deve ser técnica (equipa) ou institucional (board). Esta abertura é intencional: permite que uma start-up use o modelo para reforçar o seu ciclo de desenvolvimento, mas que uma entidade financeira, sujeita ao DORA, alinhe a aprovação ao board e registe formalmente a decisão.  

Do mesmo modo, o manual prescreve planos de comunicação de crise (Cap. 12), mas não congela um template único — sabendo que o DORA e outras normas têm formatos específicos.  
A proporcionalidade, também exigida pela DORA, já existe no SbD-ToE (classificação L1–L3), mas sem thresholds normativos fixos, para não se tornar dependente de uma só regulação.

Na prática: **o SbD-ToE entrega os mecanismos**; cabe à organização adaptá-los ao nível formal exigido. Para cumprir DORA, basta mapear as políticas já prescritas → aprová-las em board meeting → registar a decisão.  

---

## Incidentes e reporte

O segundo pilar da DORA trata de incidentes. A norma exige um processo ponta-a-ponta, desde a deteção até ao reporte formal, passando pelo registo completo, classificação de severidade e submissão de relatórios através de templates normalizados.

O SbD-ToE cobre o essencial:  
- O **Capítulo 12** obriga a que existam processos de deteção e resposta, com aprendizagem pós-incidente.  
- O **Capítulo 14** distribui responsabilidades de reporte e escalonamento.  
- O **Capítulo 01** fornece métricas de impacto que podem sustentar classificações.

Mas, mais uma vez, os **detalhes ficam de fora de propósito**. O manual não define um modelo canónico de dados para incidentes, nem fixa uma taxonomia de severidade (P0–P3), nem inclui os templates de reporte. Porquê? Porque cada norma (DORA, NIS2, HIPAA) tem os seus próprios campos e classificações. Se o SbD-ToE os tivesse fixado, deixaria de ser universal.  

Ainda assim, a integração é simples:  
- O Cap. 12 já pede um registo estruturado de incidentes. Para cumprir DORA, basta configurar esse registo para incluir os campos obrigatórios definidos nos RTS/ITS (sistemas afetados, custos, tempos, medidas).  
- A tabela de severidade genérica do SbD-ToE pode ser alinhada aos thresholds de reporte da DORA.  
- Exportadores do SIEM/ITSM podem ser usados para gerar automaticamente os ficheiros para submissão.  

Assim, o manual não falha: **dá a estrutura, mas deixa os detalhes para quem aplica a norma específica**.

---

## Testes de resiliência

O terceiro pilar da DORA reforça a necessidade de testes regulares e proporcionais, culminando no **Threat-Led Penetration Testing (TLPT)** obrigatório para certas entidades. Exige-se um programa de testes contínuo e, em casos selecionados, testes conduzidos por equipas externas com base em inteligência de ameaça real.

Aqui, o SbD-ToE brilha naturalmente:  
- O **Capítulo 03** já prescreve a prática de threat modeling, que gera cenários realistas de ataque.  
- O **Capítulo 10** fornece um catálogo completo de testes técnicos (automatizados, manuais, fuzzing, etc.).  
- O **Capítulo 11** reforça a validação de segurança em pré-produção.  

O que fica de fora — de forma deliberada — são os aspetos formais: o manual não diz quem decide a elegibilidade para TLPT (porque depende do supervisor), não descreve o processo de attestation (porque é regulatório) e não lista os requisitos administrativos para testers externos (que variam entre reguladores).  

A integração, mais uma vez, é simples:  
- O Cap. 10 pode incluir uma secção de “Readiness TLPT”, com critérios de escopo, uso de threat intel e gestão de achados.  
- Os relatórios e evidências já previstos no SbD-ToE servem como base para o attestation.  

---

## Gestão de terceiros TIC

O quarto pilar da DORA reconhece a dependência crescente de fornecedores de TIC. Exige uma estratégia clara, um registo formal de contratos, avaliação de concentração, cláusulas obrigatórias e, em alguns casos, supervisão de fornecedores críticos por autoridades competentes.

O SbD-ToE já traz mecanismos diretos:  
- O **Capítulo 05** obriga a inventários detalhados de dependências, incluindo SBOM e serviços externos.  
- O **Capítulo 14** trata de governança e contratação, cobrindo cláusulas de segurança e avaliação de fornecedores.

O que não está no manual são os **detalhes específicos do regulamento**: os templates ITS para registo de contratos, a fórmula de análise de concentração pedida pela DORA, as cláusulas jurídicas obrigatórias (jurisdição, insolvência, subcontratação) e a relação com o Lead Overseer para fornecedores críticos.  

E novamente, isto é intencional: essas exigências variam entre normas (DORA, NIS2, ISO 27036).  
O SbD-ToE prefere prescrever o que é universal (inventário, avaliação de risco, cláusulas técnicas de segurança) e deixar o detalhe para o normativo.  

Para integrar, bastaria:  
- Estender o inventário de fornecedores do Cap. 05 com os campos exigidos pelo ITS da DORA (localização, subcontratação, criticidade).  
- Acrescentar no Cap. 14 uma checklist de planos de saída testados.  
- Calcular métricas de exposição (n.º de serviços críticos por fornecedor).  

---

## Partilha de informação

O quinto pilar trata da partilha voluntária de informação sobre ameaças. O objetivo é reforçar a cooperação e inteligência coletiva, mas sempre dentro das regras de confidencialidade, privacidade e concorrência.

O SbD-ToE cobre isto de forma natural:  
- O **Capítulo 12** prevê a integração de threat intelligence (STIX/TAXII).  
- O **Capítulo 14** contempla políticas de cooperação.  

O que não define — propositadamente — são os **acordos institucionais de adesão**, as **regras de governação das comunidades** e o processo de **notificação ao supervisor**. Esses elementos não são universais: mudam entre setores e países.  

Na prática, para cumprir DORA, basta às organizações:  
- Usar os mecanismos de threat intel já prescritos pelo SbD-ToE.  
- Firmar acordos de adesão de acordo com a comunidade em causa.  
- Notificar o supervisor segundo os canais indicados.  

---

## Conclusão

O **SbD-ToE cobre o coração técnico da DORA**.  
Tudo aquilo que é universal — inventários, políticas, requisitos, testes, incidentes, governação — já está prescrito.  
As lacunas que se observam não são falhas, mas sim **abstenções deliberadas**: detalhes específicos de uma norma, que variam entre regulamentos, foram deixados em aberto para que o manual seja **universal**.  

Isto significa que, ao aplicar o SbD-ToE, uma organização já tem **a estrutura e os processos nucleares**.  
Para cumprir DORA, precisa apenas de alinhar esses processos com os **detalhes normativos específicos**: aprovar políticas em board meeting, mapear campos de incidentes aos templates, estender inventários com campos ITS, calcular métricas de concentração e formalizar acordos de partilha.  

Em suma:  
- O SbD-ToE garante **“compliance by design”** em termos técnicos.  
- A DORA acrescenta a camada de **formalidade regulatória**.  
- A combinação dos dois permite a uma organização atingir conformidade plena, com mínimo esforço adicional, sem comprometer a neutralidade e aplicabilidade transversal do manual.

---
