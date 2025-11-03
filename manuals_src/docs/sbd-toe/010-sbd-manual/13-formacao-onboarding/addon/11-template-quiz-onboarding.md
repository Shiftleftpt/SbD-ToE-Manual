---
id: quiz-onboarding
title: Template de Quiz para Validação de Onboarding
description: Exemplo de quiz técnico usado para validação de conhecimentos no processo de onboarding.
tags: [onboarding, quiz, validacao, conhecimento, rastreabilidade]
---


# 📝 Template de Quiz – Onboarding Técnico

Este documento apresenta um exemplo reutilizável de **quiz técnico** para validação de conhecimento no contexto de **formação inicial** (onboarding) em segurança.  
Pode ser adaptado por perfil, nível de risco ou capítulo do manual SbD-ToE, sendo especialmente útil em **trilhos de formação para developers**.

---

## 🎯 Objetivo

- Validar de forma objetiva a assimilação de conteúdos essenciais de segurança
- Fornecer registo auditável de conclusão de onboarding técnico
- Reforçar conceitos-chave através de exemplos realistas

---

## 📦 Contexto de uso

| Situação                         | Aplicação recomendada                                 |
|----------------------------------|--------------------------------------------------------|
| Onboarding de novo Dev           | Usar após conclusão do trilho formativo inicial        |
| Mudança de stack ou projeto      | Validar conhecimentos específicos ao novo contexto     |
| Reforço de formação contínua     | Integrar como revalidação anual (ex: revisão de acesso)|
| Checkpoint para acesso técnico   | Associar ao desbloqueio de permissões (ex: Git, CI/CD) |

> Pode ser usado num LMS, Google Form, GitHub Issue com markdown, ou integrado no fluxo de onboarding via pipelines/scripts.

---

## 🧪 Exemplo de quiz: Dev em aplicação L2

1. **Qual destas práticas é obrigatória ao fazer merge de uma PR?**  
   - a) Corrigir todos os conflitos automaticamente  
   - b) Validar requisitos de segurança aplicáveis à aplicação  
   - c) Executar apenas o `npm install`  
   - d) Ignorar dependências não utilizadas  
   ✅ **Resposta correta:** b)

2. **Qual o risco de deixar um segredo no código fonte?**  
   - a) Nenhum, se for um token temporário  
   - b) Pode causar acesso não autorizado e comprometer o ambiente  
   - c) Apenas torna o build mais lento  
   - d) É aceitável se for num branch privado  
   ✅ **Resposta correta:** b)

3. **Qual destas ferramentas é usada para verificar dependências inseguras?**  
   - a) ESLint  
   - b) Git  
   - c) SCA (ex: Xygeni, OWASP Dependency-Check)  
   - d) Jenkins  
   ✅ **Resposta correta:** c)

---

## 📌 Boas práticas de utilização

- Adaptar perguntas ao conteúdo efetivamente ensinado no trilho
- Incluir feedback imediato com explicação das respostas
- Garantir registo de conclusão (pontuação mínima, evidência de submissão)
- Reutilizar perguntas em clinics, quizzes internos, ou jogos formativos

---

## 🔗 Ligações úteis

| Documento                     | Relevância                                      |
|-------------------------------|-------------------------------------------------|
| `03-checklist-onboarding.md`  | Checklist onde este quiz pode ser referenciado |
| `trilho-formativo.md`         | Indica quando e para quem aplicar o quiz       |
| `90-catalogo-formativo.md`    | Lista tópicos que devem estar cobertos         |

---

> 🎯 Este template pode ser duplicado e adaptado por capítulo, função ou criticidade — garantindo rastreabilidade e alinhamento com o manual SbD-ToE.
