---
id: intro
title: Certificação ENISA/CSA (EUCC, EUCS, EU5G) — Nota de Enquadramento
description: Quando usar e como mapear ao SbD-ToE (evidências, decisão e reaproveitamento)
tags: [certificacao, enisa, csa, eucc, eucs, eu5g, procurement]
sidebar_position: 9
---

# Certificação ENISA/CSA: quando usar e como mapear ao SbD‑ToE

> Veja também: [CRA](/sbd-toe/002-cross-check-normativo/cra), [DORA](/sbd-toe/002-cross-check-normativo/dora), [NIS2](/sbd-toe/002-cross-check-normativo/nis2) e a [Nota de Convergência DORA & NIS2](/sbd-toe/002-cross-check-normativo/convergencia-dora-nis2).

## Âmbito

Os esquemas europeus de certificação de cibersegurança, no âmbito do **Cybersecurity Act (CSA)**, visam **reconhecimento UE** de que produtos/serviços cumprem requisitos de segurança. A **ENISA** coordena e suporta a elaboração de esquemas; a certificação é executada por **Organismos de Avaliação da Conformidade (CABs)** acreditados e supervisionada por **autoridades nacionais**.

Esta nota explica “para quem se destina”, quando é útil/necessária e como **reaproveitar controlos e evidências do SbD‑ToE**.

## Para quem se destina

- **Fabricantes de produtos TIC** → esquema **EUCC** (para ICT products; base Common Criteria). Níveis: Basic, Substantial, High.
- **Prestadores de serviços Cloud** → esquema **EUCS** (para serviços cloud). Níveis: Basic, Substantial, High.
- **Fornecedores/Operadores 5G** → esquema **EU5G** (para redes e componentes 5G). Níveis: alinhados ao risco.
- **CABs/Laboratórios** → aplicam os critérios dos esquemas.
- **Autoridades Nacionais** → supervisionam, reconhecem e listam certificados.
- **Compradores (incl. setor público)** → usam certificados como critério de procurement.

Notas:
- Regra geral, a certificação é **voluntária**, salvo quando legislação setorial, atos de execução, ou **cadernos de encargos** a tornem obrigatória para certos mercados/contratos.
- Certificação **não substitui** o **CRA** (marcação CE e obrigações regulatórias de produtos). Pode, porém, servir como **evidência forte** de práticas de segurança.

## Esquemas em foco

### EUCC — ICT products (base Common Criteria)
Objetivo: evidenciar que um produto TIC cumpre requisitos e foi avaliado segundo uma **Target of Evaluation** e **Security Functional/Assurance Requirements**. 
Nível de garantia impacta a **profundidade de testes** e a **independência**.

### EUCS — Cloud services
Objetivo: evidenciar controlos de segurança e governança de serviços Cloud. Abrange **gestão de risco, IAM, cifragem, operação, continuidade**, etc.

### EU5G — Redes 5G
Objetivo: evidenciar requisitos de segurança para fornecedores/operadores na cadeia 5G (equipamento, software, gestão, supply chain).

## Como se relaciona com DORA/NIS2/CRA

- Partilham a mesma “língua técnica” (cifragem, IAM, gestão de vulnerabilidades, testes, monitorização, continuidade).
- **CRA** impõe requisitos e **marcação CE** para produtos com elementos digitais; a certificação CSA pode **complementar** como evidência (não a substitui).
- **NIS2/DORA** exigem maturidade técnica; a certificação pode **acelerar auditorias** e aceitar **certificados como prova** em procurement/regulação.

## Árvores de decisão (simplificadas)

1) O que é o meu objeto principal?
- Produto TIC (software/firmware/hardware com SW) → considerar **EUCC**
- Serviço Cloud (IaaS/PaaS/SaaS) → considerar **EUCS**
- Fornecedor/Operador 5G → considerar **EU5G**
- Outro → certificação CSA pode não ser aplicável

2) Há exigência externa?
- Regulador/lei/setor exige? → prosseguir com certificação
- Cliente/concursos pedem? → avaliar custo/benefício e nível (Basic/Substantial/High)
- Não há exigência? → manter “readiness” e evidências; decidir estrategicamente

3) Qual o nível?
- Mercado e risco baixo → Basic/Substantial
- Mercados críticos/altamente regulados → Substantial/High

## Mapeamento SbD‑ToE → Certificação (evidência típica)

| Domínio SbD‑ToE | O que demonstra | Relevância CSA |
|-----------------|-----------------|----------------|
| Cap. 02 — Requisitos | Políticas e controlos mínimos por nível | Critérios de segurança documentados |
| Cap. 04 — Arquitetura | Design seguro, IAM, cifragem, gestão de chaves | Controlos funcionais e de desenho |
| Cap. 05 — SBOM/SCA | Inventário de componentes, gestão de CVEs | Vulnerability management e supply chain |
| Cap. 06–07 — SDLC/CI‑CD | Gates, revisão, rastreabilidade, SoD | Secure lifecycle e integridade da build |
| Cap. 08–09 — IaC/Containers | Configurações seguras e runtime | Endurecimento e consistência |
| Cap. 10–11 — Testes/Release | SAST/DAST/fuzzing; gate “no‑critical” | Eficácia de controlos antes do release |
| Cap. 12 — Operações | Monitorização, resposta, continuidade | Resiliência operacional |
| Cap. 13 — Formação | Competências e awareness | Capacidade organizacional |
| Cap. 14 — Governação | RACI, fornecedores, auditoria | Gestão e rastreabilidade |

Sugere-se criar um **dossiê de certificação** com referências cruzadas (control matrix) entre requisitos do esquema (EUCC/EUCS/EU5G) e artefactos SbD‑ToE.

## Checklist de evidências (mínimo viável)

- [ ] Política de segurança (versão, aprovação, âmbito)
- [ ] Arquitetura e modelo de dados (inclui IAM/crypto/segregação)
- [ ] SBOM por release + registos SCA + SLAs de patch
- [ ] Pipelines com gates; logs de build/assinar, SoD (segregation of duties)
- [ ] Registos de testes (SAST/DAST/fuzzing/pen)
- [ ] Relatórios de qualidade de release e “no‑critical known”
- [ ] Monitorização, runbooks, exercícios (incidente/DR)
- [ ] Formação e registos (técnica/gestão)
- [ ] Gestão de fornecedores (contratos, cláusulas, avaliações)
- [ ] Trilho auditado (quem aprovou, quando, porquê)

## Métricas úteis

- % versões com SBOM publicado
- MTTP (tempo médio até patch) por severidade
- % releases bloqueadas por gate de segurança (e depois corrigidas)
- Cobertura de testes (SAST/DAST/fuzzing) por aplicação
- % controlos mapeados ao esquema escolhido

## Próximos passos

1. Confirmar objeto (produto/serviço) e exigência externa (lei/cliente).  
2. Selecionar esquema e nível alvo (Basic/Substantial/High).  
3. Construir matriz de mapeamento requisito→evidência (SbD‑ToE).  
4. Preencher gaps (p. ex., independência de teste, amostragem).  
5. Pré‑auditoria interna; depois selecionar CAB e calendarizar avaliação.  

## Referências

- Regulamento (UE) 2019/881 — Cybersecurity Act (CSA)
- ENISA — Páginas dos esquemas de certificação (EUCC, EUCS, EU5G)
- SbD‑ToE Capítulos 01–14; CRA/NIS2/DORA cross‑checks

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Maio 2026
