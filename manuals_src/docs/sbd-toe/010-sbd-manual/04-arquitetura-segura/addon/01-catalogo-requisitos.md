---
description: Requisitos específicos aplicáveis ao design e revisão de arquiteturas
  seguras
id: catalogo-requisitos
tags:
- arquitetura
- ciclo-vida
- rastreabilidade
- requisitos
- seguranca
- segurança
- threat-modeling
title: Catálogo de Requisitos Técnicos de Arquitetura Segura
---


# 📘 Catálogo de Requisitos Técnicos de Arquitetura Segura

## ❓ Porquê este catálogo está neste capítulo (e não apenas no Cap. 2)

Embora o Capítulo 2 contenha o **catálogo geral de requisitos aplicacionais**, alguns capítulos - como este - cobrem **domínios técnicos especializados**, com **requisitos estruturais ou estratégicos** que:

- **Não se aplicam diretamente a funcionalidades ou código**
- São **avaliados em revisões técnicas, modelos de arquitetura ou critérios de projeto**
- Exigem rastreabilidade própria com base em **zonas de confiança, fluxos de dados ou decisões de design**

Este catálogo fornece os **requisitos específicos de segurança da arquitetura**, que devem ser aplicados proporcionalmente ao risco da aplicação (Cap. 1), e **complementam** o catálogo geral.

---

## 🧱 Requisitos Técnicos por Nível de Risco
| ID          | Requisito                                                                                          | L1 | L2 | L3 |
| ----------- | -------------------------------------------------------------------------------------------------- | -- | -- | -- |
| **ARC-001** | A arquitetura deve identificar e documentar zonas de confiança e fronteiras de segurança           | X  | X  | X  |
| **ARC-002** | A exposição externa de componentes deve ser minimizada e justificada                               | X  | X  | X  |
| **ARC-003** | Deve existir uma revisão de arquitetura com foco em segurança, proporcional ao risco da aplicação  |    | X  | X  |
| **ARC-004** | As decisões de arquitetura devem ser documentadas com responsáveis, datas e justificações          |    | X  | X  |
| **ARC-005** | A arquitetura deve considerar threat modeling nos fluxos e nos componentes críticos                |    | X  | X  |
| **ARC-006** | A arquitetura deve integrar controlos técnicos para isolar domínios sensíveis                      | X  | X  | X  |
| **ARC-007** | Devem existir padrões de arquitetura segura reutilizáveis, aprovados por segurança                 |    | X  | X  |
| **ARC-008** | Devem ser identificados e protegidos os fluxos de dados entre zonas de confiança                   | X  | X  | X  |
| **ARC-009** | Alterações significativas na arquitetura devem desencadear nova revisão de segurança               |    | X  | X  |
| **ARC-010** | Diagrama(s) de arquitetura devem ser versionados, revistos periodicamente e acessíveis às equipas  | X  | X  | X  |
| **ARC-011** | A arquitetura de aplicações críticas deve implementar segmentação lógica e física entre ambientes  |    |    | X  |
| **ARC-012** | Devem ser definidos critérios formais de aprovação da arquitetura para aplicações de risco elevado |    |    | X  |
| **ARC-013** | Devem existir mecanismos de validação automática da topologia em CI/CD ou repositórios como código |    |    | X  |


---

## 🧩 Notas explicativas

- **ARC-003**: A revisão pode ser feita com checklist, peer review ou workshop técnico.
- **ARC-005**: O threat modeling aqui é usado como **complemento à arquitetura**, não substituto.
- **ARC-011**: Refere-se a isolamento de ambientes (dev, staging, prod) tanto em rede como em permissões.
- **ARC-013**: Exemplo de ferramenta: validação de diagramas `.drawio` como código, Cartography, ReGraph.

---

## 🎯 Aplicação prática

- Estes requisitos devem ser integrados em **modelos de arquitetura de referência**, **revisões técnicas**, ou critérios de aceitação
- Devem estar ligados à **classificação de risco da aplicação (Cap. 1)**
- Servem como base para auditorias técnicas, conformidade, e validação de segurança em SDLC

---

## 🧾 Exemplos de evidência

| Requisito   | Tipo de evidência sugerida                              |
|-------------|----------------------------------------------------------|
| ARC-001     | Diagrama com zonas de confiança e legendas              |
| ARC-003     | Ata da revisão, checklist preenchido, decisões arquivadas|
| ARC-007     | Repositório de padrões com versionamento                 |
| ARC-013     | Job de CI com output de validação de topologia           |

---

> 🔗 Estes requisitos devem ser lidos em conjunto com:
> - [Capítulo 1 - Classificação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
<!-- > - [Capítulo 2 - Requisitos de Segurança Globais](/sbd-toe/sbd-manual/requisitos-seguranca/intro) -->
> - [Capítulo 3 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
