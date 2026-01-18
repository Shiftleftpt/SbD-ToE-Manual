---

id: riscos-processo-imagens
title: Riscos de Processo na Construção, Validação e Promoção de Imagens
description: Identificação e mitigação dos riscos introduzidos pela automação na cadeia de build, validação e execução de imagens de container
tags: [containers, imagens, risco-processo, pipeline, decisao-humana, evidencias, supply-chain, proveniencia, cicd, sbd-toe]
----------------------------------------------------------------------------------------------------------------------------

# 🛠️ Riscos de Processo na Construção, Validação e Promoção de Imagens

A construção e execução de imagens de container é hoje, na maioria das organizações, um **processo fortemente automatizado**.
Dockerfiles, manifests, pipelines, políticas e promoções entre ambientes são frequentemente **gerados, aplicados e executados sem intervenção humana direta**.

Esta realidade introduz **riscos de processo específicos**, distintos dos riscos técnicos clássicos (vulnerabilidades, misconfigurações, CVEs), que devem ser tratados explicitamente.

Este ficheiro estabelece o enquadramento canónico para esses riscos no SbD-ToE.

---

## 🎯 Âmbito e princípio fundamental

Este documento **não trata vulnerabilidades de imagens** — essas são cobertas noutros ficheiros do capítulo.
Aqui tratamos exclusivamente do **risco introduzido pela forma como as imagens são produzidas, avaliadas e aceites**.

> **Princípio central:**
> Ferramentas produzem **sinais**.
> A aceitação de risco é sempre uma **decisão humana**, baseada em evidência verificável.

Qualquer processo que viole esta separação é considerado **inseguro por desenho**, mesmo que tecnicamente “correto”.

---

## 🧩 Cadeia típica de risco em ambientes automatizados

Em ambientes modernos, a cadeia de eventos mais comum é:

1. Um artefacto (Dockerfile, manifest, pipeline) é criado ou alterado.
2. O pipeline constrói automaticamente uma imagem.
3. Ferramentas automáticas produzem sinais (scans, políticas, assinaturas).
4. A imagem é promovida para outro ambiente.
5. O workload é executado em produção.

⚠️ Em muitos contextos, **nenhuma decisão humana explícita ocorre entre os passos 2 e 5**.

Este ficheiro identifica onde esse modelo falha.

---

## 🚨 Categorias de risco de processo

### 1️⃣ Confusão entre sinal automático e decisão

**Como surge**

* “Build passou” é interpretado como “imagem segura”.
* “Sem findings” é interpretado como “risco inexistente”.
* “Policy aplicada” é interpretado como “execução autorizada”.

**Risco**

* Aceitação implícita de risco não avaliado.
* Ausência de responsável identificável.
* Impossibilidade de justificar decisões a posteriori.

**Mitigação prescrita**

* Definir pontos explícitos de decisão humana (aceitação, exceção, promoção).
* Registar quem decidiu, com base em que evidência.

**Evidência esperada**

* Registo versionado da decisão.
* Ligação clara entre sinal técnico e decisão tomada.

---

### 2️⃣ Ilusão de segurança por automação bem-sucedida

**Como surge**

* Confiança excessiva em scanners ou policies.
* Assunção de que cobertura automática é exaustiva.
* Desvalorização de risco residual.

**Risco**

* Vulnerabilidades não detetadas.
* Contexto ignorado (ex.: impacto real, exposição).
* Falsa sensação de controlo.

**Mitigação prescrita**

* Tratar sinais automáticos como **inputs**, não conclusões.
* Exigir análise humana para risco residual relevante.

**Evidência esperada**

* Justificação documentada para aceitação ou mitigação.
* Ligação a critérios de risco organizacionais.

---

### 3️⃣ Promoção automática entre ambientes

**Como surge**

* Promoções automáticas DEV → QA → PROD.
* Reutilização acrítica da mesma imagem.
* Falta de revalidação contextual.

**Risco**

* Propagação de erros ou decisões erradas.
* Execução em contextos mais sensíveis sem nova avaliação.

**Mitigação prescrita**

* Promoção por estágios com aprovação explícita em L2/L3.
* Revalidação de políticas e proveniência por ambiente.

**Evidência esperada**

* Registos de promoção com responsável identificado.
* Evidência de validação por ambiente.

---

### 4️⃣ Proveniência verificada ≠ confiança concedida

**Como surge**

* Assinaturas e attestation tratadas como autorização implícita.
* Falta de distinção entre integridade e adequação.

**Risco**

* Execução de artefactos legítimos mas inadequados.
* Incapacidade de revogar confiança contextual.

**Mitigação prescrita**

* Separar verificação de integridade de decisão de execução.
* Definir critérios organizacionais de confiança.

**Evidência esperada**

* Política explícita de aceitação de imagens.
* Registos de decisão associados à proveniência.

---

### 5️⃣ Ausência de rastreabilidade decisional

**Como surge**

* Logs técnicos sem contexto decisional.
* Falta de ligação entre commit, pipeline, imagem e execução.

**Risco**

* Auditorias inconclusivas.
* Dificuldade em responder a incidentes.
* Responsabilidade difusa.

**Mitigação prescrita**

* Rastreabilidade completa:
  **commit → pipeline → imagem → decisão → execução**

**Evidência esperada**

* Identificadores correlacionáveis.
* Retenção adequada de registos.

---

## 🧭 Regras canónicas SbD-ToE aplicáveis a imagens

Este capítulo herda e concretiza os seguintes invariantes globais do SbD-ToE:

* Separação entre **sugestão** e **decisão**
* Evidência acima de plausibilidade
* Reprodutibilidade e auditabilidade
* Responsabilidade humana explícita
* Rastreabilidade fim-a-fim

Qualquer implementação que viole estes princípios deve ser considerada **não conforme**, independentemente da maturidade técnica aparente.

---

## 🔗 Ligação aos restantes ficheiros do capítulo

Este ficheiro é **transversal** e deve ser lido em conjunto com:

* `01-imagens-base.md` — seleção e validação inicial
* `03-assinatura-cadeia-trust.md` — integridade e proveniência
* `05-policies-runtime-opa.md` — enforcement técnico
* `06-inventario-sbom.md` — rastreabilidade de componentes
* `exemplo-pipeline-container.md` / lifecycle — operacionalização

Ele fornece o **enquadramento semântico** que dá sentido prescritivo aos controlos técnicos descritos nesses documentos.

---

## ✅ Critério de conformidade

Uma organização só pode afirmar que aplica corretamente este capítulo se conseguir demonstrar, para qualquer imagem em execução:

1. Quem decidiu a sua aceitação.
2. Com base em que evidência técnica.
3. Em que contexto de risco.
4. Quando e por quanto tempo essa decisão é válida.

Sem estas respostas, não existe confiança operacional — apenas automação.
