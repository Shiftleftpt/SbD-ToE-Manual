---
id: adopcao-drp-bia
title: Integração com DRP, BIA e Classificações Existentes
sidebar_position: 3
tags: [tipo:ligacao, tema:drp, bia, classificacao, risco]
---
<!--template: sbdtoe-addon -->

# 📎 Adoção de Classificações Existentes (e.g. DRP/BIA) {classificacao-aplicacoes:addon:adopcao-drp-bia}


## 🎯 Objetivo {classificacao-aplicacoes:addon:adopcao-drp-bia#objetivo}

Orientar a reutilização de classificações já existentes — nomeadamente **DRP (Disaster Recovery Plan)** e **BIA (Business Impact Analysis)** — como base para a **classificação de risco aplicacional**, evitando duplicação de esforço e promovendo consistência na avaliação de criticidade.

---

## 📘 Contexto {classificacao-aplicacoes:addon:adopcao-drp-bia#contexto}

Muitas organizações já realizam uma **classificação de impacto** com base na continuidade do negócio, no âmbito de processos como o DRP ou BIA, ou outras. Essas classificações incluem geralmente atributos como:

- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)
- Impacto financeiro, reputacional ou operacional
- Prioridade de recuperação

Embora não tenham foco direto na segurança, estes dados são **fortemente correlacionáveis** com o risco aplicacional e podem ser utilizados como **input inicial ou justificação** da classificação de risco prescrita no SbD-ToE.

---

## 🔁 Mapeamento prático entre DRP/BIA e risco de segurança {classificacao-aplicacoes:addon:adopcao-drp-bia#mapeamento_pratico_entre_drpbia_e_risco_de_seguranca}

| Classificação DRP/BIA     | Interpretação no contexto SbD-ToE |
|---------------------------|------------------------------------|
| **Crítico**               | Risco Elevado                     |
| **Importante / Médio**    | Risco Médio                       |
| **Não essencial / Baixo** | Risco Baixo                       |

> ⚠️ Este mapeamento deve ser **confirmado por análise de segurança**, considerando a natureza dos dados e exposição da aplicação.

---

## 📝 Exemplo prático {classificacao-aplicacoes:addon:adopcao-drp-bia#exemplo_pratico}

Um sistema classificado como **Crítico** no DRP, com os seguintes parâmetros:

- **RTO:** < 4h  
- **RPO:** < 1h  
- Dados pessoais e de faturação  
- Integração com terceiros  
- Exposto à internet

→ Deve ser automaticamente classificado como **Risco Elevado**, exigindo:

- Threat Modeling formal  
- Requisitos de segurança completos  
- Testes automatizados contínuos  
- Monitorização ativa

---

## 📌 Recomendações {classificacao-aplicacoes:addon:adopcao-drp-bia#recomendacoes}

- Validar se a classificação DRP/BIA está atualizada e corresponde ao âmbito da aplicação atual
- Anexar ou referenciar a classificação de impacto no repositório onde for documentada a classificação de risco
- Se a aplicação for composta por múltiplos módulos, considerar a classificação **por componente**, não apenas global
- Em caso de divergência entre a classificação DRP e a observada em segurança, registar ambos os racionales e discutir com as equipas envolvidas

---

## 🧩 Integração operacional {classificacao-aplicacoes:addon:adopcao-drp-bia#integracao_operacional}

Na prática, a reutilização destas classificações pode ser feita de três formas:

1. **Importação direta dos dados** no registo de risco (ex: ficheiro, wiki, ferramenta)
2. **Ligação cruzada** entre artefactos (ex: link para a ficha DRP no registo de risco)
3. **Template único** que inclua campos de impacto de negócio e risco de segurança

> Uma boa prática é incluir esta validação como um dos critérios do *checklist* de classificação.

---

## 📄 Referências {classificacao-aplicacoes:addon:adopcao-drp-bia#referencias}

- [ISO 22301 — Segurança e Resiliência — Gestão da Continuidade do Negócio](https://www.iso.org/standard/75106.html)
- [NIST SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
- [NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final)
