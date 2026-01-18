---
id: evidencia-reprodutibilidade
title: Evidência, Reprodutibilidade e Auditabilidade em Testes de Segurança
description: Regras prescritivas para garantir que resultados de testes de segurança são verificáveis, reproduzíveis e auditáveis, com proteção de ativos críticos e separação entre sinal automático e decisão humana.
tags: [testes, evidência, reprodutibilidade, auditabilidade, validação, rastreabilidade, supply-chain, segredos, dados]
sidebar_position: 10
---

# 🛠️ Evidência, Reprodutibilidade e Auditabilidade em Testes de Segurança

Este anexo define regras **prescritivas** para garantir que os testes de segurança produzem **evidência verificável**, permitem **reprodução independente** e suportam **auditoria** — mesmo quando a execução é altamente automatizada.

O objetivo é evitar três falhas recorrentes em processos modernos de teste:

1. **Confundir “sinal” com “evidência”** (ex.: um relatório ou um score substitui execução observável).
2. **Perder reprodutibilidade** (ex.: o mesmo commit produz resultados incomparáveis por variação de regras, ambiente ou dados).
3. **Expor ativos críticos** (ex.: credenciais, dados, telemetria ou artefactos de build saem do perímetro sem controlo explícito).

> Regra-mãe: **um teste só “conta” como evidência quando pode ser verificado e reproduzido, com autoria e decisão atribuídas a um role humano.**

---

## 1. Separação entre sinal automático e decisão humana

Ferramentas podem:
- detetar padrões;
- correlacionar resultados;
- priorizar achados;
- sugerir correções.

Mas **não podem**:
- declarar “aprovado” ou “conforme”;
- fechar findings sem validação definida;
- autorizar exceções;
- aceitar risco residual.

### Prescrição
- Cada *gate* de segurança (pass/fail) deve ter um **responsável humano explícito** (ex.: Tech Lead, AppSec, QA Lead, Release Manager).
- “Passou no scanner” **não é** um argumento aceite sem:
  - evidência de execução (logs/artefactos),
  - condições de execução (config/versões),
  - e critérios de aprovação (policy/regras).

---

## 2. Evidência mínima (o que deve existir para um resultado ser aceite)

### 2.1 Evidência de execução (obrigatória)
Para cada execução relevante de testes de segurança, deve existir, no mínimo:

- Identificador do commit / build / artefacto testado (hash, tag, digest).
- Timestamp e *runner* / executor identificado.
- Configuração efetiva usada (ficheiro, parâmetros, profile).
- Versão do motor de teste e versões dependentes (ex.: imagens, rulepacks, assinaturas).
- Output bruto preservado (log completo, JSON/XML/HTML, artefactos).
- Resultado sumarizado (pass/fail, thresholds, severidades) **derivado do output bruto**.

> Dashboards e PDFs são apenas “apresentação”. A evidência é o **output bruto + contexto de execução**.

### 2.2 Evidência de validação (quando aplicável)
Sempre que exista triagem, exceção, supressão, ou “compensação”:

- Registo de quem validou e quando (autor/role).
- Justificação objetiva (critério + referência).
- Condição de validade (TTL, próxima data de reteste, condição de fecho).
- Ligação ao item de backlog / ticket / decisão de release.

---

## 3. Reprodutibilidade: tornar resultados comparáveis no tempo

### 3.1 Controlo de variáveis (obrigatório)
Resultados de teste só são comparáveis se as variáveis críticas forem controladas:

- **Versão do motor e regras**: rulepacks, assinaturas, políticas.
- **Ambiente de execução**: imagem de runner, sistema operativo, dependências.
- **Alvo testado**: build/digest/artefacto imutável.
- **Configuração**: profiles, listas de exclusão, limites, thresholds.
- **Dados e credenciais de teste**: dataset e permissões (ver Secção 4).

### 3.2 Prescrições práticas
- Usar *pinning* de versões (motor + regras) por pipeline e por projeto.
- Versionar (em repo) perfis e políticas de teste.
- Preservar outputs brutos com retenção mínima definida (ex.: por release).
- Garantir que cada execução pode ser reexecutada com “mesmo input” (replay).

### 3.3 Testes intrinsecamente não determinísticos
Alguns testes podem produzir variação (ex.: fuzzing, DAST com temporizações, alvos distribuídos).

**Nesses casos:**
- Preservar *seed* e parâmetros de execução quando existirem.
- Repetir execução (mínimo N) para reduzir falsos negativos.
- Tratar ausência de finding como **sinal fraco** sem evidência adicional de cobertura.

---

## 4. Proteção de ativos críticos no processo de teste

Testes de segurança frequentemente envolvem:
- credenciais e tokens para testes autenticados;
- dados representativos (ou acidentalmente reais);
- telemetria, logs e tráfego contendo segredos;
- artefactos de build e código.

### 4.1 Prescrições obrigatórias
- **Dados reais**: proibidos por omissão em testes (salvo aprovação explícita e controlos compensatórios).
- **Credenciais de teste**:
  - devem ser segregadas por ambiente,
  - mínimas (least privilege),
  - com rotação e expiração.
- **Egress e telemetria**:
  - qualquer envio de outputs para fora do perímetro deve ser tratado como dependência de supply chain;
  - exigir aprovação explícita, classificação do dado e controlo contratual/técnico.
- **Logs**:
  - aplicar regras de mascaramento;
  - garantir que outputs preservados não expõem segredos.

### 4.2 Ambientes e alvos de teste
- DAST/IAST/fuzzing devem usar ambientes com:
  - isolamento de rede,
  - limitação de impacto (rate limiting, quotas),
  - monitorização de alterações e tráfego.
- Testes ofensivos e intrusivos devem ter:
  - janela aprovada,
  - “kill switch” operacional,
  - critérios de paragem.

---

## 5. Evidência mínima por tipo de teste (tabela operativa)

| Tipo de teste | Evidência mínima de execução | Reprodutibilidade mínima | Nota crítica |
|---|---|---|---|
| SAST | commit + config + versão motor/regras + output bruto | pin de regras + baseline comparável | “0 findings” sem baseline é sinal fraco |
| DAST | alvo + janela + auth profile + output + logs de execução | config versionada + política de scope | risco elevado de exfiltração e falsos negativos |
| IAST | build + instrumentação + config + logs + findings | versão da instrumentação + ambiente controlado | outputs podem conter dados sensíveis |
| Fuzzing | alvo + parâmetros + seed (se aplicável) + crashes + logs | seed + tempo de execução + corpus versionado | ausência de crash ≠ ausência de bug |
| Pentesting / manual | scope + metodologia + evidência (PoC) + reporte | artefactos e notas de execução preservadas | exige rastreio de decisão e correção |

---

## 6. Exceções, supressões e aceitação de risco (fecho de ciclo)

Supressões, “false positives”, exceções e aceitação de risco são **factos de governação**, não “opiniões” técnicas.

### Prescrição
- Nenhuma exceção é válida sem:
  - responsável humano,
  - justificação objetiva,
  - prazo (TTL),
  - plano de reteste,
  - ligação ao release/artefacto afetado.

---

## 7. Critérios de aceitação deste anexo

Este anexo é considerado aplicado quando, no projeto:

1. Existe evidência bruta preservada para execuções relevantes.
2. Perfis e políticas de teste estão versionados e controlados.
3. O replay de uma execução é possível (ou a variação é controlada por repetição).
4. Credenciais/dados/telemetria são tratados como ativos críticos com controlos explícitos.
5. Decisões de exceção e “pass/fail” têm dono humano e rastreabilidade.

---
