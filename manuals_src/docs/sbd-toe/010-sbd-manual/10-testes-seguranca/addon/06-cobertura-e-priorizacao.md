---
id: cobertura-e-priorizacao
title: Cobertura e Priorização de Testes de Segurança
description: Estratégias para priorizar testes com base no risco e assegurar cobertura eficaz dos requisitos.
tags: [cobertura, priorização, risco, seguranca, testes]
sidebar_position: 7
---


# 🎯 Cobertura e Priorização dos Testes de Segurança

## 🌟 Objetivo

Definir **quais componentes, funcionalidades e interfaces devem ser testadas**, **com que profundidade e frequência**, e **com que tipo de teste**, com base em:

- Nível de risco e criticidade da aplicação;
- Frequência de alterações e exposição externa;
- Histórico de falhas ou findings anteriores;
- Dependências de segurança de outros sistemas.

> Cobertura sem priorização leva a desperdício. Priorização sem cobertura leva a falsas sensações de segurança.

---

## 🔍 O que é cobertura e priorização em segurança

**Cobertura** refere-se à percentagem do sistema que é abrangida pelos testes de segurança - incluindo:

- Código-fonte;
- APIs e endpoints;
- Fluxos funcionais;
- Integrações e dependências.

**Priorização** define **o que testar primeiro ou com mais intensidade**, com base em:

- Exploração provável;
- Impacto em caso de falha;
- Facilidade de teste;
- Riscos regulatórios ou reputacionais.

> 💡 Uma matriz de risco x frequência de teste ajuda a operacionalizar a estratégia.

---

## ⚙️ Como aplicar

1. **Mapear superfícies de ataque e interfaces expostas** (ex: APIs públicas, painéis de gestão);
2. **Classificar áreas por criticidade funcional e impacto de segurança**;
3. **Definir frequência mínima de testes por categoria de risco** (ex: mensal para L3, semestral para L1);
4. **Assinalar gaps de cobertura** (ex: endpoints não testados, código não instrumentado);
5. **Ajustar profundidade de testes conforme o tipo** (ex: fuzzing para parsers, DAST para interfaces externas);
6. **Rever mapa de cobertura periodicamente com equipas técnicas e segurança**.

---

## ✅ Boas práticas

- Incluir cobertura de segurança nos critérios de qualidade;
- Rastrear a cobertura real com métricas (ex: % de APIs testadas);
- Priorizar funcionalidades novas, críticas ou recentemente alteradas;
- Usar tagging por componente e criticidade nos testes;
- Avaliar cobertura efetiva dos testes automatizados (não apenas presença);
- Validar se regressões e findings estão a ser revistos em zonas de maior risco.

---

## 📎 Referências cruzadas

| Documento                       | Relevância estratégica                          |
|--------------------------------|--------------------------------------------------|
| Capítulo 01 - Gestão de Risco  | Define critérios de classificação e criticidade |
| Capítulo 02 - Requisitos       | Define o que deve ser validado e porquê         |
| `01-sast.md` a `04-fuzzing.md` | Tipos de teste aplicáveis a zonas priorizadas   |
| `05-validacao-regressao.md`    | Ajuda a definir targets persistentes            |
| `08-gestao-findings.md`        | Relaciona findings com zonas testadas ou não    |

---

> 🧩 A cobertura de testes de segurança não é binária - deve ser **contextual, proporcional e orientada ao risco real**. Cobrir o que importa é tão vital quanto testar bem.
