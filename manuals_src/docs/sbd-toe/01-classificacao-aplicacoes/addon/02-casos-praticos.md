---
id: casos-praticos
title: Exemplos de Classificação e Aplicação de Risco
sidebar_position: 2
tags: [tipo:exemplo, tema:classificacao, risco, aplicacao]
---
<!--template: handson -->

# 🧪 Casos Práticos de Classificação de Risco {classificacao-aplicacoes:addon:casos-praticos}

Estes exemplos demonstram como aplicar o [modelo dos três eixos de risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:modelo-classificacao-eixos) em diferentes cenários deste capítulo.

---

## 📝 Caso 1 – Aplicação de E-commerce {classificacao-aplicacoes:addon:casos-praticos#caso_1__aplicacao_de_e_commerce}

- **Exposição**: Pública (web + app móvel) → 3  
- **Dados**: Cartão de crédito + dados pessoais → 3  
- **Impacto**: Financeiro + reputacional → 3  

**Total: 9 → Risco Elevado (ASVS Nível 3)**

> **Implicações**:
> - Requisitos de segurança formais e completos  
> - Threat modeling obrigatório  
> - SBOM e validação de dependências  
> - DAST e fuzzing contínuos

---

## 📝 Caso 2 – Portal interno de RH hospitalar {classificacao-aplicacoes:addon:casos-praticos#caso_2__portal_interno_de_rh_hospitalar}

- **Exposição**: Apenas rede interna → 1  
- **Dados**: Dados clínicos e financeiros de colaboradores → 3  
- **Impacto**: Legal + confidencialidade sensível → 3  

**Total: 7 → Risco Elevado (ASVS Nível 3)**

> **Nota**: Apesar da baixa exposição, os dados tratados e impacto legal elevam o risco.

---

## 📝 Caso 3 – Sistema de Faturação B2B {classificacao-aplicacoes:addon:casos-praticos#caso_3__sistema_de_faturacao_b2b}

- **Exposição**: Utilizadores autenticados externos → 2  
- **Dados**: Dados financeiros e de clientes → 2  
- **Impacto**: Operacional + financeiro → 2  

**Total: 6 → Risco Médio (ASVS Nível 2)**

> **Implicações**:
> - Controlo de dependências com SCA  
> - Threat modeling leve  
> - Requisitos formalizados, mas não exaustivos

---

## 📝 Caso 4 – Aplicação de gestão de tarefas internas {classificacao-aplicacoes:addon:casos-praticos#caso_4__aplicacao_de_gestao_de_tarefas_internas}

- **Exposição**: Apenas rede interna → 1  
- **Dados**: Não sensíveis → 1  
- **Impacto**: Baixo → 1  

**Total: 3 → Risco Baixo (ASVS Nível 1)**

> **Implicações**:
> - Linters e revisão informal  
> - Sem exigência de testes automáticos  
> - Política mínima de dependências
