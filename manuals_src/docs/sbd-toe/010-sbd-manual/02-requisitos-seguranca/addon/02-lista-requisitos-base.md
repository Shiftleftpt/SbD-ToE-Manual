---
description: Matriz síntese dos requisitos aplicacionais por nível de risco (L1–L3),
  anexo para consulta rápida e referência.
id: lista-requisitos-base
tags:
- anexo
- criticidade
- tema:requisitos
- tema:resumo
- tipo-anexo
- tipo-catalogo
- tipo:catalogo
title: Compilação do Catálogo Requisitos de Segurança
---


> Importante:
>
> Recomenda-se vivamente a **curadoria e adaptação destes requisitos por cada organização e projeto**, usando as mesmas fontes como referência, para garantir relevância, proporcionalidade e alinhamento com o contexto técnico e de risco.
>
> Esta lista serve como **ponto de partida** e não substitui uma análise contextualizada e iterativa dos requisitos de segurança aplicáveis ao sistema/projeto específico.
> 
> Quando não existem requistos de segurança, usem-se estes!

---

## 🔐 AUT - Autenticação e Identidade

| ID      | Nome resumido                          | L1 | L2 | L3 |
|---------|----------------------------------------|----|----|----|
| AUT-001 | MFA obrigatório                        |    | X  | X  |
| AUT-002 | Política de passwords                  | X  | X  | X  |
| AUT-003 | Proteção contra brute force            | X  | X  | X  |
| AUT-004 | Revogação ativa de sessões             | X  | X  | X  |
| AUT-005 | Expiração automática de sessão         | X  | X  | X  |
| AUT-006 | Proibição de credenciais em claro      | X  | X  | X  |
| AUT-007 | Suporte a autenticação federada        |    | X  | X  |
| AUT-008 | Step-up para ações sensíveis           |    | X  | X  |
| AUT-009 | Reautenticação para alterações críticas| X  | X  | X  |
| AUT-010 | Alerta de acessos suspeitos            |    | X  | X  |

---

## 🔓 ACC - Controlo de Acesso

| ID      | Nome resumido                          | L1 | L2 | L3 |
|---------|----------------------------------------|----|----|----|
| ACC-001 | Controlo de acesso RBAC                | X  | X  | X  |
| ACC-002 | Princípio do menor privilégio          | X  | X  | X  |
| ACC-003 | Bloqueio e auditoria de acessos ilegítimos | X | X | X |
| ACC-004 | Separação de perfis                    | X  | X  | X  |
| ACC-005 | Controlo de acesso a APIs e serviços   | X  | X  | X  |
| ACC-006 | Proteção de recursos sensíveis         | X  | X  | X  |
| ACC-007 | Validação do modelo de acesso          |    | X  | X  |
| ACC-008 | Revogação em tempo real                | X  | X  | X  |
| ACC-009 | Autorização baseada em atributos (ABAC)|    |    | X  |
| ACC-010 | Revisão periódica de permissões        |    | X  | X  |

---

## 📈 LOG - Registo e Monitorização

| ID      | Nome resumido                          | L1 | L2 | L3 |
|---------|----------------------------------------|----|----|----|
| LOG-001 | Registo de eventos críticos            | X  | X  | X  |
| LOG-002 | Atributos mínimos em logs              | X  | X  | X  |
| LOG-003 | Proteção de integridade e acesso aos logs | X | X | X |
| LOG-004 | Análise periódica de logs              |    | X  | X  |
| LOG-005 | Retenção mínima dos logs               | X  | X  | X  |
| LOG-006 | Envio para sistema centralizado        |    | X  | X  |
| LOG-007 | Classificação e deteção de anomalias   |    | X  | X  |
| LOG-008 | Alarme em falhas do mecanismo de logging|   | X  | X  |
| LOG-009 | Logs suportam resposta a incidentes    |    | X  | X  |
| LOG-010 | Logging de eventos críticos de negócio |    |    | X  |

---

## 🕒 SES - Sessões e Estado

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| SES-001 | Expiração automática por inatividade          | X  | X  | X  |
| SES-002 | Logout manual e após alteração de credenciais | X  | X  | X  |
| SES-003 | Identificadores de sessão imprevisíveis       | X  | X  | X  |
| SES-004 | Transmissão segura dos tokens                 | X  | X  | X  |
| SES-005 | Ligação da sessão ao contexto do cliente      |    | X  | X  |
| SES-006 | Revogação explícita da sessão                 | X  | X  | X  |
| SES-007 | Prevenção de sessões long-lived               |    | X  | X  |
| SES-008 | Scope, TTL e revogação de tokens JWT          |    | X  | X  |

---

## 🧹 VAL - Validação de Dados

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| VAL-001 | Validação geral de entradas externas          | X  | X  | X  |
| VAL-002 | Uso de whitelists em vez de blacklists        | X  | X  | X  |
| VAL-003 | Validadores de esquema (ex: JSON/XML schema)  |    | X  | X  |
| VAL-004 | Sanitização contra injeções                   | X  | X  | X  |
| VAL-005 | Validação antes do uso interno                | X  | X  | X  |
| VAL-006 | Mensagens de erro seguras na validação        | X  | X  | X  |
| VAL-007 | Testes automáticos contra entradas maliciosas |    | X  | X  |

---

## ❗ ERR - Gestão de Erros

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| ERR-001 | Erros não expõem dados sensíveis              | X  | X  | X  |
| ERR-002 | Mensagens genéricas no cliente                | X  | X  | X  |
| ERR-003 | Não revelar existência de recursos            | X  | X  | X  |
| ERR-004 | Mensagens localizadas e seguras               | X  | X  | X  |
| ERR-005 | Gestão padronizada e centralizada             |    | X  | X  |
| ERR-006 | Testes automáticos para erros excessivos      |    | X  | X  |
| ERR-007 | Logs de erro com ID de sessão/contexto seguro |    | X  | X  |

---

## ⚙️ CFG - Configuração Segura

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| CFG-001 | Debug e flags desativados em produção         | X  | X  | X  |
| CFG-002 | Separação de ambientes com validação automática| X | X  | X  |
| CFG-003 | Sem hardcoded de parâmetros                   | X  | X  | X  |
| CFG-004 | Configuração externa e com permissões controladas | X | X | X |
| CFG-005 | Validação de configuração no arranque         |    | X  | X  |
| CFG-006 | Uso de cofres e gestão segura de segredos     |    | X  | X  |
| CFG-007 | Monitorização de drift de configuração        |    |    | X  |

---

## 🌐 API - Segurança de APIs

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| API-001 | Autenticação e autorização de chamadas API    | X  | X  | X  |
| API-002 | Endpoints desnecessários ocultos ou removidos | X  | X  | X  |
| API-003 | Validação de input em APIs                    | X  | X  | X  |
| API-004 | Rate limiting e deteção de abusos             |    | X  | X  |
| API-005 | Proteção por TLS e certificados atualizados   | X  | X  | X  |
| API-006 | Verificação de SDKs e wrappers usados         | X  | X  | X  |
| API-007 | Logging e auditoria de chamadas externas      |    | X  | X  |

---

## 📨 INT - Mensagens e Integrações

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| INT-001 | Validação de mensagens entre sistemas         | X  | X  | X  |
| INT-002 | Autenticação mútua ou tokens seguros          | X  | X  | X  |
| INT-003 | Transmissão cifrada com TLS                   | X  | X  | X  |
| INT-004 | Proibição de protocolos inseguros             | X  | X  | X  |
| INT-005 | Assinatura e integridade de mensagens         |    | X  | X  |
| INT-006 | Validação cruzada de origem e destino         |    | X  | X  |
| INT-007 | Monitorização e deteção de padrões anómalos   |    |    | X  |
| INT-008 | Revisão de segurança e contrato em integrações|    |    | X  |

---

## 📄 REQ - Definição de Requisitos

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| REQ-001 | Inclusão de requisitos de segurança           | X  | X  | X  |
| REQ-002 | Revisão formal de segurança dos requisitos    | X  | X  | X  |
| REQ-003 | Alinhamento com classificação de risco        | X  | X  | X  |
| REQ-004 | Versionamento e gestão de requisitos          | X  | X  | X  |
| REQ-005 | Nova análise de ameaça após alteração de requisito |    | X | X |
| REQ-006 | Rastreabilidade requisito → ameaça → teste    |    | X  | X  |
| REQ-007 | Revisão iterativa com equipas                 |    | X  | X  |

---

## 🛠️ DST - Distribuição de Artefactos

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| DST-001 | Repositórios autenticados e auditáveis        | X  | X  | X  |
| DST-002 | Aprovação para publicação pública             |    | X  | X  |
| DST-003 | Assinatura digital ou checksum                |    | X  | X  |
| DST-004 | Inclusão de SBOM nos artefactos               |    | X  | X  |
| DST-005 | Acesso segregado por role e ambiente          |    | X  | X  |
| DST-006 | Deploy apenas via pipeline validado           |    | X  | X  |
| DST-007 | Revogação e limpeza de artefactos comprometidos | X | X | X  |

---

## 💻 IDE - Ferramentas de Desenvolvimento

| ID      | Nome resumido                                 | L1 | L2 | L3 |
|---------|-----------------------------------------------|----|----|----|
| IDE-001 | Ferramentas e IDEs autorizadas                | X  | X  | X  |
| IDE-002 | Atualização e gestão de vulnerabilidades      | X  | X  | X  |
| IDE-003 | Auditoria de código gerado por ferramentas    |    | X  | X  |
| IDE-004 | Extensões e plugins de fontes confiáveis      | X  | X  | X  |
| IDE-005 | Controlo de permissões de extensões           |    | X  | X  |
| IDE-006 | Evitar uso de ambientes locais sem controlo   |    | X  | X  |

---

## 📌 Nota Final

Esta lista base pode ser usada para avaliação rápida, referência cruzada, ou integração em anexos do manual SbD-ToE (impressa ou online).

> Para o detalhe de validação, critérios e evidências, consultar a [secção de validação de requisitos](./validacao-requisitos).
