---
description: Ameaças mitigadas pelas práticas prescritas neste capítulo de arquitetura
  segura
id: ameacas-mitigadas
sidebar_position: 50
tags:
- ameacas
- ameaças
- arquitetura
- dsomm
- oscar
- risco
- stride
title: Ameaças Mitigadas
---


# 🔐 Ameaças Mitigadas - Capítulo 04: Arquitetura Segura

Este capítulo define práticas formais de **design, validação e documentação de arquitetura segura**, incluindo o uso de zonas de confiança, diagramas técnicos, requisitos de arquitetura e validação por risco.  
As ameaças mitigadas dizem respeito à **ausência de controlo sobre fronteiras técnicas, decisões de design e validação formal do modelo da arquitetura**.

> 📌 Arquitetura segura é o ponto de articulação entre **risco, ameaça, requisitos e execução segura** - e um dos principais fundamentos do SbD-ToE.

---

## 🧱 Categoria 1 - Falhas de segmentação e isolamento da arquitetura

| Ameaça                                        | Fonte                           | Como surge                                                    | Como a prática mitiga                                                             | Controlos associados                         | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------------|----------------------------------|----------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------|
| Interfaces expostas sem isolamento            | STRIDE (Information Disclosure)  | API crítica disponível sem controlo ou gateway                | Zonas de confiança com restrições explícitas entre camadas                         | `addon/01-catalogo-requisitos.md`           | ✅                                     |
| Mistura de dados e controlo na mesma zona     | OWASP SAMM Design / ISO 27034    | Lógica e dados críticos partilham contexto de execução        | Separação da arquitetura explícita entre responsabilidades                           | `addon/04-diagramas-referencia.md`          | ✅                                     |
| Acesso lateral não controlado entre módulos   | OSC&R / MITRE ATT&CK             | Módulos comunicam entre si sem autorização definida           | Modelação de fronteiras e regras de comunicação entre zonas                        | `addon/02-casos-praticos.md`                | ✅                                     |
| Ausência de isolamento entre utilizadores     | STRIDE (Elevation of Privilege)  | Vários utilizadores partilham contexto ou memória             | Requisitos obrigam isolamento contextualizado por utilizador/tenant                | `addon/01-catalogo-requisitos.md`           | ✅                                     |

---

## 🔎 Categoria 2 - Deficiências na modelação da arquitetura

| Ameaça                                        | Fonte                          | Como surge                                               | Como a prática mitiga                                                            | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------------|---------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Arquitetura inexistente ou desatualizada      | ISO 27034 / SSDF PW.4          | Equipa trabalha apenas com código ou intuição            | Criação obrigatória de diagrama rastreável e validável por revisor                | `addon/04-diagramas-referencia.md`            | ✅                                     |
| Confusão sobre localização de controlos       | STRIDE / ENISA / OWASP SAMM     | Não se sabe onde aplicar autenticação, logging, etc.     | Diagrama referencia localização esperada de controlos técnicos                    | `addon/01-catalogo-requisitos.md`             | ✅                                     |
| Ambiguidade sobre fronteiras e zonas          | BSIMM AA1.3 / OWASP SAMM        | Arquitetura não explicita onde começa ou termina a app   | Definição formal de ZTCs, fluxos e vetores de ameaça                              | `addon/04-diagramas-referencia.md`            | ✅                                     |
| Arquitetura não revê mecanismos de fallback   | OSC&R Design                    | Falta de arquitetura para falhas, limites, fail-safe     | Requisitos de arquitetura para failover, contingência e segurança por defeito      | `addon/01-catalogo-requisitos.md`             | ❌ Cap. 10                             |

---

## 🧪 Categoria 3 - Validação e evolução da arquitetura negligenciada

| Ameaça                                         | Fonte                              | Como surge                                             | Como a prática mitiga                                                          | Controlos associados                      | 🧩 Mitigada apenas por este capítulo? |
|------------------------------------------------|-------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------|----------------------------------------|
| Arquitetura nunca revista                     | ISO 27034 / SSDF PW.5              | Uma vez desenhada, nunca mais é validada              | Integração com ciclo de vida e validações periódicas por risco                 | `15-aplicacao-lifecycle.md`        | ❌ Cap. 01                             |
| Alterações estruturais sem revalidação        | CAPEC-137 / OWASP SAMM             | Mudança crítica de fluxo não revê modelo da arquitetura | Validação da arquitetura forçada por evento ou por sprint                        | `addon/05-validacao.md`                  | ✅                                     |
| Design informal ou ad hoc                     | BSIMM13 - Architecture Analysis    | Arquitetura emerge do código                           | Templates de validação e checklist mínimo de revisão                            | `addon/05-validacao.md`                  | ✅                                     |
| Exceções de arquitetura sem rasto              | SSDF RM.1 / ISO 27005 / DSOMM - Documentation           | Casos “especiais” não são revistos ou documentados     | Gestão formal de exceções com validação técnica e aprovação                      | `addon/03-excecoes.md`                   | ❌ Cap. 14                             |

---

## 🔄 Categoria 4 - Ausência de rastreabilidade e requisitos de arquitetura

| Ameaça                                       | Fonte                             | Como surge                                            | Como a prática mitiga                                                      | Controlos associados                         | 🧩 Mitigada apenas por este capítulo? |
|----------------------------------------------|------------------------------------|-------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------|
| Requisitos de arquitetura não definidos      | SSDF PW.1 / ISO 27034              | Apenas requisitos funcionais ou de negócio            | Catálogo de requisitos específicos para arquitetura                          | `addon/01-catalogo-requisitos.md`            | ✅                                     |
| Impossibilidade de mapear decisões a controlos| OWASP SAMM Design / BSIMM AA1.6    | Decisões de arquitetura não se traduzem em controlos   | Rastreabilidade entre decisão → requisito → controlo                          | `addon/06-rastreabilidade.md`                | ✅                                     |
| Diagrama não reflete controlos implementados | OWASP SAMM / SSDF                  | Equipa não tem visibilidade de cobertura              | Validação por dif entre diagrama, requisitos e implementação                  | `addon/05-validacao.md`                      | ✅                                     |

---

## 🧠 Categoria 5 - Incoerência entre arquitetura e risco

| Ameaça                                      | Fonte                             | Como surge                                           | Como a prática mitiga                                                              | Controlos associados                       | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------|----------------------------------------|
| Aplicações L1 tratadas como críticas        | OSC&R / SSDF PW.1                 | Design da arquitetura sem relação com classificação     | Validação da arquitetura proporcional ao risco (ex: app L1 pode partilhar recursos)  | `15-aplicacao-lifecycle.md`         | ❌ Cap. 01                             |
| Sobredimensionamento de segurança da arquitetura | ISO 27005 / OWASP SAMM          | Investimento excessivo em zonas de baixo risco       | Aplicação da matriz de risco e critérios de arquitetura por perfil                  | `addon/02-casos-praticos.md`              | ✅                                     |
| Ambientes de execução não refletidos no design | ENISA DevSecOps / SLSA           | Design não considera pipelines, cloud, containers    | Inclusão de ambientes e zonas operacionais na arquitetura                          | `addon/04-diagramas-referencia.md`        | ❌ Cap. 09, Cap. 07                    |

---

## ✅ Conclusão

O Capítulo 04 mitiga um conjunto de ameaças **essenciais e de difícil visibilidade**, relacionadas com **fronteiras técnicas, validação estrutural e coerência entre intenção e execução**.

> ⚠️ Muitas destas ameaças não emergem em testes - apenas no comportamento agregado de sistemas, escalabilidade, exposição, ou bypass lógico.

> ✅ Pelo menos **10 ameaças são mitigadas exclusivamente** por este capítulo, demonstrando o seu papel único na garantia de segurança por design.

> 📌 Arquitetura segura **não é documentação**: é **decisão, validação e controlo sistemático** do comportamento de software face ao risco.
