---
description: Checklist binário e auditável para avaliar a adoção prática das práticas
  prescritas no Capítulo 09 - Containers e Imagens
id: checklist-revisao
sidebar_label: Checklist de Revisão
sidebar_position: 20
tags:
- auditoria
- checklist
- containers
- imagens
- kubernetes
- supply chain
- supply-chain
title: Checklist - Containers e Imagens
---


# ✅ Checklist de Revisão Periódica — Containers e Imagens

Este checklist aplica-se a todos os projetos e pipelines que **constroem, distribuem ou executam containers e imagens** no âmbito do Capítulo 09 - Containers e Imagens.  
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições deste capítulo**, permitindo:

- Controlo sistemático da segurança na cadeia de construção e execução de containers;  
- Verificação por projeto em momentos-chave do ciclo de vida (build, deploy, operação);  
- Geração de indicadores de conformidade técnica e maturidade de *supply chain security*.

> 🗓️ **Recomenda-se a sua aplicação a cada release significativa**, ou sempre que existirem alterações nas imagens base, pipelines, registos ou configurações de *runtime*.

---

## 📋 Itens de verificação

| Item                                                                                                           | Verificado? |
|----------------------------------------------------------------------------------------------------------------|-------------|
| As imagens base utilizadas são oficiais, aprovadas e mantidas pela organização?                               | ☐           |
| Cada imagem utiliza uma *tag* imutável ou *digest SHA* para garantir reprodutibilidade?                        | ☐           |
| Existe *pipeline* automatizado de *image scanning* (vulnerabilidades, licenças, configuração)?                | ☐           |
| As vulnerabilidades críticas ou altas bloqueiam o *build* ou *deploy*?                                        | ☐           |
| Todas as imagens são assinadas digitalmente e a sua integridade é verificada antes da execução?               | ☐           |
| As imagens são geradas a partir de *Dockerfiles* ou manifestos versionados e auditáveis?                      | ☐           |
| São aplicados controlos de *least privilege* (utilizador não root, capacidades mínimas)?                      | ☐           |
| O *runtime* aplica políticas de isolamento (seccomp, AppArmor, SELinux, namespaces)?                           | ☐           |
| Os registos de containers estão privados, autenticados e com políticas de acesso restritivas?                 | ☐           |
| É verificada a proveniência (*attestation*) das imagens antes do *deploy*?                                    | ☐           |
| Os manifestos de *deploy* (Kubernetes, Compose, Helm, etc.) são validados contra políticas de segurança?      | ☐           |
| Existe retenção controlada e limpeza periódica de imagens obsoletas ou vulneráveis?                           | ☐           |
| Todas as exceções técnicas (imagens antigas, vulnerabilidades aceites) estão formalmente justificadas?        | ☐           |
| As evidências de *scanning*, assinaturas e aprovações estão arquivadas ou versionadas?                        | ☐           |
| As políticas organizacionais associadas (ver *Policies Relevantes*) estão implementadas e verificadas?        | ☐           |

---

## 🔄 Notas de aplicação prática

- Este checklist pode ser convertido em **etapa automatizada de CI/CD**, formulário digital de validação ou dashboard de conformidade de containers.  
- Cada item deve ser tratado como **indicador binário (sim/não)**, permitindo cálculo de KPIs de adoção por projeto, pipeline ou equipa.  
- A validação completa deste checklist confirma **conformidade técnica com o Capítulo 09**, sustentando auditorias de segurança e avaliações de maturidade SbD-ToE.  
- Os resultados podem ser correlacionados com o **Capítulo 05 - Dependências e SBOM**, garantindo rastreabilidade total da cadeia de fornecimento.

> ❗ Este capítulo é **essencial para a integridade e segurança da cadeia de construção e entrega de software**.  
> A ausência destas práticas compromete a confiança nos artefactos distribuídos e a conformidade com requisitos de *supply chain security* previstos em NIS 2 e DORA.
