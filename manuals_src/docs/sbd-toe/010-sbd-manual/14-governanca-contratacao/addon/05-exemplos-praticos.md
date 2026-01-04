---
id: exemplos-aplicacao-governanca
title: Exemplos de Aplicação e Onboarding
sidebar_position: 5
description: Casos práticos de aplicação de governação de segurança em projetos, exceções e contratações
tags: [exemplos, excecoes, onboarding, governance]
---



# 🧪 Exemplos de Aplicação no Ciclo de Governaça

Este anexo fornece **exemplos práticos e reutilizáveis** para aplicar os conceitos de governança e contratação de forma operativa, alinhada com os restantes elementos do modelo SbD-ToE.  
Inclui também a verificação de **formação obrigatória** para funções críticas (owners, aprovadores, validadores), em conformidade com o Cap. 13.

---

## 📜 1. Exemplo de aprovação de exceção

**Título:** [SEC] Aprovação de exceção de controlo de validação de entrada para app "GestDoc"

**Justificação:**  

A aplicação utiliza uma framework legada sem suporte nativo a validação automática. O risco foi mitigado com proxy de validação externo e logging reforçado.

**Nível de risco:** L2  

**Controlos substituídos:** REQ-VAL-002, REQ-VAL-006  
**Compensação aplicada:** Validação em proxy com schema + testes de fuzzing  

**Validade da exceção:** 6 meses  
**Owner:** paula.lima@empresa  

**Aprovadores:** AppSec + gestor de produto  
**Formação obrigatória validada:** ✔️ Owners e aprovadores com formação SbD ativa (Cap. 13)

---

## 📄 2. Exemplo de onboarding de fornecedor

**Título:** [ONB] Validação de fornecedor para integração de pagamento externo (serviço "XPay")

**Classificação de risco do sistema:** L3

**Checklist de onboarding:**
- [x] Questionário de segurança preenchido
- [x] SBOM fornecido
- [x] Cláusulas contratuais de segurança assinadas
- [x] SLA de resposta a incidentes < 24h
- [ ] Validação externa de controlos (em curso)

**Owner da integração:** ana.gomes@empresa  

**Observação:** onboarding condicionado à entrega de evidência de testes antes de go-live  
**Formação obrigatória validada:** ✔️ Owner e analista AppSec com formação em validação de terceiros (Cap. 13)

---

## 🔄 4. Exemplo de renovação contratual com revisão de requisitos

**Título:** [REV] Revisão de cláusulas e requisitos na renovação do contrato com fornecedor “DataStore”

**Contexto:**  

Contrato de licenciamento de software de armazenamento em cloud, utilizado por sistemas L2.

**Ações realizadas:**
- [x] Atualização das cláusulas contratuais para refletir novos requisitos (REQ-DAT-004, REQ-BKP-002)
- [x] Validação técnica do SBOM do agente de sincronização
- [x] Aceitação formal de SLA de mitigação de CVEs em `<`5 dias
- [x] Formação atualizada da PO e da equipa de IT Ops envolvida

**Owner da renovação:** sofia.rodrigues@empresa  

**Data da nova assinatura:** 2025-07-10  
**Formação obrigatória validada:** ✔️ Documentada em repositório interno (Cap. 13)

---

## 🧪 5. Exemplo de exceção temporária com reavaliação planeada

**Título:** [SEC] Aprovação excecional para ausência de MFA na ferramenta de gestão de builds

**Justificação:**  

A ferramenta usada (BuilderX) não suporta autenticação multifator. O risco foi compensado com restrição de IPs e logging contínuo.

**Nível de risco:** L3  

**Requisito em falta:** REQ-ACC-007  
**Compensação:** Limitação de acesso por VPN + análise diária dos logs  

**Aprovação:** Equipa AppSec + DevSecOps + CISO  
**Validade:** 3 meses com reavaliação marcada no backlog de segurança  

**Formação obrigatória validada:** ✔️ CISO e responsável técnico com formação de exceções (Cap. 13)

---

## 🛠️ 6. Exemplo de fornecedor rejeitado após onboarding incompleto

**Título:** [ONB] Rejeição de fornecedor “CloudParser” para pipeline de transformação de dados

**Classificação de risco da aplicação:** L3

**Motivo da rejeição:**
- [x] Falha na entrega de SBOM atualizado
- [x] Recusa de cláusulas contratuais sobre auditoria
- [x] Incapacidade de comprovar canal de resposta a incidentes

**Decisão:** Rejeitado pela comissão de aprovação técnica (AppSec, Owner, GRC)  

**Owner:** miguel.pinto@empresa  
**Observações:** alternativa viável já identificada (fornecedor “ParseVault”)

---

## 📆 3. Template de registo de decisão de risco

**Formato sugerido:** Jira / SharePoint / Excel rastreável

| Campo                     | Valor                                                          |
|--------------------------|----------------------------------------------------------------|
| Nome da aplicação         | app-inventario                                                |
| Nível de risco            | L2                                                             |
| Requisitos não aplicados  | REQ-LOG-005, REQ-AUD-003                                       |
| Justificação técnica      | Sem infra para retenção prolongada; compensado com snapshots  |
| Compensação aplicada      | Alertas via SIEM + backup externo                             |
| Owner e aprovação         | nuno.ferreira@empresa + CISO                                  |
| Validade da decisão       | 3 meses + reavaliação programada                              |
| Formação obrigatória      | ✔️ Ambos com certificação interna válida (`<`12 meses)

---

## ✅ Recomendações

- Estes modelos devem ser **normalizados e reutilizados** entre projetos
- Podem ser disponibilizados via templates em Confluence, Git ou ALM
- Devem ser associados aos artefactos de aplicação, fornecedor ou release
- A existência destes registos suporta auditorias, governance e decisão executiva
- A **formação obrigatória para funções críticas** (Cap. 13) deve ser verificada antes de validações formais
- Sempre que parte do processo seja suportada por mecanismos automatizados, deve ficar explícito no registo quem validou e assumiu a decisão final.

---
