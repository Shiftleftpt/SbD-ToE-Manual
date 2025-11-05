---
id: excecoes-e-aceitacao-risco
title: Exceções e Aceitação de Risco em Vulnerabilidades
description: Formalização de desvios justificados em findings SCA, com critérios e rastreabilidade
tags: [dependencias, sbom, sca, supply-chain, exceptions]
---

# ⚖️ Exceções e Aceitação de Risco em Vulnerabilidades

## 🌟 Objetivo

Definir um processo formal para lidar com situações em que uma vulnerabilidade detetada numa dependência **não pode ser corrigida de imediato**, mas o risco é aceite de forma justificada e documentada.

> 📌 Este mecanismo deve ser excecional, rastreável e com prazo definido. Nunca pode ser usado como pretexto para ignorar riscos reais.

---

## 🔍 Quando é aceitável uma exceção

Uma exceção pode ser considerada se **todos os seguintes critérios forem analisados**:

- A vulnerabilidade **não tem impacto direto** no contexto de execução da aplicação;
- Não existe alternativa viável ou atualizada com o mesmo comportamento esperado;
- Existem **controles compensatórios eficazes** (ex: sandboxing, WAF, autenticação forte);
- A dependência está no caminho de build mas **não no runtime**;
- O risco residual é documentado e aceite formalmente.

---

## 📋 Processo de aceitação de risco

| Etapa                      | Responsável           | Artefacto                            |
|---------------------------|------------------------|---------------------------------------|
| Identificação do finding  | Scanner (SCA)         | CVE + componente                     |
| Análise de impacto        | AppSec + Dev Lead     | Justificação técnica                 |
| Validação compensatória   | AppSec / Arquiteto    | Evidência de controlo alternativo    |
| Aprovação formal          | Security Officer / GRC| Registo com data e reavaliação       |
| Revisão periódica         | AppSec + QA           | Checklist de findings aceites        |

> 🧩 Sugere-se um processo de exceções com validade limitada (ex: 90 dias), com alerta de expiração.

---

## 📁 Template YAML de exceção

```yaml
- cve: CVE-2023-4567
  componente: lib-legacy@1.0.4
  motivo: "Dependência só usada no build; sem impacto no runtime"
  controlo_compensatorio: "Build isolado em container não privilegiado"
  aprovado_por: "sofia.ferreira@appsec.local"
  validade: "2024-09-30"
  revisao_agendada: true
```

> 🔐 Este ficheiro pode estar no repositório (`/security/excecoes.yaml`) ou num sistema de exceções centralizado.

---

## ✅ Check de aceitação mínima

| Critério                                  | Obrigatório? |
|-------------------------------------------|--------------|
| CVE claramente identificado                | ✅            |
| Componente afetado com versão específica  | ✅            |
| Justificação técnica detalhada            | ✅            |
| Controlo compensatório identificado       | ✅            |
| Prazo de validade definido                | ✅            |
| Responsável pela aprovação identificado   | ✅            |
| Revisão programada                        | ✅            |

---

## 🔗 Ligações com outros ficheiros

| Documento                   | Relação com exceções                               |
|-----------------------------|----------------------------------------------------|
| `02-analise-sca.md`         | Origem dos findings que podem originar exceção     |
| `04-integracao-ci-cd.md`    | Deve verificar existência e validade de exceções   |
| `08-rastreabilidade-vulnerabilidades.md` | Regista a decisão de aceitar risco como estado final |

---

> ✅ Aceitar risco não é abdicar da segurança - é uma decisão informada, documentada e revista. Deve ser visível, auditável e limitada no tempo.
