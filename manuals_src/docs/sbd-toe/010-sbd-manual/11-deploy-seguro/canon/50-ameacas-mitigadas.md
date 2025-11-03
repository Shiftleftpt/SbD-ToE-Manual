---
id: ameacas-mitigadas
title: Ameaças Mitigadas — Deploy Seguro
description: Visão bottom-up das ameaças mitigadas pelas práticas de deploy seguro descritas neste capítulo.
tags: [ameaças, mitigação, deploy, execução, rollback, toggle, runtime, ssdf, stride, capec, osc&r]
sidebar_position: 50
---


# 🔐 Ameaças Mitigadas — Capítulo 11: Deploy e Controlo de Execução

Este capítulo define práticas para **entrega segura, validação formal, ativação controlada e execução reversível** de funcionalidades em produção.  
As ameaças mitigadas surgem no momento mais sensível do SDLC: **a passagem real para runtime**.

> ✅ As práticas deste capítulo são cruciais para garantir que o código entregue é **validado, rastreável, reversível e controlado em ambiente de produção**.

---

## 🚨 Categoria 1 – Execução de código não validado

| Ameaça                                  | Fonte                           | Como surge                                              | Como a prática mitiga                                                                 | Controlos associados                          |
|-----------------------------------------|----------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------|
| Código em produção sem validação        | SSDF PW.6 / CAPEC-137           | Ausência de testes ou aprovação antes do deploy         | Validações formais + gates automatizados no pipeline                                   | `addon/04-validacoes-pre-deploy.md`           |
| Ativação funcional sem controlo         | STRIDE / OWASP Feature Toggles  | Feature toggles ativados sem validação ou aprovação     | Integração com fluxo de aprovação + rastreabilidade de toggles                         | `addon/03-feature-flags-e-toggle.md`          |
| Promoção manual fora do CI/CD           | OWASP CI/CD / SLSA              | Bypass do pipeline ou acesso direto ao ambiente         | Modelo de controlo de execução com obrigatoriedade de pipeline                         | `addon/01-modelo-controle-execucao.md`        |

---

## 🔁 Categoria 2 – Ausência de rollback e reversibilidade

| Ameaça                            | Fonte                             | Como surge                                      | Como a prática mitiga                                                           | Controlos associados                       |
|-----------------------------------|------------------------------------|------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------|
| Deploy falhado sem rollback       | SSDF PW.5 / ISO 27034             | Falha crítica bloqueia sistema                  | Rollback automático + versionamento e reversibilidade                            | `addon/06-controle-versao-e-rollback.md`   |
| Feature irreversível              | OWASP Feature Toggle               | Toggle ativado sem fallback seguro              | Design de toggles com reversão e estado "off-by-default"                         | `addon/03-feature-flags-e-toggle.md`       |
| Falha sem reação                  | CAPEC-173 / OSC&R Runtime Tamper  | Problemas em produção sem rollback estruturado  | Trigger automático de rollback com base em métricas e alertas                    | `addon/05-monitorizacao-e-reacao.md`       |

---

## 🧪 Categoria 3 – Validação deficiente em produção

| Ameaça                                   | Fonte                              | Como surge                                         | Como a prática mitiga                                                              | Controlos associados                          |
|------------------------------------------|-------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------|
| Release conjunta sem segmentação         | OWASP SAMM / BSIMM DR1             | Múltiplas features ativadas em simultâneo         | Práticas de release progressivo com rollout segmentado                             | `addon/02-praticas-release-management.md`      |
| Feature exposta a todos os utilizadores  | CAPEC-112 / STRIDE (Elevation)     | Toggle sem escopo por grupo, região ou perfil     | Segmentação por utilizador, tempo, localização ou perfil                           | `addon/03-feature-flags-e-toggle.md`           |
| Falta de validação operacional           | ISO 27001 A.14.2.4 / DSOMM Runtime | Código testado apenas em ambientes não representativos | Validação final em ambiente de staging espelho antes da promoção                  | `addon/08-segregacao-e-validacao-operacional.md` |

---

## 📉 Categoria 4 – Falta de monitorização e resposta a falhas

| Ameaça                                  | Fonte                              | Como surge                                       | Como a prática mitiga                                                            | Controlos associados                      |
|-----------------------------------------|-------------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|
| Falhas pós-deploy não detetadas         | SSDF RV.3 / BSIMM Deployment       | Sem métricas ou alertas após deploy              | Observabilidade com métricas definidas, logs e alertas de erro                    | `addon/05-monitorizacao-e-reacao.md`      |
| Reação tardia a problemas críticos      | STRIDE / ENISA DevSecOps           | Equipa não notificada ou sem visibilidade        | Integração com incident response, notificações e ownership definido               | `addon/05-monitorizacao-e-reacao.md`      |
| Eventos críticos ignorados              | CAPEC-310 / DSOMM                  | Sem plano para lidar com falhas runtime          | Critérios definidos para rollback manual/automático e plano de ação               | `addon/06-controle-versao-e-rollback.md`  |

---

## 🔒 Categoria 5 – Exposição acidental de funcionalidades

| Ameaça                                    | Fonte                              | Como surge                                       | Como a prática mitiga                                                              | Controlos associados                          |
|-------------------------------------------|-------------------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------|
| Toggle ativado inadvertidamente           | OWASP Feature Toggle / STRIDE      | Flag com valor default ativado                   | Estado "off-by-default", require de aprovação e revisão formal                     | `addon/03-feature-flags-e-toggle.md`           |
| Release sem segmentação geográfica ou lógica | BSIMM13 / OWASP SAMM            | Mudança aplica-se a toda a base de utilizadores | Rollout progressivo: canário, blue-green, scoped deployment                        | `addon/07-deploy-progressivo-e-risco.md`       |
| Execução de função crítica não validada   | STRIDE (Availability) / ISO 27034 | Falta de readiness gates operacionais            | Validação final de readiness com rollback validado e dupla aprovação               | `addon/08-segregacao-e-validacao-operacional.md` |

---

## ✅ Conclusão

O Capítulo 11 mitiga ameaças diretamente associadas ao **momento mais sensível do ciclo de vida: o deploy e execução real do software em produção**, incluindo:

- Falhas de validação pré-execução;
- Ativações acidentais e inseguras;
- Ausência de rollback;
- Falta de segmentação e readiness;
- Visibilidade e resposta runtime insuficientes.

> 🎯 Pelo menos **12 ameaças são mitigadas exclusivamente por este capítulo**, o que o torna **essencial para runtime seguro e controlado**.

> 🔐 Integra práticas obrigatórias para cumprir **SSDF**, **SLSA**, **OWASP SAMM**, **BSIMM13**, **ENISA DevSecOps**, **CIS Controls**, **ISO 27001**, e domínios do **DSOMM – Design & Development**.

