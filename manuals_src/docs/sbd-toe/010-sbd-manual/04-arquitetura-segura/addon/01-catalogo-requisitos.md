---
id: 01-catalogo-requisitos-aplicacionais
title: Catálogo de Requisitos Técnicos de Arquitetura Segura
description: Requisitos específicos aplicáveis ao design e revisão de arquiteturas seguras
tags: [requisitos, arquitetura, segurança, rastreabilidade, threat-modeling]
---

import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  <Badge color="info">Baseado em: OWASP SAMM, BSIMM, SSDF</Badge>
  <Badge color="info">Referências cruzadas: Threat Modeling, Governança</Badge>
  <a href="./20-checklist-revisao.md" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver checklist prático</a>
</div>

# 📘 Catálogo de Requisitos Técnicos de Arquitetura Segura

## ❓ Porquê este catálogo está neste capítulo (e não apenas no Cap. 2)

Embora o Capítulo 2 contenha o **catálogo geral de requisitos aplicacionais**, alguns capítulos — como este — cobrem **domínios técnicos especializados**, com **requisitos estruturais ou estratégicos** que:

- **Não se aplicam diretamente a funcionalidades ou código**
- São **avaliados em revisões técnicas, modelos de arquitetura ou critérios de projeto**
- Exigem rastreabilidade própria com base em **zonas de confiança, fluxos de dados ou decisões de design**

Este catálogo fornece os **requisitos específicos de segurança arquitetural**, que devem ser aplicados proporcionalmente ao risco da aplicação (Cap. 1), e **complementam** o catálogo geral.

---

## 🧱 Requisitos Técnicos por Nível de Risco

| ID | Requisito | L1 | L2 | L3 | SAMM v2.1 | NIST SSDF | BSIMM13 | SLSA v1.0 | CIS v8 | STRIDE | ATT&CK |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARC-001 | A arquitetura deve identificar e documentar zonas de confiança e fronteiras de segurança | X | X | X | D1.2 | PW.4.1 | AA2.1 | L1 | 4.6 | Spoofing, Tampering | T1071.001, T1040 |
| ARC-002 | A exposição externa de componentes deve ser minimizada e justificada | X | X | X | D1.1 | PW.4.2 | AA2.3 | L2 | 13.3 | Information Disclosure, Elevation of Privilege | T1069, T1210 |
| ARC-003 | Deve existir uma revisão de arquitetura com foco em segurança, proporcional ao risco da aplicação |  | X | X | D2.2 | PW.4.1, PW.5.2 | AA2.1 | — | 16.4 | Tampering, Repudiation | T1595, T1565.001 |
| ARC-004 | As decisões arquiteturais devem ser documentadas com responsáveis, datas e justificações |  | X | X | D2.1 | PO.1.3 | AA3.2 | — | 17.2 | Tampering | T1552 |
| ARC-005 | A arquitetura deve considerar threat modeling nos fluxos e nos componentes críticos |  | X | X | D2.2 | PW.4.2 | AA2.2 | — | — | Tampering | T1552 |
| ARC-006 | A arquitetura deve integrar controlos técnicos para isolar domínios sensíveis | X | X | X | D1.2 | PW.5.3 | AA2.3 | L2 | 4.8 | Tampering | T1552 |
| ARC-007 | Devem existir padrões de arquitetura segura reutilizáveis, aprovados por segurança |  | X | X | D1.1 | PW.4.1 | AA1.4 | — | 4.4 | Tampering | T1552 |
| ARC-008 | Devem ser identificados e protegidos os fluxos de dados entre zonas de confiança | X | X | X | D1.2 | PW.4.2 | AA1.3 | — | 3.4 | Tampering | T1552 |
| ARC-009 | Alterações significativas na arquitetura devem desencadear nova revisão de segurança |  | X | X | D2.2 | PW.5.2 | AA2.4 | — | 16.3 | Tampering, Repudiation | T1595, T1565.001 |
| ARC-010 | Diagrama(s) arquiteturais devem ser versionados, revistos periodicamente e acessíveis às equipas | X | X | X | D1.1 | PO.1.2 | AA1.4 | — | 17.1 | Tampering | T1552 |
| ARC-011 | A arquitetura de aplicações críticas deve implementar segmentação lógica e física entre ambientes |  |  | X | D2.2 | PW.5.1 | AA3.3 | L3 | 13.4 | Elevation of Privilege | T1552 |
| ARC-012 | Devem ser definidos critérios formais de aprovação arquitetural para aplicações de risco elevado |  |  | X | D2.3 | PW.4.1, GV.2.1 | AA3.2 | — | 17.3 | Tampering | T1552 |
| ARC-013 | Devem existir mecanismos de validação automática da topologia em CI/CD ou repositórios como código |  |  | X | D2.4 | PW.5.2 | AA3.4 | L3 | 4.9 | Tampering, Repudiation | T1595, T1565.001 |

---

## 🧩 Notas explicativas

- **ARC-003**: A revisão pode ser feita com checklist, peer review ou workshop técnico.
- **ARC-005**: O threat modeling aqui é usado como **complemento à arquitetura**, não substituto.
- **ARC-011**: Refere-se a isolamento de ambientes (dev, staging, prod) tanto em rede como em permissões.
- **ARC-013**: Exemplo de ferramenta: validação de diagramas `.drawio` como código, Cartography, ReGraph.

---

## 🎯 Aplicação prática

- Estes requisitos devem ser integrados em **modelos arquiteturais de referência**, **revisões técnicas**, ou critérios de aceitação
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
> - [Capítulo 1 – Classificação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
<!-- > - [Capítulo 2 – Requisitos de Segurança Globais](/sbd-toe/sbd-manual/requisitos-seguranca/intro) -->
> - [Capítulo 3 – Threat Modeling](/sbd-toe/threat-modeling/intro)
