---
id: 07-deploy-progressivo-e-risco
title: Deploy Progressivo e Controlo de Risco
description: Práticas como canary releases, blue/green e staged rollout para mitigar risco em deploys críticos.
tags: [grupo:execucao, risco, staging, tema:deploy-progressivo, tipo:anexo]
---


# 🚀 Deploy Progressivo e Avaliação de Risco

O deploy progressivo é uma prática essencial para mitigar riscos durante a entrega de novas versões de software. Permite uma **exposição gradual e controlada** de funcionalidades, com a capacidade de **medir impacto, recolher feedback e interromper rapidamente** em caso de erro.

---

## 🔄 Modelos comuns de deploy progressivo

| Estratégia           | Descrição                                                                 | Vantagens                                  |
|----------------------|---------------------------------------------------------------------------|--------------------------------------------|
| **Canary Release**   | Entrega para uma pequena percentagem de utilizadores                       | Detetar erros com impacto reduzido         |
| **Blue/Green Deploy**| Dois ambientes paralelos: ativa-se o novo após validação                 | Rápido rollback, sem downtime             |
| **Shadow Traffic**   | Roteia tráfego para novo sistema sem resposta ao utilizador                | Testes realistas sem impacto direto         |
| **Feature Flags**    | Ativa funcionalidade em runtime para segmentos controlados                 | Flexível, reversível, segmentável           |

---

## 🚨 Avaliação de risco em releases progressivas

Antes de iniciar um rollout progressivo, deve ser feita uma **avaliação formal do risco da release**, com base em:

- Severidade de alterações (breaking changes, novos fluxos)
- Histórico da componente / equipa
- Reversibilidade e cobertura de rollback
- Maturidade dos testes automatizados
- Nível de exposição e impacto potencial

> 📊 Releases de risco elevado devem **começar em ambientes canary + gated**.

---

## 🌐 Controlo do rollout

- **âmbitos comuns**:
  - Percentagem de utilizadores (ex: 1%, 5%, 20%)
  - Segmentos por geo / tenant / perfil / device
  - Período temporal (ex: ativa por 3 horas)

- **Critérios de bloqueio / rollback**:
  - Latência > X ms
  - Erros 5xx > Y%
  - Alertas de segurança ou picos anómalos

---

## 🔹 Integração com pipelines

- Definir gates por segmento de rollout (canary, general availability)
- Monitorizar eventos por release hash e toggle ativo
- Automatizar promoção entre estágios com validações
- Integrar validações de segurança no processo (ex: comportamento inesperado)

---

## 👨‍💻 Equipa responsável pelo rollout

| Papel          | Responsabilidades principais                              |
|----------------|-----------------------------------------------------------|
| DevOps         | Implementa estratégia de rollout e rollback               |
| QA / AppSec    | Define critérios de bloqueio e valida resultado           |
| Produto        | Define âmbito funcional, aprova promoção                 |
| Engenharia     | Monitoriza comportamento e atua se houver incidente       |

---

## ✅ Checklist de rollout seguro

- [ ] A release tem plano de rollout definido?
- [ ] Existem métricas de sucesso / erro para monitorização?
- [ ] O rollout é reversível em cada fase?
- [ ] Existe documentação do âmbito inicial e critérios de promoção?
- [ ] Os toggles estão visíveis e controlados por owner?
- [ ] As equipas responsáveis estão identificadas para cada estágio?

> 🌟 Um bom rollout é um processo técnico + organizacional, não apenas uma configuração no pipeline.
