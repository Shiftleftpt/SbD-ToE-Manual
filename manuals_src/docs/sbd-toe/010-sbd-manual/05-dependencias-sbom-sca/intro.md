---
id: intro
title: Dependências, SBOM e SCA
description: Princípios, práticas e controlos para garantir gestão segura de dependências, geração de SBOM e análise automatizada de composição de software
tags: [dependencias, sbom, sca, supply-chain, oss, cicd, governance]
sidebar_position: 0
---
import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: AA1.2, AA2.1, CMVM1.1</Badge>
  <Badge color="info">SSDF: PW.4, PW.7</Badge>
  <Badge color="info">SLSA: Nível 2 / 4</Badge>
  <Badge color="info">DSOMM: 3 / 4 (média)</Badge>
  <a href="./achievable-maturity" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver análise de maturidade</a>
</div>

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo SbD-ToE.  
A sua não aplicação **inviabiliza a confiança na cadeia de fornecimento de software**.  
Sem SBOM e governação de dependências, não há rastreabilidade nem segurança real.
:::

# Dependências, SBOM e SCA

O uso de **Open Source Software (OSS)** e bibliotecas de terceiros é comum e recomendado: acelera a entrega e evita reinventar a roda.  
Contudo, sem governação, surgem riscos materiais: componentes abandonados, CVEs conhecidos, pacotes maliciosos e falta de visibilidade da **cadeia de fornecimento**.

Este capítulo estabelece bases operacionais para uma gestão **segura, rastreável e auditável** de dependências, incluindo:
- SBOM atualizado por build,
- SCA integrado no CI/CD com *gates*,
- governação de exceções,
- **proibição de bibliotecas copiadas manualmente para o repositório**, e
- **automação de atualização com avaliação de impacto** (bots que abrem PRs quando a mudança é segura e solicitam intervenção humana quando há impacto no código).

Os requisitos aqui descritos aplicam-se a qualquer stack/língua.  
Focam-se em assegurar que:
- cada dependência é conhecida, aprovada e rastreável,
- cada build produz SBOM completo,
- vulnerabilidades são detetadas e triadas,
- **atualizações são automatizadas com análise de impacto** (semver, *release notes*, *changelogs*, testes e *static call graphs*),  
- nenhuma biblioteca entra “por cópia manual” fora do *package manager*.

Ligação a outros capítulos:
- **Cap. 02 - Requisitos de Segurança** (REQ-DEP-xxx),
- **Cap. 07 - CI/CD Seguro** (pipelines e gates),
- **Cap. 09 - Containers** (imagens como artefactos de supply chain),
- **Cap. 14 - Governança** (exigências a fornecedores).

---

## 🧭 O que cobre tecnicamente

- Gestão segura de dependências (OSS, comerciais, internas).
- Geração e manutenção de **SBOM** (CycloneDX/SPDX).
- Integração de **SCA** automatizado no CI/CD.
- Processo formal de **exceções** e aceitação de risco.
- **Repositórios internos** como fonte única de confiança.
- **Proibição de dependências copiadas localmente** (JS, PHP, DLLs, JARs, etc.).
- **Automação da atualização com avaliação de impacto** (Renovate/Dependabot/afins):
  - PRs automáticos quando o impacto é nulo/baixo (semver *patch*/*minor* compatível, testes verdes),
  - *handoff* para intervenção humana quando há impacto (major/breaking, APIs alteradas).

---

## 🧪 Pilares de governação

1. **Repositórios internos aprovados** como fonte única.  
2. **Política de dependências** com critérios de aprovação e *pinning*.  
3. **SBOM por build**, versionado e acessível.  
4. **SCA automático com gates** por severidade e criticidade (L1–L3).  
5. **Exceções formais** com prazo e mitigação compensatória.  
6. **Auditorias periódicas** para impedir bibliotecas copiadas manualmente.  
7. **Automação de atualização com avaliação de impacto** e integração nos testes/gates.

---

## ⚙️ Como deve ser feito

- Configurar *package managers* para usarem **apenas** repositórios internos.  
- Gerar **SBOM** em cada build (CycloneDX/SPDX); arquivar.  
- Integrar **SCA** com bloqueio automático para CVEs críticos (limiares por Lx).  
- Formalizar **exceções** (ex.: `excecoes.yaml`) e rever periodicamente.  
- Ativar **bots de atualização** com:
  - análise de *semver*, *release notes* e *diffs*,
  - execução de testes e validações (CI),
  - **PRs “auto-merge” condicionados** a *no-impact* comprovado,
  - marcação “requires-human” quando há impacto no código (*breaking*).  
- Remover bibliotecas copiadas manualmente e substituí-las por dependências declaradas.

---

## 📆 Quando aplicar

- **Início**: política e configuração de repositórios internos.  
- **Nova dependência**: revisão de origem/licença/manutenção/CVEs.  
- **Build**: gerar SBOM + executar SCA.  
- **Release**: validar findings e exceções.  
- **Ciclo regular**: atualizar dependências (bots) e rever findings.  
- **CVE crítico**: avaliar impacto e remediar versões afetadas.

---

## 👥 Quem está envolvido

| Papel/Função       | Contributo principal |
|--------------------|----------------------|
| **Developer / Lead** | Incluir dependências, triagem inicial, *pinning*, correções |
| **AppSec**           | Políticas, *tuning*, *gates*, exceções e revisão de risco |
| **DevOps / CI/CD**   | SBOM, SCA, repositórios internos, bots de atualização |
| **QA / Test Engineer** | Evidências, testes de regressão, validação de PRs de bots |
| **Product Owner**    | Decisão *go/no-go* perante findings/risco residual |
| **GRC / Gestão**     | Auditoria, conformidade, retenção de evidências |

---

## 🎯 Para quê

- Reduzir risco de componentes vulneráveis/abandonados.  
- Garantir rastreabilidade e resposta rápida a CVEs.  
- **Acelerar *time‑to‑fix*** com bots que **avaliam impacto**, automatizam PRs seguros e solicitam intervenção humana quando necessário.  
- Evitar riscos ocultos (bibliotecas copiadas manualmente).  
- Cumprir SSDF, SLSA, NIS2 e boas práticas de mercado.

---

## 🧮 Aplicação proporcional L1–L3

| Prática                       | L1 (baixo)                 | L2 (médio)                                 | L3 (alto/crit.)                                  |
|-------------------------------|----------------------------|--------------------------------------------|--------------------------------------------------|
| SBOM                          | Básico por build           | Completo por release                        | Assinado + verificação de integridade            |
| SCA                           | Aviso                      | Bloqueio High/Critical                      | Bloqueio Medium+                                 |
| Pinning                       | Recomendado                | Obrigatório                                 | Obrigatório + proveniência verificada            |
| Exceções                      | Simples                    | Formais + revisão periódica                 | Formais + validação executiva                    |
| Repositório interno           | Recomendado                | Obrigatório                                 | Obrigatório + assinatura/verificação              |
| Bibliotecas copiadas locais   | Proibidas (política)       | Auditoria periódica                         | Enforcement em CI/CD                              |
| **Bots de atualização**       | Opcional                   | Ativos com auto‑PR e *no‑impact merge*      | Ativos + *impact analysis* + *canary* + *gates*  |

---

## 📜 Políticas Organizacionais Relevantes

| Política                          | Obrigatória | Aplicação              | Conteúdo mínimo esperado                                  |
|----------------------------------|-------------|------------------------|-----------------------------------------------------------|
| Política de Dependências         | Sim         | Todos os projetos      | Critérios de aprovação, *pinning*, bloqueio externo       |
| Política de SBOM                 | Sim         | Todos os builds        | CycloneDX/SPDX, versionamento, retenção                   |
| Política de Exceções a CVEs      | Sim         | Projetos críticos      | Justificação, prazo, mitigação compensatória              |
| Política de Bibliotecas Locais   | Sim         | Todos os repositórios  | Proibição de JS/PHP/DLL/JAR locais fora de *package manager* |
| **Política de Atualização Automática** | Sim   | L2–L3                   | Bots ativos, *impact analysis*, critérios de *auto‑merge*, *handoff* humano |

Na versão impressa, consultar o **Anexo de Políticas do Manual**, onde estas políticas estão consolidadas transversalmente.
