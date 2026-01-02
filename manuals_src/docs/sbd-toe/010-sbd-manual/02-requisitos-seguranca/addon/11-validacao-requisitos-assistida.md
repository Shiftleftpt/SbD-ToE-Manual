---
id: validacao-requisitos-assistida
title: Validação de Requisitos Assistida por Ferramentas
description: Procedimentos de validação quando requisitos são sugeridos, gerados ou adaptados por ferramentas automatizadas
tags: [addon, validacao, ferramentas, automacao, ia, requisitos, agent.md]
---

# 🤖 Validação de Requisitos Assistida por Ferramentas

## 🎯 Objetivo

Este addon estabelece os **procedimentos de validação obrigatórios** quando requisitos de segurança são:
- **Sugeridos por ferramentas** de análise de código, SAST, dependency scanners ou frameworks de requisitos (ASVS, OWASP);
- **Gerados automaticamente** a partir de análise de arquitetura, mapeamento de superfície de ataque ou threat modeling assistido;
- **Adaptados automaticamente** por ferramentas de proporcionalidade de risco (ex: "aplicação L3 → requisitos reforçados").

**Contexto normativo:**  
Este addon implementa os pressupostos de [agent.md](https://github.com/your-org/agent-spec) (seção 7: Cap 02) e os 5 Invariantes Canónicos (I1–I5) no domínio de **engenharia de requisitos assistida**. É o paralelo conceptual de [Cap 01 - addon-11: Validação Assistida por Ferramentas](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/11-validacao-assistida-ferramentas), mas aplicado ao ciclo de vida de requisitos.

---

## 🔒 Os 5 Invariantes no Contexto de Requisitos

### **I1: Separação sugestão (ferramenta) vs. decisão (humana)**

**No contexto de requisitos:**
- **Ferramenta sugere**: "Aplicar requisito ASVS 2.1.1 (MFA obrigatório)" após análise de criticidade
- **Humano decide**: "Aceitar requisito ASVS 2.1.1" OU "Requisito não aplicável porque autenticação já delegada a IdP externo"
- **Registro obrigatório**: Quem aprovou/rejeitou, quando, por quê

**Violação típica:**  
Backlog populado automaticamente com requisitos extraídos de ASVS sem validação por AppSec Engineer ou Developer, resultando em sobrecarga de trabalho com requisitos não-contextuais.

---

### **I2: Evidência acima de plausibilidade**

**No contexto de requisitos:**
- **Plausibilidade**: "Requisito X parece adequado porque aplicação tem exposição pública"
- **Evidência**: "Requisito X é necessário porque threat model identifica ameaça T01 (Spoofing) sem mitigação"
- **Validação necessária**: Mapear requisito sugerido → ameaça real → controlo aplicado → evidência de teste

**Violação típica:**  
Requisitos aplicados porque "ferramenta recomendou" sem validar se a ameaça subjacente existe na aplicação específica (ex: requisito de proteção SQL Injection em app sem SQL).

---

### **I3: Reprodutibilidade e auditabilidade**

**No contexto de requisitos:**
- **Reprodutibilidade**: Capacidade de reexecutar ferramenta e obter os mesmos requisitos sugeridos (versionamento de ferramenta + configuração)
- **Auditabilidade**: Trilho de decisões: "Requisito REQ-XXX sugerido por ferramenta Y versão Z em data D; validado por especialista E; aprovado/rejeitado por razão R"
- **Versionamento obrigatório**: Cada requisito tem histórico de alterações (REQ-XXX-v1 → REQ-XXX-v2 porque critério mudou)

**Violação típica:**  
Requisitos definidos em backlog efémero (Jira, Azure Boards) sem versionamento, impossibilitando rastrear "por que requisito X foi alterado de L1 para L2".

---

### **I4: Proteção de ativos críticos**

**No contexto de requisitos:**
- **Risco**: Catálogo de requisitos pode revelar superfície de ataque da aplicação (ex: "Implementar WAF contra OWASP Top 10" revela vulnerabilidades web)
- **Confidencialidade**: Requisitos críticos (especialmente L3) devem ter controlo de acesso por papel (Developer, AppSec, GRC)
- **Supply chain**: Se ferramenta de requisitos é SaaS externa, dados enviados (arquitetura, tecnologias, ameaças) podem vazar

**Violação típica:**  
Requisitos documentados em Wiki público ou repositório sem controlo de acesso, expondo informações sensíveis a atacantes.

---

### **I5: Rastreabilidade de decisão e execução**

**No contexto de requisitos:**
- **Rastreabilidade de decisão**: REQ-XXX foi aceito/rejeitado por quem, quando, com base em que evidência
- **Rastreabilidade de execução**: REQ-XXX foi implementado (commit SHA), testado (resultado teste), validado (aprovação AppSec), deployado (artefacto assinado)
- **Integração**: Matriz `requisito | decisão | implementação | teste | evidência | aprovação`

**Violação típica:**  
Requisitos "implementados" sem evidência de teste ou validação, impossibilitando provar conformidade em auditoria.

---

## 🚨 Taxonomia de Erros: Riscos de Requisitos Assistidos

### **Erro Tipo A: Requisitos de catálogos externos sem validação**

**Descrição:**  
Ferramenta extrai requisitos de ASVS, OWASP WSTG, NIST SSDF ou CIS Benchmarks e insere diretamente no backlog sem validação de contexto.

**Exemplo concreto:**
```yaml
# Requisito sugerido por ferramenta (ASVS 2.1.1)
REQ-AUTH-001: "Implementar MFA para todos os utilizadores"

# Problema: Aplicação usa Azure AD com MFA já configurado
# Requisito duplicado e não-aplicável

# Validação necessária:
- [ ] Verificar se autenticação é delegada a IdP externo
- [ ] Confirmar que MFA já está ativo no IdP
- [ ] Decidir: Requisito não aplicável OU adaptar para "Validar MFA no IdP"
```

**Consequências:**
- **Sobreproteção**: Requisitos redundantes ou excessivos para o nível de risco
- **Underprotection**: Requisitos genéricos que não cobrem ameaças específicas da aplicação
- **Trabalho desnecessário**: Implementação de controlos já existentes

**Mitigação obrigatória:**
- [ ] Validação por **AppSec Engineer** de cada requisito sugerido
- [ ] Mapeamento `requisito → ameaça → contexto` antes de aprovar
- [ ] Aprovação explícita documentada (template seção 5.1)

---

### **Erro Tipo B: Requisitos auto-gerados de análise de arquitetura**

**Descrição:**  
Ferramenta analisa diagrama de arquitetura, identifica componentes (API, DB, autenticação) e gera requisitos automaticamente sem considerar decisões de design.

**Exemplo concreto:**
```yaml
# Requisito gerado por ferramenta de threat modeling
REQ-DATA-005: "Encriptar dados em repouso com AES-256"

# Problema: Aplicação usa Azure SQL Database com TDE já ativo
# Requisito duplicado com controlo gerido pela plataforma

# Validação necessária:
- [ ] Confirmar se encriptação é responsabilidade da aplicação ou da plataforma
- [ ] Se plataforma: adaptar requisito para "Validar TDE ativo no Azure SQL"
- [ ] Se aplicação: confirmar algoritmo e gestão de chaves
```

**Consequências:**
- **Falsos requisitos**: Controlos assumidos necessários quando já existem na plataforma
- **Lacunas críticas**: Ferramenta não deteta requisitos específicos de domínio (ex: conformidade GDPR para dados pessoais)
- **Desperdício de tempo**: Implementação de controlos desnecessários

**Mitigação obrigatória:**
- [ ] Revisão por **Arquitetos de Software** de requisitos gerados
- [ ] Validação de contexto: plataforma vs. aplicação
- [ ] Especialistas de domínio adicionam requisitos não-detetados
- [ ] Aprovação explícita documentada (template seção 5.2)

---

### **Erro Tipo C: Requisitos adaptados automaticamente por risco**

**Descrição:**  
Ferramenta ajusta automaticamente requisitos com base no nível de criticidade (L1/L2/L3) sem considerar proporcionalidade real.

**Exemplo concreto:**
```yaml
# Requisito base (L1)
REQ-LOG-001: "Registar eventos de autenticação (login, logout)"

# Adaptação automática para L3
REQ-LOG-001-L3: "Registar todos os eventos de autenticação + tentativas falhadas + mudanças de privilégios + acessos a dados críticos + retenção 5 anos"

# Problema: Requisito L3 pode ser desproporcional se aplicação não tem dados críticos
# Ou insuficiente se aplicação tem requisitos regulatórios específicos (ex: GDPR → retenção máxima 2 anos)

# Validação necessária:
- [ ] Confirmar se adaptação L3 é proporcional ao risco real
- [ ] Verificar requisitos regulatórios (GDPR, NIS2, DORA)
- [ ] Ajustar retenção, campos registados, destino logs
```

**Consequências:**
- **Sobreproteção**: Requisitos L3 excessivos para aplicações sem dados críticos
- **Não-conformidade**: Requisitos automáticos podem violar regulamentos (ex: retenção excessiva)
- **Falta de contexto**: Adaptação genérica não considera especificidades de negócio

**Mitigação obrigatória:**
- [ ] Validação por **GRC/Compliance** de requisitos regulatórios
- [ ] Revisão de proporcionalidade por **AppSec Engineer**
- [ ] Ajuste de critérios por especialistas de domínio
- [ ] Aprovação explícita documentada (template seção 5.3)

---

## ✅ Checklists de Validação por User Story

### **C1: Validação de US-01 (Seleção de Requisitos por Criticidade)**

**Contexto:**  
US-01 aplica matriz de controlos e extrai requisitos por nível (L1/L2/L3). Se assistido por ferramenta, checklist adicional é obrigatório.

**Checklist obrigatória quando assistido:**
- [ ] **Ferramenta identificada**: Nome, versão, data de execução documentados
- [ ] **Configuração rastreável**: Parâmetros de entrada (nível L1/L2/L3, tipo aplicação, frameworks) versionados
- [ ] **Output completo anexado**: Lista de requisitos sugeridos + raciocínio da ferramenta (se disponível)
- [ ] **Validação humana por requisito**:
  - [ ] Cada requisito sugerido foi revisto por **Developer** ou **Team Lead**
  - [ ] Requisitos não-aplicáveis foram identificados e justificados (ex: "MFA não aplicável porque IdP externo")
  - [ ] Requisitos em falta foram adicionados por especialistas (não-detetados pela ferramenta)
- [ ] **Aprovação final**: **AppSec Engineer** aprova lista final de requisitos (pode diferir da sugestão da ferramenta)
- [ ] **Registo de divergências**: Se ferramenta sugeriu X mas equipa decidiu Y, justificação documentada

**Integração com US-01:**  
O campo "Se assistida por ferramenta" em US-01 deve referenciar esta checklist (C1) e exigir cumprimento antes de DoD.

---

### **C2: Validação de US-05 (Definição de Critérios de Aceitação)**

**Contexto:**  
US-05 define critérios de aceitação para cada requisito (ex: "REQ-AUTH-001 cumprido se MFA ativo e testado"). Se critérios forem gerados automaticamente, validação é obrigatória.

**Checklist obrigatória quando assistido:**
- [ ] **Ferramenta identificada**: Nome, versão, método de geração de critérios documentados
- [ ] **Critérios sugeridos anexados**: Output da ferramenta com critérios propostos
- [ ] **Validação de testabilidade**:
  - [ ] Cada critério é objetivamente testável (não vago como "segurança adequada")
  - [ ] Critérios têm evidência clara (ex: "MFA testado" → log de teste + aprovação)
  - [ ] Critérios são proporcionais ao risco (L1 vs. L2 vs. L3)
- [ ] **Revisão por QA**: Critérios revistos por **QA** para confirmar viabilidade de teste
- [ ] **Aprovação por AppSec**: **AppSec Engineer** aprova critérios finais (pode ajustar sugestões da ferramenta)
- [ ] **Conflito ferramenta vs. especialista**: Se QA ou AppSec discordar, decisão final documentada com justificação

**Integração com US-05:**  
Adicionar campo "Se critérios assistidos por ferramenta" em DoD de US-05, exigindo cumprimento de C2.

---

### **C3: Validação de US-09 (Validação por Requisito/Domínio)**

**Contexto:**  
US-09 valida que cada requisito REQ-XXX tem evidência de implementação e teste. Se validação for automatizada (testes SAST/SCA/DAST), risco de falsos positivos.

**Checklist obrigatória quando assistido:**
- [ ] **Ferramenta de validação identificada**: Nome, versão, tipo (SAST, SCA, DAST, fuzzing) documentados
- [ ] **Resultados de scan anexados**: Relatórios completos com findings, severidades, contexto
- [ ] **Tratamento de falsos positivos**:
  - [ ] Findings marcados como "falso positivo" têm justificação técnica (não apenas "ignorar")
  - [ ] Validação manual obrigatória para **L3** em domínios críticos (criptografia, autenticação, privilege escalation)
  - [ ] Aprovação de falsos positivos por **AppSec Engineer** documentada
- [ ] **Validação de cobertura**:
  - [ ] Ferramenta validou todos os requisitos aplicáveis? (ex: SAST pode não cobrir requisitos de infraestrutura)
  - [ ] Lacunas identificadas são cobertas por testes manuais ou outros métodos
- [ ] **Aprovação final**: **AppSec Engineer** aprova que requisito está validado (mesmo se ferramenta reportou "pass")
- [ ] **Escalação de conflito**: Se ferramenta reporta "pass" mas AppSec identifica issue, procedimento de escalação aplicado (seção 6)

**Integração com US-09:**  
Adicionar campo "Se validação assistida por ferramenta" em DoD de US-09, exigindo cumprimento de C3.

---

## 🔀 Procedimentos de Escalação: Developer vs. Tool vs. AppSec

### **Cenário 1: Ferramenta sugere requisito, Developer discorda**

**Exemplo:**  
- **Ferramenta**: "Aplicar REQ-DATA-005: Encriptar dados em repouso com AES-256"  
- **Developer**: "Dados já encriptados por Azure SQL TDE, requisito duplicado"

**Procedimento:**
1. **Developer documenta discordância**: Issue ou comentário em backlog com justificação técnica
2. **AppSec Engineer revisa**: Valida se TDE cobre o requisito ou se há gap adicional
3. **Decisão final**:
   - Se TDE suficiente: Requisito marcado como "Não aplicável - Controlo na plataforma"
   - Se TDE insuficiente (ex: dados em cache não cobertos): Requisito adaptado para "Encriptar dados em cache com AES-256"
4. **Registo**: Decisão documentada em `requisitos-decisoes.md` (template seção 7)

---

### **Cenário 2: Ferramenta reporta "pass", AppSec identifica falha**

**Exemplo:**  
- **SAST Tool**: "REQ-AUTH-001 (MFA) validado: Código usa biblioteca MFA"  
- **AppSec Engineer**: "MFA configurado mas não obrigatório, utilizadores podem bypass"

**Procedimento:**
1. **AppSec documenta finding**: Issue crítico com evidência (screenshot, log, código)
2. **Developer corrige**: Implementa obrigatoriedade de MFA (ex: middleware de validação)
3. **Re-teste obrigatório**: SAST + teste manual por QA
4. **Aprovação**: AppSec valida correção antes de marcar requisito como cumprido
5. **Registo**: Falso positivo documentado em `validacao-falsos-positivos.md` (template seção 7) para ajustar ferramenta no futuro

---

### **Cenário 3: Especialista adiciona requisito não-detetado por ferramenta**

**Exemplo:**  
- **Ferramenta**: Lista 20 requisitos extraídos de ASVS  
- **GRC/Compliance**: "Falta requisito GDPR: Direito ao esquecimento (REQ-GDPR-001)"

**Procedimento:**
1. **Especialista documenta requisito em falta**: Issue em backlog com justificação (requisito regulatório)
2. **AppSec revisa e aprova**: Valida se requisito é aplicável e proporcional
3. **Requisito adicionado ao catálogo**: Integrado na matriz de controlos com tag `source:manual`
4. **Ferramenta atualizada (se possível)**: Configuração ajustada para detetar requisito no futuro
5. **Registo**: Lacuna documentada em `lacunas-ferramentas.md` (template seção 7) para tracking de melhoria contínua

---

## 📋 Templates de Documentação

### **Template 1: Registo de Decisão de Requisito**

```markdown
---
id: REQ-DECISAO-YYYY-MM-DD-XXX
data: YYYY-MM-DD
requisito: REQ-XXX-vY
ferramenta: [Nome da ferramenta | Manual]
versao_ferramenta: X.Y.Z (se aplicável)
---

## Contexto
- **Requisito sugerido por**: [Ferramenta | Especialista | Regulamento]
- **Fonte**: [ASVS 2.1.1 | Threat Model | GDPR Art. 17]
- **Nível de criticidade**: [L1 | L2 | L3]

## Sugestão da Ferramenta (se aplicável)
```yaml
requisito: REQ-AUTH-001
descricao: "Implementar MFA para todos os utilizadores"
justificacao: "Aplicação classificada como L2, ASVS recomenda MFA"
```

## Validação Humana
- **Revisor**: [Nome do Developer/AppSec]
- **Data revisão**: YYYY-MM-DD
- **Decisão**: [Aceitar | Rejeitar | Adaptar]
- **Justificação**: [Texto explicativo]

## Decisão Final
- **Status**: [Aprovado | Rejeitado | Adaptado]
- **Aprovador**: [Nome do AppSec Engineer]
- **Data aprovação**: YYYY-MM-DD
- **Requisito final**: REQ-XXX-vY (se adaptado, incluir nova descrição)
- **Rastreamento**: [Link para issue | PR | documento]

## Evidências
- [ ] Output da ferramenta anexado (se aplicável)
- [ ] Justificação técnica documentada
- [ ] Aprovação formal registada
```

---

### **Template 2: Registo de Falsos Positivos**

```markdown
---
id: FP-YYYY-MM-DD-XXX
data: YYYY-MM-DD
requisito: REQ-XXX-vY
ferramenta: [Nome da ferramenta de validação]
---

## Contexto
- **Ferramenta reportou**: [Pass | Fail | Warning]
- **Realidade**: [Requisito não cumprido | Falso positivo | Lacuna]
- **Severidade**: [Crítica | Alta | Média | Baixa]

## Evidência do Falso Positivo
- **Finding da ferramenta**: [Transcrição ou screenshot]
- **Validação manual**: [Descrição técnica do teste manual]
- **Conclusão**: [Por quê é falso positivo]

## Ação Corretiva
- **Correção no código**: [Sim | Não] (se não, justificar)
- **Ajuste na ferramenta**: [Regra ajustada | Configuração alterada | N/A]
- **Re-teste**: [Data | Resultado]

## Aprovação
- **Aprovador**: [Nome do AppSec Engineer]
- **Data aprovação**: YYYY-MM-DD
- **Comentários**: [Observações adicionais]
```

---

### **Template 3: Registo de Lacunas de Ferramenta**

```markdown
---
id: LACUNA-YYYY-MM-DD-XXX
data: YYYY-MM-DD
ferramenta: [Nome da ferramenta]
---

## Descrição da Lacuna
- **Requisito não-detetado**: REQ-XXX-vY
- **Motivo**: [Limitação técnica | Falta de configuração | Domínio específico]
- **Impacto**: [Crítico | Alto | Médio | Baixo]

## Descoberta
- **Descoberto por**: [Nome do especialista]
- **Método de descoberta**: [Revisão manual | Teste | Auditoria]
- **Data descoberta**: YYYY-MM-DD

## Mitigação Aplicada
- **Requisito adicionado manualmente**: [Sim | Não]
- **Tag no catálogo**: `source:manual`
- **Processo alternativo**: [Descrição de como requisito será validado no futuro]

## Melhoria Futura
- **Possível ajuste na ferramenta**: [Sim | Não] (se sim, descrever)
- **Follow-up**: [Issue criada | Feature request | N/A]
- **Responsável**: [Nome]
- **Prazo**: YYYY-MM-DD
```

---

## 🔗 Integração com User Stories Existentes

### **Mapeamento US → Checklist → Erro Tipo**

| User Story | Checklist Obrigatória | Erro Tipo Mitigado | Template Aplicável |
|---|---|---|---|
| US-01 (Seleção de requisitos) | C1 | Erro A (catálogos sem validação) | Template 1 (Decisão) |
| US-05 (Critérios de aceitação) | C2 | Erro B (auto-gerados) + Erro C (adaptação automática) | Template 1 (Decisão) |
| US-09 (Validação por requisito) | C3 | Risco de falsos positivos em testes automatizados | Template 2 (Falsos Positivos) |
| US-02 (Revisão por alteração) | C1 (se ferramenta re-sugere requisitos) | Erro A + Erro C | Template 1 (Decisão) |
| US-04 (Análise de risco residual) | Manual (sem checklist específica) | - | Template 1 (justificar exceção) |

---

## 📚 Exemplos Práticos

### **Exemplo 1: Boas Práticas — Validação de Requisito ASVS Assistida**

**Cenário:**  
Ferramenta extrai requisitos ASVS para aplicação L2, sugere 30 requisitos. Equipa valida cada um antes de aprovar.

**Processo aplicado:**
1. **Ferramenta executa**: SonarQube Security Scan v9.x sugere 30 requisitos ASVS baseados em análise de código
2. **Developer revisa**: Identifica 5 requisitos não-aplicáveis (ex: "SQL Injection protection" mas app usa NoSQL)
3. **Especialista adiciona**: GRC identifica 2 requisitos GDPR em falta (direito ao esquecimento, portabilidade)
4. **AppSec aprova**: Valida lista final de 27 requisitos (30 - 5 + 2), documenta decisões
5. **Rastreamento**: Cada decisão registada com Template 1 (Decisão de Requisito)

**Evidências:**
- Output da ferramenta: `sonarqube-scan-2026-01-15.json`
- Decisões documentadas: 7 ficheiros `REQ-DECISAO-*.md` (5 rejeições + 2 adições)
- Aprovação: Email de AppSec Engineer datado 2026-01-20

**Resultado:**  
Lista de requisitos final é contextual, proporcional e auditável. Ferramenta acelerou processo mas não substituiu decisão humana.

---

### **Exemplo 2: Más Práticas — Requisitos Auto-Aplicados sem Validação**

**Cenário:**  
Ferramenta extrai 50 requisitos ASVS e insere automaticamente no backlog Jira. Equipa implementa todos sem questionar.

**Problemas identificados:**
1. **Sobreproteção**: 15 requisitos eram redundantes (controlos já existentes na plataforma Azure)
2. **Underprotection**: 3 requisitos críticos de domínio (GDPR, PCI-DSS) não foram detetados
3. **Desperdício**: 2 sprints gastos implementando controlos desnecessários
4. **Falta de rastreabilidade**: Nenhuma decisão documentada, impossível auditar "por quê requisito X foi aplicado"

**Consequências:**
- **Custo**: ~80 horas de desenvolvimento desperdiçadas
- **Risco**: Lacunas críticas não-cobertas (GDPR)
- **Não-conformidade**: Auditoria reprovada por falta de evidências de decisão

**Correção aplicada:**
- Revisão retroativa de todos os 50 requisitos com AppSec Engineer
- Documentação de decisões com Template 1 (7 dias de trabalho)
- Remoção de 15 requisitos redundantes, adição de 3 críticos em falta
- Implementação de checklist C1 para futuras execuções

---

### **Exemplo 3: Boas Práticas — Escalação de Conflito Developer vs. Tool**

**Cenário:**  
SAST reporta "REQ-CRYPTO-001 cumprido" mas AppSec identifica uso de algoritmo fraco (SHA-1).

**Processo aplicado:**
1. **SAST reporta**: "Criptografia detetada: SHA-1 usado para hashing"
2. **AppSec revisa**: Identifica que SHA-1 é inadequado para assinaturas (collision attacks)
3. **Issue criada**: Finding crítico documentado com evidência (código, referências CVE)
4. **Developer corrige**: Substitui SHA-1 por SHA-256 em 2 horas
5. **Re-teste**: SAST + validação manual por AppSec confirmam correção
6. **Registo**: Falso positivo documentado com Template 2 (ferramenta ajustada para detetar SHA-1 como "fraco")

**Evidências:**
- Finding SAST: `sast-report-2026-01-18.pdf` (página 15)
- Issue crítico: `SEC-2026-042` em Jira
- Correção: Commit `abc123def` com tag `security-fix`
- Aprovação: Comentário de AppSec Engineer em issue

**Resultado:**  
Falso positivo corrigido em <24h, ferramenta ajustada para evitar recorrência, processo de escalação validado.

---

## 🎓 Formação e Sensibilização

### **Públicos-alvo:**
- **Developers**: Compreender quando validar requisitos sugeridos por ferramentas (Checklist C1)
- **AppSec Engineers**: Procedimentos de aprovação e escalação (seção 6)
- **QA**: Validação de critérios de aceitação gerados automaticamente (Checklist C2)
- **GRC/Compliance**: Identificar requisitos regulatórios não-detetados (seção 5, Erro Tipo A)

### **Materiais obrigatórios:**
- [ ] Apresentação: "5 Invariantes no Contexto de Requisitos" (30 min)
- [ ] Hands-on: Aplicação de Checklist C1 em requisito ASVS real (1 hora)
- [ ] Quiz de validação: 10 perguntas sobre escalação de conflitos (aprovação mínima: 80%)
- [ ] Certificação: Attestation de participação + compreensão registada

### **Cadência:**
- **Inicial**: Obrigatória para todos os papéis antes de participar em US-01/US-05/US-09
- **Anual**: Refresh training com atualizações de ferramentas e lições aprendidas
- **Ad-hoc**: Quando nova ferramenta de requisitos for introduzida

---

## 📊 Métricas e KPIs

### **KPI 1: Taxa de aceitação de requisitos sugeridos**
- **Definição**: % de requisitos sugeridos por ferramenta que foram aceitos sem alteração
- **Meta**: 60-80% (se >90%, ferramenta pode estar sub-configurada; se <50%, sobre-sugestão)
- **Fonte**: Comparar output ferramenta vs. lista final aprovada

### **KPI 2: Tempo médio de validação por requisito**
- **Definição**: Tempo entre sugestão da ferramenta e aprovação final por AppSec
- **Meta**: <2 dias úteis (L1), <5 dias úteis (L2/L3)
- **Fonte**: Timestamps em `REQ-DECISAO-*.md`

### **KPI 3: Taxa de falsos positivos em validação**
- **Definição**: % de requisitos marcados como "cumpridos" por ferramenta mas reprovados por AppSec
- **Meta**: <5% (se >10%, ferramenta precisa ajuste)
- **Fonte**: Ficheiros `FP-*.md` (Template 2)

### **KPI 4: Lacunas de ferramenta identificadas**
- **Definição**: Número de requisitos críticos não-detetados por ferramenta, adicionados manualmente
- **Meta**: <3 por aplicação L2/L3 (se >5, considerar ferramenta adicional)
- **Fonte**: Ficheiros `LACUNA-*.md` (Template 3)

### **KPI 5: Conformidade a checklists obrigatórias**
- **Definição**: % de US-01/US-05/US-09 assistidas onde checklist C1/C2/C3 foi cumprida
- **Meta**: 100% em L2/L3, >90% em L1
- **Fonte**: Audit trail de DoD em backlog

---

## 🔗 Ligações Úteis

- [Cap 01 - addon-11: Validação Assistida por Ferramentas (Classificação)](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/11-validacao-assistida-ferramentas) — Paralelo conceptual para classificação
- [Cap 02 - intro.md: Fundamentos de Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap 02 - US-01: Seleção de Requisitos por Criticidade](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-01)
- [Cap 02 - US-05: Definição de Critérios de Aceitação](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-05)
- [Cap 02 - US-09: Validação por Requisito/Domínio](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-09)
- [agent.md: Invariantes Canónicos I1-I5](https://github.com/your-org/agent-spec) — Especificação normativa
- [07-roles.md: Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

---

## 📝 Revisão e Manutenção

- **Owner**: AppSec Engineer (lidera revisão)
- **Contribuidores**: GRC/Compliance (requisitos regulatórios), QA (critérios de teste), Developers (feedback operacional)
- **Frequência de revisão**: Anual ou quando nova ferramenta de requisitos for introduzida
- **Versionamento**: Este addon segue versionamento semântico (v1.0.0 = inicial, v1.1.0 = novos templates, v2.0.0 = mudança de processo)
- **Aprovação de alterações**: GRC/Compliance + AppSec Engineer + mínimo 2 Developers

---

## ✅ Checklist de Implementação do Addon

- [ ] Addon publicado em wiki/repositório acessível a todas as equipas
- [ ] Checklists C1/C2/C3 integradas em DoD de US-01/US-05/US-09 (ver seção 8)
- [ ] Templates 1/2/3 disponíveis em repositório com instruções de uso
- [ ] Formação obrigatória ministrada a Developers, AppSec, QA, GRC (ver seção 9)
- [ ] Procedimentos de escalação comunicados e testados (ver seção 6)
- [ ] KPIs configurados em dashboard de governança (ver seção 10)
- [ ] Revisão anual agendada com GRC/Compliance + AppSec
- [ ] Política organizacional de validação de requisitos assistidos aprovada por Gestão Executiva (se aplicável, ver Cap 01 US-11)

---

**Última atualização**: 2026-01-01  
**Versão**: 1.0.0  
**Autores**: AppSec Team + GRC/Compliance  
**Aprovação**: [Nome do CISO/Gestão Executiva] — [Data]
