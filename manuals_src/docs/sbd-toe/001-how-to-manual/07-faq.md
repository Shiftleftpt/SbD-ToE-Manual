---
id: faq
title: FAQ — Perguntas Frequentes
description: Respostas rápidas sobre aplicabilidade, âmbito, compliance e implementação do SbD-ToE
tags: [faq, aplicabilidade, compliance, implementacao]
sidebar_position: 7
---

# FAQ — Perguntas Frequentes

## Âmbito e Aplicabilidade

### Para quem é o SbD-ToE?

Organizações que:
- **Desenvolvem** software (produto próprio, ferramentas internas, apps para clientes).
- **Contratem** desenvolvimento (outsourcing, contractors, system integrators).
- **Adquirem** SaaS/PaaS/IaaS crítico e precisam validar segurança do fornecedor.
- **Operam** infraestrutura TIC crítica (on-prem, cloud, hybrid).
- Estão sujeitas a **regulação** (NIS2, DORA, CRA, GDPR) e precisam de evidências técnicas de conformidade.

O SbD-ToE **não** é apenas para empresas de software. É para qualquer organização com **sistemas TIC críticos**.

---

### A minha organização não desenvolve software. O SbD-ToE é relevante?

**Sim, muito provavelmente.**

Mesmo sem desenvolvimento interno, a maioria das organizações:
- **Adquire ou contrata** software (ERP, CRM, core systems, SaaS).
- **Opera** infraestrutura (servidores, cloud, rede).
- **Gere dados sensíveis** (clientes, colaboradores, financeiros).

O SbD-ToE ajuda a:
- **Classificar** aplicações por criticidade (Cap. 01).
- **Definir requisitos** de segurança para fornecedores (Cap. 02, 14).
- **Validar segurança** de software adquirido (Cap. 10: pentests, auditorias).
- **Gerir fornecedores** conforme DORA/NIS2 (Cap. 05, 14: SBOM, contratos, SLAs).
- **Operar com resiliência** (Cap. 12: logs, backups, incidentes, monitorização).

**Exemplo:** Banco que usa SAP/Oracle (não desenvolve) ainda precisa de:
- Classificar o ERP como L3 (crítico).
- Exigir SBOM e SLAs de patch ao fornecedor.
- Integrar logs no SIEM corporativo.
- Fazer pentests anuais.
- Documentar tudo para auditoria DORA.

→ **Capítulos aplicáveis:** 01, 02, 05, 10, 12, 14.

---

### Qual a diferença entre SbD-ToE e ISO 27001?

| Aspeto | SbD-ToE | ISO 27001 |
|--------|---------|-----------|
| **Foco** | Segurança **aplicacional** e pipeline (desenvolvimento, aquisição, operação de software) | Gestão de segurança da informação (ISMS) **organizacional** |
| **Nível** | Técnico-operacional detalhado | Alto nível, abstrato (controlos genéricos) |
| **Estrutura** | 14 capítulos por domínio técnico (SBOM, CI/CD, IaC, threat modeling, testes) | 114 controlos distribuídos por 14 domínios (A.5–A.18) |
| **Certificável?** | Não (é framework interno) | Sim (certificação por CAB acreditado) |
| **Relação** | **Implementa** controlos ISO 27001 com detalhe técnico (A.8, A.12, A.14, A.16) | **Exige** controlos; deixa "como" em aberto |

**Em termos práticos:**
- ISO 27001 diz: "Deve gerir vulnerabilidades" (controlo A.12.6).
- SbD-ToE diz: "Cap. 05 — Como fazer SBOM, SCA, patching com SLAs, exceções formais, integração CI/CD".

**Podem coexistir?** Sim, e devem. SbD-ToE fornece o "como técnico" que acelera implementação e auditoria ISO 27001.

---

## Compliance e Regulação

### O SbD-ToE cobre DORA/NIS2/CRA/GDPR?

**Sim, mas de forma diferente:**

| Regulamento | Cobertura SbD-ToE | Lacunas intencionais | Cross-check |
|-------------|-------------------|---------------------|-------------|
| **DORA** | 80–90% dos requisitos técnicos (Art. 5/18/19–20/26–28) | Templates ITS, aprovação board formal, concentração de fornecedores | [02-dora.md](/sbd-toe/002-cross-check-normativo/dora) |
| **NIS2** | 80–90% dos requisitos técnicos (Art. 20/21/23) | Registo autoridade nacional, templates de reporte | [NIS2.md](/sbd-toe/002-cross-check-normativo/nis2) |
| **CRA** | 70–80% (SBOM, patching, disclosure, testes) | Marcação CE, declaração de conformidade, organismos notificados | [05-cra.md](/sbd-toe/002-cross-check-normativo/cra) |
| **GDPR** | 60–70% (Art. 25/32: PbD, segurança do tratamento) | ROPA, base legal, DPIA completa, transferências internacionais | [07-gdpr.md](/sbd-toe/002-cross-check-normativo/gdpr) |

**Princípio:** O SbD-ToE fornece o **núcleo técnico** reutilizável. As partes jurídico-administrativas (contratos, bases legais, declarações formais) são tratadas por Jurídico/GRC.

---

### Posso usar o SbD-ToE como evidência de compliance?

**Sim.** Cada capítulo gera artefactos reutilizáveis:

- **Matriz de classificação L1–L3** → evidência para DORA Art. 5, NIS2 Art. 21, GDPR Art. 5/32.
- **SBOM por release** → evidência para DORA Art. 5, NIS2 Art. 21, CRA (obrigatório).
- **Relatórios SAST/DAST/pentest** → evidência para DORA Art. 19–20, NIS2 Art. 21, CRA, ISO 27001 A.14.2.
- **Runbook incidentes 72h** → evidência para DORA Art. 18, NIS2 Art. 23, GDPR Art. 33/34.
- **Contratos fornecedores** → evidência para DORA Art. 26–28, NIS2 Art. 21, GDPR Art. 28.

**Um único conjunto de evidências serve para múltiplos reguladores e auditorias.**

---

### E certificação? Há certificação SbD-ToE?

**Não.** O SbD-ToE não é um esquema de certificação. É um **framework operacional interno**.

**Mas:** as evidências SbD-ToE podem ser reutilizadas para certificações externas:
- **ISO 27001** (ISMS)
- **EUCC/EUCS/EU5G** (esquemas CSA da ENISA)
- **SOC 2 Type II** (para cloud/SaaS)

Ver: [Certificação ENISA/CSA](/sbd-toe/002-cross-check-normativo/enisa-csa-certificacao)

---

## Implementação

### Quanto tempo demora implementar o SbD-ToE?

Depende da maturidade inicial:

| Cenário | Duração estimada | Fases prioritárias |
|---------|------------------|-------------------|
| **Greenfield** (nova organização/produto) | 3–6 meses | Cap. 01–02 (classificação/requisitos) → 06–07 (SDLC/CI-CD) → 12 (ops) |
| **Brownfield com maturidade baixa** | 6–12 meses | Cap. 01 (inventário) → 05 (SBOM/SCA) → 10 (testes) → 12 (incidentes) → 14 (governação) |
| **Brownfield com maturidade média** (já tem CI/CD, logs, etc.) | 4–8 meses | Gap analysis → Cap. 03 (TM) → 05 (SBOM) → 10 (testes avançados) → 14 (fornecedores) |
| **Compliance-driven** (DORA/NIS2 deadline) | 6–18 meses | Usar playbooks específicos ([DORA](/sbd-toe/002-cross-check-normativo/sbd-toe-4-dora-playbook), [NIS2](/sbd-toe/002-cross-check-normativo/sbd-toe-4-nis2-playbook)) |

**Nota:** A implementação é **iterativa** (não "big bang"). Começa-se por apps críticas (L3) e expande-se progressivamente.

---

### Preciso implementar todos os capítulos?

**Não necessariamente.** Depende do contexto:

**Obrigatórios para todos:**
- Cap. 01 (Classificação)
- Cap. 02 (Requisitos mínimos)
- Cap. 12 (Monitorização e operações)
- Cap. 14 (Governação)

**Condicionais:**
- **Desenvolves software?** → Cap. 06–07 (SDLC/CI-CD), Cap. 10 (testes).
- **Usas containers?** → Cap. 09.
- **Usas IaC?** → Cap. 08.
- **Apps L3 (críticas)?** → Cap. 03 (Threat Modeling), Cap. 04 (Arquitetura).
- **DORA/CRA?** → Cap. 05 (SBOM obrigatório).

**Princípio:** Implementa o que é **relevante e proporcional** ao risco.

---

### Quanto custa implementar o SbD-ToE?

Não há custo de licença (é framework aberto). Os custos são **internos** (tempo de equipa) e **ferramentas**:

| Item | Estimativa |
|------|-----------|
| Tempo de equipa (análise, políticas, setup) | 200–500 horas (1–3 FTEs × 3–6 meses) |
| Ferramentas (SAST/DAST/SCA) | 5k–50k€/ano (depende de escala; há opções open-source) |
| SIEM/logging | 10k–100k€/ano (ou cloud-native incluído) |
| Formação (equipa técnica + gestão) | 5k–20k€ |
| Auditoria/validação externa (opcional) | 10k–50k€ |

**ROI:** Redução de incidentes, aceleração de compliance, reutilização de evidências, menor custo de auditoria.

---

## Exceções e Desvios

### O que são "exceções" no SbD-ToE?

**Exceção** = desvio formal de um requisito de segurança, com:
- Justificação técnica ou de negócio.
- Aprovação por autoridade designada (AppSec/CISO/Board, conforme criticidade).
- Período de validade (TTL).
- Plano de remediação ou compensação.
- Trilho auditado.

**Exemplo:** "Deploy de app L3 com CVE High conhecido, mas com WAF compensatório, aprovado por CISO, TTL 30 dias, patch agendado."

Ver: Cap. 02 addon 08, Cap. 05 addon 09, Cap. 14.

---

### Todas as exceções são permitidas?

**Não.** Há categorias de **exceções inaceitáveis**:

- Vulnerabilidades RCE críticas sem compensação.
- Ausência de MFA em apps L3.
- Dados sensíveis não cifrados.
- Violações de conformidade regulatória (ex: DORA/NIS2/GDPR).

**Regra:** Se o regulador ou a criticidade não o permite, não é exceção — é **não-conformidade**.

Ver: [DORA cross-check — Exceções](/sbd-toe/002-cross-check-normativo/dora#gestão-de-exceções-e-desvios-artigos-5-18-19–20-26–28-dora)

---

## Relação com Outros Frameworks

### SbD-ToE vs. OWASP SAMM/BSIMM/SSDF?

| Framework | Tipo | Relação com SbD-ToE |
|-----------|------|---------------------|
| **OWASP SAMM** | Modelo de maturidade (self-assessment) | SbD-ToE **implementa** práticas SAMM com detalhe operacional |
| **BSIMM** | Observação descritiva (o que outros fazem) | SbD-ToE usa insights BSIMM como inspiração; vai além com prescrição |
| **NIST SSDF** | Práticas de desenvolvimento seguro (alto nível) | SbD-ToE mapeia e **detalha** cada prática SSDF |

**Convergência:** Todos falam de threat modeling, SAST/DAST, SBOM, testes. SbD-ToE **operacionaliza** com addons, templates, checklists.

---

### Posso usar SbD-ToE com DevSecOps?

**Sim, é o core do SbD-ToE.**

- Cap. 06–07: Integração de segurança em pipelines (shift-left).
- Cap. 10: Testes contínuos (SAST/DAST/fuzzing).
- Cap. 08–09: IaC e containers (infrastructure-as-code segura).
- Cap. 12: Observabilidade e resposta rápida.

**Princípio:** Segurança automatizada, não manual.

---

## Regulação Multi-Jurisdicional

### Estou sujeito a DORA + NIS2 + GDPR. Há duplicação?

**Muito pouca.** A maioria dos controlos técnicos convergem:

- **Gestão de vulnerabilidades** → DORA Art. 5, NIS2 Art. 21, CRA (SBOM/patching).
- **Incidentes** → DORA Art. 18 (24h), NIS2 Art. 23 (24h/72h/1M), GDPR Art. 33 (72h).
- **Fornecedores** → DORA Art. 26–28, NIS2 Art. 21, GDPR Art. 28.
- **Testes** → DORA Art. 19–20, NIS2 Art. 21.

**Estratégia:**
1. Implementa SbD-ToE Cap. 01–14 (núcleo técnico comum).
2. Usa playbooks específicos para ajustes (campos de reporte, templates).
3. Runbook de incidentes único com bifurcação de canais (DORA → EBA, NIS2 → CSIRT, GDPR → DPO).

Ver: [Convergência DORA & NIS2](/sbd-toe/002-cross-check-normativo/convergencia-dora-nis2)

---

## Métricas e Melhoria Contínua

### Como medir se estou "SbD-ToE compliant"?

Métricas-chave por capítulo:

| Capítulo | Métrica |
|----------|---------|
| **Cap. 01** | % apps classificadas (L1–L3) |
| **Cap. 02** | % apps com requisitos mínimos implementados |
| **Cap. 05** | % releases com SBOM; MTTP (tempo médio até patch) |
| **Cap. 07** | % commits com gates de segurança passados |
| **Cap. 10** | Cobertura SAST/DAST; % releases bloqueadas por CVE crítico |
| **Cap. 12** | MTTD/MTTR (tempo até deteção/resposta); % backups testados |
| **Cap. 14** | % fornecedores com contratos auditados; % exceções no prazo |

**Dashboard único** com KPIs agregados: "SbD-ToE Compliance Score".

---

### O SbD-ToE é "one-time" ou contínuo?

**Contínuo.**

- Novas apps → classificar (Cap. 01).
- Novos CVEs → patch/excepção (Cap. 05).
- Mudanças arquiteturais → re-TM (Cap. 03).
- Novos fornecedores → onboarding (Cap. 14).
- Exercícios trimestrais → incidentes/DR (Cap. 12).

**Revisão formal:** Anual (políticas, exceções, gaps).

---

## Próximos Passos

### Por onde começo?

1. **Ler:** [Como usar este manual](/sbd-toe/001-how-to-manual/como-usar-este-manual)
2. **Inventariar:** Cap. 01 — Listar e classificar apps críticas.
3. **Gap analysis:** Comparar estado atual vs. requisitos Cap. 02.
4. **Quick wins:** Cap. 05 (SBOM), Cap. 12 (logs centralizados), Cap. 14 (RACI).
5. **Roadmap:** Escolher playbook relevante ([DORA](/sbd-toe/002-cross-check-normativo/sbd-toe-4-dora-playbook), [NIS2](/sbd-toe/002-cross-check-normativo/sbd-toe-4-nis2-playbook), [CRA](/sbd-toe/002-cross-check-normativo/sbd-toe-4-cra-playbook), [GDPR](/sbd-toe/002-cross-check-normativo/sbd-toe-4-gdpr-playbook)).

---

### Onde obter suporte?

- **Documentação completa:** SbD-ToE Capítulos 01–14
- **Cross-checks normativos:** Secção 002
- **Playbooks práticos:** Ver cada regulamento
- **Comunidade:** (a definir — fórum, GitHub Discussions, etc.)

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Maio 2026
