---
id: anotacoes-evidencia
title: Anotações e Evidência de Validações
sidebar_position: 9
description: Estratégias para anotar decisões e evidências de validação de segurança no próprio código ou ciclo de desenvolvimento
tags: [evidência, anotação, validação, rastreabilidade, SDLC]
---

# 🏷️ Anotações e Evidência de Validações

> 💡 **Nota prática**:  
> Ferramentas como **GitHub**, **GitLab**, **Xygeni**, **SonarQube**, **Semgrep**, ou até simples editores como **VSCode** permitem o uso de **comentários estruturados, etiquetas e marcações especiais** que indicam que uma validação de segurança foi feita - ou que uma exceção foi aceite.  
> Estas anotações tornam a revisão mais eficaz, ajudam a construir rastreabilidade e servem como evidência auditável da aplicação prática das guidelines de segurança.

---

## 📌 Objetivos

- Tornar visível e rastreável a aplicação de validações de segurança.
- Facilitar revisões técnicas e auditorias internas.
- Reforçar a cultura de validação explícita e responsabilidade por decisão técnica.
- Apoiar processos de exceção, revisão de findings e controlo de qualidade.

---

## 👥 Quem deve aplicar

- **Desenvolvedores**: ao escrever ou revisar código sensível.
- **Revisores técnicos**: ao aceitar PRs com impacto em segurança.
- **Segurança / AppSec**: ao avaliar exceções, justificações e rastreabilidade.

---

## ⏱️ Quando aplicar

- Durante o desenvolvimento, em código com requisitos ou risco de segurança.
- No momento de revisão de PRs e pull requests sensíveis.
- Ao justificar findings de ferramentas SAST/SCA.
- Sempre que uma exceção for aceite ou mitigada por design.

---

## 🧱 Boas práticas de anotação

1. **Usar marcações padronizadas e pesquisáveis**
   - Ex: `@sec:input-validated`, `@sec:auth-required`, `@sec:checked`, `@sec:waived`

2. **Anotar diretamente no código, junto à função crítica**
   - Preferencialmente antes de blocos de lógica sensível.

3. **Associar anotação à referência formal (requisito, exceção, finding)**
   - Ex: `@sec:justificado #SEC-EXC-014`, `@sec:reviewed-CWE79`

4. **Reutilizar comentários nas revisões e reports**
   - As anotações servem de fonte para gerar evidência e relatórios.

5. **Não abusar - apenas onde há decisão explícita**
   - Comentários inúteis reduzem o sinal:ruído e perdem valor técnico.

---

## ✅ Como validar

- Verificação automatizada por script (ex: `grep @sec:` ou verificação em CI).
- Checklist de revisão técnica com marcação de presença de tags.
- Confirmação manual por reviewer de que a anotação é justificada.
- Integração com painéis de rastreabilidade (ex: Xygeni, dashboards internos).

---

## 🧾 Como evidenciar

- Presença das anotações no código versionado (por commit ou PR).
- Logs de scans que referenciam ou extraem essas marcações.
- Reports de release que indicam blocos anotados e sua função.
- Tabela de rastreabilidade `@sec:*` → requisito/finding → justificação (se exceção).

---

## 🔄 Ligação a outras práticas

| Tema                                      | Ficheiro associado               |
|-------------------------------------------|----------------------------------|
| Justificação de exceções                  | `addon/05-excecoes-e-justificacoes.md` |
| Revisão e validação de código             | `addon/08-validacoes-codigo.md` |
| Guidelines de desenvolvimento e equipa    | `addon/01`, `addon/07`           |
| Linters e scanners integrados             | `addon/02`, ferramentas com tagging |

---

> 📌 As anotações são um meio leve mas poderoso de **tornar validações auditáveis, rastreáveis e colaborativas**.  
> Devem ser parte do processo técnico normal e respeitar convenções bem definidas por equipa ou organização.
