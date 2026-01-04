---

id: gestao-excecoes
title: Gestão de Exceções e Justificações Formais em IaC
sidebar_position: 9
description: Procedimentos e critérios para tratamento de exceções às práticas prescritas de IaC Seguro.
tags: [excecoes, governacao, iac, controlo, seguranca, auditoria]
-----------------------------------------------------------------

# ⚠️ Gestão de Exceções e Não-Conformidades em Projetos IaC

## 🌟 Objetivo

Definir um **processo formal, auditável e temporário** para a gestão de exceções a políticas, requisitos ou controlos de segurança aplicáveis a projetos de Infraestrutura como Código (IaC).

Este mecanismo existe para **permitir continuidade operacional sem comprometer governação**, assegurando que qualquer desvio é:

* explicitamente conhecido;
* tecnicamente justificado;
* mitigado;
* limitado no tempo.

> Exceções são um mecanismo legítimo de gestão de risco. **Exceções não controladas são falhas de segurança.**

---

## 📌 O que deve ser feito

1. Definir **critérios objetivos** para aceitação de exceções em IaC;
2. Estabelecer um **fluxo formal de submissão, análise e aprovação**;
3. Registar todas as exceções com **metadados mínimos obrigatórios**;
4. Garantir **ligação direta entre exceção, código, ambiente e requisito violado**;
5. Aplicar **prazo de validade (TTL)** e revisão periódica obrigatória;
6. Revogar automaticamente exceções expiradas ou não revalidadas;
7. Reavaliar exceções sempre que haja **mudança relevante de contexto** (arquitetura, fornecedor, risco).

---

## ⚙️ Como deve ser feito

| Elemento          | Prescrição                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| Formato           | YAML ou JSON versionado (preferencial); `.md` apenas para exceções documentais                                 |
| Campos mínimos    | ID, requisito violado, descrição, justificação, impacto, mitigação, ambiente, responsável, aprovador, validade |
| Local de registo  | Diretório `exceptions/` no repositório IaC ou repositório central dedicado                                     |
| Ligação ao código | Comentário estruturado (`# iac-exception: IAC-003`) ou anotação Rego                                           |
| Aprovação         | AppSec obrigatório; GRC adicional para L3                                                                      |
| Validade          | Máx. 90 dias, renovação exige nova avaliação                                                                   |

---

## 🗒️ Exemplo de exceção formalizada

```yaml
id: IAC-EXC-003-2025-07-10
requisito: IAC-003
descricao: Execução temporária sem scanner tfsec
ambiente: staging
artefacto_afetado: pipeline-iac-staging
justificacao: Deploy urgente para restauro de capacidade após incidente P1
impacto: Possível omissão temporária de deteção de más configurações
mitigacao: Execução manual de tfsec pós-deploy + revisão AppSec
aprovado_por: appsec@org
validade: 2025-07-20
```

---

## 🗓️ Quando aplicar

| Situação                             | Ação esperada                        |
| ------------------------------------ | ------------------------------------ |
| Ferramenta de validação indisponível | Submissão imediata de exceção formal |
| Requisito tecnicamente impossível    | Exceção com mitigação compensatória  |
| Desvio intencional em IaC            | Registo explícito e visível          |
| Revisão periódica                    | Avaliação mensal ou por sprint       |

---

## 🧩 Integração com enforcement

* Exceções **não desativam regras** globalmente;
* São avaliadas **por regra e por contexto**;
* Devem ser **interpretáveis por *policy engines*** (OPA/Sentinel);
* Exceções expiradas resultam em **bloqueio automático** do pipeline.

---

## ✅ Benefícios diretos

* Elimina desvios silenciosos e técnicos fora de governação;
* Permite equilíbrio entre agilidade e segurança;
* Fornece evidência clara para auditoria;
* Reduz acumulação de dívida técnica e de risco.

---

## 🔗 Referências cruzadas

| Documento                           | Relação                                            |
| ----------------------------------- | -------------------------------------------------- |
| `addon/06-controle-enforcement.md`  | Tratamento técnico de exceções em *policy-as-code* |
| `addon/08-matriz-requisitos-iac.md` | Requisitos IAC e validação                         |
| Cap. 14 — Governança e Contratação  | Processo organizacional de exceções                |
| SSDF (RV.1)                         | Gestão de desvios e risco                          |
| OWASP SAMM (AA2.4, SR2.2)           | Governação de risco técnico                        |
| SLSA (Build L3)                     | Controlo e aprovação formal                        |
