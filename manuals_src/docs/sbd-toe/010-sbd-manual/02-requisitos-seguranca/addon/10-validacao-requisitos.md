---
id: plano-validacao
title: Plano de Validação de Requisitos de Segurança
description: Orientações de verificação por requisito do catálogo
tags: [validação, requisitos, teste, evidência, rastreabilidade]
---

# 🧪 Validação dos Requisitos de Segurança

Este documento constitui uma **extensão normativa prática do Capítulo 2**, focada não na definição dos requisitos de segurança, mas na sua **validação concreta**.

> É o equivalente a perguntar:  
> **“Dado o requisito `REQ-XYZ`, como o validamos na prática, com que profundidade, em que contexto, e com que evidência?”**

O objetivo é garantir que todos os requisitos definidos:

- São **efetivamente implementados**;
- São **verificáveis** por métodos objetivos e rastreáveis;
- Produzem **evidência concreta e auditável**;
- Podem ser **mapeados aos ciclos de desenvolvimento**, controlo de qualidade e auditoria.

---

### 🔐 AUT — Autenticação e Gestão de Identidade

| ID        | Tag                 | Nome resumido                              | Nível | Validação Recomendada                                                                                                                                     | Evidência Esperada                                                                                   |
|-----------|--------------------|---------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| AUT-001   | SEC-Lx-AUT-MFA     | MFA obrigatório                             | L2+    | Verificar exigência de MFA em ambiente real. Tentar login sem segundo fator. Confirmar logs de falha e fallback.                                         | Captura de ecrã ou log de falha de autenticação sem MFA.                                              |
| AUT-002   | SEC-Lx-AUT-PWD     | Política de passwords segura                | L1+    | Rever política ativa. Tentar alterar password inválida. Confirmar rejeição e logging.                                                                     | Exemplo de política. Log de erro ou alerta de falha.                                                  |
| AUT-003   | SEC-Lx-AUT-BRUTE   | Proteção contra brute force                 | L2+    | Simular várias tentativas erradas. Confirmar bloqueio, CAPTCHA ou atraso.                                           | Log com contagem de falhas. Evidência de bloqueio.                                                    |
| AUT-004   | SEC-Lx-AUT-LOGOUT  | Logout revoga sessão                        | L1+    | Efetuar logout. Tentar reusar sessão. Confirmar falha e pedido de nova autenticação.                               | Captura de revalidação ou erro. Log de sessão revogada.                                               |
| AUT-005   | SEC-Lx-AUT-IDLE    | Timeout por inatividade                     | L2+    | Simular inatividade. Confirmar expiração da sessão e redirect.                                                      | Log de timeout ou sessão terminada automaticamente.                                                   |
| AUT-006   | SEC-Lx-AUT-STORAGE | Proteção de credenciais                     | L1+    | Validar uso de hashing + salting e TLS. Verificar ausência de senhas em claro.                                     | Excertos de configuração, outputs de scan ou inspeção manual.                                         |
| AUT-007   | SEC-Lx-AUT-FED     | Suporte a autenticação federada             | L3     | Simular login federado via SAML/OIDC. Confirmar fluxo e logging.                                                    | Log de autenticação via fornecedor externo. Captura de login bem-sucedido.                           |
| AUT-008   | SEC-Lx-AUT-REAUTH  | Reautenticação para ações críticas          | L3     | Simular ação sensível (ex: alteração de perfil). Confirmar exigência de MFA adicional ou password.                  | Captura de reautenticação. Log associado à ação.                                                      |
| AUT-009   | SEC-Lx-AUT-CHANGE  | Reautenticação prévia à alteração de cred. | L2+    | Alterar credenciais sem sessão válida. Confirmar bloqueio ou erro.                                                  | Log da tentativa bloqueada. Evidência de sessão verificada.                                           |
| AUT-010   | SEC-Lx-AUT-ALERT   | Alertas de segurança para eventos críticos  | L3     | Simular login anómalo. Confirmar notificação ao utilizador e registo no sistema.                                    | Exemplo de notificação enviada. Log do evento crítico detetado.                                       |

---

### 🔐 ENC — Dados Sensíveis e Criptografia

| ID        | Tag                 | Nome resumido                                      | Nível | Validação Recomendada                                                                                                                                       | Evidência Esperada                                                                                      |
|-----------|--------------------|----------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ENC-001   | SEC-Lx-ENC-TRANS   | Encriptação de dados em trânsito                   | L1+    | Rever configuração de TLS. Testar downgrade de protocolo. Interceptar tráfego com proxy para verificar cifragem.                                            | TLS ativo. Resultado de scanner. Logs de conexão cifrada.                                                |
| ENC-002   | SEC-Lx-ENC-REST    | Encriptação de dados em repouso                   | L2+    | Verificar configuração de bases de dados, discos, buckets, backups. Rever políticas de encriptação.                                                         | Provas de configuração (ex: screenshots, policies, outputs de comandos).                                 |
| ENC-003   | SEC-Lx-ENC-ALG     | Uso de algoritmos criptográficos robustos         | L2+    | Rever código e configs. Verificar ausência de algoritmos fracos (ex: MD5, RC4). Validar presença de AES, RSA, etc.                                          | Auditoria de código/config. Saída de scanner de criptografia.                                            |
| ENC-004   | SEC-Lx-ENC-HASH    | Proteção de passwords com hashing seguro          | L1+    | Verificar uso de algoritmos como bcrypt, PBKDF2, scrypt. Confirmar uso de sal e parâmetros de iteração suficientes.                                          | Código com funções de hashing. Logs ou base de dados com hashes adequados.                              |
| ENC-005   | SEC-Lx-ENC-KEYMGMT | Gestão segura de chaves e segredos                | L3     | Verificar uso de cofres de segredos (ex: Vault, AWS Secrets Manager). Confirmar rotação e acesso mínimo.                                                    | Configuração do cofre. Políticas de acesso. Log de acesso a segredos.                                   |
| ENC-006   | SEC-Lx-ENC-EXPORT  | Prevenção de exportação indevida de dados         | L2+    | Tentar extrair dados sensíveis através de logs, dumps, erros ou endpoints. Rever políticas de exportação e anonimização.                                    | Logs controlados. Dumps limpos. Evidência de anonimização ou bloqueio.                                  |
| ENC-007   | SEC-Lx-ENC-LOG     | Mascaramento de dados sensíveis em logs           | L1+    | Forçar erro com dados sensíveis. Rever logs e confirmar ausência ou máscara de dados (ex: passwords, tokens, cartões).                                     | Captura de logs limpos. Política de logging aplicada.                                                    |
| ENC-008   | SEC-Lx-ENC-ROTATE  | Rotação periódica de segredos e chaves            | L3     | Rever configuração de rotação automática. Verificar data de criação/expiração dos segredos. Simular rotação manual.                                          | Evidência de rotação. Logs de expiração/substituição. Política de validade.                             |
| ENC-009   | SEC-Lx-ENC-LEAK    | Deteção de segredos expostos                     | L2+    | Executar ferramentas de scanning de segredos em repositórios (ex: TruffleHog, GitLeaks). Rever histórico e validação por branch/tag.                        | Relatório de scan. Issues abertas. Logs de deteção e correção.                                           |
| ENC-010   | SEC-Lx-ENC-BROWSER | Prevenção de caching de dados sensíveis no browser | L2+    | Verificar headers HTTP (ex: Cache-Control, Pragma, Expires). Testar comportamento com ferramentas de inspeção e refresh do browser.                         | Headers corretos. Captura de rede. Confirmação de comportamento.                                         |

---

### ⚙️ CFG — Configuração Segura e Gestão de Parâmetros

| ID        | Tag                 | Nome resumido                                      | Nível | Validação Recomendada                                                                                                                                       | Evidência Esperada                                                                                      |
|-----------|--------------------|----------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| CFG-001   | SEC-Lx-CFG-CENTRAL | Configuração centralizada e rastreável             | L2+    | Verificar que configurações estão em repositório ou sistema central. Auditar existência de histórico e versionamento.                                       | Ficheiros versionados. Histórico de alterações. Config server ou repo de config.                         |
| CFG-002   | SEC-Lx-CFG-NOCODE  | Separação entre código e configuração              | L1+    | Rever código para ausência de parâmetros embutidos. Confirmar uso de variáveis externas, ficheiros ou cofres.                                              | Ausência de hardcoded configs. Uso de `.env`, `appsettings.json`, Vault, etc.                            |
| CFG-003   | SEC-Lx-CFG-NOVAR   | Ausência de segredos em variáveis públicas         | L1+    | Validar que variáveis com segredos não estão expostas em UI, consola ou ambiente público.                                                                   | Auditoria de ambiente. Evidência de limpeza de output.                                                   |
| CFG-004   | SEC-Lx-CFG-ENV     | Separação de configurações por ambiente            | L2+    | Confirmar que existem configurações distintas para dev, staging, prod. Rever uso de feature flags e config por contexto.                                    | Configs por ambiente. Feature flags ou ficheiros separados.                                              |
| CFG-005   | SEC-Lx-CFG-DEFAULT | Remoção de configurações e credenciais por omissão | L2+    | Rever configurações padrão de frameworks, plataformas e containers. Confirmar ausência de users/ports/passwords default.                                    | Evidência de hardening. Scanner ou auditoria manual a configs.                                           |
| CFG-006   | SEC-Lx-CFG-TRACE   | Desativação de debug, tracing e interfaces admin   | L1+    | Tentar aceder a endpoints de debug, tracing ou interfaces de gestão. Verificar se estão desativados ou autenticados.                                        | Captura de resposta 403/404 ou login. Evidência de proteção.                                             |
| CFG-007   | SEC-Lx-CFG-VERS    | Gestão de versões de bibliotecas e componentes     | L2+    | Rever se versões utilizadas são explícitas e auditáveis (ex: lockfile). Confirmar ausência de versões flutuantes (`latest`, `*`).                           | Ficheiros de lock (`package-lock.json`, `requirements.txt`, etc.). SBOM.                                 |
| CFG-008   | SEC-Lx-CFG-RUNTIME | Proteção contra runtime config injection           | L3     | Tentar modificar configs em tempo de execução via API, UI ou ambiente. Rever proteção contra overrides.                                                      | Teste negativo. Logs de tentativa bloqueada. Documentação da proteção.                                   |


---

### 🧱 VAL — Validação e Sanitização de Dados

| ID        | Tag                 | Nome resumido                                  | Nível | Validação Recomendada                                                                                                                                           | Evidência Esperada                                                                                      |
|-----------|--------------------|--------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| VAL-001   | SEC-Lx-VAL-INPUT    | Validação de campos de entrada                  | L1+    | Rever código de backend e frontend. Confirmar existência de validações explícitas por tipo, comprimento, formato e regras de negócio.                           | Testes de input inválido. Código com validações. Logs de erros controlados.                             |
| VAL-002   | SEC-Lx-VAL-CROSS    | Validação cruzada entre campos                  | L2+    | Confirmar que campos relacionados (ex: data início/fim, username/email) são validados em conjunto. Simular inconsistências e verificar rejeição.                | Casos de teste de inconsistência. Código com validação composta.                                         |
| VAL-003   | SEC-Lx-VAL-BLACK    | Rejeição de listas negras e padrões inválidos   | L2+    | Simular entradas conhecidas como perigosas (ex: `<script>`, comandos SQL). Confirmar bloqueio explícito e logging.                                              | Logs de rejeição. Evidência de bloqueios e validações negativas.                                         |
| VAL-004   | SEC-Lx-VAL-SQLI     | Prevenção contra SQL Injection                  | L1+    | Rever código para uso de prepared statements. Executar testes automatizados (ex: via scanner SAST/DAST ou manual).                                              | Relatórios de scanner. Logs de execução. Ausência de concatenação em queries.                           |
| VAL-005   | SEC-Lx-VAL-XSS      | Prevenção contra Cross-Site Scripting (XSS)     | L1+    | Testar output em campos editáveis/renderizados no browser. Confirmar que dados são corretamente escapados ou codificados.                                       | Testes com payloads XSS. Sanitização de output observável.                                               |
| VAL-006   | SEC-Lx-VAL-UPLOAD   | Validação de uploads de ficheiros               | L2+    | Testar upload de ficheiros com tipos e extensões alteradas. Confirmar que sistema verifica conteúdo, MIME type, tamanho e extensões permitidas.                | Evidência de rejeição de uploads inválidos. Logs. Código de validação.                                   |
| VAL-007   | SEC-Lx-VAL-ENCODING | Normalização e codificação coerente de input    | L3     | Rever sistema para evitar ataques por codificação ambígua (ex: `%c0%ae`, UTF-7). Confirmar normalização consistente antes de validar.                          | Código com normalização. Testes com payloads ambíguos. Logs de erro.                                     |
| VAL-008   | SEC-Lx-VAL-ENUM     | Validação de valores fixos ou enumerados        | L1+    | Confirmar que listas fechadas (ex: roles, países) são validadas contra conjuntos explícitos e não inferidos.                                                    | Código com `enum` ou listas fixas. Testes com valores inválidos.                                         |
| VAL-009   | SEC-Lx-VAL-CLIENT   | Validação não depende apenas do lado cliente    | L1+    | Verificar que todas as validações aplicadas no frontend são também aplicadas no backend. Simular request direto via API com dados inválidos.                   | Rejeição pelo backend. Logs de erro. Código com duplicação de validações.                                |

---


## 🧾 LOG — Registo, Auditoria e Monitorização

| ID       | Tag               | Nível | Descrição resumida                                     | Validação Recomendada                                                                                                                                   | Evidência Esperada                                                       |
|----------|------------------|--------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| LOG-001  | SEC-L1-LOG-GERAL | L1+    | Atividade relevante deve ser registada                  | Rever código/configuração para confirmar que ações críticas (login, alteração, erro, acesso) são registadas. Validar cobertura de logs em runtime.     | Logs auditáveis com eventos mapeados por tipo e contexto.               |
| LOG-002  | SEC-L2-LOG-INTEG | L2+    | Logs devem ser íntegros e não manipuláveis              | Validar presença de mecanismos de proteção (hash, write-once, syslog remoto). Tentar alterar log em disco e detetar alteração.                          | Evidência de WORM, syslog remoto, ou mecanismos de detecção de tamper.  |
| LOG-003  | SEC-L2-LOG-ALERT | L2+    | Deve existir alerta para eventos de segurança           | Gerar evento anómalo (ex: login falhado repetido) e verificar se alerta é enviado. Confirmar thresholds e canais de alerta (email, SIEM, etc).          | Logs + registo de alerta disparado com timestamp e detalhe.             |
| LOG-004  | SEC-L3-LOG-CORR  | L3     | Deve existir correlação entre eventos em diferentes fontes | Simular evento distribuído (ex: acesso seguido de alteração suspeita). Confirmar correlação por ID de sessão, IP ou user ID em central de logs.        | Dashboards ou queries que agregam eventos correlacionados.              |
| LOG-005  | SEC-L2-LOG-DADOS | L2+    | Dados sensíveis não devem ser registados em logs        | Rever código e logs gerados. Confirmar ausência de dados sensíveis (passwords, tokens, dados pessoais). Executar testes com inputs sensíveis.           | Logs limpos + testes automatizados com inputs sensíveis.                |
| LOG-006  | SEC-L2-LOG-CONT  | L2+    | Logs devem ser centralizados e acessíveis               | Confirmar envio de logs para sistema central (ex: ELK, CloudWatch, SIEM). Rever configuração de forwarding e estrutura de logs.                         | Visualização centralizada com logs por aplicação.                       |
| LOG-007  | SEC-L3-LOG-TIME  | L3     | Logs devem ter timestamp com precisão e timezone         | Rever estrutura de logs e confirmar presença de timestamp ISO 8601 + timezone. Validar ordenação em dashboards e auditorias.                            | Logs com timestamps precisos e normalizados.                            |

---

## 📮 API — Segurança de APIs e Serviços Externos

| ID       | Tag               | Nível | Descrição resumida                                      | Validação Recomendada                                                                                                                                     | Evidência Esperada                                                       |
|----------|------------------|--------|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| API-001  | SEC-L1-API-AUTH   | L1+    | Todas as APIs devem exigir autenticação ou controlo de acesso | Testar endpoints sem credenciais. Confirmar rejeição com erro 401/403. Rever documentação OpenAPI.                                                        | Logs de rejeição, testes automatizados, documentação atualizada.         |
| API-002  | SEC-L2-API-RATE   | L2+    | Implementar controlo de taxa de pedidos (rate limiting)     | Efetuar testes com bursts de chamadas. Confirmar resposta 429 ou mecanismo de bloqueio temporário. Rever config de gateway/API proxy.                    | Evidência de rate limiting em runtime ou logs.                          |
| API-003  | SEC-L2-API-SCHEMA | L2+    | Validar requests/responses contra schema esperado          | Testar com payloads inválidos (missing fields, tipos errados). Confirmar rejeição automática. Rever testes de contrato e OpenAPI.                        | Rejeições consistentes + testes de schema/documentação.                 |
| API-004  | SEC-L3-API-INT    | L3     | Validar chamadas entre sistemas com autenticação mútua     | Rever configuração de autenticação mútua (MTLS, tokens entre serviços). Testar chamadas cruzadas sem identidade.                                          | Evidência de autenticação cruzada bem-sucedida + falhas controladas.    |
| API-005  | SEC-L2-API-METHOD | L2+    | Apenas métodos autorizados devem estar expostos             | Validar que endpoints não expõem métodos não utilizados (ex: PUT/DELETE). Verificar controlo por método no gateway ou backend.                            | Inventário de métodos ativos + testes negativos.                        |
| API-006  | SEC-L2-API-VERSAO | L2+    | As APIs devem ter versionamento explícito                   | Confirmar presença de `/v1/`, headers ou outro mecanismo de versionamento. Validar impacto de alterações não compatíveis.                                | Documentação de versão + testes de regressão por versão.                |

---




---




## 🧩 Notas complementares

- A coluna **Nível** indica os níveis de risco em que o requisito é obrigatório:
  - `L1+` → aplica-se a todas as aplicações (nível baixo, médio e elevado);
  - `L2+` → aplica-se a aplicações de risco médio ou elevado;
  - `L3` → aplica-se apenas a aplicações de risco elevado.
- Esta tabela deverá ser **complementada com os restantes domínios técnicos** (ex: `ACC`, `VAL`, `ENC`, `CFG`, etc.).
- Todos os identificadores devem estar presentes nas matrizes de aplicação  e podem ser referenciados em checklists e artefactos técnicos.

> 📌 Esta estrutura permite rastrear, validar e comprovar a aplicação prática de cada requisito, em qualquer projeto, de forma objetiva, proporcional e auditável.
> 📌 A validação descrita aqui deve ser integrada no ciclo de desenvolvimento, nas pipelines CI/CD, e mantida como evidência para controlo contínuo de conformidade.

