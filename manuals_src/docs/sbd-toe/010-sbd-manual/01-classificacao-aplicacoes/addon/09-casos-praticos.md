---
id: casos-praticos
sidebar_position: 9
tags:
- aplicacao
- base
- cat_basilar
- ciclo-vida
- risco
- tema:classificacao
- tipo:exemplo
title: Exemplos de Aplicação deC lassificação de Risco
---


# 🧪 Casos Práticos de Classificação de Risco

Estes exemplos demonstram como aplicar o [modelo dos três eixos de risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos) em diferentes cenários deste capítulo.

---

## 📝 Caso 1 - Aplicação de E-commerce

- **Exposição**: Pública (web + app móvel) → 3  
- **Dados**: Cartão de crédito + dados pessoais → 3  
- **Impacto**: Financeiro + reputacional → 3  

**Total: 9 → Risco Elevado**

> **Implicações**:
> - Requisitos de segurança formais e completos  
> - Threat modeling obrigatório  
> - SBOM e validação de dependências  
> - DAST e fuzzing contínuos

---

## 📝 Caso 2 - Portal interno de RH hospitalar

- **Exposição**: Apenas rede interna → 1  
- **Dados**: Dados clínicos e financeiros de colaboradores → 3  
- **Impacto**: Legal + confidencialidade sensível → 3  

**Total: 7 → Risco Elevado**

> **Nota**: Apesar da baixa exposição, os dados tratados e impacto legal elevam o risco.

---

## 📝 Caso 3 - Sistema de Faturação B2B

- **Exposição**: Utilizadores autenticados externos → 2  
- **Dados**: Dados financeiros e de clientes → 2  
- **Impacto**: Operacional + financeiro → 2  

**Total: 6 → Risco Médio**

> **Implicações**:
> - Controlo de dependências com SCA  
> - Threat modeling leve  
> - Requisitos formalizados, mas não exaustivos

---

## 📝 Caso 4 - Aplicação de gestão de tarefas internas

- **Exposição**: Apenas rede interna → 1  
- **Dados**: Não sensíveis → 1  
- **Impacto**: Baixo → 1  

**Total: 3 → Risco Baixo**

> **Implicações**:
> - Linters e revisão informal  
> - Sem exigência de testes automáticos  
> - Política mínima de dependências
