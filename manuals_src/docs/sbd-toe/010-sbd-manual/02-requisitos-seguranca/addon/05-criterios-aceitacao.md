---
description: Critérios de aceitação mínimos para cada requisito do catálogo base do
  capítulo, para apoio à validação, auditoria e integração em projetos.
id: criterios-aceitacao
tags:
- anexo
- auditoria
- tema:requisitos
- tipo-anexo
- tipo:aceitacao
- validacao
- validação
title: Critérios de Aceitação
---


<!--template: sbdtoe-addon -->

# 🛠️ Critérios de Aceitação dos Requisitos de Segurança

Este anexo apresenta, para cada requisito do Catálogo Base, o critério mínimo de aceitação recomendado, permitindo validação objetiva, integração em backlogs e auditorias, e articulação clara com equipas de desenvolvimento e segurança.

> Os critérios apresentados são genéricos e podem ser ajustados por organização/projeto, mantendo sempre o princípio de serem auditáveis e verificáveis.

---

## 🔐 AUT - Autenticação e Identidade

| ID      | Nome resumido            | Critério de aceitação                                  |
|---------|--------------------------|--------------------------------------------------------|
| AUT-001 | MFA obrigatório          | MFA está ativado; login sem segundo fator não é possível. |
| AUT-002 | Política de passwords    | Sistema rejeita passwords fracas; registo/teste evidencia bloqueio. |
| AUT-003 | Proteção brute force     | Conta bloqueada após N tentativas falhadas; logs evidenciam bloqueio. |
| AUT-004 | Revogação ativa sessão   | Logout expulsa sessão ativa; token inválido após logout. |
| AUT-005 | Expiração automática     | Sessão termina após tempo de inatividade pré-definido. |
| AUT-006 | Sem credenciais em claro | Auditoria confirma que senhas nunca são armazenadas/transmitidas em texto claro. |
| AUT-007 | Autenticação federada    | Fluxo federado funcional; login via SAML/OIDC testado. |
| AUT-008 | Step-up para ações sensíveis | Operações críticas requerem MFA extra; teste evidencia proteção. |
| AUT-009 | Reautenticação em alterações críticas | Alterações sensíveis exigem validação adicional (ex: senha atual). |
| AUT-010 | Alerta de acessos suspeitos | Acessos anómalos resultam em alerta/notificação ao utilizador. |

---

## 🔓 ACC - Controlo de Acesso

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| ACC-001 | Controlo de acesso RBAC  | Perfis e permissões mapeados; role limitado impede acesso a recursos restritos. |
| ACC-002 | Princípio do menor privilégio | Contas de utilizador não têm permissões desnecessárias; auditoria evidencia restrição. |
| ACC-003 | Bloqueio e auditoria de acessos ilegítimos | Tentativas de acesso não autorizado são bloqueadas e registadas. |
| ACC-004 | Separação de perfis      | Perfis de utilizador, admin e serviço são diferenciados; logs evidenciam ações distintas. |
| ACC-005 | Controlo de acesso a APIs e serviços | Endpoints requerem autenticação/autorização; chamadas não autenticadas são rejeitadas. |
| ACC-006 | Proteção de recursos sensíveis | Acesso não autorizado a dados críticos é impedido e registado. |
| ACC-007 | Validação do modelo de acesso | Modelo de ameaças e permissões revisto; documentação existe e está atualizada. |
| ACC-008 | Revogação em tempo real  | Remoção de acesso reflete-se imediatamente; teste de permissão falha após revogação. |
| ACC-009 | Autorização baseada em atributos (ABAC) | Decisão de acesso depende de atributos dinâmicos; logs evidenciam aplicação. |
| ACC-010 | Revisão periódica de permissões | Auditorias periódicas removem permissões obsoletas; registos de revisão mantidos. |

---

## 📈 LOG - Registo e Monitorização

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| LOG-001 | Registo de eventos críticos | Logs registam acessos, alterações e falhas de segurança críticas. |
| LOG-002 | Atributos mínimos em logs | Cada log inclui quem, quando, o quê e onde. |
| LOG-003 | Proteção de integridade e acesso aos logs | Logs não podem ser alterados por utilizadores comuns; proteção por permissões/assinatura. |
| LOG-004 | Análise periódica de logs | Existência de processo/documentação de análise periódica de logs. |
| LOG-005 | Retenção mínima dos logs | Logs mantidos pelo período definido em política. |
| LOG-006 | Envio para sistema centralizado | Eventos críticos enviados e registados em SIEM/monitorização central. |
| LOG-007 | Classificação e deteção de anomalias | Política de severidade definida; anomalias disparam alertas. |
| LOG-008 | Alarme em falhas do mecanismo de logging | Falhas de logging resultam em alertas/documentação. |
| LOG-009 | Logs suportam resposta a incidentes | Logs detalhados disponíveis para análise pós-incidente. |
| LOG-010 | Logging de eventos críticos de negócio | Eventos críticos do negócio são registados e rastreados. |

---

## 🕒 SES - Sessões e Estado

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| SES-001 | Expiração automática por inatividade | Sessão termina automaticamente após período de inatividade. |
| SES-002 | Logout manual e após alteração de credenciais | Logout manual termina todas as sessões ativas; alteração de senha invalida tokens anteriores. |
| SES-003 | Identificadores de sessão imprevisíveis | Tokens/sessões têm entropia elevada e não são previsíveis. |
| SES-004 | Transmissão segura dos tokens | Tokens transmitidos apenas por canais seguros (HTTPS, Secure/HttpOnly cookies). |
| SES-005 | Ligação da sessão ao contexto do cliente | Mudança de IP/user-agent termina sessão ou exige revalidação. |
| SES-006 | Revogação explícita da sessão | Sessão pode ser terminada a pedido; token fica inválido imediatamente. |
| SES-007 | Prevenção de sessões long-lived | TTL máximo configurado; sessões prolongadas não são possíveis. |
| SES-008 | Scope, TTL e revogação de tokens JWT | Tokens JWT incluem claims de âmbito, expiração, e podem ser revogados. |

---

## 🧹 VAL - Validação de Dados

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| VAL-001 | Validação geral de entradas externas | Inputs inválidos são rejeitados; logs evidenciam bloqueio. |
| VAL-002 | Uso de whitelists em vez de blacklists | Apenas valores explícitos/aceites são permitidos; teste evidencia rejeição de valores não permitidos. |
| VAL-003 | Validadores de esquema (ex: JSON/XML schema) | Payloads malformados são rejeitados automaticamente; logs de parsing disponíveis. |
| VAL-004 | Sanitização contra injeções | Inputs potencialmente perigosos são neutralizados; ataques resultam em falha controlada. |
| VAL-005 | Validação antes do uso interno | Dados são validados antes de uso em lógica de negócio ou gravação. |
| VAL-006 | Mensagens de erro seguras na validação | Erros não expõem lógica interna nem dados sensíveis. |
| VAL-007 | Testes automáticos contra entradas maliciosas | Testes automatizados cobrem XSS, SQLi, e outras injeções; resultados registados. |

---

## ❗ ERR - Gestão de Erros

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| ERR-001 | Erros não expõem dados sensíveis | Mensagens de erro não incluem dados sensíveis; logs internos detalhados, cliente vê mensagem abstrata. |
| ERR-002 | Mensagens genéricas no cliente | Cliente recebe sempre mensagem genérica (“Erro ao processar pedido”). |
| ERR-003 | Não revelar existência de recursos | Mensagens de erro são idênticas para recursos existentes/inexistentes. |
| ERR-004 | Mensagens localizadas e seguras | Mensagens são traduzidas e não incluem conteúdo executável. |
| ERR-005 | Gestão padronizada e centralizada | Framework de erro centraliza tratamento e logging de exceções. |
| ERR-006 | Testes automáticos para erros excessivos | Testes automatizados garantem que erros são tratados e não há fugas de informação. |
| ERR-007 | Logs de erro com ID de sessão/contexto seguro | Logs incluem apenas IDs pseudonimizados/contextuais; dados pessoais nunca registados. |

---

## ⚙️ CFG - Configuração Segura

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| CFG-001 | Debug e flags desativados em produção | Parâmetros de debug, trace, dev_mode desligados em produção. |
| CFG-002 | Separação de ambientes com validação automática | Deploys/testes apenas possíveis em ambientes segregados; logs evidenciam segregação. |
| CFG-003 | Sem hardcoded de parâmetros | Código fonte não contém segredos nem parâmetros sensíveis em claro. |
| CFG-004 | Configuração externa e com permissões controladas | Configuração é externa ao código e com permissões de acesso restritivas. |
| CFG-005 | Validação de configuração no arranque | Sistema falha arranque quando parâmetros obrigatórios estão em falta ou incorretos. |
| CFG-006 | Uso de cofres e gestão segura de segredos | Segredos só existem em cofres seguros; auditoria evidencia ausência local. |
| CFG-007 | Monitorização de drift de configuração | Alterações inesperadas em configuração disparam alertas/logs. |

---

## 🌐 API - Segurança de APIs

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| API-001 | Autenticação e autorização de chamadas API | Endpoints só aceitam chamadas autenticadas/autorizadas. |
| API-002 | Endpoints desnecessários ocultos ou removidos | Endpoints de debug/legacy não expostos; só disponíveis em ambientes de teste. |
| API-003 | Validação de input em APIs | Inputs malformados são rejeitados; logs registam tentativa. |
| API-004 | Rate limiting e deteção de abusos | Limite configurado e ativo; chamadas excessivas resultam em resposta 429 ou bloqueio. |
| API-005 | Proteção por TLS e certificados atualizados | Certificados válidos, canal TLS obrigatório; cabeçalhos seguros ativos. |
| API-006 | Verificação de SDKs e wrappers usados | SBOM gerado; dependências e versões documentadas; auditoria de licenças. |
| API-007 | Logging e auditoria de chamadas externas | Todas as chamadas externas registadas; logs contêm dados essenciais. |

---

## 📨 INT - Mensagens e Integrações

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| INT-001 | Validação de mensagens entre sistemas | Mensagens malformadas são rejeitadas/controladas. |
| INT-002 | Autenticação mútua ou tokens seguros | Integrações só aceites de fontes autenticadas; tokens válidos/revogados. |
| INT-003 | Transmissão cifrada com TLS | Todo o tráfego entre sistemas cifrado; verificação de TLS ativo. |
| INT-004 | Proibição de protocolos inseguros | Protocolos inseguros (HTTP, FTP) rejeitados ou redirecionados para seguro. |
| INT-005 | Assinatura e integridade de mensagens | Mensagens sensíveis assinadas/verificadas; logs evidenciam verificação. |
| INT-006 | Validação cruzada de origem e destino | Só origens/destinos autorizados aceites; logs de rejeição mantidos. |
| INT-007 | Monitorização e deteção de padrões anómalos | Comportamento anómalo dispara alertas; logs analisados periodicamente. |
| INT-008 | Revisão de segurança e contrato em integrações | Integrações documentadas; cláusulas contratuais e checklists disponíveis. |

---

## 📄 REQ - Definição de Requisitos

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| REQ-001 | Inclusão de requisitos de segurança | Requisitos explícitos em backlog/documentação; todos marcados. |
| REQ-002 | Revisão formal de segurança dos requisitos | Processo/documento de revisão de requisitos executado. |
| REQ-003 | Alinhamento com classificação de risco | Mapeamento entre requisitos e nível de criticidade disponível. |
| REQ-004 | Versionamento e gestão de requisitos | Histórico de alterações disponível; controlo de versões aplicado. |
| REQ-005 | Nova análise de ameaça após alteração de requisito | Alterações relevantes disparam nova análise de threat modeling. |
| REQ-006 | Rastreabilidade requisito → ameaça → teste | Matriz ou ferramenta demonstra ligação entre requisitos, ameaças e testes. |
| REQ-007 | Revisão iterativa com equipas | Alterações de requisitos discutidas, revistas e registadas periodicamente. |

---

## 🛠️ DST - Distribuição de Artefactos

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| DST-001 | Repositórios autenticados e auditáveis | Autenticação obrigatória e logs ativos para aceder a artefactos. |
| DST-002 | Aprovação para publicação pública | Publicação em registry público requer aprovação/documentação formal. |
| DST-003 | Assinatura digital ou checksum | Artefactos assinados ou validados por hash antes de publicação. |
| DST-004 | Inclusão de SBOM nos artefactos | SBOM gerado e anexado a cada release ou artefacto distribuído. |
| DST-005 | Acesso segregado por role e ambiente | Só utilizadores/automações autorizados acedem a binários relevantes. |
| DST-006 | Deploy apenas via pipeline validado | Artefactos só deployados por pipeline controlado/auditado. |
| DST-007 | Revogação e limpeza de artefactos comprometidos | Versões comprometidas são removidas e utilizadores notificados. |

---

## 💻 IDE - Ferramentas de Desenvolvimento

| ID      | Nome resumido            | Critério de aceitação                                   |
|---------|--------------------------|---------------------------------------------------------|
| IDE-001 | Ferramentas e IDEs autorizadas | Só ferramentas/IDEs aprovadas são usadas; lista mantida e atualizada. |
| IDE-002 | Atualização e gestão de vulnerabilidades | IDEs mantidas atualizadas; histórico de updates disponível. |
| IDE-003 | Auditoria de código gerado por ferramentas | Código gerado é revisto/auditado antes de produção. |
| IDE-004 | Extensões e plugins de fontes confiáveis | Só extensões de fontes reconhecidas são instaladas; logs de instalação disponíveis. |
| IDE-005 | Controlo de permissões de extensões | Permissões revistas e apenas as necessárias concedidas; execução sandboxed verificada. |
| IDE-006 | Evitar uso de ambientes locais sem controlo | Utilização de ambientes locais limitada e controlada; logs de rede/proxy disponíveis. |

---

## 📌 Nota Final

Os critérios de aceitação devem ser integrados nos processos de validação e auditoria dos projetos, podendo ser complementados por testes automáticos, revisões manuais ou artefactos de evidência documental.

> Para ligação direta ao requisito correspondente, consultar o [Catálogo Base de Requisitos](lista-requisitos-base).
