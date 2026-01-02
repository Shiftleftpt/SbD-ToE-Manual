---
id: validacao-requisitos
title: Estratégias de Validação de Requisitos
description: Formas recomendadas de testar e verificar requisitos definidos no catálogo
tags: [validação, requisitos, testes, evidência, ciclo de vida]
---

# ✅ Validação de Requisitos de Segurança

## 🌟 Objetivo

Prescrever a forma de validar a aplicação dos **requisitos de segurança definidos no Capítulo 2**, com ênfase em mecanismos rastreáveis, contínuos e integráveis no ciclo de desenvolvimento.

A validação permite:

- Confirmar que os requisitos definidos foram **efetivamente aplicados**;
- Assegurar que os controlos estão **presentes, funcionais e eficazes**;
- Produzir **evidência verificável e auditável** da conformidade com os requisitos de segurança aplicacionais.

---

## 📌 Princípios orientadores

A validação deve ser:

- **Sistemática**: associada a momentos bem definidos do ciclo de vida;
- **Proporcional ao risco**: validando com mais profundidade requisitos de maior criticidade;
- **Rastreável**: com ligação entre requisito, validação e resultado;
- **Repetível**: automatizável ou documentada de forma clara;
- **Independente**: sempre que possível, realizada por alguém fora da implementação direta.

---

## 🛠️ Como validar

A escolha do método depende do tipo de requisito e do momento em que é aplicado. Os métodos incluem:

### 1. Análise Estática (SAST)

- Usada para requisitos que se traduzem em padrões de código, configurações ou estruturas previsíveis.
- Aplica-se durante o desenvolvimento e no pipeline de build.
- Deve abranger a verificação de:
  - presença de validações de entrada;
  - uso de bibliotecas aprovadas;
  - aplicação de controlos criptográficos mínimos;
  - controlo de fluxo de autenticação e autorização.
- Os resultados devem ser integrados com os identificadores de requisitos (ex: `SEC-L2-*`).

### 2. Análise Dinâmica (DAST)

- Aplica-se a requisitos que se manifestam na execução da aplicação.
- Deve ser usada em ambiente de teste ou pré-produção.
- Permite validar:
  - exposição de endpoints e headers;
  - comportamento perante entradas maliciosas;
  - ausência de erros ou divulgações indevidas;
  - resposta a falhas de autenticação ou autorizações mal configuradas.

### 3. Testes funcionais de segurança

- Complementam a análise dinâmica e verificam o comportamento do sistema com base nos critérios de aceitação de cada requisito.
- Devem incluir:
  - Verificação do comportamento esperado (positivo);
  - Exploração de comportamentos indevidos ou bypasses (negativo);
  - Cobertura de casos-limite, restrições e falhas previstas no requisito.

### 4. Revisão técnica estruturada

- Realizada por analistas, arquitetos ou elementos da equipa de segurança.
- Foca-se em requisitos cujo controlo seja distribuído ou implícito (ex: segregação lógica, dependências, controlo de sessão).
- Deve ocorrer após marcos relevantes: release candidate, pull request crítico, auditoria interna.

### 5. Validação contínua em CI/CD

- Requisitos críticos e rastreáveis devem estar ligados a mecanismos de bloqueio na pipeline.
- Isso inclui:
  - Avaliações automáticas do código e da configuração;
  - Rejeição de builds que violem critérios mínimos (ex: falta de MFA, falta de logging, hardcoded secrets);
  - Revalidação dos requisitos com cada alteração de risco (ex: nova feature, nova integração).

---

## 📆 Quando validar

| Fase SDLC               | Objetivo da validação                          | Método primário                        |
|-------------------------|-----------------------------------------------|----------------------------------------|
| Planeamento e definição | Confirmação da aplicabilidade dos requisitos  | Análise técnica + validação manual     |
| Desenvolvimento         | Detecção precoce de incumprimento             | SAST + revisão de código               |
| Testes                  | Verificação do comportamento previsto         | Testes funcionais + DAST               |
| Pré-release / entrega   | Validação de conformidade total               | Validação cruzada + CI/CD gates        |
| Produção / operação     | Monitorização contínua de requisitos ativos   | Revalidação, logging, alertas          |

---

## 🧬 Resultados esperados da validação

Cada requisito validado deve gerar:

- **Evidência de execução** (relatório, log, artefacto de validação);
- **Resultado binário ou graduado** (ex: conforme / não conforme / parcial);
- **Ligação ao identificador do requisito** (ex: `SEC-L2-INPUT-VALID`);
- **Recomendação ou medida corretiva**, se necessário.

---

## � Validação Manual Obrigatória em L3 (Domínios Críticos)

**Contexto normativo:**  
Este addon implementa os requisitos de **I2 (Evidência acima de plausibilidade)** de [agent.md](https://github.com/your-org/agent-spec), aplicados ao contexto de validação de requisitos. Em aplicações L3, testes automatizados (SAST/DAST/SCA) **não são suficientes** em domínios críticos onde falsos positivos podem ocultar vulnerabilidades reais.

### Domínios que exigem validação manual em L3

| Domínio Crítico | Risco de Automação | Validação Manual Obrigatória |
|---|---|---|
| **Criptografia** | Ferramentas SAST detetam uso de algoritmos mas não validam contexto (ex: RSA-2048 adequado para assinatura mas insuficiente para encriptação de dados a longo prazo) | Revisão por especialista: algoritmo, modo, tamanho de chave, gestão de chaves, rotação, compliance (FIPS 140-2, eIDAS) |
| **Autenticação** | DAST pode confirmar presença de MFA mas não valida bypasses (ex: endpoint `/admin/debug` sem autenticação) | Teste manual de escalação de privilégios, bypass de autenticação, session fixation, token leakage |
| **Autorização** | SAST deteta checks de permissão mas não valida lógica de negócio (ex: utilizador pode aceder a dados de outro utilizador do mesmo tenant) | Teste manual de IDOR (Insecure Direct Object Reference), privilege escalation horizontal/vertical, boundary testing |
| **Validação de Dados Sensíveis** | Scanners identificam falta de validação mas não compreendem semântica (ex: campo "email" aceita SQL injection mas passa validação de regex) | Revisão de validação contextual: tipo de dado vs. uso, encoding, sanitization, output encoding |
| **Gestão de Sessões** | Ferramentas validam flags (HttpOnly, Secure, SameSite) mas não testam lógica de expiração, concorrência, invalidação | Teste manual: concurrent sessions, session timeout, logout efetivo, session hijacking, CSRF bypass |
| **Logging & Auditoria** | SAST confirma presença de logs mas não valida completude (ex: login registado mas não mudanças de permissões) | Revisão manual: cobertura de eventos críticos, integridade de logs, retenção, proteção contra tampering |

### Procedimento de validação manual L3

:::userstory
**História.**  
Como **AppSec Engineer**, quero **realizar validação manual de requisitos críticos em L3** antes do go-live, para garantir que testes automatizados não ocultam vulnerabilidades contextuais ou de lógica de negócio.

**Critérios de aceitação (BDD).**
- **Dado** que aplicação é L3 e tem requisitos em domínios críticos (criptografia, autenticação, autorização)  
  **Quando** SAST/DAST reportam "pass" para esses requisitos  
  **Então** executo validação manual adicional e documento resultados em relatório separado

**Checklist de validação manual L3.**
- [ ] **Criptografia:**
  - [ ] Algoritmos usados são adequados ao contexto (assinatura vs. encriptação vs. hashing)?
  - [ ] Tamanho de chaves cumpre compliance (FIPS, eIDAS, GDPR)?
  - [ ] Gestão de chaves é segura (KMS, rotação, não-hardcoded)?
  - [ ] Modo de operação é correto (ex: CBC com IV aleatório, GCM para AEAD)?
- [ ] **Autenticação:**
  - [ ] Todos os endpoints críticos exigem autenticação (incluindo `/admin/*`, `/api/internal/*`)?
  - [ ] MFA é obrigatório e não pode ser bypassed?
  - [ ] Tokens têm expiração adequada e são invalidados em logout?
  - [ ] Teste manual de session fixation, credential stuffing, brute force?
- [ ] **Autorização:**
  - [ ] Teste IDOR em todos os recursos críticos (dados, ficheiros, configurações)?
  - [ ] Privilege escalation horizontal/vertical testado?
  - [ ] Lógica de negócio respeitada (ex: utilizador A não acede a dados de utilizador B mesmo no mesmo tenant)?
- [ ] **Validação de Dados:**
  - [ ] Validação contextual (não apenas regex): tipo vs. uso?
  - [ ] Output encoding correto (HTML, JSON, SQL, LDAP)?
  - [ ] Teste de bypasses: SQL injection, XSS, command injection, path traversal?
- [ ] **Sessões:**
  - [ ] Concurrent sessions controladas (ou permitidas mas monitorizadas)?
  - [ ] Session timeout testado (idle + absolute)?
  - [ ] Logout invalida sessão em servidor (não apenas cookie)?
  - [ ] CSRF testado em operações críticas (mudança password, transferências)?
- [ ] **Logging:**
  - [ ] Eventos críticos registados: login, logout, mudança permissões, acesso a dados sensíveis, falhas de autorização?
  - [ ] Logs protegidos contra tampering (append-only, assinatura, SIEM)?
  - [ ] Retenção cumpre requisitos regulatórios (GDPR, NIS2)?

**Artefactos obrigatórios.**
- Relatório de validação manual: `validacao-manual-L3-YYYY-MM-DD.md`
- Evidências: screenshots, logs de teste, PoC de vulnerabilidades encontradas
- Aprovação: AppSec Engineer assina relatório antes de go-live
:::

**Proporcionalidade:**
| Nível | Validação Manual Obrigatória? |
|---|---|
| L1 | Não (apenas SAST/DAST automático) |
| L2 | Recomendado para autenticação e autorização |
| L3 | **Obrigatório para todos os 6 domínios críticos** |

**Integração no SDLC:**
- **Fase:** Pré-release, após SAST/DAST reportarem "pass"
- **Responsável:** AppSec Engineer (não pode ser Developer da própria equipa)
- **SLA:** 5 dias úteis antes de go-live
- **Bloqueio:** Go-live não pode ocorrer sem aprovação do relatório de validação manual

---

## ⚠️ Tratamento de Falsos Positivos e Falsos Negativos

**Contexto normativo:**  
Este addon implementa os requisitos de **I2 (Evidência acima de plausibilidade)** e **I5 (Rastreabilidade de decisão)** de [agent.md](https://github.com/your-org/agent-spec). Ferramentas automatizadas produzem falsos positivos (alertam quando não há vulnerabilidade) e falsos negativos (não alertam quando há vulnerabilidade).

### Definições

- **Falso Positivo (FP):** Ferramenta reporta vulnerabilidade mas, após análise humana, não existe risco real
- **Falso Negativo (FN):** Ferramenta não reporta vulnerabilidade mas, após análise humana ou incidente, existe risco real

### Procedimento de gestão de falsos positivos

:::userstory
**História.**  
Como **Developer** e **AppSec Engineer**, quero **registar e justificar falsos positivos de ferramentas SAST/DAST**, para evitar ruído operacional mantendo rastreabilidade de decisões.

**Critérios de aceitação (BDD).**
- **Dado** que ferramenta SAST/DAST reportou finding com severidade ≥ Média  
  **Quando** Developer analisa e conclui que é falso positivo  
  **Então** regista justificação técnica e submete para aprovação de AppSec Engineer

**Checklist de gestão de FP.**
- [ ] **Análise técnica documentada:**
  - [ ] Finding ID da ferramenta (ex: `SONAR-123`, `SEMGREP-456`)
  - [ ] Requisito afetado (ex: `REQ-CRYPTO-001`)
  - [ ] Razão técnica do falso positivo (ex: "Ferramenta deteta MD5 mas é usado para checksum, não criptografia")
  - [ ] Evidência (código, configuração, documentação)
- [ ] **Aprovação por AppSec Engineer:**
  - [ ] Validação da justificação técnica
  - [ ] Confirmação que não existe risco residual
  - [ ] Registo em ficheiro `falsos-positivos/FP-YYYY-MM-DD-XXX.md` (Template 2 de addon-11)
- [ ] **Supressão na ferramenta:**
  - [ ] Comentário inline explicativo (ex: `// nosemgrep: sql-injection - parametrized query`)
  - [ ] Tag de supressão com link para ficheiro de justificação
  - [ ] Data de criação e owner da supressão
- [ ] **Revisão periódica:**
  - [ ] Falsos positivos revistos a cada 6 meses (L2) ou 3 meses (L3)
  - [ ] Revalidação: FP continua válido ou ferramenta foi atualizada e agora deteta corretamente?

**Artefactos obrigatórios.**
- Ficheiro: `falsos-positivos/FP-YYYY-MM-DD-XXX.md` (estrutura: Template 2 de addon-11)
- Supressão inline com comentário explicativo
- Aprovação de AppSec Engineer (email, issue comentada, ou commit reviewado)
:::

### Procedimento de deteção de falsos negativos

:::userstory
**História.**  
Como **AppSec Engineer**, quero **identificar falsos negativos de ferramentas** (vulnerabilidades não-detetadas), para ajustar configuração ou adicionar validação manual.

**Critérios de aceitação (BDD).**
- **Dado** que ocorreu incidente ou pentesting externo identificou vulnerabilidade  
  **Quando** confirmo que SAST/DAST não detetou a vulnerabilidade  
  **Então** registo falso negativo, ajusto ferramenta (se possível) e adiciono validação manual ao processo

**Checklist de gestão de FN.**
- [ ] **Registo de falso negativo:**
  - [ ] Vulnerabilidade identificada (CVE, CWE, descrição)
  - [ ] Requisito afetado (ex: `REQ-AUTH-001`)
  - [ ] Ferramenta que deveria ter detetado (SAST X, DAST Y)
  - [ ] Razão técnica da falha (ex: "SAST não deteta SQL injection em queries dinâmicas com string concatenation")
- [ ] **Mitigação imediata:**
  - [ ] Correção da vulnerabilidade (PR crítico)
  - [ ] Validação manual até ferramenta ser ajustada
- [ ] **Ajuste de ferramenta (se possível):**
  - [ ] Configuração ajustada (ex: adicionar regra custom)
  - [ ] Atualização de versão da ferramenta
  - [ ] Se impossível: documentar limitação e adicionar validação manual permanente
- [ ] **Prevenção futura:**
  - [ ] Adicionar teste de regressão (caso de teste que falhou)
  - [ ] Incluir padrão de código vulnerável em training de equipa
  - [ ] Atualizar checklist de validação manual (se L3)

**Artefactos obrigatórios.**
- Ficheiro: `falsos-negativos/FN-YYYY-MM-DD-XXX.md`
- Evidência: vulnerability report, PoC, correção aplicada
- Lessons learned: documento de retrospetiva (se severidade ≥ Alta)
:::

### Métricas de qualidade de ferramentas

**KPIs para monitorização de SAST/DAST:**
- **Taxa de falsos positivos:** `(FP aprovados / Total findings) × 100` — Meta: <15% (se >30%, ferramenta gera ruído excessivo)
- **Taxa de falsos negativos:** `(FN identificados / Total vulnerabilidades reais) × 100` — Meta: <5% (se >10%, ferramenta inadequada)
- **Tempo médio de aprovação de FP:** Dias desde Developer identifica FP até AppSec aprova — Meta: <3 dias
- **Cobertura de domínios críticos:** % de domínios críticos (6 listados acima) com deteção efetiva — Meta: 100% em L3

**Decisões baseadas em métricas:**
- Se taxa de FP >30%: Ajustar configuração de ferramenta ou substituir por alternativa
- Se taxa de FN >10%: Adicionar ferramenta complementar ou reforçar validação manual
- Se tempo de aprovação FP >5 dias: Processo de aprovação é gargalo, considerar delegação ou automação

**Proporcionalidade:**
| Nível | Gestão de FP Obrigatória? | Gestão de FN Obrigatória? | Revisão Periódica de FP |
|---|---|---|---|
| L1 | Recomendado | Recomendado | Anual |
| L2 | Obrigatório | Obrigatório | Semestral |
| L3 | Obrigatório + Aprovação AppSec | Obrigatório + Root Cause Analysis | Trimestral |

---

## 📎 Referências cruzadas

Este documento complementa os seguintes artefactos do capítulo:

| Documento                             | Relação com a validação                    |
|--------------------------------------|--------------------------------------------|
| [Catalogo de Requisitos](./catalogo-requisitos)    | Define os requisitos a validar             |
| [Controlos por Nivel de classificação](./matriz-controlos-por-risco) | Aponta os requisitos por nível de risco |
| [addon-11: Validação Assistida por Ferramentas](./11-validacao-requisitos-assistida) | Templates de decisão (FP/FN), Invariantes I2/I5 |
| [US-09: Validação por Requisito](../aplicacao-lifecycle#us-09---validação-por-requisitodomínio-req-xxx--evidência) | Integração com validação assistida (checklist C3) |
| [agent.md: Invariantes I2 e I5](https://github.com/your-org/agent-spec) | Fundamento normativo para evidência e rastreabilidade |


---

## 🔁 Melhoria contínua

A validação de requisitos deve ser incorporada num ciclo de melhoria contínua, onde os métodos são:

- **Revistos com base em incidentes ou findings reais**;
- **Atualizados com novas técnicas** ou alterações ao catálogo;
- **Automatizados sempre que possível**, para reforçar a escalabilidade e cobertura;
- **Monitorizados com indicadores de conformidade** ao longo do tempo (ex: % requisitos validados por release).

---

> 📌 A validação eficaz transforma requisitos em proteção real.  
> Não basta definir - é preciso confirmar, medir, melhorar.
