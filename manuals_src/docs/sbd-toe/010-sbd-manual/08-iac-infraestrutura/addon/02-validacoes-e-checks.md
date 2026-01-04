---
id: validacoes-e-checks
title: Validações Automáticas e Controlo de Qualidade no Projeto IaC
sidebar_position: 1
description: Estratégias prescritivas de validação, evidência e controlo para garantir uma adoção segura, auditável e verificável de Infraestrutura como Código.
tags: [planeamento, controlo, iac, segurança, validação, governação]
---

# 🧪 Validações Automáticas e Controlo de Qualidade no Projeto IaC

## 🌟 Objetivo

Garantir que **todas as alterações em projetos de Infraestrutura como Código (IaC)** são tratadas como **entrada não confiável**, sujeitas a **validações automáticas bloqueantes**, e acompanhadas de **evidência auditável** antes de qualquer aplicação em ambiente real.

Este ficheiro estabelece o **mínimo técnico obrigatório** para assegurar que o projeto IaC:

- é **correto** (sintaxe e estrutura);
- é **seguro** (configuração, permissões, exposição);
- é **compreendido** (impacto real do `plan`);
- é **auditável** (evidência ligada à decisão e execução);
- não degrada controlo quando suportado por **automação ou ferramentas assistidas**.

> No modelo SbD-ToE, a validação automatizada é um **mecanismo de controlo**, não uma otimização opcional.  
> Sem validação bloqueante e evidência mínima, não existe governação efetiva de IaC.

---

## 🧩 Princípio base: entrada não confiável por origem

Em contexto moderno de engenharia, alterações de IaC podem ser produzidas por:
- humanos,
- templates,
- normalizadores,
- scripts,
- geradores,
- mecanismos assistidos ou automatizados.

**Prescrição fundamental:**  
👉 **A origem da alteração nunca é uma garantia de segurança.**  
👉 **Todo o IaC proposto é tratado como entrada não confiável**, com reforço adicional quando a alteração é produzida ou modificada por mecanismos automatizados.

Consequentemente:
- nenhuma alteração pode chegar a `apply` sem validação bloqueante;
- a validação deve incidir sobre **efeitos reais**, não apenas sobre forma;
- a decisão de executar deve ser **explícita, rastreável e evidenciada**.

Este princípio é operacionalizado por validações técnicas e gates definidos neste documento.

---

## 📌 O que deve ser feito (prescrição mínima)

A organização **deve garantir**, no mínimo:

1. Execução de **linters e validadores sintáticos** (ex.: `terraform validate`, `tflint`);
2. Aplicação de **scanners de segurança específicos para IaC**;
3. Validação de **conformidade com políticas internas** (naming, tagging, permissões, módulos);
4. Integração de **todas as validações no pipeline CI/CD**, com **falha obrigatória**;
5. Geração e validação de **`terraform plan` (ou equivalente)** antes de qualquer `apply`;
6. **Validação semântica do impacto real** do `plan`;
7. Bloqueio automático quando **requisitos críticos não são cumpridos**;
8. **Armazenamento e correlação de evidência mínima** (plan + relatórios + aprovação).

---

## ⚙️ Como aplicar (tipos de validação)

| Tipo de Validação | Finalidade técnica |
|------------------|-------------------|
| **Sintática** | Garantir que o código é válido e executável |
| **Estrutural / Linting** | Impor padrões, evitar más práticas recorrentes |
| **Segurança** | Detetar exposições, permissões excessivas, configurações inseguras |
| **Policy-as-Code** | Impor regras organizacionais de forma automática |
| **Validação semântica** | Avaliar o impacto real do `plan` |
| **Controlo de execução** | Impedir `apply` sem validação e aprovação |
| **Evidência** | Garantir rastreabilidade decisão → execução |

### Ferramentas e técnicas exemplificativas

| Categoria | Exemplos |
|---------|----------|
| Sintaxe / formato | `terraform fmt`, `terraform validate`, `yamllint` |
| Linting | `tflint`, `actionlint`, `ansible-lint` |
| Segurança | `tfsec`, `checkov`, `kics`, `terrascan` |
| Policies | OPA/Rego, Sentinel, Conftest |
| Pipeline | Gates obrigatórios em PR/MR e pré-`apply` |
| Local | Pre-commit hooks obrigatórios |

> As ferramentas são **meios**; o requisito é o **efeito verificável**.

---

## 🔍 Validação semântica do `plan` (obrigatória quando aplicável)

Para além da sintaxe, deve ser avaliado o **impacto real do `plan`**, incluindo:

- criação, alteração ou destruição de recursos por ambiente;
- expansão de permissões (ex.: IAM, roles, wildcards);
- exposição de rede (endpoints públicos, regras permissivas);
- ausência de cifragem ou logging em recursos críticos;
- alterações indiretas por módulos, providers ou dependências;
- *diffs* inesperados ou não explicados.

**Prescrição:**  
👉 A validação semântica **deve funcionar como gate bloqueante**, não como aviso informativo.

---

## 🧾 Evidência mínima obrigatória

Para que a validação seja auditável, a organização deve garantir:

- `plan` gerado em CI associado a:
  - PR/MR,
  - commit hash,
  - ambiente alvo;
- relatórios de linters, scanners e policies associados ao mesmo PR/MR;
- registo explícito de **aprovação antes de `apply`**;
- retenção dos artefactos proporcional ao risco e obrigações internas.

Sem esta evidência, **não existe prova de controlo**, apenas execução técnica.

---

## 🕒 Quando aplicar

| Momento | Validações esperadas |
|-------|----------------------|
| Commit / Push | Linters locais, pre-commit hooks |
| Pull Request | Linters + scanners + policies + `plan` |
| Merge para release | Validação reforçada + evidência completa |
| Pré-`apply` | Verificação final de plan, hashes e ambiente |
| Periodicamente | Drift, revalidação de módulos e dependências |

---

## 👥 Perfis envolvidos

| Papel | Responsabilidade |
|-----|------------------|
| DevOps / Infra | Integração técnica das validações no pipeline |
| AppSec / Segurança | Definição e manutenção das políticas |
| Desenvolvimento | Correção de findings e explicação de impacto |
| Cloud / Arquitetura | Validação de efeitos reais e desenho seguro |

---

## 🧪 Exemplos práticos

- Pipeline bloqueado por `tfsec` em permissões IAM demasiado amplas;
- `checkov` a impedir merge por bucket sem cifragem;
- Política OPA a bloquear `plan` com criação de endpoint público;
- Job `validate-iac` obrigatório antes de `apply`;
- PR rejeitado por *diff* não explicado em recurso crítico.

---

## ✅ Checklist de controlo (por projeto)

- [ ] Todas as alterações são tratadas como entrada não confiável
- [ ] Validações automáticas são bloqueantes
- [ ] Existe validação semântica do `plan`
- [ ] `plan` e relatórios estão ligados a PR/MR + commit
- [ ] A aprovação antes de `apply` é registada e auditável
- [ ] Evidência é retida conforme criticidade

---

## 🔗 Referências cruzadas

| Documento | Relação |
|---------|---------|
| `15-aplicacao-lifecycle.md` | User stories de validação, plan e aprovação |
| `addon/04-principios-sbd-iac.md` | Princípios SbD aplicados a IaC |
| `addon/11-uso-ferramentas-automatizadas-iac.md` | Regras para automação/assistência |

---

> ⚠️ A ausência de validações automáticas bloqueantes e de evidência mínima transforma IaC num **canal privilegiado de risco sistémico**, comprometendo segurança, auditoria e governação.
