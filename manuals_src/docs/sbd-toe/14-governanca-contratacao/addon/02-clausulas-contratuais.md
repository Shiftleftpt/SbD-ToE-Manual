---
id: modelo-validacao-fornecedores
title: Modelo de Validação de Fornecedores
sidebar_position: 3
description: Processo para validação de segurança em fornecedores, contratados e terceiros técnicos
tags: [fornecedores, validacao, terceiros, contratacao]
---



# 📜 Cláusulas Contratuais de Segurança {governanca-contratacao:addon:modelo-validacao-fornecedores}

## 🌟 Objetivo {governanca-contratacao:addon:modelo-validacao-fornecedores#objetivo}

Fornecer um conjunto de **cláusulas contratuais reutilizáveis e proporcionais ao risco**, adaptáveis ao tipo de contratação, para garantir que os requisitos de segurança são **formalmente exigidos, rastreáveis e auditáveis**.

Estas cláusulas devem:

- Refletir os **requisitos mínimos por risco** (Capítulo 1 e 2);
- Ser aplicáveis a diferentes tipos de contrato: SaaS, outsourcing, licenciamento ou equipas mistas;
- Ser válidas durante **todo o ciclo de vida contratual**, e não apenas na fase inicial;
- Prever mecanismos de validação, penalização e responsabilização objetiva.

---

## 📘 O que são cláusulas contratuais de segurança {governanca-contratacao:addon:modelo-validacao-fornecedores#o_que_sao_clausulas_contratuais_de_seguranca}

São disposições formais incorporadas nos contratos com fornecedores, parceiros ou contratados, que visam garantir a **conformidade com requisitos técnicos, legais e organizacionais de segurança**, incluindo:

- Aplicação de controlos mínimos;
- Notificação de incidentes;
- Entrega de evidência (ex: SBOM, testes, relatórios);
- Gestão de vulnerabilidades e atualizações;
- Responsabilização por falhas ou incumprimentos.

> 📎 Estas cláusulas são essenciais para transferir obrigações de segurança e alinhar o fornecedor com os princípios do SbD-ToE.

---

## 🛠️ Como aplicar {governanca-contratacao:addon:modelo-validacao-fornecedores#como_aplicar}

### 🧩 Por tipo de contrato {governanca-contratacao:addon:modelo-validacao-fornecedores#por_tipo_de_contrato}

#### 🏷️ SaaS / Serviços geridos {governanca-contratacao:addon:modelo-validacao-fornecedores#saas__servicos_geridos}

| Tema                    | Cláusula sugerida                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------|
| Segurança mínima        | O fornecedor garante conformidade com os controlos definidos conforme o nível de risco da aplicação. |
| Vulnerabilidades        | Compromisso de correção de CVEs críticos em \<72h após divulgação pública.                        |
| SBOM / transparência    | Disponibilização de SBOM atualizado com dependências críticas, mediante solicitação.             |
| Incidentes              | Notificação de incidentes de segurança no prazo máximo de 24h após deteção.                      |
| Auditoria / evidência   | Direito da organização a solicitar evidência de controlos ou realizar auditorias formais.         |

#### 🛠️ Outsourcing de desenvolvimento {governanca-contratacao:addon:modelo-validacao-fornecedores#outsourcing_de_desenvolvimento}

| Tema                    | Cláusula sugerida                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------|
| Requisitos por risco    | Aplicação dos requisitos do Catálogo SbD-ToE conforme o nível de risco da aplicação.             |
| Integração no CI/CD     | Artefactos entregues devem integrar pipelines com testes de segurança automatizados.             |
| Revisões de segurança   | Aceitação de revisões de código e arquitetura pela equipa de segurança da organização.            |
| Propriedade intelectual | Código-fonte e documentação de segurança são propriedade da organização contratante.             |

#### 👥 Desenvolvimento interno (contratados ou equipas mistas) {governanca-contratacao:addon:modelo-validacao-fornecedores#desenvolvimento_interno_contratados_ou_equipas_mistas}

| Tema                    | Cláusula sugerida                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------|
| Acesso restrito         | Acesso apenas a ambientes de desenvolvimento, com credenciais temporárias e rastreáveis.         |
| Formação em SbD         | Obrigatoriedade de formação em práticas de Security by Design antes de contribuição técnica.     |
| Responsabilidades       | Aplicação dos requisitos de segurança atribuídos via tickets documentados.                       |
| Rastreabilidade         | Registo completo do trabalho ligado a tarefas e validações de segurança.                         |

#### 💽 Contratos de licenciamento (software externo) {governanca-contratacao:addon:modelo-validacao-fornecedores#contratos_de_licenciamento_software_externo}

| Tema                    | Cláusula sugerida                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------|
| Conformidade            | Conformidade com normas reconhecidas (ex: ISO 27001, OWASP ASVS).                                |
| CVEs e atualizações     | Obrigação de comunicar e mitigar vulnerabilidades críticas com celeridade.                       |
| Atualizações de segurança | Direito da organização a atualizações corretivas durante o contrato.                          |
| Dados e telemetria      | Transparência e consentimento explícito para recolha de dados ou métricas.                       |

---

## 📊 Cláusulas adicionais por nível de risco {governanca-contratacao:addon:modelo-validacao-fornecedores#clausulas_adicionais_por_nivel_de_risco}

| Nível de Risco | Cláusulas adicionais recomendadas                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------|
| **L1 (baixo)** | Compromisso genérico com boas práticas; política de notificação de incidentes                         |
| **L2 (médio)** | Aplicação do Catálogo SbD-ToE; fornecimento de evidência técnica sob solicitação                      |
| **L3 (elevado)** | Testes de segurança obrigatórios; SBOM entregue; SLA para correções críticas; direito formal de auditoria |

> 📘 Usar a matriz de aplicação de requisitos (Cap. 1 – Anexo 06) como base para decidir o nível contratual exigido.

---

## 📋 Campos recomendados por cláusula {governanca-contratacao:addon:modelo-validacao-fornecedores#campos_recomendados_por_clausula}

Cada cláusula deve incluir:

- Referência ao **requisito aplicável** (ex: REQ-LOG-002, ARC-005);
- Indicação do **nível de risco** (L1–L3);
- Forma de validação esperada (evidência técnica, auditoria, testes);
- Penalizações ou impacto contratual em caso de incumprimento;
- Periodicidade de revisão (ex: em renovações, novas versões ou releases).

---

## 📂 Integração com procurement e jurídico {governanca-contratacao:addon:modelo-validacao-fornecedores#integracao_com_procurement_e_juridico}

- Disponibilizar cláusulas em **formato modular** (blocos por tipo e por risco);
- Manter repositório de versões validadas (ex: Git, Confluence, SharePoint);
- Integrar no modelo de onboarding de fornecedores (ver `03-modelo-validacao-fornecedores.md`);
- Garantir formação básica dos stakeholders na ligação entre risco e exigência contratual.

---

## ✅ Boas práticas {governanca-contratacao:addon:modelo-validacao-fornecedores#boas_praticas}

- Preferir cláusulas **objetivas, auditáveis e proporcionais ao risco**;
- Evitar linguagem vaga ou genérica sem critérios de validação;
- Alinhar cláusulas com requisitos reais de segurança (Cap. 2 e 7);
- Reavaliar cláusulas periodicamente, especialmente em renovações ou mudanças técnicas;
- Registar as cláusulas efetivamente aplicadas a cada contrato.

---

## 🔗 Referências cruzadas {governanca-contratacao:addon:modelo-validacao-fornecedores#referencias_cruzadas}

| Documento / Capítulo                 | Relação com cláusulas contratuais                   |
|--------------------------------------|-----------------------------------------------------|
| Capítulo 01 — Gestão de Risco        | Define a proporcionalidade por nível L1–L3         |
| Capítulo 02 — Requisitos de Segurança| Catálogo e requisitos aplicáveis por risco         |
| addon/03-modelo-validacao-fornecedores.md | Requisitos de onboarding contratual               |
| canon/20-checklist-revisao.md        | Verifica a formalização e aplicação contratual      |

---
