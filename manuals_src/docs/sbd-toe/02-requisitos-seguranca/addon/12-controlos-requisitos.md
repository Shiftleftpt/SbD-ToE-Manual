---
id: catalogo-requisitos
title: Catálogo de Requisitos Aplicacionais
description: Lista essencial de requisitos de segurança organizados por categoria e nível de risco
tags: [requisitos, catalogo, rastreabilidade, criticidade, ASVS]
---


# ✅ Validação de Requisitos de Segurança {requisitos-seguranca:addon:catalogo-requisitos}

Este documento define como cada requisito do `01-catalogo-requisitos.md` deve ser validado na prática, incluindo:

- O tipo de validação recomendada (automática, manual, runtime ou de configuração);
- A evidência esperada para auditoria;
- A proporcionalidade por nível de risco (L1, L2, L3).

> Este ficheiro complementa o catálogo de requisitos e permite verificar, por projeto, a sua implementação objetiva.

---

## 📚 Índice {requisitos-seguranca:addon:catalogo-requisitos#indice}

- [🔐 AUT — Autenticação e Identidade](#-aut--autenticacao-e-identidade)
- [🔓 ACC — Controlo de Acesso](#-acc--controlo-de-acesso)
- [📈 LOG — Registo e Monitorização](#-log--registo-e-monitorizacao)
- [🕒 SES — Sessões e Estado](#-ses--sessoes-e-estado)
- [🧹 VAL — Validação de Dados](#-val--validacao-de-dados)
- [❗ ERR — Gestão de Erros](#-err--gestao-de-erros)
- [⚙️ CFG — Configuração Segura](#-cfg--configuracao-segura)
- [🌐 API — Segurança de APIs](#-api--seguranca-de-apis)
- [📨 INT — Mensagens e Integrações](#-int--mensagens-e-integracoes)
- [📄 REQ — Definição de Requisitos](#-req--definicao-de-requisitos)
- [🛠️ DST — Distribuição de Artefactos](#-dst--distribuicao-de-artefactos)
- [💻 IDE — Ferramentas de Desenvolvimento](#-ide--ferramentas-de-desenvolvimento)

---

## 🔐 AUT — Autenticação e Identidade {requisitos-seguranca:addon:catalogo-requisitos#aut__autenticacao_e_identidade}

| ID       | Tag                 | Nome resumido                             | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                   |
|----------|---------------------|--------------------------------------------|--------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| AUT-001  | SEC-Lx-AUT-MFA      | MFA obrigatório                            | L2+    | Verificar exigência de MFA em ambiente real. Tentar login sem segundo fator.         | Captura de ecrã ou log de falha de autenticação sem MFA.             |
| AUT-002  | SEC-Lx-AUT-PWD      | Política de passwords                      | L1+    | Rever política de complexidade e comprimento. Tentar criação com pwd fraca.          | Screenshot de política, registo de falha em tentativa inválida.      |
| AUT-003  | SEC-Lx-AUT-BF       | Proteção contra brute force                | L1+    | Simular múltiplas tentativas falhadas. Verificar lockout ou throttling.              | Log de bloqueio automático ou fallback CAPTCHA.                      |
| AUT-004  | SEC-Lx-AUT-LOGOUT   | Revogação ativa de sessões                 | L1+    | Efetuar logout global. Verificar invalidade de tokens anteriores.                    | Log de sessão revogada, teste de token inválido após logout.         |
| AUT-005  | SEC-Lx-AUT-TIMEOUT  | Expiração automática de sessão             | L1+    | Configurar tempo de inatividade. Aguardar e tentar continuar sessão.                 | Screenshot de timeout, logs de expiração.                            |
| AUT-006  | SEC-Lx-AUT-PLAIN    | Proibição de credenciais em claro          | L1+    | Rever configurações e dumps. Inspecionar comunicação e storage.                      | Evidência de encriptação, ausência de senhas em ficheiros.           |
| AUT-007  | SEC-L2-AUT-FEDERADA | Suporte a autenticação federada            | L2+    | Verificar integração SAML/OIDC com provedor externo.                                 | Captura de ecrã do fluxo de login federado.                          |
| AUT-008  | SEC-L2-AUT-STEPUP   | Step-up para ações sensíveis               | L2+    | Executar ação sensível. Confirmar reautenticação obrigatória.                        | Screenshot da exigência extra. Log de revalidação.                   |
| AUT-009  | SEC-Lx-AUT-REAUTH   | Reautenticação para alterações críticas    | L1+    | Tentar alterar senha ou email. Confirmar pedido de senha atual.                      | Captura do pedido de revalidação. Log de operação condicionada.      |
| AUT-010  | SEC-L2-AUT-ALERT    | Alerta de acessos suspeitos                | L2+    | Simular acesso suspeito. Verificar envio de alerta ao utilizador.                   | Log de alerta. Screenshot de notificação enviada.                    |

---

## 🔓 ACC — Controlo de Acesso {requisitos-seguranca:addon:catalogo-requisitos#acc__controlo_de_acesso}

| ID       | Tag                  | Nome resumido                             | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                     |
|----------|----------------------|--------------------------------------------|--------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| ACC-001  | SEC-Lx-ACC-RBAC      | Controlo de acesso RBAC                    | L1+    | Rever modelo de permissões. Verificar mapeamento por função e restrição efetiva.      | Screenshot da matriz de permissões. Output de teste com role limitado. |
| ACC-002  | SEC-Lx-ACC-LEASTPRIV | Princípio do menor privilégio              | L1+    | Rever contas com permissões elevadas. Testar acesso com utilizadores normais.         | Listagem de permissões. Resultado de teste com acesso negado.          |
| ACC-003  | SEC-Lx-ACC-BLOCK     | Bloqueio e auditoria de acessos ilegítimos | L1+    | Tentar acesso não autorizado. Confirmar rejeição e log gerado.                        | Log de tentativa bloqueada. Código de erro apropriado.                 |
| ACC-004  | SEC-Lx-ACC-ROLES     | Separação de perfis                        | L1+    | Validar diferenciação entre utilizadores, admins e serviços.                          | Screenshot de perfis. Logs de ações distintas por perfil.              |
| ACC-005  | SEC-Lx-ACC-API       | Controlo de acesso a APIs e serviços       | L1+    | Tentar invocar endpoint interno sem token. Rever middleware de autorização.           | Código de erro 403 ou 401. Log de bloqueio.                            |
| ACC-006  | SEC-Lx-ACC-RESOURCE  | Proteção de recursos sensíveis             | L1+    | Tentar aceder a recursos sem permissão. Validar negação e logging.                    | Screenshot de resposta de erro. Log com contexto de acesso.            |
| ACC-007  | SEC-L2-ACC-THREATMOD | Validação do modelo de acesso              | L2+    | Rever documentação de threat modeling. Validar mapeamento de ameaças a permissões.    | Documento de modelação. Registos de revisão de segurança.             |
| ACC-008  | SEC-Lx-ACC-REVOKE    | Revogação em tempo real                    | L1+    | Remover acesso de utilizador ativo. Testar falha imediata de ação autorizada antes.   | Log de revogação e tentativa falhada após remoção.                    |
| ACC-009  | SEC-L3-ACC-ABAC      | Autorização baseada em atributos (ABAC)    | L3     | Rever política de autorização dinâmica. Validar decisões condicionadas a atributos.    | Logs de decisão ABAC. Screenshot de regras condicionais.              |
| ACC-010  | SEC-L2-ACC-REVIEW    | Revisão periódica de permissões            | L2+    | Consultar registos de auditoria de permissões. Validar ciclo de revisão documentado. | Registo formal de revisão. Evidência de permissões removidas.         |
---
## 📈 LOG — Registo e Monitorização {requisitos-seguranca:addon:catalogo-requisitos#log__registo_e_monitorizacao}

| ID       | Tag                  | Nome resumido                                | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                    |
|----------|----------------------|-----------------------------------------------|--------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| LOG-001  | SEC-Lx-LOG-EVENTOS   | Registo de eventos críticos                   | L1+    | Simular login, alteração de dados e falha de acesso. Verificar logs gerados.          | Logs com timestamp, utilizador e ação registada.                      |
| LOG-002  | SEC-Lx-LOG-DETALHE   | Atributos mínimos em logs                     | L1+    | Rever logs: devem conter quem, quando, o quê e onde.                                  | Exemplo real de log com campos completos.                             |
| LOG-003  | SEC-Lx-LOG-INTEGRIDADE| Proteção de integridade e acesso aos logs     | L1+    | Tentar alterar ficheiro de log. Rever permissões de escrita.                          | Evidência de proteção (ex: read-only, assinatura).                    |
| LOG-004  | SEC-L2-LOG-ANALISE   | Análise periódica de logs                     | L2+    | Verificar existência de cron job ou integração com SIEM.                              | Log de execução de análise. Screenshot do SIEM.                       |
| LOG-005  | SEC-Lx-LOG-RETENCAO  | Retenção mínima dos logs                      | L1+    | Consultar política de retenção e configurações do sistema de logs.                    | Política aprovada. Screenshot da configuração (ex: 90 dias).          |
| LOG-006  | SEC-L2-LOG-SIEM      | Envio para sistema centralizado               | L2+    | Confirmar integração com SIEM. Verificar logs recebidos.                             | Screenshot de eventos recebidos pelo SIEM.                            |
| LOG-007  | SEC-L2-LOG-SEVERIDADE| Classificação e deteção de anomalias          | L2+    | Rever política de classificação. Simular evento anómalo e avaliar deteção.            | Alerta gerado. Screenshot da configuração de severidade.              |
| LOG-008  | SEC-L2-LOG-ALARME    | Alarme em falhas do mecanismo de logging      | L2+    | Interromper mecanismo de logging. Confirmar envio de alerta.                          | Log de alarme ou e-mail enviado. Screenshot da falha monitorizada.    |
| LOG-009  | SEC-L2-LOG-INCIDENTE | Logs suportam resposta a incidentes           | L2+    | Rever planos de resposta. Verificar integração de logs no fluxo de resposta.          | Exemplo de incidente com logs associados.                             |
| LOG-010  | SEC-L3-LOG-NEGOCIO   | Logging de eventos críticos de negócio        | L3     | Identificar eventos críticos (ex: submissão de IRS). Confirmar registo no sistema.    | Log contendo o evento de negócio e respetivo contexto.                |
---
## 🕒 SES — Sessões e Estado {requisitos-seguranca:addon:catalogo-requisitos#ses__sessoes_e_estado}

| ID       | Tag                   | Nome resumido                              | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|---------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| SES-001  | SEC-Lx-SES-TIMEOUT    | Expiração automática por inatividade        | L1+    | Iniciar sessão e aguardar tempo de inatividade. Confirmar encerramento automático.    | Log de encerramento. Screenshot do timeout ao retomar sessão.            |
| SES-002  | SEC-Lx-SES-LOGOUT     | Logout manual e após alteração de credenciais | L1+    | Realizar logout e tentar reusar sessão anterior. Alterar senha e verificar invalidação. | Tokens inválidos. Log de logout. Screenshot do fluxo de revalidação.    |
| SES-003  | SEC-Lx-SES-ENTROPIA   | Identificadores de sessão imprevisíveis     | L1+    | Capturar vários tokens de sessão. Avaliar entropia e aleatoriedade.                   | Amostra de tokens. Resultado de análise de entropia.                     |
| SES-004  | SEC-Lx-SES-TRANSPORTE | Transmissão segura dos tokens               | L1+    | Verificar headers e cookies. Confirmar uso de HTTPS e flags Secure/HttpOnly.          | Captura de cabeçalhos. Configuração do servidor ou aplicação.            |
| SES-005  | SEC-L2-SES-CONTEXTO   | Ligação da sessão ao contexto do cliente    | L2+    | Alterar IP ou user-agent a meio da sessão. Verificar deteção de anomalia.             | Log de encerramento automático. Screenshot do evento de segurança.       |
| SES-006  | SEC-Lx-SES-REVOGACAO  | Revogação explícita da sessão               | L1+    | Logout manual ou revogação por administração. Tentar reutilizar token anterior.       | Log de revogação. Resposta 401 a pedidos subsequentes.                   |
| SES-007  | SEC-L2-SES-DURACAO    | Prevenção de sessões long-lived             | L2+    | Verificar configuração de TTL para sessões. Rever política de refresh.                | Configuração de tokens. Screenshot da definição de tempo.                |
| SES-008  | SEC-L2-SES-JWT        | Scope, TTL e revogação de tokens JWT        | L2+    | Rever payload dos tokens. Confirmar presença de claims como `exp`, `aud`, `scope`.    | Exemplo de token com claims definidos. Política de revogação ativa.      |
---
## 🧹 VAL — Validação de Dados {requisitos-seguranca:addon:catalogo-requisitos#val__validacao_de_dados}

| ID       | Tag                   | Nome resumido                                     | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|----------------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| VAL-001  | SEC-Lx-VAL-VALIDACAO  | Validação geral de entradas externas              | L1+    | Enviar inputs inválidos (tipos, tamanhos, formatos). Confirmar bloqueio.              | Log de rejeição. Screenshot de resposta com erro de validação.           |
| VAL-002  | SEC-Lx-VAL-WHITELIST  | Uso de whitelists em vez de blacklists            | L1+    | Rever expressões regulares e listas aplicadas. Verificar política de aceitação.       | Código validado. Screenshot das regras aplicadas.                        |
| VAL-003  | SEC-L2-VAL-SCHEMA     | Validadores de esquema (ex: JSON/XML schema)      | L2+    | Submeter payloads malformados. Confirmar rejeição automática.                         | Logs de erro. Screenshot do erro de parsing conforme esquema.            |
| VAL-004  | SEC-Lx-VAL-SANITIZACAO| Sanitização contra injeções                       | L1+    | Injetar payloads suspeitos (ex: SQL, JS). Confirmar neutralização ou falha controlada. | Log de input rejeitado. Comportamento não executado.                     |
| VAL-005  | SEC-Lx-VAL-ORDEM      | Validação antes do uso interno                    | L1+    | Rever fluxo de dados. Confirmar validação antes de gravação ou lógica de negócio.     | Código de validação no início da função. Log de erro controlado.         |
| VAL-006  | SEC-Lx-VAL-MENSAGEM   | Mensagens de erro seguras na validação            | L1+    | Submeter input inválido. Verificar que resposta não expõe lógica interna.             | Mensagem genérica. Log com detalhe técnico.                              |
| VAL-007  | SEC-L2-VAL-TESTES     | Testes automáticos contra entradas maliciosas     | L2+    | Rever cobertura de testes automatizados para XSS, SQLi, etc.                          | Relatório de testes. Exemplo de caso de teste parametrizado.             |
---
## ❗ ERR — Gestão de Erros {requisitos-seguranca:addon:catalogo-requisitos#err__gestao_de_erros}

| ID       | Tag                   | Nome resumido                                   | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|--------------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ERR-001  | SEC-Lx-ERR-EXPOSICAO  | Erros não expõem dados sensíveis                | L1+    | Forçar erro interno (ex: exceção). Verificar resposta e logs.                         | Mensagem genérica no cliente. Stack trace apenas em log interno.         |
| ERR-002  | SEC-Lx-ERR-MENSAGEM   | Mensagens genéricas no cliente                  | L1+    | Submeter input inválido. Verificar feedback ao utilizador.                            | Mensagem abstrata (ex: "Erro ao processar pedido").                      |
| ERR-003  | SEC-Lx-ERR-ENUMERACAO | Não revelar existência de recursos              | L1+    | Tentar login com utilizador inexistente. Verificar resposta idêntica.                 | Resposta genérica (ex: "Credenciais inválidas"). Log diferenciado.       |
| ERR-004  | SEC-Lx-ERR-LOCALIZACAO| Mensagens localizadas e seguras                 | L1+    | Alterar idioma do sistema. Verificar traduções e ausência de conteúdo injetável.      | Mensagens traduzidas. Logs com mensagens sem código executável.          |
| ERR-005  | SEC-L2-ERR-CENTRAL    | Gestão padronizada e centralizada               | L2+    | Rever framework de erro. Confirmar tratamento unificado de exceções.                  | Diagrama ou código da camada central de tratamento de erros.             |
| ERR-006  | SEC-L2-ERR-TESTES     | Testes automáticos para erros excessivos        | L2+    | Rever testes automatizados para erros malformados.                                    | Casos de teste com asserts sobre mensagens seguras.                      |
| ERR-007  | SEC-L2-ERR-LOG        | Logs de erro com ID de sessão/contexto seguro   | L2+    | Verificar conteúdo dos logs. Confirmar que ID de sessão não expõe dados pessoais.     | Logs com IDs pseudonimizados. Ausência de dados sensíveis.               |
---
## ⚙️ CFG — Configuração Segura {requisitos-seguranca:addon:catalogo-requisitos#cfg__configuracao_segura}

| ID       | Tag                   | Nome resumido                                    | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|---------------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| CFG-001  | SEC-Lx-CFG-DEBUG      | Debug e flags desativados em produção             | L1+    | Verificar ficheiros de configuração e variáveis de ambiente.                          | Valor `false` ou `off` em `debug`, `trace`, `dev_mode`.                  |
| CFG-002  | SEC-Lx-CFG-AMBIENTES  | Separação de ambientes com validação automática   | L1+    | Rever pipelines CI/CD. Confirmar validação e isolamento por ambiente.                 | YAML ou script de validação de ambiente. Logs de deploy segregado.       |
| CFG-003  | SEC-Lx-CFG-HARDCODE   | Sem hardcoded de parâmetros                       | L1+    | Rever código fonte e variáveis embutidas.                                             | Ausência de valores sensíveis no repositório. Uso de placeholders.       |
| CFG-004  | SEC-Lx-CFG-EXTERNO    | Configuração externa e com permissões controladas | L1+    | Verificar uso de ficheiros `.env`, `config.yaml`, etc.                                | Screenshot de ficheiros externos com permissões corretas.                |
| CFG-005  | SEC-L2-CFG-VALIDACAO  | Validação de configuração no arranque            | L2+    | Parâmetros inválidos devem impedir arranque. Confirmar mensagens claras.              | Log de erro e falha controlada. Código de verificação no arranque.       |
| CFG-006  | SEC-L2-CFG-SEGREDOS   | Uso de cofres e gestão segura de segredos         | L2+    | Confirmar integração com Vault ou equivalente. Verificar ausência de segredos locais. | Screenshot da chamada ao cofre. Logs sem segredos.                       |
| CFG-007  | SEC-L3-CFG-DRIFT      | Monitorização de drift de configuração            | L3     | Introduzir alteração em runtime. Verificar deteção e alerta.                          | Alerta de alteração inesperada. Log de evento de drift.                  |
---

## 🌐 API — Segurança de APIs {requisitos-seguranca:addon:catalogo-requisitos#api__seguranca_de_apis}

| ID       | Tag                   | Nome resumido                                   | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|--------------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| API-001  | SEC-Lx-API-AUTHZ      | Autenticação e autorização de chamadas API      | L1+    | Tentar chamadas sem autenticação/autorização. Confirmar rejeição.                     | Resposta 401/403. Logs de acesso negado.                                |
| API-002  | SEC-Lx-API-ENDPOINTS  | Endpoints desnecessários ocultos ou removidos   | L1+    | Listar endpoints expostos. Verificar ausência de debug ou rotas legacy.               | Output de `swagger` ou rota listada sem endpoints sensíveis.             |
| API-003  | SEC-Lx-API-INPUT      | Validação de input em APIs                      | L1+    | Submeter JSON/XML inválido. Confirmar rejeição.                                       | Log de erro. Resposta com código 400 e mensagem de validação.            |
| API-004  | SEC-L2-API-RATELIMIT  | Rate limiting e deteção de abusos               | L2+    | Efetuar chamadas repetidas. Confirmar throttling ou bloqueio.                         | Resposta 429. Log com contagem de chamadas.                              |
| API-005  | SEC-Lx-API-TLS        | Proteção por TLS e certificados atualizados     | L1+    | Verificar headers e certificados em uso.                                              | Certificado válido. Headers com `Strict-Transport-Security`.             |
| API-006  | SEC-Lx-API-SDK        | Verificação de SDKs e wrappers usados           | L1+    | Auditar dependências usadas por APIs. Verificar versões e licenças.                   | SBOM da API. Logs de scans de dependências.                              |
| API-007  | SEC-L2-API-LOG        | Logging e auditoria de chamadas externas        | L2+    | Efetuar chamadas a serviços externos. Verificar logging detalhado e métricas.         | Log de chamadas externas. Dashboard com métricas.                        |
---

## 📨 INT — Mensagens e Integrações {requisitos-seguranca:addon:catalogo-requisitos#int__mensagens_e_integracoes}

| ID       | Tag                   | Nome resumido                                       | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|------------------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| INT-001  | SEC-Lx-INT-VALIDACAO  | Validação de mensagens entre sistemas               | L1+    | Enviar mensagens malformadas. Confirmar rejeição com erro controlado.                 | Log de rejeição. Resposta com erro de parsing.                          |
| INT-002  | SEC-Lx-INT-AUTH       | Autenticação mútua ou tokens seguros                | L1+    | Verificar uso de mTLS, JWTs ou tokens com validade.                                   | Header de autenticação. Configuração segura.                            |
| INT-003  | SEC-Lx-INT-TLS        | Transmissão cifrada com TLS                         | L1+    | Inspecionar canal de comunicação. Confirmar TLS 1.2+.                                 | Output de `curl -v`. Certificado válido.                                |
| INT-004  | SEC-Lx-INT-PROTOCOLOS | Proibição de protocolos inseguros                   | L1+    | Tentar uso de HTTP ou FTP. Confirmar bloqueio ou redirecionamento para HTTPS/SFTP.    | Log de rejeição. Política de rede ou headers seguros.                   |
| INT-005  | SEC-L2-INT-ASSINATURA | Assinatura e integridade de mensagens               | L2+    | Verificar presença de assinatura digital (ex: JWS, XML-SIG).                          | Exemplo de mensagem assinada. Código de verificação da assinatura.      |
| INT-006  | SEC-L2-INT-WHITELIST  | Validação cruzada de origem e destino               | L2+    | Alterar origem do pedido (ex: spoof de domínio). Confirmar rejeição.                  | Lista de domínios autorizados. Log de tentativa rejeitada.              |
| INT-007  | SEC-L3-INT-MONITORIZA | Monitorização e deteção de padrões anómalos         | L3     | Simular tráfego atípico. Confirmar alerta ou deteção automatizada.                   | Log de evento anómalo. Alerta no SIEM.                                  |
| INT-008  | SEC-L3-INT-TERCEIROS  | Revisão de segurança e contrato em integrações      | L3     | Verificar existência de cláusulas contratuais e checklist de segurança aplicado.       | Contrato com cláusula de segurança. Registo de revisão técnica.         |
---
## 📄 REQ — Definição de Requisitos {requisitos-seguranca:addon:catalogo-requisitos#req__definicao_de_requisitos}

| ID       | Tag                   | Nome resumido                                      | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|-----------------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| REQ-001  | SEC-Lx-REQ-INCLUSAO   | Inclusão de requisitos de segurança                 | L1+    | Rever user stories e especificações. Confirmar presença explícita de requisitos.       | Backlog com requisitos marcados. Documento com secção de segurança.     |
| REQ-002  | SEC-Lx-REQ-REVISAO    | Revisão formal de segurança dos requisitos          | L1+    | Verificar processo de análise em fase de planeamento.                                 | Registo de reunião de revisão. Checklist preenchido.                    |
| REQ-003  | SEC-Lx-REQ-ALINHAMENTO| Alinhamento com classificação de risco              | L1+    | Comparar requisitos definidos com nível de risco da aplicação (L1, L2, L3).            | Mapeamento entre requisitos e criticidade.                              |
| REQ-004  | SEC-Lx-REQ-VERSIONAMENTO | Versionamento e gestão de requisitos             | L1+    | Confirmar existência de repositório com histórico de alterações.                      | Histórico de commits. Controlos de versão visíveis.                     |
| REQ-005  | SEC-L2-REQ-THREATS    | Nova análise de ameaça após alteração de requisito  | L2+    | Modificar requisito. Confirmar disparo de nova análise de ameaça.                     | Registo de threat modeling associado à alteração.                       |
| REQ-006  | SEC-L2-REQ-RASTREIO   | Rastreabilidade requisito → ameaça → teste          | L2+    | Verificar matriz de rastreabilidade. Confirmar ligação entre artefactos.              | Documento ou ferramenta com relação 3 pontos.                           |
| REQ-007  | SEC-L2-REQ-ITERACAO   | Revisão iterativa com equipas                       | L2+    | Confirmar iteração contínua no ciclo de sprint ou equivalente.                        | Logs de reuniões. Backlog com alterações versionadas.                   |
---
## 🛠️ DST — Distribuição de Artefactos {requisitos-seguranca:addon:catalogo-requisitos#dst__distribuicao_de_artefactos}

| ID       | Tag                   | Nome resumido                                      | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|-----------------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| DST-001  | SEC-Lx-DST-REPO       | Repositórios autenticados e auditáveis             | L1+    | Verificar configurações de repositório (ex: Nexus, Artifactory).                      | Screenshot de autenticação obrigatória. Logs de acesso configurados.    |
| DST-002  | SEC-L2-DST-APROVACAO  | Aprovação para publicação pública                  | L2+    | Simular publicação em registry público. Confirmar necessidade de aprovação prévia.    | Workflow de aprovação. Log de revisão antes da publicação.              |
| DST-003  | SEC-L2-DST-ASSINATURA | Assinatura digital ou checksum                     | L2+    | Rever processo de build. Confirmar assinatura automática ou validação por hash.       | Artefacto com assinatura. Script de verificação de integridade.         |
| DST-004  | SEC-L2-DST-SBOM       | Inclusão de SBOM nos artefactos                    | L2+    | Verificar se SBOM é gerado e incluído no pipeline.                                    | Ficheiro SBOM anexo. Log de geração durante CI/CD.                      |
| DST-005  | SEC-L2-DST-SEGREGA    | Acesso segregado por role e ambiente               | L2+    | Verificar permissões de acesso aos binários.                                          | Políticas RBAC aplicadas. Logs de acesso controlado.                    |
| DST-006  | SEC-L2-DST-PIPELINE   | Deploy apenas via pipeline validado                | L2+    | Simular bypass manual. Confirmar rejeição.                                            | Log de execução do pipeline como única fonte de deploy.                 |
| DST-007  | SEC-Lx-DST-REVOGACAO  | Revogação e limpeza de artefactos comprometidos    | L1+    | Publicar versão comprometida (ex: com CVE). Confirmar processo de remoção e alerta.   | Histórico de remoção. Notificação de revogação.                         |
---

## 💻 IDE — Ferramentas de Desenvolvimento {requisitos-seguranca:addon:catalogo-requisitos#ide__ferramentas_de_desenvolvimento}

| ID       | Tag                   | Nome resumido                                      | Nível | Validação Recomendada                                                                 | Evidência Esperada                                                       |
|----------|-----------------------|-----------------------------------------------------|--------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| IDE-001  | SEC-Lx-IDE-AUTORIZADA | Ferramentas e IDEs autorizadas                     | L1+    | Rever lista de ferramentas permitidas. Verificar uso fora da whitelist.               | Documento de ferramentas aprovadas. Screenshot de IDE em uso.           |
| IDE-002  | SEC-Lx-IDE-ATUALIZADA | Atualização e gestão de vulnerabilidades           | L1+    | Verificar versão atual das IDEs. Avaliar presença de atualizações em falta.           | Página “About” da IDE. Log de gestão de updates.                        |
| IDE-003  | SEC-L2-IDE-CODIGO     | Auditoria de código gerado por ferramentas         | L2+    | Usar scaffolding/boilerplate. Confirmar revisão de código resultante.                 | Pull request com validação. Comentários de revisão.                     |
| IDE-004  | SEC-Lx-IDE-FONTES     | Extensões e plugins de fontes confiáveis           | L1+    | Rever marketplace ou fonte de instalação. Validar assinatura ou origem.               | Screenshot de instalação. Fonte oficial listada.                        |
| IDE-005  | SEC-L2-IDE-PERMISSOES | Controlo de permissões de extensões                | L2+    | Analisar permissões concedidas. Verificar execução sandboxed.                         | Screenshot de permissões. Registos de sandboxing.                       |
| IDE-006  | SEC-L2-IDE-ISOLAMENTO | Evitar uso de ambientes locais sem controlo        | L2+    | Verificar rede, proxy, DNS local em IDEs. Confirmar isolamento ou controlo.           | Log de rede. Política de proxy forçado.                                 |
---

## 📌 Nota Final {requisitos-seguranca:addon:catalogo-requisitos#nota_final}

Este catálogo de validação cobre de forma robusta a generalidade das aplicações empresariais, web e cloud-native. No entanto, aplicações com perfis técnicos específicos — como sistemas embarcados (embedded), IoT, SCADA, mobile, aplicações médicas ou sistemas de tempo real — poderão necessitar de requisitos adicionais e validações específicas.

Algumas fontes recomendadas para consulta e curadoria desses requisitos específicos incluem:

- [OWASP Mobile Security Testing Guide (MSTG)](https://owasp.org/www-project-mobile-security-testing-guide/)
- [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/)
- [IEC 62443 — Segurança em Sistemas Industriais e SCADA](https://webstore.iec.ch/publication/7033)
- [NIST SP 800-213 — IoT Device Cybersecurity Guidance](https://csrc.nist.gov/publications/detail/sp/800-213/final)
- [BSIMM for Embedded & Device Software](https://www.bsimm.com/)

Durante a definição e manutenção contínua deste catálogo e respetivo documento de validação, devem ser mantidos os mesmos padrões de qualidade, estrutura e rastreabilidade definidos neste capítulo:

- Organização por grupo funcional com IDs únicos;
- Proporcionalidade por nível de risco (L1, L2, L3);
- Tabelas normalizadas com validação recomendada e evidência esperada;
- Ligação clara ao catálogo `01-catalogo-requisitos.md`.

> A consistência entre catálogo e validação é fundamental para garantir rastreabilidade, auditabilidade e alinhamento com o modelo SbD-ToE.

