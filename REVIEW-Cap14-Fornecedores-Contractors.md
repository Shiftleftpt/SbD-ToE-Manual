# REVIEW: Capítulo 14 - Governança e Contratação
## Gaps Identificados em Validação e Preparação de Fornecedores/Contractors

**Data:** 13 Novembro 2025  
**âmbito:** Análise de cobertura de contratação, validação e onboarding de fornecedores críticos e contractors

---

## 1. Sumário de Findings

### ✅ O que o Cap. 14 cobre bem

| Aspecto | User Story | Cobertura |
|---------|-----------|-----------|
| Exceções formais com alçadas | US-01 | ✅ Excelente (3 níveis, SLA, calendário automático) |
| Cláusulas contratuais de segurança | US-02 | ✅ Bom (template recomendado, validação jurídica) |
| Validação inicial de fornecedores | US-06 | ✅ Bom (questionário, análise AppSec, registo GRC) |
| Reavaliação contínua de fornecedores | US-14 | ✅ Excelente (trimestral L3, semestral L2, anual L1) |
| Modelo formal de governação | US-12 | ✅ Excelente (alçadas explícitas, papéis, SLAs) |
| Designação de owners de segurança | US-09 | ✅ Bom (Security Champion formal, formação obrigatória) |
| Rastreabilidade organizacional | US-04, 08, 13 | ✅ Excelente (checklist versionado, auditoria) |

---

### ⚠️ Gaps e Áreas de Melhoria

#### **GAP 1: Falta de User Story para "Preparação Técnica de Contractors" (Pré-Onboarding)**

**Problema:**
- US-06 valida fornecedores, mas não define **como preparar contractors tecnicamente** antes de ganhem acesso
- Não há processo estruturado para:
  - Triagem de skills de segurança
  - Trilho de formação obrigatória pré-acesso
  - Teste de compreensão (quiz)
  - Configuração de ambiente sandbox para prática
  - Assinatura de termos de responsabilidade

**Impacto:**
- Contractors podem ganhar acesso sem compreender políticas de segurança
- Risco de erro involuntário (credenciais expostas, acesso a dados não autorizados)
- Falta de evidência de preparação para auditoria/conformidade (DORA, NIS2)

**Recomendação:**
- Criar **US-15: Preparação Técnica e Validação de Contractors/Fornecedores pré-acesso**

---

#### **GAP 2: Falta de Integração Explícita com Cap. 13 (Formação e Onboarding)**

**Problema:**
- Cap. 14 menciona "formação obrigatória (Cap. 13)" em US-09, mas não detalha:
  - Qual trilho de formação é obrigatório por tipo de contractor
  - SLA de conclusão antes de acesso técnico
  - Quem valida compreensão (AppSec vs. HR)
  - Como tracked e reportado

**Impacto:**
- Falta de clareza sobre responsabilidades (HR vs. Security)
- Contractors podem começar antes de formação completa
- Não há evidência consolidada de "contractor ready for access"

**Recomendação:**
- Criar **US-16: Trilho de Formação Obrigatória e Validação pré-Acesso (Contractors)**
  - Complementa US-09 e articula com Cap. 13

---

#### **GAP 3: Falta de Processo de "Offboarding Seguro" de Fornecedores/Contractors**

**Problema:**
- US-14 reavalia fornecedores, mas **não há user story para rescisão, desativação de acesso, e recuperação de ativos**
- Cenários não cobertos:
  - Contractor termina ou muda de projeto
  - Fornecedor descontinua serviço crítico
  - Breach ou incidente crítico em fornecedor
  - Plano de saída testado (US-05 Cap. 14 menciona "plano de saída", mas não está formalizado em US específica)

**Impacto:**
- Contractors podem manter acesso após término
- Ativos (credentials, código, dados) podem não ser recuperados
- Risco de vazamento pós-rescisão

**Recomendação:**
- Criar **US-17: Offboarding Seguro de Contractors e Rescisão de Fornecedores Críticos**

---

#### **GAP 4: Falta de "Monitorização Contínua de Conformidade de Fornecedores" em Runtime**

**Problema:**
- US-14 reavalia fornecedores **periodicamente** (anual/semestral), mas **não há monitorização contínua** de:
  - Incidentes reportados pelo fornecedor em tempo real
  - Novas CVEs em stack do fornecedor
  - Mudanças de SLA não conformes
  - Possíveis breach em fornecedor

**Impacto:**
- Gaps entre ciclos de avaliação (até 12 meses para L1)
- Risco não detetado até próxima reavaliação

**Recomendação:**
- Criar **US-18: Monitorização Contínua de Conformidade de Fornecedores (Alertas e Escalação)**

---

#### **GAP 5: Falta de Template/Checklist Específico para "Validação de Segurança de Contractors"**

**Problema:**
- US-06 menciona "questionário", mas **não existe template concreto** com:
  - Questões de security awareness (nivel mínimo esperado)
  - Verificação de background check
  - Validação de acesso anterior a sistemas sensíveis
  - Compreensão de política de confidencialidade
  - Confirmação de equipamentos seguros (ex.: sem malware)

**Impacto:**
- Variabilidade nas práticas de validação entre equipas
- Critério não claro para aprovação/rejeição

**Recomendação:**
- Criar **addon file: "02-template-validacao-contractors.md"**

---

#### **GAP 6: Falta de "Ambiente Sandbox para Contractors" (Prática de Segurança)**

**Problema:**
- Não há recomendação para criar ambiente isolado onde contractors praticam antes de acesso real
- Risco de erro em produção por falta de experiência em ferramentas

**Impacto:**
- Contractors podem fazer erros críticos em produção
- Falta de confiança da organização

**Recomendação:**
- Adicionar prática em **recomendacoes-avancadas.md**: "Ambiente sandbox isolado para onboarding de contractors"

---

#### **GAP 7: Falta de "Auditoria de Acesso de Contractors"**

**Problema:**
- Não há US específica para **auditar regularmente que contractors têm apenas acesso necessário** (principle of least privilege)
- Risco de "acesso creep" (permissões acumuladas ao longo do tempo)

**Impacto:**
- Contractors podem reter acesso a recursos que não necessitam mais
- Violação de principle of least privilege

**Recomendação:**
- Criar **US-19: Revisão Trimestral de Acesso de Contractors (Least Privilege Validation)**

---

#### **GAP 8: Falta de "Cláusula de Non-Compete e IP/Confidencialidade" em Contratos**

**Problema:**
- US-02 menciona "cláusulas de segurança", mas **não detalha obrigações de confidencialidade, IP ownership, non-compete**
- Risco legal/IP se contractor divulga informação

**Impacto:**
- Falta de proteção legal de propriedade intelectual e dados confidenciais

**Recomendação:**
- Expandir US-02 com template específico que inclui:
  - Confidentiality Agreement (NDA)
  - IP Ownership (código desenvolvido, descobertas)
  - Non-Compete (duração, âmbito)

---

#### **GAP 9: Falta de "Ciclo de Feedback Pós-Projeto" de Contractors**

**Problema:**
- Não há processo para coletar feedback pós-término sobre:
  - Compreensão de políticas
  - Incidentes ou desvios durante projeto
  - Recomendações de melhoria
  - Rating de segurança do contractor

**Impacto:**
- Oportunidade perdida de aprendizagem
- Sem feedback para decisão de re-hire

**Recomendação:**
- Criar **US-20: Feedback Pós-Projeto e Rating de Contractors (para re-hire)**

---

## 2. Propostas de Novas User Stories

### **US-15: Preparação Técnica e Validação de Contractors pré-Acesso**

```markdown
**Contexto.** Contractors ganham acesso sem compreender políticas de segurança, 
ferramentas obrigatórias, ou procedimentos. Risco de erro involuntário.

**História.**  
Como **Security Champion + HR/Recruiter**, quero **executar processo estruturado 
de preparação técnica de contractors (triagem, formação, teste, ambiente sandbox) 
antes de ganhem acesso a sistemas**, para **garantir que estão preparados, 
compreenderam políticas, e podem trabalhar seguramente**.

**BDD.**  
- Dado um novo contractor aprovado por Procurement e validado (US-06)
- Quando chega data de início
- Então trilho de preparação é acionado: formação obrigatória, quiz, sandbox, 
  confirmação de assinatura de NDA

**DoD.**  
- [ ] Checklist de preparação preenchido (triagem skills, formação requerida definida)
- [ ] Trilho de formação baseado em perfil (Dev, DevOps, QA, etc.) iniciado
- [ ] Quiz de compreensão de políticas de segurança completado (score mínimo 80%)
- [ ] Acesso a ambiente sandbox fornecido para prática (ex.: GitHub org privado, 
      aplicação demo)
- [ ] NDA e confidentiality agreement assinados digitalmente
- [ ] Checklist de onboarding técnico validado pela equipa
- [ ] Acesso real a sistemas concedido apenas após todos os passos
- [ ] Registo de "ready for access" documentado em GRC com data e validador

**Integração.** Planeamento; Resp: HR (coordenação) + AppSec Engineer (validação) 
+ Tech Lead (sandbox setup); SLA: Conclusão em 2–3 dias antes de data de início; 
Trigger: Contrato assinado

**Ligações úteis.**  
- [Cap. 13 - Formação e Onboarding](/formacao-onboarding/aplicacao-lifecycle.md)
- [Validação de Fornecedores - US-06 acima](#us-06)
- [Template de Validação Contractors - addon/02](governanca-contratacao/addon/02-template-validacao-contractors.md)
```

---

### **US-16: Trilho de Formação Obrigatória pré-Acesso (Contractors)**

```markdown
**Contexto.** Contractors iniciados sem completar formação de segurança obrigatória. 
Sem integração clara entre Cap. 13 (Formação) e Cap. 14 (Governação).

**História.**  
Como **CISO + Training Manager**, quero **definir trilho de formação obrigatória 
por perfil de contractor, com SLA de conclusão antes de acesso técnico**, para 
**garantir consciência de segurança mínima e conformidade regulatória (DORA, NIS2)**.

**BDD.**  
- Dado um contractor novo iniciado
- Quando trilho de formação é atribuído
- Então deve completar cursos obrigatórios, passar quiz, e ter registo em LMS/HRIS

**DoD.**  
- [ ] Trilho de formação definido por perfil (Dev, DevOps, QA, Arquitetura, etc.)
- [ ] Cursos obrigatórios listados: 
    - [O1] Security Awareness (2h, Cap. 00 + 02)
    - [O2] SbD-ToE Overview (1h, Cap. 01–03)
    - [O3] Coding Practices (2h, Cap. 06) - se developer
    - [O4] CI/CD Security (1h, Cap. 07) - se DevOps
    - [O5] Incident Response (1h, Cap. 12)
- [ ] Quiz de avaliação (score mínimo 80%) completado por cada curso
- [ ] Registo centralizado (LMS ou Confluence) com datas, scores, validador
- [ ] SLA de conclusão comunicado: Máximo 5 dias antes de acesso
- [ ] Notificação automática se SLA em risco
- [ ] Sign-off de "formação completa" fornecido ao AppSec Engineer (libera acesso)

**Integração.** Planeamento + Execução; Resp: Training Manager (coordenação) + 
AppSec Engineer (validação) + HR (rastreabilidade); SLA: Formação completa antes 
de acesso; Trigger: Contractor aprovado (fim de US-06)

**Ligações úteis.**  
- [Cap. 13 - Formação e Onboarding](/formacao-onboarding/aplicacao-lifecycle.md)
- [Designação de Owners - US-09](#us-09)
- [Preparação Técnica - US-15](#us-15-nova)
```

---

### **US-17: Offboarding Seguro de Contractors e Rescisão de Fornecedores**

```markdown
**Contexto.** Contractors terminam e mantêm acesso. Ativos (código, credenciais, 
documentos) não são recuperados. Risco de vazamento pós-rescisão.

**História.**  
Como **Security Champion + HR + DevOps**, quero **executar processo formal de 
offboarding seguro quando contractor termina ou fornecedor é rescindido**, para 
**garantir que acesso é desativado, ativos recuperados, e confidencialidade 
mantida**.

**BDD.**  
- Dado um contractor cuja data de termo é conhecida (ou fornecedor rescindido)
- Quando data de offboarding chega
- Então acesso é revogado, ativos recuperados, e processo é documentado

**DoD.**  
- [ ] Checklist de offboarding preparado 2 semanas antes (IT, HR, AppSec)
- [ ] Notificação enviada ao contractor/fornecedor com data de desativação
- [ ] Acesso a sistemas revogado (Git, Jira, VPN, cloud, databases): 
      - Contas de utilizador desativadas
      - SSH keys removidas
      - API tokens revogados
      - MFA removido
- [ ] Ativos recuperados:
      - Código/repositórios transferidos ou archived
      - Documentação entregue
      - Laptop/hardware retornado e wiped
      - Secrets (API keys, passwords) rotacionados
- [ ] Last backup de trabalho do contractor realizado
- [ ] Sign-off de "offboarding completo" registado em GRC
- [ ] Reminder enviado ao contractor: confidentiality obligations continuam pós-término

**Integração.** Operações + Validação; Resp: HR (coordenação) + DevOps (acesso tech) 
+ AppSec Engineer (validação) + Security Champion (checkpoints); SLA: Offboarding 
completo em <24h da data de termo; Trigger: Data de término conhecida

**Ligações úteis.**  
- [Reavaliação de Fornecedores - US-14](#us-14)
- [Plano de Saída - Cap. 14 intro](governanca-contratacao/intro.md)
```

---

### **US-18: Monitorização Contínua de Conformidade de Fornecedores (Alertas)**

```markdown
**Contexto.** Fornecedores são avaliados periodicamente (US-14), mas risco entre 
ciclos não é detetado. CVEs, incidentes ou mudanças de SLA não são monitorados.

**História.**  
Como **AppSec Engineer + Security Monitoring**, quero **monitorizar continuamente 
conformidade de fornecedores (incidentes, CVEs, SLA) e escalar automaticamente se 
gaps surgem**, para **reduzir risco residual entre ciclos de avaliação formal**.

**BDD.**  
- Dado um fornecedor crítico (L2–L3) com contrato vigente
- Quando incidente, CVE crítico, ou breach é reportado
- Então alerta automático é gerado, escalado para AppSec e Procurement

**DoD.**  
- [ ] Integração com feed de incidentes do fornecedor (ex.: status page, email)
- [ ] Monitorização de CVEs em dependências do fornecedor (via SBOM)
- [ ] Alerta automático se:
      - CVE crítico não mitigado em 72h (L3) ou 7 dias (L2)
      - Incidente reportado pelo fornecedor
      - SLA não cumprido (ex.: uptime <99.5%, RTO excedido)
      - Mudança de propriedade/localização
- [ ] Escalação automática: AppSec Engineer → Procurement Officer → CISO
- [ ] Trigger automático de revisão especial (US-14 fora de ciclo)
- [ ] Registo de alerta e ação documentado em GRC
- [ ] Dashboard com status de fornecedores críticos e alertas ativas

**Integração.** Operações contínuo; Resp: AppSec Engineer (setup) + Security 
Monitoring (operação); Triggers: Incidente, CVE, SLA, mudança contrato; SLA: 
Alerta em <1h de deteção

**Ligações úteis.**  
- [Reavaliação de Fornecedores - US-14](#us-14)
- [Monitorização - Cap. 12](/monitorizacao-operacoes/aplicacao-lifecycle.md)
```

---

### **US-19: Revisão Trimestral de Acesso de Contractors (Least Privilege)**

```markdown
**Contexto.** Contractors ganham acesso inicial, mas permissões acumulam ao longo 
do tempo. Sem revisão periódica, principle of least privilege é violado.

**História.**  
Como **Security Champion + Infrastructure Lead**, quero **revisar trimestralmente 
acesso de contractors em ativo, validando que têm apenas acesso necessário ao 
projeto atual**, para **manter least privilege, reduzir risco, e remover acesso 
excessivo**.

**BDD.**  
- Dado contractors ativos com acesso a sistemas
- Quando ciclo trimestral chega
- Então acesso é revisado, validado com Tech Lead, e removido se não necessário

**DoD.**  
- [ ] Lista de contractors ativos extraída (Git, Jira, VPN, Cloud IAM)
- [ ] Por cada contractor:
      - Acesso listado (repos, CI/CD, databases, cloud resources)
      - Tech Lead valida: necessário? (Sim/Não/Modificar scope)
      - Se Não necessário: acesso removido no mesmo dia
      - Se Modificar: novo acesso configurado, antigo removido
- [ ] Checklist de revisão preenchido e assinado por Tech Lead + Security Champion
- [ ] Notificação enviada a contractor informando acesso revisado e removido (se aplicável)
- [ ] Registo de mudanças documentado em audit trail (Git, IAM logs)
- [ ] Relatório consolidado entregue ao AppSec Engineer

**Integração.** Validação; Resp: Security Champion (coordenação) + Tech Lead 
(validação) + DevOps (mudanças técnicas); Triggers: Calendário (trimestral); 
SLA: Revisão completada em 1 semana

**Ligações úteis.**  
- [Preparação Técnica - US-15](#us-15-nova)
- [Offboarding - US-17](#us-17-nova)
- [IAM/Acesso - Cap. 02, Requisito SEC-L2/L3-Aut-03](requisitos-seguranca/aplicacao-lifecycle.md)
```

---

### **US-20: Feedback Pós-Projeto e Rating de Contractors**

```markdown
**Contexto.** Contractors terminam projeto sem feedback sobre desempenho de 
segurança. Sem dados para decisão de re-hire ou referência a otros projetos.

**História.**  
Como **Security Champion + Tech Lead**, quero **recolher feedback pós-projeto de 
contractors sobre compreensão de segurança, incidentes, e recomendações**, para 
**informar decisão de re-hire e melhorar programa de preparação**.

**BDD.**  
- Dado um contractor cujo projeto termina
- Quando offboarding é iniciado (US-17)
- Então feedback form é enviado para Tech Lead + AppSec Engineer preencherem

**DoD.**  
- [ ] Feedback form criado com perguntas:
      - Compreensão de políticas de segurança (escala 1–5)
      - Incidentes durante projeto? (sim/não + descrição)
      - Contractor seguiu best practices? (sim/não + exemplos)
      - Áreas de melhoria na formação/preparação?
      - Recomendação de re-hire? (sim/não/talvez + justificação)
      - Rating de segurança geral (1–5 stars)
- [ ] Feedback recolhido de Tech Lead + AppSec Engineer
- [ ] Resultado registado em sistema centralizado (HR, Procurement)
- [ ] Rating positivo/negativo armazenado para referência futura
- [ ] Insights agregados (se múltiplos contractors de fornecedor) para US-14 reavaliação

**Integração.** Operações pós-projeto; Resp: Security Champion (coordenação) + Tech 
Lead + AppSec Engineer (preenchimento); Triggers: Offboarding iniciado; SLA: 
Feedback em 3 dias após termo

**Ligações úteis.**  
- [Offboarding - US-17](#us-17-nova)
- [Reavaliação de Fornecedores - US-14](#us-14)
```

---

## 3. Addon Files Recomendados

### **addon/02-template-validacao-contractors.md** (NOVO)

Criar template concreto com:
- Checklist de triagem (skills, background check, experiência)
- Questões de security awareness
- Verificação de equipamentos seguros
- Confirmação de NDA/confidentiality
- Scoring e critério de aprovação/rejeição

---

### **addon/12-guia-preparacao-sandbox.md** (NOVO)

Criar guia para:
- Setup de ambiente sandbox isolado para contractors
- Tipos de sandbox (GitHub org, dev app instance, etc.)
- Acesso: como provisionar, como revogar
- Prática: exercícios de security (code review seguro, test escrita, etc.)
- Transição de sandbox para acesso real

---

### **addon/13-checklist-offboarding.md** (NOVO)

Criar checklist executável com:
- Timeline (2 semanas antes até <24h após)
- Tarefas por owner (HR, DevOps, AppSec, Tech Lead, Security Champion)
- Verificação de conclusão
- Registo de completude

---

### **Expandir addon/01-modelo-governancao.md** (EXISTENTE)

Incluir:
- Cláusulas obrigatórias em contratos (NDA, IP, non-compete, confidentiality)
- Template de contrato para contractors (diferente de fornecedores)
- Níveis de alçada para aprovação de contractors (vs. fornecedores de software)

---

## 4. Recomendações de Mudanças a Cap. 14

### 4.1 Adicionar User Story US-15 a US-20

- Inserir na secção "📖 User Stories normalizadas" após US-14

### 4.2 Expandir US-02 (Cláusulas Contratuais)

Incluir template específico com:
```yaml
Cláusulas Obrigatórias em Contratos:
  - Segurança Técnica:
      - Compliance com SbD-ToE (Cap. 2–13)
      - SBOM em cada release
      - SCA obrigatório
      - Conformidade DORA/NIS2 (se setor financeiro/crítico)
  - Confidencialidade & IP:
      - NDA (duração pós-término)
      - IP Ownership (código desenvolvido)
      - Non-Compete (duração, âmbito geográfico)
  - Notificação de Incidentes:
      - Breach/incidente notificado em <4h
      - Relatório completo em <7 dias
  - Rescisão:
      - Plano de saída testado anualmente
      - Portabilidade de dados em <30 dias
```

### 4.3 Adicionar Matriz de Proporcionalidade expandida

Incluir novas práticas:
```
| Prática | L1 | L2 | L3 |
|---------|----|----|-----|
| Preparação técnica de contractors | Básico | Recomendado | Obrigatório + quiz |
| Triagem de skills/background | Opcional | Recomendado | Obrigatório |
| Trilho de formação pré-acesso | Básico | Obrigatório | Obrigatório + 80% score |
| Ambiente sandbox para prática | Opcional | Recomendado | Obrigatório |
| Revisão trimestral de acesso | Anual | Semestral | Trimestral |
| Offboarding formal | Básico | Obrigatório | Obrigatório + 24h |
| Monitorização contínua de fornecedores | Não | Recomendado | Obrigatório |
| Feedback pós-projeto | Opcional | Recomendado | Obrigatório |
```

### 4.4 Adicionar Integração Explícita com Cap. 13

Na secção "📖 User Stories", adicionar nota de cross-reference:

> **🔗 Integração com Cap. 13 - Formação e Onboarding**  
> US-15 e US-16 implementam trilho de formação obrigatória para contractors.  
> Ver Cap. 13 para definição de conteúdos, trilhos por perfil, quiz, e LMS.  
> Responsabilidade: Training Manager (Cap. 13) + Security Champion (Cap. 14).

### 4.5 Criar Secção "Ciclo de Vida de Contractor"

Adicionar diagrama visual:

```
[Novo Contractor]
    ↓
[US-06: Validação de Fornecedor] → [Aprovado / Rejeitado]
    ↓
[US-15: Preparação Técnica] → [Sandbox setup, NDA, formação]
    ↓
[US-16: Trilho de Formação] → [Cursos obrigatórios, quiz 80%]
    ↓
[Acesso Real Concedido]
    ↓
[Trabalho em Projeto] ← [US-19: Revisão Trimestral de Acesso (se projeto >3 meses)]
    ↓
[Fim do Projeto / Contractor Termina]
    ↓
[US-17: Offboarding Seguro] → [Acesso revogado, ativos recuperados]
    ↓
[US-20: Feedback Pós-Projeto] → [Rating, lições aprendidas]
    ↓
[Arquivo + Learning]
```

---

## 5. Impacto de Conformidade Normativa

### DORA (Digital Operational Resilience Act)

As novas US cobrem:
- **Art. 5 (Risk Management):** Validação de risco de contractors e fornecedores (US-06, 15, 16)
- **Art. 26–28 (Terceiros):** Validação inicial, reavaliação, e offboarding (US-06, 14, 17)
- **Art. 27 (Plano de Saída):** Formalizado em US-17

### NIS2 (Diretiva Cibersegurança)

- **Art. 18 (Acesso por Terceiros):** Triagem, formação, e revisão periódica (US-15, 16, 19)
- **Art. 23 (Supply Chain):** Monitorização contínua (US-18)

### ISO 27001

- **A.6.1 (Recursos Humanos):** Onboarding/offboarding seguro (US-15, 16, 17)
- **A.15.1 (Gestão de Fornecedores):** Avaliação, monitorização, rescisão (US-06, 14, 18)

---

## 6. Resumo de Ações Recomendadas

| Ação | Prioridade | Owner | Timeline |
|------|-----------|-------|----------|
| Adicionar US-15 a 20 a Cap. 14 | Alta | AppSec Manager | 1 semana |
| Expandir addon/01-modelo-governancao.md com templates de contratos | Alta | Jurídico + AppSec | 2 semanas |
| Criar addon/02-template-validacao-contractors.md | Alta | HR + AppSec | 1 semana |
| Criar addon/12-guia-preparacao-sandbox.md | Média | DevOps + AppSec | 2 semanas |
| Criar addon/13-checklist-offboarding.md | Média | HR + AppSec | 1 semana |
| Integração explícita Cap. 13 ↔ Cap. 14 | Alta | Training Manager | 1 semana |
| Atualizar matriz de proporcionalidade | Média | AppSec | 3 dias |
| Criar diagrama "Ciclo de Vida de Contractor" | Baixa | Documentation | 3 dias |

---

## 7. Conclusão

O **Cap. 14 está bem estruturado em governação, exceções, e reavaliação de fornecedores**, mas **deixa gaps críticos em:**

1. **Preparação técnica pré-acesso** (US-15)
2. **Trilho de formação obrigatória** (US-16, integração explícita com Cap. 13)
3. **Offboarding seguro** (US-17)
4. **Monitorização contínua** (US-18)
5. **Revisão de acesso periódica** (US-19)
6. **Feedback pós-projeto** (US-20)

A adição destas 6 user stories e 3 addon files **cobrirá completamente o ciclo de vida de contractors e fornecedores**, desde validação inicial até offboarding seguro, alinhado com DORA, NIS2, e ISO 27001.

---

**Documento preparado para revisão e implementação no SbD-ToE Manual.**
