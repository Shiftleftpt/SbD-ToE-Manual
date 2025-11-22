---
id: ameacas-mitigadas
title: Ameaças Mitigadas por Práticas do Capítulo 01
sidebar_position: 50
tags: [ameacas, canon, controlo, mitigacao, risco]
---

# 🔐 Ameaças Mitigadas - Capítulo 01: Classificação da Criticidade Aplicacional

Este capítulo **não define controlos técnicos diretos**, mas estabelece a **estrutura de decisão que governa a aplicação proporcional e justificada de segurança em software**. A ausência desta estrutura gera múltiplas ameaças - técnicas, organizacionais e processuais.

> A correta classificação do risco é **pré-condição de todos os controlos eficazes**. A sua ausência compromete por completo o modelo SbD-ToE.

---

## 🎯 Categoria 1 - Falha de proporcionalidade no esforço de segurança

| Ameaça                                         | Fonte                        | Como surge                                                 | Como a prática mitiga                                                                  | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|------------------------------------------------|-------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------|
| Falta de aplicação de controlos mínimos        | OWASP ASVS 1.1               | Equipa assume que não é necessário                         | Classificação formal obriga a aplicar controlos por nível de risco                      | `addon/matriz-controlos-por-risco.md`      | ✅                                     |
| Overengineering e fricção excessiva            | OSC&R P1.1                   | Equipa aplica todos os controlos independentemente do risco| Modelo de proporcionalidade evita sobreproteção sem justificação                       | `addon/modelo-classificacao-eixos.md`      | ✅                                     |
| Inconsistência entre projetos com mesmo risco  | BSIMM13 - Governance G2.3    | Cada equipa aplica regras diferentes                       | Classificação centralizada normaliza decisões por perfil de risco                     | `addon/matriz-controlos-por-risco.md`      | ✅                                     |
| Segurança opcional em produtos low-risk        | SSDF PW.1 / ENISA SDLC       | Sem política clara, produtos L1 não têm controlos mínimos   | Mapeamento obriga baseline mínima para todos os perfis                                 | `addon/modelo-classificacao-eixos.md`      | ✅                                     |

---

## 🔁 Categoria 2 - Falhas por ausência de revisão ou rastreabilidade

| Ameaça                                      | Fonte                              | Como surge                                             | Como a prática mitiga                                                             | Controlos associados                           | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|-------------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------|----------------------------------------|
| Mudanças críticas sem reclassificação       | CAPEC-137 / ISO 27005 Sec.10       | Funcionalidade nova altera risco, sem nova avaliação   | Modelo define pontos de reavaliação e templates para análise de impacto           | `addon/ciclo-vida-risco.md`, `15-aplicacao-lifecycle.md` | ✅ |
| Integração com APIs ou terceiros ignorada   | STRIDE (Elevation of Privilege)    | Exposição alargada sem impacto revisto                 | DRP e BIA forçam reclassificação por alteração de superfície                       | `addon/adopcao-drp-bia.md`                 | ✅                                     |
| Deploy com risco alterado não revisto       | MITRE - T1589 / T1608              | Mudança de contexto técnico sem análise                | Checklist força revisão por eventos críticos no ciclo de vida                     | `checklist-revisao.md`               | ❌ Cap. 15                             |
| Versões diferentes com classificações divergentes | OSC&R / SSDF RM.1              | Patch ou major release altera criticidade, sem avaliação | Modelo impõe versão rastreável por classificação                                  | `addon/risco-residual.md`                 | ✅                                     |

---

## 🗃️ Categoria 3 - Documentação e justificação insuficientes

| Ameaça                                  | Fonte                            | Como surge                                               | Como a prática mitiga                                                     | Controlos associados                            | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------|-----------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------|----------------------------------------|
| Aceitação informal de riscos críticos   | CAPEC-1003 / SSDF RM.2           | Sem registo formal da aceitação                          | Checklist + modelo de aprovação formal com rastreio de owners              | `addon/criterios-aceitacao-risco.md`         | ✅                                     |
| Impossibilidade de auditoria posterior  | ISO 27005 Sec.8.2 / SSDF RV.3    | Decisão de segurança sem rasto                           | Versionamento obrigatório e rastreio de decisão por eixo e owner           | `addon/risco-residual.md`                    | ✅                                     |
| Risco aceite por responsáveis inapropriados | BSIMM13 - G1.1                | Quem aprova não tem legitimidade                         | Critérios de aceitação forçam owner técnico e de negócio                    | `addon/criterios-aceitacao-risco.md`         | ✅                                     |
| Falta de explicabilidade regulatória    | NIST 800-30 Step 3               | Autoridade não consegue justificar proteção diferencial   | Documentação obriga a descrição da base de decisão                          | `addon/modelo-classificacao-eixos.md`        | ✅                                     |

---

## 🧠 Categoria 4 - Risco técnico mal definido

| Ameaça                                  | Fonte                              | Como surge                                                  | Como a prática mitiga                                                         | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------|-------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------|
| Interfaces expostas mal avaliadas       | STRIDE (Information Disclosure)     | Serviços públicos tratados como internos                    | Eixo E define criticidade por exposição                                      | `addon/01-modelo-classificacao-eixos.md`      | ❌ Cap. 03, Cap. 04                    |
| Dados sensíveis não reconhecidos        | CAPEC-112 / ISO 27005               | Falta de classificação de dados tratados                    | Eixo D impõe análise por tipo e sensibilidade de dados                        | `addon/08-mapeamento-ameacas-risco.md`        | ❌ Cap. 02                            |
| Assunção de ambientes seguros por defeito | ENISA Threat Landscape 2022      | Ambientes assumidos como protegidos sem validação           | DRP e matriz forçam consideração do ambiente de execução                      | `addon/03-adopcao-drp-bia.md`                 | ✅                                     |
| Ignorar dependências críticas           | OSC&R / SSDF PW.4                  | Dependência de serviços não identificada como risco         | Mapeamento de ameaça + eixo I (impacto externo)                              | `addon/08-mapeamento-ameacas-risco.md`        | ❌ Cap. 05                            |

---

## 📉 Categoria 5 - Controlo deficiente da evolução do risco

| Ameaça                                     | Fonte                                | Como surge                                             | Como a prática mitiga                                                      | Controlos associados                           | 🧩 Mitigada apenas por este capítulo? |
|--------------------------------------------|---------------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------|----------------------------------------|
| Risco residual nunca revisto               | CAPEC-115 / ISO 27005 Sec.9          | Mitigações aplicadas, mas risco não revisto            | Modelo obriga definição explícita de risco residual                         | `addon/06-risco-residual.md`                   | ✅                                     |
| Falta de eventos de reavaliação planeados  | SSDF RM.3 / NIST 800-30 Step 4       | Risco só é revisto por iniciativa informal             | Integração com o ciclo de vida define marcos obrigatórios                   | `addon/07-ciclo-vida-risco.md`                 | ✅                                     |
| Reclassificação dependente de exceções     | BSIMM13 - Governance                 | Apenas casos problemáticos são reavaliados             | Política e checklist impõem reavaliação cíclica                             | `20-checklist-revisao.md`                | ❌ Cap. 14                            |
| Decisões de risco sem feedback do negócio  | ENISA DevSecOps / IR Governance      | Aceitação de risco feita sem visão de impacto global   | Modelo força articulação com owner funcional e impacto de negócio           | `addon/09-criterios-aceitacao-risco.md`        | ✅                                     |

---

## ✅ Conclusão

A aplicação rigorosa deste capítulo garante que:

- A **necessidade, intensidade e legitimidade** da aplicação de segurança são justificadas, rastreáveis e auditáveis;
- Os riscos são formalmente classificados, revistos e aceites com base em critérios objetivos;
- Nenhum controlo técnico (dos capítulos seguintes) é aplicado de forma cega, redundante ou ausente.

> 📌 Este capítulo **mitiga diretamente pelo menos 15 ameaças únicas** que não são tratadas em mais nenhum ponto do manual.

> ⚠️ A ausência desta prática **põe em causa a aplicabilidade proporcional** de todo o modelo SbD-ToE - comprometendo desde a definição de requisitos até à rastreabilidade de exceções.

