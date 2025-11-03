---
id: aplicacao-por-level
title: Aplicação com proporcionalidade
description: Guia operativo e narrativo da proporcionalidade L1–L3 no SbD-ToE, com ligação a capítulos prescritivos e regulatórios
tags: [levels, proporcionalidade, risco, aplicacao, nis2, dora, pci, hipaa]
sidebar_position: 4
---



# Aplicação por Nível de Risco

O SbD-ToE baseia-se no princípio da proporcionalidade ao risco.  
Nem todas as aplicações justificam o mesmo esforço, mas todas requerem um mínimo inegociável de segurança.  
Os três níveis definidos — L1, L2 e L3 — funcionam como um mapa de orientação: indicam com clareza o que é obrigatório em cada cenário, quais os reforços exigidos e onde encontrar detalhe nos capítulos prescritivos.

---

## Nível L1 — Aplicações de Baixo Risco

O nível L1 aplica-se a aplicações de impacto reduzido, como protótipos, sistemas internos ou software sem dados sensíveis.  
O objetivo é estabelecer um piso comum de segurança, suficiente para mitigar vulnerabilidades triviais, mas sem onerar equipas com processos complexos.  

**Práticas obrigatórias em L1:**
- Classificação simplificada de criticidade (Cap. 01).  
- Definição e implementação de requisitos mínimos (Cap. 02).  
- Adoção de coding guidelines básicas com linters automáticos (Cap. 06).  
- Uso de imagens oficiais **pinned** para containers (Cap. 09).  
- Inventário manual de dependências críticas (Cap. 05).  
- Logging básico e monitorização elementar (Cap. 12).  
- Formação inicial da equipa em segurança (Cap. 13).  

Este nível assegura que mesmo sistemas de baixo risco não ficam desprotegidos nem invisíveis no processo de governação.  
Ainda que não estejam sujeitos a exigências regulatórias intensas, as práticas de L1 alinham-se com princípios universais de *security by design* presentes no GDPR, em controlos de normas ISO/IEC e nas recomendações genéricas da ENISA.  
Assim, uma organização pode demonstrar que mesmo o software menos crítico cumpre o mínimo normativo esperado.

---

## Nível L2 — Aplicações de Risco Moderado

O nível L2 corresponde à maioria das aplicações de produção, especialmente aquelas que processam dados de utilizadores, informação de negócio ou que interagem com sistemas externos.  
Aqui a segurança deixa de ser apenas defensiva e torna-se disciplina sistemática, com reforço de práticas em todos os domínios.  

**Práticas obrigatórias em L2 (inclui todas as de L1, mais):**
- Classificação completa da criticidade com múltiplos eixos (Cap. 01).  
- Requisitos reforçados alinhados com ameaças prevalentes (Cap. 02).  
- Sessões de threat modeling documentadas (Cap. 03).  
- Revisão arquitetural formal com padrões seguros (Cap. 04).  
- SBOM automatizado com scanners em pipeline (Cap. 05).  
- Pipelines CI/CD com gates de aprovação obrigatórios (Cap. 07).  
- IaC validado com linters e *policy-as-code* (Cap. 08).  
- Containers sujeitos a scans regulares e baseline de runtime (Cap. 09).  
- Testes de segurança automatizados (Cap. 10).  
- Deploy automatizado com controlos de configuração (Cap. 11).  
- Monitorização automatizada com dashboards (Cap. 12).  
- Formação contínua adaptada a funções (Cap. 13).  
- Cláusulas contratuais reforçadas com fornecedores (Cap. 14).  

Ao introduzir threat modeling obrigatório, revisões arquiteturais formais e automação de SBOM, este nível cria disciplina e consistência.  
Os pipelines deixam de ser apenas mecanismos de integração e tornam-se pontos de controlo que bloqueiam versões inseguras.  
Do ponto de vista regulatório, estas práticas alinham-se com obrigações de NIS2 (gestão de risco digital, reporte de incidentes), DORA (resiliência operacional e testes periódicos), PCI-DSS (proteção de dados financeiros) e HIPAA (salvaguarda de informação clínica).  
L2 é, em muitos casos, o nível em que organizações atingem uma zona de conformidade robusta com normas e regulamentos transversais.

---

## Nível L3 — Aplicações de Alto Risco

O nível L3 aplica-se a software crítico: sistemas financeiros, de saúde, infraestruturas essenciais ou aplicações com impacto social elevado.  
Aqui a tolerância ao risco é mínima, e cada prática é formal, documentada e auditada.  

**Práticas obrigatórias em L3 (inclui todas as de L1 e L2, mais):**
- Revisão formal da classificação aprovada por GRC e gestão (Cap. 01).  
- Cumprimento integral de todos os requisitos definidos (Cap. 02).  
- Threat modeling detalhado com cenários avançados (Cap. 03).  
- Arquitetura documentada, auditada e sujeita a revisões independentes (Cap. 04).  
- SBOM completo, assinado e monitorizado em tempo real (Cap. 05).  
- Revisão de código com cobertura total e scanners avançados (Cap. 06).  
- Pipelines com assinaturas de release e segregação de ambientes (Cap. 07).  
- Governação de IaC com enforcement obrigatório (Cap. 08).  
- Containers assinados e atestados, com runtime enforcement (Cap. 09).  
- Testes avançados (fuzzing, DAST, IAST) com cobertura integral (Cap. 10).  
- Deploy governado com rollback seguro e segregação rigorosa (Cap. 11).  
- Integração com SIEM/SOAR e playbooks de resposta (Cap. 12).  
- Programa contínuo de treino com simulações realistas (Cap. 13).  
- Governação contratual com métricas, auditorias e penalizações (Cap. 14).  

Neste nível, os pipelines transformam-se em cadeias de confiança assinadas, a arquitetura é revista por auditores independentes e a resposta a incidentes é suportada por automação avançada (SIEM, SOAR).  
As relações com fornecedores incluem métricas de conformidade e cláusulas vinculativas.  
Do ponto de vista regulatório, L3 materializa as exigências mais severas: NIS2 e DORA para infraestruturas críticas, PCI-DSS para sistemas financeiros, HIPAA para proteção de dados clínicos, GDPR para privacidade, e AI Act para software de alto impacto social.  
Cumprir L3 significa alinhar práticas técnicas de ponta com as mais exigentes obrigações regulatórias internacionais.

---

## Considerações Finais

O modelo L1–L3 não é uma escala de maturidade organizacional, mas sim de criticidade aplicacional.  
O que muda não é a competência da equipa, mas o grau de rigor exigido em função do risco.  

- L1 evita vulnerabilidades triviais e garante mínimos normativos.  
- L2 introduz disciplina sistemática e facilita conformidade transversal.  
- L3 assegura resiliência estratégica e cumprimento dos referenciais mais exigentes.  

Esta abordagem permite às organizações dimensionar esforços de forma proporcional, demonstrar conformidade regulatória perante múltiplos referenciais (NIS2, DORA, PCI-DSS, HIPAA, GDPR, AI Act) e criar transparência: cada aplicação sabe exatamente o que deve cumprir, sem sobrecarga nem ambiguidades.
