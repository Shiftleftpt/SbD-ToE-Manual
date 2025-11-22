---
description: Princípios e controlos para garantir um processo de deploy seguro, validado
  e rastreável em ambientes de produção
id: intro
sidebar_position: 0
tags:
- cat_operacional
- deploy
- gates
- grp_operacao_melhoria
- operacao-continuidade
- produção
- rollback
title: Deploy Seguro
---


:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design - Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua e mensurável.  

Os capítulos operacionais implementam o SbD-ToE em contextos técnicos específicos. Estes capítulos traduzem as prescrições basilares em práticas de **execução verificável**, promovendo a **integração contínua da segurança** ao longo do ciclo de vida do software.
:::


# Deploy Seguro

## 

O momento de *deploy* é, por natureza, o mais delicado de todo o ciclo de vida. Até ao último instante, a aplicação pode estar íntegra, testada e auditada; mas se a passagem a produção for feita de forma insegura, todo o investimento anterior perde valor.  
Estudos de incidentes (ENISA Threat Landscape, relatórios de falhas DevOps) demonstram que o comprometimento de segurança associados ao software ocorrem na **fase de release e operação inicial**, seja por falhas de rastreabilidade, ausência de rollback ou uso de artefactos não confiáveis.  

Este capítulo não se limita a “executar o pipeline”. Procura sim **estabelecer práticas que tornem cada deploy auditável, reversível e proporcional ao risco da aplicação**.  
A segurança do deploy não é apenas uma questão técnica: é também uma forma de governação - traduz-se na capacidade de explicar, perante uma auditoria ou incidente, *quem decidiu*, *o que foi aprovado* e *como se garantiu a integridade do que chegou a produção*.  

👉 Este capítulo complementa:  
- **Cap. 07 - CI/CD Seguro**, onde se garante a integridade do build e pipelines.  
- **Cap. 12 - Monitorização e Operações**, que cobre a deteção de anomalias e resposta a incidentes no runtime.  

---

## 🧭 O que cobre tecnicamente

O âmbito técnico do *deploy seguro* cobre os seguintes eixos principais:

- Aprovação formal e gates automáticos de release, com critérios definidos por severidade.  
- Deploy apenas a partir de artefactos assinados, com proveniência validada e SBOM associado.  
- Validação funcional e de segurança em ambientes de staging antes da promoção.  
- Gestão rigorosa de credenciais e segredos usados no momento do deploy.  
- Rollback seguro, configurado e testado periodicamente.  
- Rastreabilidade end-to-end, permitindo traçar cada incidente até ao commit original.  
- Monitorização pós-deploy, para avaliar saúde e integridade da aplicação em tempo real.  

Cada um destes elementos não deve ser visto de forma isolada. O verdadeiro rigor científico surge quando são aplicados em conjunto, formando uma **malha de controlos complementares** que reduzem drasticamente a probabilidade de falha ou a sua duração (MTTR).

---

## 🧪 Prescrição prática

O que distingue organizações maduras não é apenas o *que* fazem no deploy, mas a forma como tratam este processo como **um mecanismo documentado e reproduzivel de validação e contenção de risco**.  

- **O que fazer**  
  Garantir que todos os *deploys* ocorrem apenas a partir de artefactos confiáveis, passando por gates de aprovação e validações em staging, com rollback automatizado sempre preparado.  

- **Como fazer**  
  Automatizar pipelines com versionamento, aplicar princípio do menor privilégio, ensaiar rollback em testes regulares e integrar a telemetria do deploy com monitorização e resposta a incidentes.  

- **Quando**  
  Antes de cada release, em cada alteração relevante à infraestrutura e sempre que ocorra um incidente que exija rollback.  

- **Porquê**  
  Porque a fase de deploy é o ponto onde uma falha de segurança pode ter impacto imediato na disponibilidade, na integridade de dados e na reputação organizacional. A aplicação destas práticas responde diretamente a normas como **SSDF RV.1/RV.4**, **SLSA L3**, e é requerida em diretivas como a **NIS2** e normas ISO (27034, 27001).  

---

## 👥 Papéis envolvidos

Nenhum *deploy* seguro é responsabilidade de um só perfil. A prática exige **coordenação transversal**:

- **Dev** → garante que o artefacto está pronto, assinado e documentado.  
- **QA/Testes** → executa validações funcionais e de segurança em staging.  
- **AppSec** → define e aprova gates de segurança, gerindo exceções formais e temporárias.  
- **DevOps/SRE** → executa pipelines, prepara rollback e assegura rastreabilidade técnica.  
- **Gestão de Produto** → toma a decisão final de *go/no-go* e documenta a aceitação de risco residual.  

Esta matriz de papéis não é opcional: é o que garante que **cada deploy é simultaneamente técnico e governado**, capaz de resistir tanto a falhas operacionais como a escrutínio regulatório.  

---

## 📜 Políticas Organizacionais Relevantes

| Política | Obrigatória? | Aplicação | Conteúdo mínimo |
|----------|--------------|-----------|-----------------|
| Política de Deploy Seguro | Sim | DevOps/SRE + AppSec | Deploy apenas de artefactos assinados e rastreáveis |
| Política de Aprovação de Release | Sim | Gestão de Produto + AppSec | Gates formais, critérios por criticidade, exceções registadas |
| Política de Rollback | Sim | DevOps/SRE | Rollback automatizado, testado periodicamente |
| Política de Validação em Staging | Recomendado | QA/Testes | Validação funcional + segurança antes da promoção |
| Política de Monitorização Pós-Deploy | Sim | DevOps + GRC | Logs de deploy + métricas de saúde |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do manual**, onde estas políticas estão consolidadas transversalmente.
