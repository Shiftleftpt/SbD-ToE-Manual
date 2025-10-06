---
id: gestao-excecoes
title: Gestão de Exceções e Justificações Formais em IaC
sidebar_position: 9
description: Procedimentos e critérios para tratamento de exceções às práticas prescritas de IaC Seguro.
tags: [exceções, governação, iac, controlo, segurança, auditoria]
---


# ⚠️ Gestão de Exceções e Não-Conformidades em Projetos IaC {iac-infraestrutura:addon:gestao-excecoes}

## 🌟 Objetivo {iac-infraestrutura:addon:gestao-excecoes#objetivo}

Definir uma abordagem formal para gerir **exceções a políticas, requisitos ou controlos de segurança** em projetos de Infraestrutura como Código (IaC), garantindo rastreabilidade, justificação e mitigação de riscos associados.

> A existência de exceções é legítima — a sua gestão deficiente é que compromete a segurança.

---

## 📌 O que deve ser feito {iac-infraestrutura:addon:gestao-excecoes#o_que_deve_ser_feito}

1. **Estabelecer critérios claros para a aceitação de exceções** a requisitos de segurança aplicáveis a IaC;
2. **Definir processo de submissão e aprovação** com validação por segurança/AppSec;
3. **Registar todas as exceções com metadados essenciais**: motivo, impacto, mitigação, duração e responsáveis;
4. **Garantir visibilidade contínua de exceções ativas** e associá-las a artefactos (PRs, módulos, ambientes);
5. **Aplicar controlo de expiração automática ou revisão periódica** para exceções temporárias;
6. **Reavaliar exceções sempre que o contexto técnico ou organizacional se altere.**

---

## ⚙️ Como deve ser feito {iac-infraestrutura:addon:gestao-excecoes#como_deve_ser_feito}

| Elemento                    | Descrição                                                                      |
| --------------------------- | ------------------------------------------------------------------------------ |
| Formato                     | YAML, JSON, ou ficheiro `.md` com frontmatter normalizado                      |
| Campos mínimos              | ID, data, autor, requisito violado, justificação, impacto, mitigação, validade |
| Local de registo            | Diretório `exceptions/`, repositório dedicado, ou wiki técnica                 |
| Ligação a código            | Comentário estruturado no código (`# exception: IAC-003`)                      |
| Aprovação necessária        | Equipa de segurança ou autoridade designada                                    |
| Validade máxima recomendada | 90 dias (renovável com nova justificação e validação)                          |

---

## 🗒️ Exemplo de exceção formalizada {iac-infraestrutura:addon:gestao-excecoes#exemplo_de_excecao_formalizada}

```yaml
id: exception-iac-003-20250710
requisito: IAC-003
descricao: "Execução temporária de Terraform sem scanner tfsec devido a falha no repositório."
ambiente: staging
modulo: network-baseline
justificacao: "Deploy urgente para restauro de capacidade após incidente P1."
mitigacao: "Execução posterior de tfsec em ambiente controlado."
aprovado_por: "appsec@org"
validade: "2025-07-20"
```

---

## 🗓️ Quando aplicar {iac-infraestrutura:addon:gestao-excecoes#quando_aplicar}

| Situação                              | Ação esperada                                                       |
| ------------------------------------- | ------------------------------------------------------------------- |
| Ferramenta de validação inoperacional | Submissão de exceção justificada                                    |
| Requisito impossível de cumprir       | Formalização com mitigação aceitável                                |
| Exceção técnica em repositório IaC    | Comentário visível + ficheiro associado                             |
| Revisão de exceções                   | Tarefa periódica (mensal ou sprint) de revisão por equipa de AppSec |

---

## ✅ Benefícios {iac-infraestrutura:addon:gestao-excecoes#beneficios}

* Garante que exceções são transparentes, justificadas e mitigadas;
* Reduz risco organizacional ao evitar violações silenciosas;
* Suporta auditoria e resposta a incidentes com registos completos;
* Permite equilíbrio entre agilidade técnica e segurança formal.

---

> 🔗 Este mecanismo está alinhado com os requisitos `IAC-010`, `REQ-005`, `REQ-006`, e boas práticas SSDF (RV.1), SAMM (AA2.4), BSIMM (SR2.2), SLSA (Build L3).
