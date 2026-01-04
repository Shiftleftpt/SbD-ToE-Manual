---
id: checklist-offboarding
title: Checklist de Offboarding Seguro
description: Procedimento formalizado e executável para rescisão segura de contractors e fornecedores
tags: [governanca, contractors, offboarding, rescisao, seguranca, auditoria]
---

# ✅ Checklist de Offboarding Seguro

**Versão:** 1.0  
**Última atualização:** Novembro 2025  
**Responsável:** HR (coordenação) + DevOps (técnico) + AppSec (validação) + Security Champion  
**Ciclo:** T-14 dias antes até T+1 dia após término

---

## 📖 Objetivo

Formalizar e executar processo de **offboarding seguro** para:
- Contractors cujo contrato termina
- Fornecedores críticos que são rescindidos
- Membros de equipa (internos ou externos) que saem da organização

**Benefício:** Revogação completa de acesso, recuperação de ativos, conformidade DORA/NIS2

---

## 🏃 Timeline de Offboarding

```
T-14 dias: Notificação de término é conhecida
  └─ HR notifica Security Champion + DevOps + AppSec

T-10 dias: Preparação começa
  └─ Checklist de offboarding enviado a stakeholders

T-5 dias: Avisos iniciais
  └─ Notificação ao contractor/fornecedor (email + verbal)
  └─ Backup de trabalho iniciado

T-1 dia: Avisos finais
  └─ Last day confirmation email
  └─ Equipamentos recolhidos agendados

T+0 (Dia de Término):
  └─ Acesso revogado em T+0 (imediato após fim do expediente), com verificação até T+1
  └─ Assets finais recuperados

T+1 dia: Verificação
  └─ Sign-off de conclusão
  └─ Entrevista de saída (feedback)

T+7 dias: Auditoria
  └─ Revisão de logs (comportamento suspeito?)
  └─ Validação de limpeza
```

---

## 📋 PRÉ-OFFBOARDING (T-14 a T-1)

### 1. Notificação Inicial e Planning

| Item | Owner | Status | Data | Notas |
|------|-------|--------|------|-------|
| **HR notifica: CISO, Security Champion, Tech Lead, DevOps Lead, Manager** | HR | [ ] | ____ | Email com data de término |
| **Meeting de planning 2 semanas antes** | Security Champion | [ ] | ____ | Checklist enviado, responsabilidades atribuídas |
| **Aviso ao contractor (se conhecido com antecedência)** | Manager | [ ] | ____ | Verbal + escrito |
| **Documentar motivo de saída** | HR | [ ] | ____ | Resignação, fim de contrato, rescisão, etc. |

---

### 2. Backup e Recuperação de Trabalho

| Item | Owner | Executado | Verificado | Notas |
|------|-------|-----------|-----------|-------|
| **Identificar todos os repositórios/dados do contractor** | Tech Lead | [ ] | [ ] | Listar Git repos, Jira boards, compartilhados OneDrive |
| **Last commit identificado** | DevOps | [ ] | [ ] | Data, SHA, conteúdo |
| **Backup full de repositórios privados** | DevOps | [ ] | [ ] | Ex.: `git clone --mirror` |
| **Backup de código-fonte desenvolvido** | DevOps | [ ] | [ ] | Archive zip, versionado com timestamp |
| **Backup de documentação criada** | Tech Lead | [ ] | [ ] | Wikis, README, specs, design docs |
| **Backup de comunicação importante** | HR | [ ] | [ ] | Mails críticas, mensagens Slack (se compliance requer) |
| **Arquivo em storage seguro** | DevOps | [ ] | [ ] | Rétention: 7 anos (DORA requirement), acesso restricted |

**Armazenamento:**
```
Location: /archive/offboarded/{contractor-name}/{date}/
├─ git-repos-backup.tar.gz
├─ code-artifacts/
├─ documentation/
└─ metadata.json (index, sizes, checksums)
```

---

### 3. Notificações Pré-Offboarding

| Comunicação | De | Para | Quando | Conteúdo |
|-------------|----|----|--------|----------|
| **Aviso de Offboarding** | Security Champion | Contractor | T-7 dias | Data exata de término, lista de o que entregar |
| **Aviso de Rescisão de Equipamento** | HR | Contractor | T-5 dias | Quando/onde devolver laptop, telemóvel, badges, etc. |
| **Aviso de Confidencialidade Pós-Término** | Legal | Contractor | T-1 dia | Obrigações legais de sigilo continuam, duração, consequências |
| **Last Access Email** | Security Champion | Contractor + Manager | T-0 | Último dia de acesso - atividades finais? |

---

## 🔐 OFFBOARDING EXECUTION (T+0 DATA DE TÉRMINO)

### 4. Revogação de Acesso Técnico (`<`24h após T+0)

**Timeline:** Começar revogação entre T+0 (fim de expediente) e T+1 (manhã)

#### 4.1 Git & CI/CD Access

| Item | Owner | Comando/Ação | Status | Verificação |
|------|-------|------------|--------|-------------|
| **Remover contractor de Github/GitLab orgs** | DevOps | `github:remove-member {org} {user}` | [ ] | Contractor não consegue clonar repos private |
| **Revogar SSH keys (todas)** | DevOps | Delete de `~/.ssh/authorized_keys` e Git platform | [ ] | SSH clone fails |
| **Revogar Personal Access Tokens (PATs)** | DevOps | Revoke via GitHub/GitLab settings | [ ] | API calls fail com 401 |
| **Revogar CI/CD credentials** | DevOps | Delete service account tokens | [ ] | CI/CD pipeline fails se contractor tenta trigger |
| **Remove collaborator permissions** | Tech Lead | Remove from all repositories | [ ] | No "edit" access visible |
| **Archive contractor repos (se pessoal)** | DevOps | `git archive` and move to `/archive` | [ ] | Repos marked as archived on platform |

**Verificação:**
```bash
# Post-revocation check (5 min após revogação)
ssh -i /tmp/test-key git@github.com
# Expected: Permission denied (publickey)

git clone https://github.com/[org]/[private-repo]
# Expected: fatal: repository not found / access denied
```

---

#### 4.2 VPN, Wifi, Physical Access

| Item | Owner | Ação | Status | Verificação |
|------|-------|------|--------|-------------|
| **Desativar VPN account** | IT | Deactivate in VPN management console | [ ] | VPN login fails |
| **Revogar Wifi credentials** | IT | Remove MAC address / WiFi certificate | [ ] | Device cannot connect |
| **Desativar badge/card access** | Facilities | Card deactivated in access control system | [ ] | Badge scan denied at doors |
| **Desativar parking pass** | Facilities | Remove license plate from parking system | [ ] | Cannot access parking |

---

#### 4.3 Cloud & SaaS Platforms

| Plataforma | Item | Owner | Ação | Status | Verificação |
|-----------|------|-------|------|--------|-------------|
| **AWS** | IAM User | DevOps | Deactivate access key + delete user | [ ] | `aws s3 ls` fails (401) |
| **Azure** | Service Principal / User | DevOps | Delete or disable in Entra ID | [ ] | Cannot login to Azure portal |
| **Google Cloud** | Service Account | DevOps | Delete service account | [ ] | GCP API calls fail |
| **Jira** | User Account | Tech Lead | Deactivate user in directory | [ ] | Cannot login, all issues reassigned |
| **Confluence** | User Account | Tech Lead | Deactivate user | [ ] | Cannot access wikis |
| **Slack** | User Account | HR | Deactivate user | [ ] | Cannot login, marked as "inactive" |
| **Email** | Corporate Email | HR | Disable mailbox (may keep 30 days) | [ ] | OWA/IMAP login fails |

---

#### 4.4 Database & Data Store Access

| Item | Owner | Ação | Status | Verificação |
|------|-------|------|--------|-------------|
| **Revogar PostgreSQL roles** | DBA | `DROP ROLE contractor_name` | [ ] | psql connection rejected |
| **Revogar MySQL users** | DBA | `DROP USER 'contractor'@'%'` | [ ] | MySQL login fails |
| **Revogar MongoDB auth** | DBA | Remove user from database | [ ] | MongoDB auth fails |
| **Revogar S3/Storage acces** | DevOps | Remove IAM policy, delete credentials | [ ] | AWS S3 upload/download fails |
| **Revogar Vault access** | DevOps | Remove AppRole, invalidate token | [ ] | Vault `auth` fails |

---

#### 4.5 MFA & Authentication

| Item | Owner | Ação | Status | Verificação |
|------|-------|------|--------|-------------|
| **Remover MFA device** | IT | Remove from Microsoft Authenticator / Authy | [ ] | Contractor cannot log in com MFA |
| **Revogar biometric access** | Facilities | Remove fingerprint from system | [ ] | Badge reader rejects biometric |
| **Revogar corporate device registration** | IT | Remove from MDM (Mobile Device Management) | [ ] | Device loses corporate mail, VPN |


#### 4.6 Integrações, Automação e Acessos Indiretos

| Item | Owner | Ação | Status | Verificação |
|------|-------|------|--------|-------------|
| **Inventariar integrações associadas ao utilizador** | DevOps | Listar apps/integrações ligadas a Git, CI/CD, ChatOps, ALM | [ ] | Lista anexada ao offboarding |
| **Revogar tokens de aplicações e integrações** | DevOps | Revogar tokens OAuth, webhooks, apps instaladas, bots, runners | [ ] | Eventos/ações deixam de executar |
| **Revogar credenciais em gestores de segredos e automação** | DevOps | Invalidar tokens/approles, remover bindings a pipelines | [ ] | Acesso falha / execuções falham |
| **Remover configurações de sincronização/exportação** | IT/DevOps | Desativar sincronizações, forwards, ligações a storage externo | [ ] | Não existe export pós-T+0 |
| **Validar que não existem permissões herdadas por grupos** | IT/Tech Lead | Rever grupos/roles indiretos em diretórios e plataformas | [ ] | Sem acesso residual via grupo |

---

### 5. Recuperação de Ativos Físicos

| Item | Recolhido Por | Responsável | Status | Verificação |
|------|---------------|-------------|--------|-------------|
| **Laptop/Desktop computer** | IT | Security Champion | [ ] | Device serial verified, collected in person |
| **Mobile phone (if corporate)** | IT | Security Champion | [ ] | Wiped on site (or scheduled) |
| **Badges/Cards** | Facilities | Security Champion | [ ] | Physically returned |
| **Keys (office, lab, locker)** | Facilities | Security Champion | [ ] | All accounted for |
| **Hardware tokens (security key, fob)** | IT | Security Champion | [ ] | Returned and destroyed |
| **External drives/USB sticks** | Tech Lead | Security Champion | [ ] | Scanned for unauthorized data |
| **Documents/printouts** | HR | Security Champion | [ ] | Collected, shredded or archived |
| **Other equipment** | HR | Security Champion | [ ] | Specify: _________________ |

**Procedure:**
```
1. Schedule collection meeting (T+0 or T+1)
2. Witness: Security Champion + HR + IT
3. Device powered off, inventory checked
4. Wiping scheduled (within 48h) or done on-site
5. Sign-off form completed
6. Evidence photographed/logged
```

---

### 6. Secrets & Credentials Rotation

| Item | Owner | Ação | Status | Verificação |
|------|-------|------|--------|-------------|
| **API keys contractor had access to** | AppSec | Revoke in platform, rotate secrets | [ ] | Old key returns 401 |
| **Database passwords** | DBA | Rotate in Vault + all apps updated | [ ] | Old password fails login |
| **JWT signing keys** | DevOps | Rotate if contractor had access | [ ] | Old tokens become invalid |
| **SSH host keys (if compromised risk)** | DevOps | Regenerate (ex.: GitHub deploy keys) | [ ] | Old SSH key fails |
| **OAuth tokens** | DevOps | Revoke all tokens for contractor's app | [ ] | App reauthenticates |
| **Certificates/SSL keys** | DevOps | Rotate if contractor had access | [ ] | Old cert expires or revoked |

**Timing:** All rotations SAME DAY or next day latest (DORA requirement)

---

## 📋 PÓS-OFFBOARDING (T+1 a T+7)

### 7. Verificação de Conclusão

**T+1 (Dia após término):**

| Item | Owner | Verificado | Observações |
|------|-------|-----------|-------------|
| **Confirmação: Todos acessos revogados** | DevOps | [ ] | Cross-check todas plataformas |
| **Confirmação: Todas devices recuperados** | IT | [ ] | Serial numbers matched, wiping initiated |
| **Confirmação: Contractor não consegue fazer login em nenhuma plataforma** | AppSec | [ ] | Teste login (deve falhar) em 5 plataformas random |
| **Backup de dados verificado** | DevOps | [ ] | Archive integridade validada (checksums OK) |
| **Sign-off form assinado** | Security Champion | [ ] | Todas as partes assinaram |

**Sign-Off Form Template:**

```
OFFBOARDING SIGN-OFF

Contractor: ________________
Data de Término: ________________
Data de Offboarding Completado: ________________

Confirmamos que o seguinte foi completado:
  ✓ Acesso técnico revogado (Git, Cloud, VPN, Email, Jira, Slack)
  ✓ Ativos físicos recuperados (laptop, badge, chaves)
  ✓ Secrets rotacionados (API keys, DB passwords, etc.)
  ✓ Backup de dados arquivado
  ✓ Confidentiality agreement assinado e reforçado
  ✓ Nenhum acesso residual identificado

Assinado por:
  - HR Manager: _________________ Data: _____
  - Security Champion: _________________ Data: _____
  - DevOps Lead: _________________ Data: _____
  - Tech Lead: _________________ Data: _____

Escalonamento (se necessário):
  Incidentes durante offboarding: [_______________]
  CISO Notificado? [ ] Sim [ ] Não
  Data: _____

Contacto para follow-up: _________________
```

---

### 8. Entrevista de Saída (Feedback)

**T+1 ou T+2, 1-1 com contractor (opcional mas recomendado)**

| Tópico | Questão | Resposta | Ações |
|--------|---------|----------|-------|
| **Segurança** | Como foram as políticas de segurança? Claras? Impedimento? | [_____] | [ ] Feedback para training |
| **Incidentes** | Algum incidente/erro de segurança durante projeto? | [_____] | [ ] Incident ticket se sim |
| **Access Control** | Acesso foi apropriado? Tiveste permissões excessivas? | [_____] | [ ] Adjustment para próximo |
| **Tooling** | Ferramentas de segurança foram intuitivas? | [_____] | [ ] Tool review se feedback negativo |
| **Formação** | Formação de onboarding foi suficiente? | [_____] | [ ] Trilho iterado se gaps |
| **Recomendações** | Recomendações de melhoria? | [_____] | [ ] Backlog item criado |

**Resultado:** Scoring (1–5) agregado para "Contractor Security Rating" (ver US-20)

---

### 9. Auditoria de Logs (T+3 a T+7)

**AppSec Engineer revisão:**

| Verificação | Query | Resultado esperado | Status |
|-------------|-------|-------------------|--------|
| **Último acesso ao Git** | Git logs últimas 72h | Nenhum novo commit/push | [ ] |
| **Último acesso ao VPN** | VPN logs últimas 72h | Acesso terminado T+0 | [ ] |
| **Último acesso ao email** | Email logs últimas 72h | Nenhum login após T+0 | [ ] |
| **Último acesso à cloud** | Cloud audit logs últimas 72h | Nenhuma ação após T+0 | [ ] |
| **Comportamento suspeito** | SIEM alerts últimos 7 dias | Nenhum alert relacionado ao contractor | [ ] |
| **Data exfiltration attempt** | DLP logs últimos 7 dias | Nenhuma tentativa de upload/download | [ ] |
| **Atividade via integrações/bots** | Logs de automação/ChatOps/GitHub Apps/CI | Nenhuma execução associada ao utilizador após T+0 | [ ] |

**Se anomalia encontrada:**
- [ ] Alertar CISO imediatamente
- [ ] Iniciar incidente investigation
- [ ] Rever logs de acesso residual
- [ ] Escalação para Legal se necessário

---

## 📊 Artefactos & Documentação

**Manter por 7 anos (DORA requirement):**

```
Archive Location: /compliance/offboarding/{contractor-name}/{date}/
├─ offboarding-checklist.pdf (signed)
├─ backup-manifest.json
│  ├─ repositories: [list]
│  ├─ artifacts: [list]
│  └─ timestamp, checksums
├─ device-inventory.pdf (with photos)
├─ secrets-rotation-log.txt
├─ access-revocation-log.txt
├─ audit-logs-excerpt.pdf (last 72h)
├─ exit-interview.pdf
└─ sign-off-form.pdf
```

---

## ⚠️ Red Flags & Escalation

Se qualquer uma das seguintes ocorrer, **ESCALATE IMEDIATAMENTE**:

| Red Flag | Ação | Owner |
|----------|------|-------|
| **Contractor tenta fazer login após T+0** | Escalate CISO, investigate login attempt | Security Monitoring |
| **Dados faltam no backup** | Investigate theft/deletion, forensics | DevOps + CISO |
| **Secrets não foram rotacionados a tempo** | Rotate AGORA, investigate why | AppSec + DevOps |
| **Equipamento "desaparecido"** | Escalate HR + Legal, possibly theft | Facilities + HR |
| **Contractor não devolveu equipamento** | Legal letter, escalate to management | HR + Legal |
| **Comportamento suspeito nos logs** | Full forensics, preserve evidence | AppSec + CISO |
| **Contractor em lista de sanções (após saída)** | Legal + CISO, compliance check | Compliance + Legal |

---

## 📎 Checklists por Tipo de Saída

### A. Rescisão Imediata (por Causa)

```
Diferença: Sem avisos, revogação no mesmo dia

[ ] Security incident confirmado
[ ] Violação de política de segurança
[ ] Roubo de ativos
[ ] Breach potencial
[ ] Comportamento malicioso confirmado

Ações especiais:
- [ ] Device wiped on-site (não permitir levar laptop)
- [ ] Backup forense realizado ANTES de wipe
- [ ] Legal notificado
- [ ] CISO escalação obrigatória
- [ ] Possível relato a authorities
```

### B. Rescisão Amigável (Fim de Contrato)

```
Timeline: Planeado com 2 semanas de aviso

[ ] Backup de trabalho completo
[ ] Knowledge transfer realizado
[ ] Entrevista de saída feita
[ ] Referências para re-hire consideradas
[ ] Thank you email sent
```

### C. Fim de Contrato por Expiração

```
Automático após data pré-definida

[ ] Notificação automática em HR system
[ ] Offboarding inicia T-14 dias automaticamente
[ ] Extensão? Re-negotiate com Procurement
```

---

## 🏁 Success Criteria

Offboarding é considerado **COMPLETO** quando:

- ✅ Todos os acessos técnicos revogados (0 acesso residual)
- ✅ Todos os ativos físicos recuperados
- ✅ Secrets rotacionados
- ✅ Backup arquivado com integridade confirmada
- ✅ Sign-off form assinado por 4+ partes
- ✅ Auditoria de logs show nenhuma atividade pós-termo
- ✅ Confidentiality obligations reforçadas
- ✅ Arquivo completo em storage de compliance (7 anos)

---

## 📎 Referências & Links

- [Preparação Técnica - US-15](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-15)
- [Offboarding - US-17](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-17)
- [Feedback Pós-Projeto - US-20](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-20)
- [Template de Validação](14-exemplo_template-validacao-contractors.md)
- [Política de Confidencialidade Pós-Término] (link interno)

---

**Propriedade:** HR + DevOps + AppSec  
**Revisão:** Anual  
**Última atualização:** Novembro 2025
