---
id: template-validacao-contractors
title: Template de Validação de Contractors
description: Checklist e modelo de validação estruturado para triagem, aprovação e onboarding de contractors
tags: [governanca, contractors, validacao, triagem, checklist, onboarding]
---

# 📋 Template de Validação de Contractors

**Versão:** 1.0  
**Última atualização:** Novembro 2025  
**Responsável:** HR + AppSec Engineer  
**Frequência de revisão:** Anual (validar contra políticas de segurança mais recentes)

---

## 📖 Uso deste Template

Este documento serve como **checklist estruturado de validação para novos contractors** antes de contratação formal ou acesso a sistemas. É utilizado em **US-06 (validação inicial de fornecedores)** e **US-15 (preparação técnica pré-acesso)**.

**Responsabilidades:**
- **Procurement Officer:** Coordenação do fluxo, preencher partes 1–3
- **AppSec Engineer:** Preencher partes 4–5, validação de segurança
- **Tech Lead:** Validar requisitos técnicos e preparação (parte 6)
- **HR:** Verificação de referências e documentação legal (parte 2)

**Tempo estimado:** 2–3 semanas antes de data de início

---

## ✅ PARTE 1: Informações Básicas

| Campo | Preenchimento | Observações |
|-------|---------------|-------------|
| **Nome completo do contractor** | [_______________] | |
| **Email corporativo** | [_______________] | Será criado após aprovação |
| **Telemóvel de contacto** | [_______________] | |
| **Nacionalidade** | [_______________] | Relevante para data residency (GDPR, etc.) |
| **Data de início planeada** | [_______________] | |
| **Duração do contrato** | [_______________] | Ex.: 3 meses, 6 meses, indefinido |
| **Fornecedor/Agência** | [_______________] | Se aplicável |
| **Papel/Função** | [_______________] | Ex.: Backend Developer, DevOps Engineer, QA |
| **Equipa/Projeto** | [_______________] | |
| **Tech Lead responsável** | [_______________] | Validador técnico |
| **Security Champion** | [_______________] | Validador de segurança |
| **Classificação de criticidade** | [ ] L1  [ ] L2  [ ] L3 | Definida por Tech Lead + AppSec |

---

## ✅ PARTE 2: Verificação de Background e Documentação Legal

### 2.1 Verificação de Referências

| Item | Sim | Não | N/A | Observações |
|------|-----|-----|-----|-------------|
| **Contato com referência anterior (Tech Lead/Manager)** | [ ] | [ ] | [ ] | Data: [_____]. Feedback: [_________________] |
| **Verificação de background check (polícia/criminal)** | [ ] | [ ] | [ ] | Status: [_____________] |
| **Verificação de credenciais profissionais** | [ ] | [ ] | [ ] | Certificações validadas? [_________________] |

### 2.2 Documentação Legal

| Item | Submetido | Validado | Observações |
|------|-----------|----------|-------------|
| **Contrato assinado** | [ ] | [ ] | Data: [_____] |
| **NDA (Non-Disclosure Agreement)** | [ ] | [ ] | Assinado digitalmente? [ ] Sim |
| **Confidentiality Agreement** | [ ] | [ ] | Duração pós-término: [___________] |
| **IP Assignment (se aplicável)** | [ ] | [ ] | Código desenvolvido pertence a: [__________] |
| **Non-Compete (se aplicável)** | [ ] | [ ] | Duração: [_____], âmbito: [____________] |
| **Data Protection/GDPR compliance** | [ ] | [ ] | Contractor confirmou aceitar processamento de dados? |

---

## ✅ PARTE 3: Avaliação Técnica Inicial

### 3.1 Skills e Background Técnico

| Questão | Resposta | Validado por | Observações |
|---------|----------|--------------|-------------|
| **Experiência em segurança** | [_______________] | Tech Lead | Ex.: "2 anos em secure coding" |
| **Experiência com ferramentas de segurança?** | [ ] Sim [ ] Não | AppSec | Quais: [__________________] |
| **Experiência anterior em ambientes regulatórios (DORA, ISO, PCI)?** | [ ] Sim [ ] Não | AppSec | Detalhes: [__________________] |
| **Certificações relevantes** | [_______________] | HR | Ex.: OSCP, CEH, CSSLP, CKAD |
| **Linguagens de programação** | [_______________] | Tech Lead | Relevantes para projeto |
| **CI/CD e Infra experiência** | [ ] Sim [ ] Não | DevOps | Ferramentas: [__________________] |
| **Conhecimento de containers/Kubernetes** | [ ] Sim [ ] Não | DevOps | Nível: [ ] Básico [ ] Intermédio [ ] Avançado |

### 3.2 Triagem de Segurança Inicial

| Questão | Resposta | Avaliação |
|---------|----------|-----------|
| **Contractor concorda em aceitar política de segurança da empresa?** | [ ] Sim [ ] Não | Status: [ ] ✅ Approved [ ] ❌ Rejected |
| **Contractor confirmou que não tem conflito de interesses?** | [ ] Sim [ ] Não | Status: [ ] ✅ Approved [ ] ❌ Rejected |
| **Contractor concorda em usar equipamentos corporativos seguros?** | [ ] Sim [ ] Não | Status: [ ] ✅ Approved [ ] ❌ Rejected |
| **Contractor confirmou que não está em lista de sanções internacionais?** | [ ] Sim [ ] Não | Status: [ ] ✅ Approved [ ] ❌ Rejected |

**Resultado da Triagem:** [ ] ✅ Aprovado  [ ] ❌ Rejeitado

**Justificação (se rejeitado):** [_____________________]

---

## ✅ PARTE 4: Validação de Segurança (AppSec Engineer)

### 4.1 Questões de Security Awareness (Nível Mínimo)

**Instruções:** Enviar este formulário ao contractor. Score mínimo requerido: **70%**

| # | Pergunta | Resposta Esperada | Contractor Respondeu? | Score |
|---|----------|------------------|----------------------|-------|
| 1 | Qual é o primeiro passo se suspeita de phishing? | Não responder, reportar a segurança | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 2 | Pode partilhar credenciais corporativas com colegas? | Não, cada um tem acesso pessoal | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 3 | Qual é o procedimento se esquece password? | Contactar IT/Password reset seguro | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 4 | Pode conectar VPN pessoal ou proxy externo? | Não, apenas VPN corporativa | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 5 | Qual é o processo para reportar incidente de segurança? | Contactar [CISO/Security email] imediatamente | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 6 | Pode trazer dispositivos pessoais não autorizados? | Não, apenas equipamentos aprovados | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 7 | MFA é obrigatório para login corporativo? | Sim, sempre ativar MFA | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 8 | Qual é a duração da sessão antes de timeout automático? | [Política interna, ex.: 30 min] | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 9 | Pode deixar estação desbloqueada sem vigilância? | Não, lock ou logout obrigatório | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |
| 10 | Qual é a política de confidencialidade pós-término? | Dados confidenciais permanecem confidenciais | [ ] Sim [ ] Não | [ ] ✅ [ ] ❌ |

**Score Total:** __/10 (__%)  
**Mínimo requerido:** 70% (7/10)  
**Resultado:** [ ] ✅ PASSED  [ ] ❌ FAILED (Retry: [ ] Agendado em [____])

---

### 4.2 Validação de Equipamentos

| Item | Status | Observações |
|------|--------|-------------|
| **Computador é pessoal ou corporativo?** | [ ] Pessoal [ ] Corporativo | Se pessoal, requer aprovação especial |
| **Sistema operativo e versão** | [_______________] | Deve estar atualizado (últimos 6 meses de patches) |
| **Antivírus/Antimalware instalado?** | [ ] Sim [ ] Não | Ferramenta: [__________________] |
| **Firewall ativado?** | [ ] Sim [ ] Não | |
| **Disco criptografado (LUKS/BitLocker)?** | [ ] Sim [ ] Não | Obrigatório para L2–L3 |
| **Última verificação de malware** | [_______________] | Data e resultado |
| **Confirmação: Contractor compromete-se a manter equipamento seguro** | [ ] Sim [ ] Não | |

**Resultado:** [ ] ✅ Aprovado  [ ] ⚠️ Condicional (com plano) [ ] ❌ Rejeitado

---

### 4.3 Avaliação de Risco (AppSec Engineer)

| Dimensão | L1 | L2 | L3 | Observações |
|----------|----|----|-----|-------------|
| **Risco de acesso a dados sensíveis** | [ ] | [ ] | [ ] | [_________________] |
| **Risco de modificação de código crítico** | [ ] | [ ] | [ ] | [_________________] |
| **Risco de elevação de privilégios** | [ ] | [ ] | [ ] | [_________________] |
| **Risco de vazamento de IP/confidenciais** | [ ] | [ ] | [ ] | [_________________] |

**Risco Geral:** [ ] Baixo [ ] Médio [ ] Alto [ ] Muito Alto  
**Aprovação:** [ ] ✅ Recomendado  [ ] ⚠️ Condicional [ ] ❌ Não recomendado

**Justificação:** [_____________________________________]

---

## ✅ PARTE 5: Relatório de Decisão

### 5.1 Síntese de Validação

| Critério | Resultado | Responsável |
|----------|-----------|-------------|
| **Documentação Legal** | [ ] ✅ Completo [ ] ⚠️ Pending [ ] ❌ Falta | [__________] |
| **Background Check** | [ ] ✅ Passed [ ] ⚠️ Review [ ] ❌ Failed | [__________] |
| **Técnica/Skills** | [ ] ✅ Approved [ ] ⚠️ Conditional [ ] ❌ Rejected | [__________] |
| **Security Awareness** | [ ] ✅ Passed (>70%) [ ] ⚠️ Retry [ ] ❌ Failed | [__________] |
| **Avaliação de Risco** | [ ] ✅ Approved [ ] ⚠️ Conditional [ ] ❌ Not recommended | [__________] |

### 5.2 Decisão Final

**Decisão Geral:**  
[ ] ✅ **APROVADO** → Prosseguir para Preparação Técnica (US-15)  
[ ] ⚠️ **APROVADO COM CONDIÇÕES** → Especificar plano de mitigação abaixo  
[ ] ❌ **REJEITADO** → Contactar Procurement com justificação  

**Plano de Mitigação (se condicional):**
```
1. [_____________________________] → Prazo: [_____] → Owner: [_______] → Status: [ ]
2. [_____________________________] → Prazo: [_____] → Owner: [_______] → Status: [ ]
3. [_____________________________] → Prazo: [_____] → Owner: [_______] → Status: [ ]
```

### 5.3 Aprovações Formais

| Papel | Nome | Assinatura Digital | Data | Observações |
|-------|------|-------------------|------|-------------|
| **HR Manager** | [__________] | [Signed] | [____] | |
| **Tech Lead** | [__________] | [Signed] | [____] | |
| **AppSec Engineer** | [__________] | [Signed] | [____] | |
| **Procurement Officer** | [__________] | [Signed] | [____] | Se L2–L3 |

---

## ✅ PARTE 6: Próximos Passos (Pós-Aprovação)

Se APROVADO, as seguintes ações são acionadas automaticamente:

### 6.1 Timeline de Preparação

| Data | Ação | Owner | Status |
|------|------|-------|--------|
| T-14 dias | Sandbox setup + LMS enrollment | DevOps + Training | [ ] Done |
| T-10 dias | Email de bem-vindo + onboarding info | HR | [ ] Done |
| T-7 dias | Formação online iniciada | Training Manager | [ ] Done |
| T-3 dias | Quiz de compreensão (score >80%) | Contractor + AppSec | [ ] Done |
| T-1 dia | Confirmação de conclusão | Security Champion | [ ] Done |
| T-0 (Dia 1) | Acesso concedido + Onboarding técnico | DevOps | [ ] Done |

### 6.2 Checklists Subsequentes

Após aprovação neste template, o contractor segue:
1. **US-15:** Preparação Técnica (Sandbox, NDA, formação)
2. **US-16:** Trilho de Formação Obrigatória (Cap. 13)
3. **Acesso Real:** Após conclusão de US-15 e US-16

---

## 📎 Anexos e Referências

- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)
- [US-06: Fluxo de Validação de Fornecedores](aplicacao-lifecycle.md#us-06)
- [US-15: Preparação Técnica de Contractors](aplicacao-lifecycle.md#us-15)
- [US-16: Trilho de Formação](aplicacao-lifecycle.md#us-16)
- [Modelo de Governação](01-modelo-governancao.md)

---

## 🏁 Notas Finais

- **Este template é obrigatório para L2–L3** e recomendado para L1.
- **Manter histórico de todas as validações** por 7 anos (DORA requirement).
- **Revisar este template anualmente** contra políticas de segurança atualizadas.
- **Escalação:** Se algum campo levanta red flag, contactar CISO antes de aprovação.
