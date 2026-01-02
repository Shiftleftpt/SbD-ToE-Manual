---
id: confidencialidade-catalogo
title: Confidencialidade e Controlo de Acesso ao Catálogo de Requisitos
description: Gestão de requisitos sensíveis, classificação de informação e proteção contra supply chain risks
tags: [addon, confidencialidade, acesso, supply-chain, i4, agent.md]
---

# 🔒 Confidencialidade e Controlo de Acesso ao Catálogo de Requisitos

## 🎯 Objetivo

Este addon estabelece os **critérios de classificação e controlo de acesso** ao catálogo de requisitos de segurança, garantindo que:
- Requisitos **não revelam informações sensíveis** sobre aplicações a atacantes externos
- Acesso ao catálogo é **controlado por papel e necessidade** (least privilege)
- Requisitos gerados/armazenados em **ferramentas SaaS** são tratados como risco de supply chain
- **Conformidade regulatória** (GDPR, NIS2, segredos comerciais)

**Contexto normativo:**  
Este addon implementa o **Invariante I4 (Proteção de ativos críticos)** de [agent.md](https://github.com/your-org/agent-spec). Complementa [addon-11: Validação Assistida](./11-validacao-requisitos-assistida) na gestão de riscos de ferramentas externas.

---

## 🚨 Riscos de Exposição de Requisitos

### Cenário 1: Revelação de Superfície de Ataque

**Exemplo crítico:**
```yaml
# Requisito exposto publicamente (❌ MAU)
REQ-WEB-005: "Implementar WAF para proteger contra OWASP Top 10: SQL Injection, XSS, CSRF, XXE, SSRF"

# Risco: Atacante sabe que aplicação é web app vulnerável a estas ameaças
# Informação revelada:
# - Aplicação expõe endpoints web
# - Aplicação pode ter SQL backend (SQL Injection)
# - Aplicação processa XML (XXE)
# - Aplicação faz requests externos (SSRF)
```

**Mitigação:**
```yaml
# Requisito genérico para público (✅ BOM)
REQ-WEB-005: "Implementar controlo de proteção de aplicações web conforme OWASP guidelines"

# Requisito detalhado para interno (🔒 CONFIDENCIAL)
REQ-WEB-005-INTERNAL: "Implementar WAF Cloudflare ou AWS WAF com rules:
- SQL Injection (backend PostgreSQL em RDS)
- XSS (aplicação usa React com dangerouslySetInnerHTML em 3 componentes)
- SSRF (API Gateway faz requests para serviços internos AWS via VPC)
- Proteger endpoints: /api/v2/*, /admin/*, /webhook/*"
```

---

### Cenário 2: Revelação de Tecnologias e Versões

**Exemplo crítico:**
```yaml
# Requisito exposto (❌ MAU)
REQ-CRYPTO-001: "Substituir OpenSSL 1.1.1 por OpenSSL 3.0.x para mitigar CVE-2022-XXXX"

# Risco: Atacante sabe que aplicação usava OpenSSL 1.1.1 (vulnerável)
# Timing attack: Se requisito publicado mas não implementado, janela de exploração
```

**Mitigação:**
```yaml
# Requisito genérico (✅ BOM)
REQ-CRYPTO-001: "Atualizar bibliotecas criptográficas para versões sem vulnerabilidades conhecidas"

# Requisito detalhado interno (🔒 CONFIDENCIAL)
REQ-CRYPTO-001-INTERNAL: "Atualizar OpenSSL 1.1.1k → 3.0.7+ (CVE-2022-XXXX)
- Aplicações afetadas: api-gateway-prod, auth-service-prod
- Deadline: 2025-01-31 (30 dias após disclosure)
- Rollback plan: Manter 1.1.1k em standby por 7 dias"
```

---

### Cenário 3: Revelação de Arquitectura Interna

**Exemplo crítico:**
```yaml
# Requisito exposto (❌ MAU)
REQ-NET-003: "Configurar Network Policies no Kubernetes para isolar namespace 'production-db' de 'production-web'"

# Risco: Atacante sabe:
# - Infraestrutura usa Kubernetes
# - Existe namespace 'production-db' (alvo de ataque)
# - Web e DB estão no mesmo cluster (lateral movement possível)
```

**Mitigação:**
```yaml
# Requisito genérico (✅ BOM)
REQ-NET-003: "Implementar segmentação de rede entre camadas de aplicação"

# Requisito detalhado interno (🔒 CONFIDENCIAL)
REQ-NET-003-INTERNAL: "K8s Network Policies:
- Cluster: prod-cluster-eu-west-1
- Namespaces: production-web, production-api, production-db, production-cache
- Regras:
  - production-web → production-api (port 8080)
  - production-api → production-db (port 5432)
  - production-api → production-cache (port 6379)
  - DENY all other traffic
- Validação: Scan com kube-bench, teste de lateral movement"
```

---

## 🔐 Modelo de Classificação de Requisitos

### Níveis de Classificação

| Nível | Descrição | Quem pode aceder | Onde guardar | Retenção |
|---|---|---|---|---|
| **PÚBLICO** | Requisitos genéricos sem detalhes técnicos | Todos | Wiki pública, GitHub público | Indefinida |
| **INTERNO** | Requisitos com tecnologias mas sem detalhes críticos | Developers, AppSec, GRC, Auditores | Repositório privado, Wiki interna | 5 anos |
| **CONFIDENCIAL** | Requisitos com arquitetura, vulnerabilidades, configurações específicas | AppSec, Arquitetos, GRC (need-to-know) | Repositório privado com access control, ferramenta GRC | 7 anos |
| **RESTRITO** | Requisitos com dados regulados (PII, segredos comerciais, infraestrutura crítica) | AppSec Lead, CISO, Auditores (explicit approval) | Encrypted storage, acesso com MFA + audit log | 10 anos ou conforme regulamento |

---

### Critérios de Classificação

**Classificar como CONFIDENCIAL se requisito contém:**
- [ ] Tecnologias específicas e versões (ex: "PostgreSQL 14.2", "Kubernetes 1.28")
- [ ] Nomes de serviços internos (ex: "auth-service-prod", "payment-gateway")
- [ ] Configurações de rede (IPs internos, portas, firewalls, VPCs)
- [ ] Vulnerabilidades conhecidas (CVEs) antes de mitigação estar deployada
- [ ] Detalhes de arquitetura (número de instâncias, regiões, providers)
- [ ] Endpoints ou URLs internos (ex: `/admin/*`, `/api/internal/*`)

**Classificar como RESTRITO se requisito contém:**
- [ ] Dados regulados por GDPR (ex: "Implementar pseudonimização de PII em tabela X")
- [ ] Segredos comerciais (ex: "Algoritmo proprietário de pricing")
- [ ] Infraestrutura crítica NIS2 (ex: "Requisitos de uptime 99.99% para serviço de pagamentos bancários")
- [ ] Dados de segurança nacional (defesa, utilities críticas)

**Classificar como PÚBLICO:**
- [ ] Requisitos genéricos de frameworks (ASVS, OWASP, NIST)
- [ ] Boas práticas sem detalhes técnicos (ex: "Implementar autenticação multi-fator")
- [ ] Referências a padrões públicos (ISO 27001, SOC 2)

---

## 👥 Controlo de Acesso por Papel

### Matriz de Acesso

| Papel | PÚBLICO | INTERNO | CONFIDENCIAL | RESTRITO |
|---|---|---|---|---|
| **Developer** | ✅ Leitura | ✅ Leitura | ✅ Leitura (need-to-know) | ❌ |
| **Team Lead / Scrum Master** | ✅ Leitura | ✅ Leitura | ✅ Leitura (need-to-know) | ❌ |
| **AppSec Engineer** | ✅ Leitura/Escrita | ✅ Leitura/Escrita | ✅ Leitura/Escrita | ✅ Leitura (explicit approval) |
| **AppSec Lead** | ✅ Leitura/Escrita | ✅ Leitura/Escrita | ✅ Leitura/Escrita | ✅ Leitura/Escrita |
| **Arquitetos de Software** | ✅ Leitura | ✅ Leitura | ✅ Leitura/Escrita (arquitetura) | ❌ |
| **Product Owner** | ✅ Leitura | ✅ Leitura | ❌ | ❌ |
| **GRC/Compliance** | ✅ Leitura | ✅ Leitura/Escrita | ✅ Leitura | ✅ Leitura (compliance) |
| **CISO / Gestão Executiva** | ✅ Leitura | ✅ Leitura | ✅ Leitura | ✅ Leitura/Escrita |
| **Auditores Internos** | ✅ Leitura | ✅ Leitura | ✅ Leitura | ✅ Leitura (auditoria) |
| **Auditores Externos** | ✅ Leitura | ✅ Leitura (NDA) | ✅ Leitura (NDA + explicit approval) | ❌ (apenas sumário) |
| **Contractors / Consultores** | ✅ Leitura | ❌ (apenas se NDA) | ❌ (apenas se NDA + need-to-know) | ❌ |

---

## 🛡️ Procedimentos de Proteção

### Procedimento 1: Classificação de Requisito Novo

:::userstory
**História.**  
Como **AppSec Engineer**, quero **classificar novo requisito antes de publicar**, para garantir que informações sensíveis não são expostas inadequadamente.

**Critérios de aceitação (BDD).**
- **Dado** que foi criado novo requisito REQ-XXX-YYY-vZ.W  
  **Quando** reviso conteúdo contra critérios de classificação  
  **Então** atribuo nível (PÚBLICO | INTERNO | CONFIDENCIAL | RESTRITO) e documento justificação

**Checklist de classificação.**
- [ ] **Identificar informações sensíveis:**
  - [ ] Tecnologias e versões específicas?
  - [ ] Nomes de serviços, endpoints, IPs internos?
  - [ ] Vulnerabilidades (CVEs) não-mitigadas?
  - [ ] Detalhes de arquitetura ou configuração?
  - [ ] Dados regulados (PII, segredos comerciais)?
- [ ] **Determinar nível:**
  - [ ] Se 0 itens sensíveis: PÚBLICO
  - [ ] Se 1-2 itens sensíveis (tecnologias): INTERNO
  - [ ] Se 3+ itens sensíveis (arquitetura, CVEs): CONFIDENCIAL
  - [ ] Se dados regulados: RESTRITO
- [ ] **Criar versão pública (se necessário):**
  - [ ] Requisito PÚBLICO genérico (ex: REQ-XXX-YYY)
  - [ ] Requisito CONFIDENCIAL detalhado (ex: REQ-XXX-YYY-INTERNAL)
  - [ ] Link entre ambos documentado
- [ ] **Aplicar controlos de acesso:**
  - [ ] Ficheiro em directório correto (`public/`, `internal/`, `confidential/`, `restricted/`)
  - [ ] Permissões Git/filesystem configuradas
  - [ ] Tag de classificação no metadata YAML

**Artefacto:**
```yaml
---
id: REQ-WEB-005-INTERNAL
classificacao: CONFIDENCIAL
justificacao: "Revela arquitetura interna (PostgreSQL, AWS VPC) e endpoints críticos"
data_classificacao: 2026-01-15
classificador: João Silva (AppSec Engineer)
revisor: Maria Costa (AppSec Lead)
versao_publica: REQ-WEB-005
---
```
:::

---

### Procedimento 2: Revisão Periódica de Classificação

:::userstory
**História.**  
Como **GRC/Compliance**, quero **rever classificação de requisitos anualmente**, para garantir que requisitos antigos não foram desclassificados inadequadamente ou que novos riscos surgiram.

**Critérios de aceitação (BDD).**
- **Dado** que decorreu 12 meses desde última revisão de classificação  
  **Quando** executo auditoria de requisitos CONFIDENCIAL e RESTRITO  
  **Então** confirmo que classificação continua adequada ou reclassifico se necessário

**Checklist de revisão.**
- [ ] **Requisitos CONFIDENCIAL:**
  - [ ] Vulnerabilidades (CVEs) mencionadas já foram mitigadas? → Considerar desclassificar para INTERNO
  - [ ] Tecnologias mencionadas são agora públicas (ex: migrou para cloud pública)? → Considerar desclassificar
  - [ ] Novos riscos surgiram (ex: serviço tornou-se crítico)? → Considerar elevar para RESTRITO
- [ ] **Requisitos RESTRITO:**
  - [ ] Dados regulados continuam a existir? (GDPR, PII)
  - [ ] Requisitos de retenção cumpridos? (10 anos, ou conforme regulamento)
  - [ ] Acesso continua restrito a papéis corretos?
- [ ] **Requisitos PÚBLICO:**
  - [ ] Detalhes técnicos foram adicionados inadvertidamente? → Elevar para INTERNO
- [ ] **Documentar alterações:**
  - [ ] Ficheiro de auditoria: `auditorias-classificacao/AUDIT-YYYY-MM-DD.md`
  - [ ] Tabela: `requisito | classificacao_anterior | classificacao_nova | justificacao | data`

**Frequência:**
- CONFIDENCIAL: Revisão anual obrigatória
- RESTRITO: Revisão semestral obrigatória
- INTERNO/PÚBLICO: Revisão ad-hoc (se alteração de requisito)
:::

---

### Procedimento 3: Gestão de Acesso a Ferramentas SaaS

:::userstory
**História.**  
Como **CISO**, quero **avaliar risco de ferramentas SaaS** que armazenam requisitos, para garantir que supply chain risk é mitigado.

**Contexto:**  
Ferramentas como Jira Cloud, Confluence Cloud, ServiceNow, ou plataformas de threat modeling (ThreatModeler, IriusRisk) podem armazenar requisitos. Se ferramenta é SaaS, dados saem do controlo da organização.

**Critérios de aceitação (BDD).**
- **Dado** que ferramenta SaaS é proposta para armazenar requisitos  
  **Quando** avalio risco de supply chain  
  **Então** aplico controlos adequados ou rejeito ferramenta se risco > aceitável

**Checklist de avaliação SaaS.**
- [ ] **Due diligence do fornecedor:**
  - [ ] Certificações (ISO 27001, SOC 2 Type II)?
  - [ ] Localização de dados (GDPR: dados na UE)?
  - [ ] Política de retenção e eliminação de dados?
  - [ ] Histórico de breaches ou incidentes?
- [ ] **Controlos técnicos:**
  - [ ] Encriptação em trânsito (TLS 1.3+)?
  - [ ] Encriptação em repouso (AES-256)?
  - [ ] Customer-managed encryption keys (CMEK) disponível?
  - [ ] Autenticação MFA obrigatória para acesso admin?
  - [ ] Audit logs disponíveis e exportáveis?
- [ ] **Controlos contratuais:**
  - [ ] DPA (Data Processing Agreement) assinado?
  - [ ] Cláusula de notificação de breach (<24h)?
  - [ ] Direito de auditoria da segurança do fornecedor?
  - [ ] SLA de disponibilidade (99.9%+)?
  - [ ] Exit strategy (exportação de dados em <30 dias)?
- [ ] **Decisão:**
  - [ ] Se risco aceitável: Aprovar com controlos documentados
  - [ ] Se risco médio: Aprovar apenas para requisitos PÚBLICO/INTERNO
  - [ ] Se risco alto: Rejeitar ou exigir deployment on-premise/private cloud

**Artefacto:**
- Ficheiro: `avaliacoes-saas/SAAS-EVAL-[fornecedor]-YYYY-MM-DD.md`
- Decisão: Aprovado | Aprovado com restrições | Rejeitado
- Aprovador: CISO + GRC/Compliance
:::

**Ferramentas de alto risco (requerem avaliação rigorosa):**
- Jira Cloud, Confluence Cloud (se requisitos CONFIDENCIAL)
- Plataformas de threat modeling SaaS (ThreatModeler, IriusRisk)
- ServiceNow (se requisitos RESTRITO)
- Ferramentas de IA generativas (ChatGPT, GitHub Copilot) — **PROIBIDO para requisitos CONFIDENCIAL/RESTRITO**

---

## 📊 KPIs e Monitorização

### Indicadores de Segurança

| KPI | Meta | Frequência | Ação se não cumprido |
|---|---|---|---|
| **% requisitos classificados** | 100% | Mensal | Bloquear publicação de requisitos não-classificados |
| **% requisitos CONFIDENCIAL com acesso auditado** | 100% | Trimestral | Revisão de acessos por GRC |
| **Tempo médio de classificação** | <2 dias | Mensal | Formação adicional de AppSec |
| **Incidentes de exposição inadvertida** | 0 | Contínuo | Root cause analysis + correção de processo |
| **% requisitos RESTRITO revistos no prazo** | 100% | Semestral | Alerta a CISO + revisão forçada |

### Alertas Críticos

- **Alerta 1:** Requisito CONFIDENCIAL commitado em repositório público → **RESPOSTA IMEDIATA** (revoke commit, rotação de credenciais se aplicável)
- **Alerta 2:** Acesso a requisito RESTRITO por papel não-autorizado → **AUDITORIA** (quem, quando, por quê) + notificação CISO
- **Alerta 3:** Ferramenta SaaS sem DPA armazena requisitos CONFIDENCIAL → **BLOQUEIO** de integração + migração de dados

---

## 🔗 Integração com Outros Artefactos

| Artefacto | Integração com Confidencialidade |
|---|---|
| [addon-11: Validação Assistida](./11-validacao-requisitos-assistida) | Ferramentas SaaS que sugerem requisitos: avaliar risco supply chain |
| [addon-12: Versionamento](./12-versionamento-requisitos) | Histórico de versões pode revelar vulnerabilidades passadas → CONFIDENCIAL |
| [US-15: Audit Trail](../aplicacao-lifecycle#us-15) | Audit trail de decisões pode conter informações sensíveis → CONFIDENCIAL |
| [Catálogo de Requisitos](./catalogo-requisitos) | Dividir em public/ e confidential/ directories |
| [Matriz de Controlos por Risco](./matriz-controlos-por-risco) | Matriz genérica: PÚBLICO; Matriz detalhada por app: CONFIDENCIAL |

---

## 📐 Proporcionalidade por Nível

| Aspecto | L1 | L2 | L3 |
|---|---|---|---|
| **Classificação obrigatória?** | Recomendado (apenas CONFIDENCIAL) | Obrigatório (PÚBLICO/INTERNO/CONFIDENCIAL) | Obrigatório (todos os níveis) |
| **Controlo de acesso por papel** | Opcional | Obrigatório | Obrigatório + MFA + audit log |
| **Avaliação de ferramentas SaaS** | Opcional | Obrigatório (se CONFIDENCIAL) | Obrigatório (todos os requisitos) |
| **Revisão periódica de classificação** | Anual | Anual | Semestral |
| **Encriptação de requisitos RESTRITO** | N/A | Recomendado | Obrigatório (AES-256, CMEK) |
| **Audit log de acessos** | Não | Recomendado | Obrigatório (90 dias retenção) |

---

## ✅ Checklist de Implementação

- [ ] Estrutura de directórios criada: `public/`, `internal/`, `confidential/`, `restricted/`
- [ ] Matriz de controlo de acesso implementada (Git permissions ou ferramenta GRC)
- [ ] Template de classificação aplicado a todos os requisitos existentes
- [ ] Versões públicas criadas para requisitos CONFIDENCIAL críticos
- [ ] Avaliação de ferramentas SaaS completada (se aplicável)
- [ ] DPAs assinados com fornecedores SaaS
- [ ] Formação obrigatória ministrada (classificação + controlo de acesso)
- [ ] Dashboard de KPIs configurado (% classificados, incidentes, revisões)
- [ ] Alertas críticos configurados (commit público inadvertido, acesso não-autorizado)
- [ ] Política organizacional de classificação aprovada por CISO
- [ ] Processo de revisão periódica agendado (anual/semestral conforme nível)

---

**Última atualização**: 2026-01-01  
**Versão do addon**: 1.0.0  
**Autores**: AppSec Team + GRC/Compliance + CISO  
**Aprovação**: [Nome do CISO/Gestão Executiva] — [Data]
