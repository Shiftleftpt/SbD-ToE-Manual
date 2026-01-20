---
id: ia-nos-testes
title: IA no Processo de Testes de Segurança
description: Como usar IA/GenAI para acelerar testes de segurança (planeamento, triagem, regressões, fuzzing e validação) sem degradar evidência, confidencialidade ou controlo humano
tags: [genai, ia, testes, seguranca, triagem, regressao, fuzzing, evidencias, governanca]
---

# 🤖 IA no Processo de Testes de Segurança (GenAI)

A adoção pervasiva de IA/GenAI no SSDLC altera profundamente **como produzimos e interpretamos evidência**.  
No domínio de testes de segurança isto é especialmente crítico, porque:

- o output dos scanners já era “ruidoso” (FP/FN), e a IA pode amplificar esse ruído se for usada como oráculo;
- os testes dependem de **contexto** (arquitetura, fluxos autenticados, dados sensíveis, compensating controls);
- a segurança exige **decisão humana rastreável**, e não “decisão automatizada” sem cadeia de responsabilidade.

Este addon prescreve como usar IA para acelerar e aumentar cobertura **sem substituir validação empírica** nem comprometer confidencialidade.

---

## 1) Princípios canónicos

### P1 — IA é “assistente”, não “decisor”
A IA pode propor: triagens, hipóteses, priorização, caminhos de reprodução, patch candidates, testes.  
A decisão final (corrigir/aceitar/suprimir/defer) é sempre humana e rastreável — ver **US-21** e **US-22** no lifecycle.

### P2 — Evidência tem de ser reprodutível sem IA
Qualquer finding confirmado tem de poder ser reproduzido por:
- teste automatizado (regressão),
- PoC mínima,
- log/artefacto determinístico (SARIF, HTTP transcript, crash dump, etc.).

### P3 — Dados sensíveis nunca entram “às cegas” num modelo
Prompts e contextos devem respeitar:
- minimização (apenas o necessário),
- redacção/masking,
- segregação de segredos (nunca colar tokens/headers reais),
- política organizacional de uso de IA (ver anexo transversal de políticas).

### P4 — Risco “modelo/supply chain” também é risco de segurança
Ferramentas de IA (cloud ou local) fazem parte da cadeia de confiança.
Devem existir controlos equivalentes aos aplicados a dependências e CI/CD:
- versionamento do modelo/config,
- logging de prompts/outputs (quando permitido),
- revisão de permissões e acessos,
- verificação de integridade/proveniência quando aplicável.

---

## 2) Casos de uso recomendados (e como fazer com segurança)

### 2.1 Triagem assistida (SAST/DAST/IAST/SCA/Fuzzing)
**Objetivo:** reduzir tempo de análise e melhorar consistência da decisão.

**Prática:**
- Fornecer à IA apenas:
  - ID do finding + regra/tool,
  - excerto mínimo do code path,
  - contexto técnico não sensível (padrão de autenticação, WAF existente, etc.),
  - política de severidade L1–L3 e critérios de gate.
- Exigir output estruturado (JSON/Markdown) com:
  - hipótese de exploitabilidade,
  - condições necessárias,
  - mitigação existente (se aplicável),
  - recomendação de validação empírica (passos concretos).

**Anti-padrão:** “IA disse que é falso positivo” sem prova.

**Evidência esperada:**
- decisão documentada via template (US-21 / T1),
- ligação a validação empírica (US-22 / T1–T5),
- registo de supressão com rationale e aprovador (se FP).

---

### 2.2 Geração assistida de testes de regressão de segurança
**Objetivo:** transformar findings corrigidos em proteção futura.

**Prática:**
- Pedir à IA para produzir:
  - esqueleto de teste (unit/integration/e2e),
  - payloads representativos,
  - asserts que comprovem falha antes e “pass” após correção.
- O developer valida e ajusta:
  - boundary conditions,
  - mocks/stubs,
  - fixtures seguras.

**Restrições:**
- Nunca aceitar código gerado sem revisão.
- Exigir que o teste referencia explicitamente:
  - o finding (ID),
  - o requisito relevante (Cap. 02),
  - o commit/PR de correção.

**Evidência esperada:**
- teste versionado,
- pipeline a executar regressões,
- relatório de execução anexado à release.

---

### 2.3 Assistência para autenticação em DAST (scripts/flows)
**Objetivo:** reduzir fricção em DAST autenticado e aumentar cobertura real.

**Prática:**
- A IA pode ajudar a construir um *login flow* genérico, mas:
  - credenciais reais não entram no prompt,
  - tokens/cookies reais são mascarados,
  - o fluxo final é testado em staging com conta técnica dedicada e rotação.

**Evidência esperada:**
- configuração do DAST versionada,
- cobertura por endpoints críticos,
- relatório DAST autenticado anexado à release.

---

### 2.4 Fuzzing assistido por IA (corpora, mutações e priorização)
**Objetivo:** aumentar capacidade de encontrar edge cases e crashes úteis.

**Prática:**
- IA para:
  - gerar seeds/corpora a partir de schemas (OpenAPI/GraphQL),
  - sugerir mutações (encoding, nesting, size),
  - priorizar endpoints por risco e histórico.
- Execução sempre em ambiente isolado, com:
  - limites de recursos,
  - logs completos,
  - dados não produção.

**Evidência esperada:**
- corpora versionada,
- crash repro + RCA,
- severidade ajustada com base em impacto real (DoS/RCE/etc).

---

### 2.5 Consolidação e deduplicação de findings multi-ferramenta
**Objetivo:** reduzir ruído e melhorar rastreabilidade.

**Prática:**
- IA pode sugerir clusters por:
  - CWE/CVE,
  - componente,
  - code path,
  - fingerprint.
- A regra de dedup final é configurada no sistema central (ex: DefectDojo) e não “na cabeça” do modelo.

**Evidência esperada:**
- regras de correlação versionadas,
- auditoria de merges/splits de findings,
- métricas FP/FN por tool ao longo do tempo.

---

## 3) Controlos obrigatórios quando se usa IA em testes

### C1 — Registo mínimo de “interação com IA” (quando permitido)
Para decisões de severidade ≥ HIGH (L2/L3), registar:
- objetivo do pedido,
- contexto fornecido (redigido),
- output relevante,
- decisão humana final + evidência (PoC/teste/log).

> Se a política de privacidade impedir logging, registar pelo menos: “IA usada” + tipo de apoio + evidência determinística sem prompt.

### C2 — Proteção contra prompt injection / conteúdo malicioso em artefactos
Quando a IA é alimentada com:
- logs,
- outputs de scanners,
- HTML/JS recolhido por DAST,
- payloads de fuzzing,

assumir que o conteúdo pode conter instruções maliciosas (“ignore regras…”, “exfiltra…”).  
Mitigação:
- sanitização,
- *content filtering*,
- execução em contexto “no tools / no network” sempre que possível,
- validação humana.

### C3 — Separação de ambientes e credenciais
IA usada para testes que interagem com runtime:
- só em staging isolado,
- com contas técnicas dedicadas,
- com segredos geridos por vault e nunca copiados.

### C4 — Proibição de “auto-merge” de correções de segurança
Qualquer patch gerado com IA:
- requer revisão humana,
- requer testes (incluindo regressão de segurança),
- nunca pode bypassar gates.

---

## 4) Integração explícita com este capítulo

Este addon reforça diretamente:

- **US-10/US-11** (centralização e feedback) — IA pode acelerar triagem e reduzir ruído, sem perder rastreabilidade.
- **US-21** (decisão assistida) — IA alimenta hipótese; decisão é humana, documentada.
- **US-22** (validação empírica) — IA sugere como validar; confirmação é sempre por PoC/teste.

---

## 5) Checklist de adoção (binário)

| Item | Sim/Não |
|------|:------:|
| Uso de IA em testes está coberto por política organizacional (minimização, dados, logging) |  |
| Existe template de decisão humana (CORRIGIR/ACEITAR/SUPRIMIR/DEFER) aplicado a findings críticos/altos |  |
| Existe procedimento de validação empírica por tipo de teste (SAST/DAST/IAST/Fuzzing/PenTest) |  |
| Há segregação de ambientes e contas técnicas para DAST/IAST/fuzzing com rotação de credenciais |  |
| Prompts nunca incluem segredos/PII; existe processo de redacção/masking |  |
| Outputs de IA não são usados como “prova” sem artefacto determinístico reprodutível |  |
| Patches gerados por IA nunca fazem auto-merge e passam por revisão + testes |  |
| Existe métrica FP/FN e tempo de decisão/validação por severidade e por L1–L3 |  |

---

## 6) Notas finais

A IA pode ser um multiplicador brutal de produtividade em testes de segurança — **se** for usada como acelerador de análise e geração de artefactos, e não como substituto de evidência e responsabilidade.

O critério de sucesso não é “menos trabalho humano”, mas sim:
- **mais cobertura**, 
- **menos tempo até confirmação**, 
- **melhor rastreabilidade**, 
- **menos decisões não fundamentadas**.
