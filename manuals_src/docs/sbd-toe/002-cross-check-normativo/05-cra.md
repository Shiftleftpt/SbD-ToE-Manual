---
id: cra
title: CRA - Cross-Check Normativo
description: Análise de como o SbD-ToE cobre requisitos técnicos do Cyber Resilience Act (Produtos com Elementos Digitais)
tags: [cross-check, cra, regulamentacao, produtos-digitais, sbom, vulnerabilidades]
sidebar_position: 5
---

# CRA: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 CRA](/sbd-toe/002-cross-check-normativo/sbd-toe-4-cra-playbook).
> 
> Para padrões aplicacionais universais, ver capítulos base do SbD-ToE (01–14).

## Âmbito

O **Cyber Resilience Act (CRA)** estabelece requisitos **horizontais de segurança para produtos com elementos digitais** (hardware, software, componentes integrados) colocados no mercado da UE. Foca: ciclo de vida seguro, gestão de vulnerabilidades, transparência (SBOM/declarações), correções rápidas, reporte de vulnerabilidades exploradas.

O SbD-ToE foi desenhado para aplicações e pipelines software; grande parte dos controlos técnicos e processuais **alinha com o núcleo de obrigações CRA**. Este documento identifica cobertura, lacunas intencionais e ações de adaptação.

## Aviso Regulatório

O CRA introduz obrigações de: classificação crítica, marcação CE, declaração de conformidade, avaliação de conformidade (inclui módulos com envolvimento de organismos notificados em certas categorias), obrigações pós-comercialização (vulnerability handling), e comunicação rápida a ENISA (ou ponto único) de vulnerabilidades ativamente exploradas.

O SbD-ToE cobre o "como" técnico, mas **não substitui**:
- Procedimentos formais de avaliação de conformidade (módulos A, B, C, D, etc.)
- Interações com organismos notificados
- Emissão da declaração UE de conformidade / marcação CE
- Processo jurídico de responsabilidade do fabricante/importador/distribuidor

## PARTE I: Obrigações CRA vs. SbD-ToE

| Domínio CRA | Referência Regulamentar (Resumo) | Cobertura SbD-ToE | Lacuna Intencional | Ação de Adaptação |
|-------------|----------------------------------|-------------------|--------------------|-------------------|
| Gestão do Ciclo de Vida Seguro | Requisitos de segurança aplicável durante todo o ciclo (design → desenvolvimento → distribuição → manutenção) | Cap. 02 (requisitos), Cap. 06 (desenvolvimento), Cap. 07 (CI/CD), Cap. 11 (pré-deploy) | Não distingue papéis fabricante/importador/distribuidor | Mapear roles SbD-ToE → papéis CRA em política interna |
| Identificação e Gestão de Vulnerabilidades | Processos para receber, avaliar, priorizar e corrigir vulnerabilidades | Cap. 05 (SBOM/SCA), Cap. 10 (testes), Cap. 12 (monitorização), Addons exceções | Mecanismo formal de receção externa (coordinated disclosure portal) | Implementar canal público + política ADVD (coordinated disclosure) |
| SBOM / Transparência | Disponibilização de informação de componentes e dependências críticas | Cap. 05 (SBOM contínuo) | Formato exato de disponibilização externa (ex: CycloneDX export público) | Criar rotina de export SBOM sanitizada para stakeholders |
| Correções e Patches Rápidos | Aplicar correções de segurança sem demora injustificada | Cap. 05 (gestão CVE), Cap. 07 (automação CI/CD), Cap. 12 (deteção de exploração) | Critérios de severidade CRA (prazos regulamentares) | Definir SLA de patch CRA: Crítico ≤15d, Alto ≤30d, Médio ≤90d |
| Reporte de Vulnerabilidades Exploited | Notificar autoridade (ex: ENISA/ponto único) sobre vulnerabilidades exploradas ativamente | Cap. 12 (deteção, métricas exploração) | Template de notificação e trigger formal | Adicionar runbook: "Vuln Explorada" + export JSON com campos mínimos |
| Medidas para Prevenção de Vulnerabilidades | Controlo de qualidade e testes de segurança antes de release | Cap. 10 (SAST/DAST/fuzzing), Cap. 11 (gate de release) | Critérios formais de rejeição/liberação por criticidade | Adicionar matriz: nível criticidade → bloqueio automático release |
| Documentação de Segurança | Instruções e info de segurança para utilizadores/admins | Cap. 02 (requisitos), Cap. 04 (arquitetura) | Manual não gera "security usage guide" para produto | Criar artifact "Guia de Segurança do Produto" a partir de Cap. 04/06 |
| Monitorização Pós-Comercialização | Observação contínua de exploração e falhas | Cap. 12 (monitorização, alertas) | Integração com canal de feedback utilizador | Criar backlog específico "Feedback Segurança" + triagem semanal |
| Gestão de Exceções | Justificação de desvios temporários | Cap. 02 addon 08, Cap. 05 addon 09, Cap. 14 governance | Não mapeia limites CRA de aceitabilidade | Introduzir lista de vulnerabilidades "não-exceptuáveis" (ex: RCE crítico) |
| Segurança na Cadeia | Componentes de terceiros seguros, verificação de integridade | Cap. 05 (SCA), Cap. 07 (pipeline), Cap. 09 (runtime containers) | Processo de verificação de firmware/hardware | Adicionar checklist supply chain físico (hash, secure boot se aplicável) |
| Conformidade e CE Mark | Declaração e marcação de conformidade | (Não coberto) | Avaliação técnica/legal formal | Estabelecer processo paralelo GRC + jurídico |

## PARTE II: Cobertura Detalhada

### 1. Ciclo de Vida Seguro
O SbD-ToE define gates de segurança desde a classificação até ao deploy. Isto suporta a obrigação CRA de garantir segurança "by design" e durante a manutenção.

**Ação:** Consolidar num documento único: "Matriz de Controle CRA" listando controlos por fase (design, build, test, release, manutenção).

### 2. Vulnerability Handling & Coordinated Disclosure
SbD-ToE já prevê triagem interna (SCA, scans, testes). CRA exige também canal externo para investigadores ou utilizadores reportarem falhas.

**Ação:** Criar página pública com política de disclosure (escopo, chave PGP, tempo de resposta, não iniciar ação legal de boa fé).

### 3. SBOM e Transparência
SBOM contínuo (Cap. 05) é base para fornecer visibilidade. CRA poderá exigir formato padronizado (CycloneDX/SPDX).

**Ação:** Gerar export sanitized (sem caminhos internos sensíveis) e manter versão por release maior.

### 4. Patching Rápido
Definir SLA CRA diferenciado por severidade e criticidade do produto. Integrar no pipeline: se CVE crítico → tarefa automática + alerta CISO.

**Ação:** Automação: Workflow CI que abre issue + etiqueta "CRA-Patch".

### 5. Reporte de Vulnerabilidade Explorada
Quando exploração confirmada (telemetria, IOC, prova), gerar relatório mínimo: ID vulnerabilidade, componente, versão afetada, impacto, mitigação temporária, prazo patch.

**Ação:** Script de extração (ex: export do SIEM + SBOM) → JSON pronto.

### 6. Qualidade e Testes de Segurança
SbD-ToE cobre variedade de testes. Alinhar com exigência CRA de evitar lançamento com vulnerabilidades conhecidas críticas.

**Ação:** Gate "no-critical-known" antes de release; exceções só com aprovação board (criticidade máxima).

### 7. Documentação de Segurança do Produto
Gerar guia para administradores/utilizadores: configurações seguras, atualização, contacto de segurança, políticas de logging.

**Ação:** Template derivado de Cap. 04 (arquitetura) + Cap. 11 (deploy seguro).

### 8. Monitorização Pós-Comercialização
Cap. 12 já define monitorização; adicionar painéis específicos: "Vulnerabilidades conhecidas vs. status patch".

**Ação:** Dashboard com: total vulns abertas, tempo médio patch, percentagem SLA atendido.

### 9. Exceções
Política de exceções adaptada: vulnerabilidades RCE críticas nunca podem ser exceção; outras só com compensação robusta e TTL curto.

**Ação:** Adicionar tabela "Exceções Inaceitáveis CRA" ao policy central.

### 10. Cadeia de Fornecimento
Expandir além de software: firmware, módulos criptográficos, dispositivos integrados.

**Ação:** Checklist físico: origem componente, hash firmware, canal de atualização seguro.

### 11. Conformidade e Marcação CE
Fora do escopo técnico do SbD-ToE. Requer processo documental legal.

**Ação:** Criar swimlane separado GRC/Jurídico; manter referência dos controlos técnicos como evidência de segurança.

## Lacunas Intencionais

| Área | Motivo da Lacuna | Risco se Ignorado | Mitigação Proposta |
|------|------------------|-------------------|--------------------|
| Declaração UE Conformidade | Requer abordagem jurídica | Falha de mercado / penalizações | Integrar equipa legal cedo |
| Organismo Notificado | Processo regulado fora do manual | Atraso certificação | Definir critério de quando envolver |
| Formato Oficial SBOM Externo | Evolução de padrões | Incompatibilidade com requisitos comprador | Implementar export plugin CycloneDX |
| Canal Disclosure Externo | Universalidade do manual | Perda de reporte responsável | Publicar política em site /SECURITY.md |
| Firmware/Hardware Secure Boot | Foco software aplicacional | Vetor físico ignorado | Adicionar checklist supply chain físico |

## Métrica Simples CRA (Autoavaliação)

Responda SIM aos seguintes pontos:
1. Existe política de segurança do produto cobrindo design→manutenção? ✓
2. Há SBOM completo gerado por release? ✓
3. Existe canal público de vulnerability disclosure? ✓
4. SLA de patch documentado e monitorizado? ✓
5. Gate que bloqueia release com CVE crítico conhecido? ✓
6. Dashboard de vulnerabilidades pós-comercialização ativo? ✓
7. Export SBOM externa sanitizada disponível para clientes/reguladores? ✓
8. Política de exceções define vulnerabilidades inaceitáveis? ✓
9. Guia de Segurança do Produto publicado? ✓
10. Processo de reporte de exploração ativa documentado? ✓

≥8/10 → Boa maturidade CRA técnica. `<`6 → Priorizar SBOM, patching, disclosure, gating crítico.

## Ações Prioritárias (Roadmap Inicial)

1. Formalizar política ciclo de vida seguro (integrar CRA requisitos) 
2. Implementar canal disclosure externo (security.txt + página) 
3. Ajustar pipeline com gate "no critical known" 
4. Definir SLA patch CRA e métricas de acompanhamento 
5. Gerar SBOM e export CycloneDX por release 
6. Criar guia de segurança do produto 
7. Criar runbook de reporte exploração ativa 
8. Adicionar dashboard pós-comercialização 
9. Checklist supply chain físico (se aplicável) 
10. Swimlane CE Conformidade (jurídico + GRC)

## Referências

- Texto final do Cyber Resilience Act (Regulamento (UE) 2024/XXX) 
- SbD-ToE Manual Capítulos 01–14 
- ENISA Guidance on Product Security & Vulnerability Disclosure 
- ISO/IEC 29147 (Vulnerability Disclosure), ISO/IEC 30111 (Vulnerability Handling)
- CycloneDX / SPDX especificações

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Maio 2026
