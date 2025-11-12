---
id: aplicacao-lifecycle
title: Como Fazer
description: Como aplicar as práticas prescritas de segurança em containers ao longo do ciclo de vida de desenvolvimento e operação
tags: [tipo:aplicacao, ciclo-vida, containers, imagens, seguranca, isolamento, sbom, supply-chain]
genia: us-format-normalization
---

# ⚙️ Aplicação ao Ciclo de Vida - Containers e Execução Isolada

Garantir a segurança de *containers* não é apenas uma preocupação de runtime: envolve decisões desde a seleção da imagem base até ao modo como estas imagens são executadas, monitorizadas e auditadas.  
Este capítulo mostra, de forma prescritiva e integrada, como aplicar controlos técnicos e de governação em cada fase do ciclo de vida.

---

## 🧭 Quando aplicar

Os riscos associados a containers surgem em diferentes momentos: na escolha da imagem base, na forma como é construída, nas políticas aplicadas em produção e até na reação a incidentes.  
A tabela seguinte sintetiza **quando cada prática deve ser aplicada** e qual a justificação que suporta a sua necessidade.

| Fase SDLC | Ação | Justificação |
|-----------|------|--------------|
| Design / Planeamento | Definir baseline de segurança para imagens e runtime | Evitar vulnerabilidades desde a conceção |
| Desenvolvimento | Construção de imagens a partir de bases confiáveis e **pinned** | Mitigar risco de supply chain |
| CI/CD | Linters, SCA e scanners de imagens automáticos em pipelines | *Shift-left* de vulnerabilidades e misconfigs |
| Pré-produção | Assinatura de imagens, validação de proveniência, políticas Admission Control | Garantir integridade antes do go-live |
| Produção | Monitorização de execução, runtime enforcement e resposta a incidentes | Minimizar impacto de exploração em execução |

---

## 👥 Quem executa cada ação

A segurança em containers exige uma **responsabilidade partilhada**.  
Cada papel contribui com uma parte da cadeia de confiança, e apenas a colaboração entre equipas garante que o ciclo de vida se mantém íntegro.

| Papel | Responsabilidades principais |
|-------|-------------------------------|
| **Dev Team** | Especificar dependências, construir imagens seguras, corrigir vulnerabilidades identificadas |
| **DevOps / Plataforma** | Manter repositórios de imagens confiáveis, configurar pipelines, *enforcing* Admission Control |
| **AppSec** | Definir políticas, rever alertas críticos, validar conformidade com baseline de segurança |
| **GRC / Auditoria** | Validar registos de conformidade, exceções e governação sobre imagens e runtime |

---

## 📖 User Stories Reutilizáveis

### US-01 – Construção de imagens a partir de bases seguras, minimalistas e pinned por digest

**Contexto.**  
Imagens construídas sobre bases não confiáveis ou com versões flutuantes herdam vulnerabilidades. O ponto de partida é crítico para toda a cadeia de confiança.

:::userstory
**História.**   
Como **Dev Team**, quero construir imagens a partir de bases confiáveis, versionadas por digest SHA256 e sem componentes desnecessários, para reduzir superfície de ataque e garantir rastreabilidade desde o primeiro byte.

**Critérios de aceitação (BDD).**  
- **Dado** que início a construção de uma imagem de container  
  **Quando** seleciono a imagem base  
  **Então** a imagem referida tem origem confiável (repositório oficial) e digest fixo (`sha256:...`)
- **Dado** um Dockerfile novo  
  **Quando** é submetido  
  **Então** o linter (Hadolint) não reporta pacotes desnecessários (`curl`, `bash`, `wget`, `ping`) em runtime
- **Dado** uma imagem construída  
  **Quando** é publicada  
  **Então** contém apenas binários e bibliotecas necessários para a aplicação funcionar

**Checklist.**  
- [ ] Imagem base de repositório oficial confiável (ex: `gcr.io/distroless`, `alpine:3.19` com hash)
- [ ] Digest SHA256 fixo no Dockerfile (sem `latest` ou tags flutuantes)
- [ ] Sem ferramentas interativas instaladas (shells, debug tools)
- [ ] Multi-stage build utilizado para remover resíduos de compilação
- [ ] Utilizador não-root definido na imagem (`USER nobody` ou equivalente)
- [ ] Dockerfile validado por Hadolint

:::

**🧾 Artefactos & evidências.**  
- `Dockerfile` com digest fixo no repositório Git
- Output de `hadolint Dockerfile` sem bloqueios críticos
- Relatório de layers da imagem publicada

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Imagens oficiais com versão (não `latest`) |
| L2 | Sim | Digest fixo + validação Hadolint + sem ferramentas interativas |
| L3 | Sim | Digest fixo + Hadolint + multi-stage + Distroless + scanner integrado na build |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Desenvolvimento | Construção inicial da imagem | Dev Team | Imediato |

**Ligações úteis.**  
[Imagens Base Seguras](/sbd-toe/sbd-manual/containers-imagens/addon/imagens-base)  

---

### US-02 – Validação automática de vulnerabilidades em imagens no pipeline CI/CD

**Contexto.**  
Vulnerabilidades descobertas tarde no ciclo têm custo exponencial. Shift-left é imperativo: identificar CVEs durante a build, não em produção.

:::userstory
**História.**   
Como **DevOps**, quero que o pipeline execute scanners de vulnerabilidades (SCA) em cada build de imagem e bloqueie automaticamente se o risco exceder o threshold definido, para reduzir risco de supply chain.

**Critérios de aceitação (BDD).**  
- **Dado** que uma imagem é construída no pipeline  
  **Quando** o scanner SCA (ex: Trivy) é executado  
  **Então** gera relatório com CVEs catalogadas por severidade (Critical, High, Medium, Low)
- **Dado** um CVE com severidade acima do threshold (ex: High em L2)  
  **Quando** o scanner identifica  
  **Então** o pipeline falha e o build é bloqueado
- **Dado** uma vulnerability com fix disponível  
  **Quando** é reportada  
  **Então** o relatório inclui versão recomendada para update

**Checklist.**  
- [ ] Scanner SCA (Trivy, Grype, ou similar) integrado no CI/CD
- [ ] Threshold definido por nível de risco (L1: bloqueio Critical; L2: bloqueio High+; L3: bloqueio Medium+)
- [ ] Relatório anexado ao PR ou artefacto de build
- [ ] Bloqueio automático se limiar violado (não apenas aviso)
- [ ] Relatório exportado em formato estruturado (JSON/SARIF) para auditoria

:::

**🧾 Artefactos & evidências.**  
- Logs do scanner no pipeline
- Relatório JSON do Trivy/Grype
- Comentário automático no PR com resultados

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Aviso de Critical + Medium |
| L2 | Sim | Bloqueio de High/Critical |
| L3 | Sim | Bloqueio de Medium+ |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Build da imagem | DevOps | Automático |

**Ligações úteis.**  
[Vulnerabilidades em Imagens](/sbd-toe/sbd-manual/containers-imagens/addon/vulnerabilidades-imagens)  

---

### US-03 – Assinatura e verificação de proveniência de imagens com Cosign e Rekor

**Contexto.**  
Sem proveniência verificável, imagens podem ser adulteradas ou substituídas. A assinatura é o segundo pilar da confiança (após a construção segura).

:::userstory
**História.**   
Como **AppSec**, quero que todas as imagens produzidas sejam assinadas digitalmente e tenham proveniência verificável registada em transparency log, para garantir integridade e origem em todo o deploy.

**Critérios de aceitação (BDD).**  
- **Dado** que uma imagem foi construída e publicada  
  **Quando** o pipeline conclui o build  
  **Então** a imagem é assinada com `cosign sign` utilizando identidade federada (OIDC) ou chave privada
- **Dado** uma imagem assinada  
  **Quando** é publicada  
  **Então** a assinatura é registada no transparency log Rekor (public ou private) com timestamp e hash da imagem
- **Dado** um cluster Kubernetes  
  **Quando** um pod tenta usar imagem não assinada (em L2/L3)  
  **Então** a Admission Control (Kyverno/OPA) rejeita a criação

**Checklist.**  
- [ ] Assinatura Cosign ativa no pipeline
- [ ] OIDC federado configurado (ex: GitHub Actions, GitLab CI) para emitir tokens sem chaves estáticas
- [ ] Transparency log (Rekor) integrado
- [ ] Verificação automática antes de deploy
- [ ] Policy de Admission Control configurada (OPA/Kyverno) para rejeitar não-assinadas em L2/L3

:::

**🧾 Artefactos & evidências.**  
- Assinatura Cosign anexada à imagem no registry
- Entrada no Rekor com proveniência
- Logs de verificação Cosign no pipeline

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Assinatura opcional, aviso se não assinada |
| L2 | Recomendado | Assinatura recomendada, verificação em Admission Control |
| L3 | Sim | Assinatura obrigatória, verificação bloqueante |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Pré-produção | Publicação em registry | AppSec + DevOps | Antes do deploy |

**Ligações úteis.**  
[Assinatura e Cadeia de Trust](/sbd-toe/sbd-manual/containers-imagens/addon/assinatura-cadeia-trust)  

> **Padrão Comum:** Assinatura e verificação de proveniência ocorrem em **múltiplos contextos** 
> (CI/CD, IaC, imagens container, deploy). Este US foca o contexto de **imagens container** com 
> *Cosign* e *Rekor*; ver também [Cap 07-US-06: Assinatura e proveniência em artefactos CI/CD] 
> e [Cap 08-US-09: Assinatura de módulos IaC]. Todos aplicam o **mesmo princípio** (sign → validate → use).

---

### US-04 – Aplicação de políticas formais de segurança no runtime com OPA/Kyverno

**Contexto.**  
Um container sem restrições de execução expande a superfície de ataque exponencialmente. Políticas formais garantem conformidade automática com baseline de segurança.

:::userstory
**História.**   
Como **DevOps**, quero que todas as execuções de containers em Kubernetes sejam validadas por políticas formais (OPA/Kyverno), para garantir que apenas workloads conformes com baseline de segurança são permitidos.

**Critérios de aceitação (BDD).**  
- **Dado** que um pod é criado no cluster  
  **Quando** a política de admissão valida  
  **Então** rejeita qualquer pod que não cumpra: `runAsNonRoot: true`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, `capabilities: drop: ["ALL"]`
- **Dado** um pod que viola a política  
  **Quando** tenta ser criado  
  **Então** é bloqueado e o evento é auditado
- **Dado** uma tentativa de *bypass* (ex: `privileged: true`)  
  **Quando** é detetada  
  **Então** a tentativa é registada e gera alerta

**Checklist.**  
- [ ] OPA/Kyverno instalado no cluster
- [ ] Políticas escritas em Rego (OPA) ou YAML (Kyverno) e versionadas
- [ ] Modo `audit` primeiro (logging sem bloqueio), depois `enforce` (bloqueio ativo)
- [ ] Regras específicas por namespace ou label (ex: `tier=production` mais restritivo)
- [ ] Documentação clara das políticas e exemplos de conformidade

:::

**🧾 Artefactos & evidências.**  
- Manifests de políticas OPA/Kyverno no repositório
- Logs de rejeições e aceitações de pods
- Relatório de auditoria de tentativas violadas

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Validação básica (non-root) em modo audit |
| L2 | Sim | Policies restritivas em modo enforce |
| L3 | Sim | Policies completas + auditoria detalhada + revisão periódica |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Produção | Criação de pod | DevOps | Imediato |

**Ligações úteis.**  
[Hardening de Containers](/sbd-toe/sbd-manual/containers-imagens/addon/hardening-containers), [Policies de Runtime OPA](/sbd-toe/sbd-manual/containers-imagens/addon/policies-runtime-opa)  

---

### US-05 – Monitorização e Resposta a Incidentes em Runtime

**Contexto.**  
Ataques de runtime só são detetados com monitorização ativa contínua. Ausência de alertas permite persistência silenciosa de comprometimentos.

:::userstory
**História.**   
Como **AppSec + GRC**, quero monitorizar comportamento de containers em execução e gerar alertas para eventos suspeitos, para permitir deteção e resposta rápida a incidentes de segurança.

**Critérios de aceitação (BDD).**  
- **Dado** que um container está em execução em produção  
  **Quando** ocorre comportamento suspeito (ex: acesso a ficheiros críticos, alteração de binários, tentativa de escape)  
  **Então** o evento deve ser registado em log centralizado e gerar alerta imediato
- **Dado** um incidente crítico detetado  
  **Quando** ocorre  
  **Então** alertas são enviados a canais configurados (Slack, PagerDuty, etc.) com contexto completo
- **Dado** uma investigação de incidente  
  **Quando** é necessário rastreabilidade  
  **Então** logs completos incluem: timestamp, pod, namespace, container, processo, actor, ação, resultado

**Checklist.**  
- [ ] Tool de monitorização runtime (ex: Falco, Sysdig, AppArmor) instalada
- [ ] Policies de detecção baseadas em comportamento anómalo
- [ ] Alertas para eventos críticos (escalada de privilégios, file modifications, network escape)
- [ ] Integração com sistema de alertas (SIEM, Prometheus, webhooks)
- [ ] Playbook de resposta a incidentes documentado e testado
- [ ] Retenção de logs com período mínimo definido (ex: 90 dias L2, 180 dias L3)
- [ ] Dashboard de eventos em tempo real

:::

**🧾 Artefactos & evidências.**  
- Configuração do runtime monitor versionada em Git
- Logs estruturados (JSON) centralizados
- Alertas configurados no SIEM
- Playbook de resposta a incidentes
- Relatório de incidentes detetados/investigados

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Monitorização básica, alertas críticos |
| L2 | Sim | Alertas críticos configurados, playbook documentado |
| L3 | Sim | Cobertura total, resposta automática, investigação correlacionada |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Produção | Execução de containers | AppSec + GRC | Contínuo, resposta em minutos |

**Ligações úteis.**  
[Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-06 – Geração e Rastreabilidade de SBOM em Imagens

**Contexto.**  
Sem SBOM, não há visibilidade sobre componentes presentes nem análise rápida de impacto de CVEs. SBOM é prerequisito para supply chain integrity.

:::userstory
**História.**   
Como **DevOps**, quero gerar SBOM (Software Bill of Materials) automaticamente a cada build de imagem e armazená-lo versionado, para permitir rastreabilidade de componentes, análise de vulnerabilidades e compliance auditável.

**Critérios de aceitação (BDD).**  
- **Dado** que uma imagem é construída no pipeline  
  **Quando** o build conclui  
  **Então** é gerado SBOM em formato CycloneDX/SPDX JSON com todas as camadas e dependências
- **Dado** um SBOM gerado  
  **Quando** é armazenado  
  **Então** é versionado com a imagem (tag, digest, timestamp) e acessível para auditoria
- **Dado** uma análise de vulnerabilidades  
  **Quando** é executada  
  **Então** usa SBOM como input e correlaciona CVEs a componentes específicos

**Checklist.**  
- [ ] SBOM gerado automaticamente (Syft, Trivy, ou similar)
- [ ] Formato CycloneDX ou SPDX JSON (compatível com ecosistema)
- [ ] SBOM anexado ao artefacto de build (registry label, armazenamento separado)
- [ ] Incluem todas as dependências diretas e transitivas
- [ ] Versionado com hash da imagem e identificador de build
- [ ] Retenção mínima de 1 ano
- [ ] Consulta disponível para auditoria e compliance

:::

**🧾 Artefactos & evidências.**  
- Ficheiro `sbom.json` (ou similar) versionado por imagem
- Metadata no registry (labels/annotations com SBOM reference)
- SBOM correlacionado com build ID e pipeline logs

> **Referência:** Este US especializa [Cap 05-US-02: SBOM em cada build]
> para o contexto de imagens e containers. SBOM de imagens deve incluir todas as camadas e dependências de sistema, complementando SBOM de dependências de aplicação.

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | SBOM básico, formato Syft JSON |
| L2 | Sim | SBOM completo em CycloneDX, retenção 1 ano |
| L3 | Sim | SBOM em CycloneDX, integração com proveniência (assinado), retenção 2+ anos |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Build de imagem | DevOps | Em cada build |

**Ligações úteis.**  
[Inventário e SBOM](/sbd-toe/sbd-manual/containers-imagens/addon/inventario-sbom), [Dependências, SBOM e SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)  

---

### US-07 – Governação de Registries com Allowlist e Digest-Only

**Contexto.**  
Pulls de registries não confiáveis ou com tags mutáveis expõem a cadeia de fornecimento a ataques de typosquatting e image tampering. Governance forma é imperativa.

:::userstory
**História.**   
Como **DevOps + AppSec**, quero impor allowlist de registries confiáveis e ***enforce* referências por digest SHA256** (nunca por tag), para impedir uso de imagens não verificadas ou adulteradas.

**Critérios de aceitação (BDD).**  
- **Dado** que um workload referencia uma imagem  
  **Quando** a política de Admission Control verifica a origem  
  **Então** rejeita se a imagem não estiver em allowlist ou se for referenciada por tag (aceita apenas digest `sha256:...`)
- **Dado** uma tentativa de pull de registry não confiável  
  **Quando** é executada  
  **Então** é bloqueada com mensagem clara de policy violation
- **Dado** um tag flutuante (ex: `latest`, `v1`)  
  **Quando** é referenciado em workload  
  **Então** é rejeitado; exigir digest fixo

**Checklist.**  
- [ ] Allowlist de registries confiáveis documentada e publicada
- [ ] Política OPA/Kyverno obrigando referências por digest
- [ ] Bloqueio de tags mutáveis (latest, stable, master, v1.x, etc.)
- [ ] Exceções formalizadas e auditadas (com prazo)
- [ ] Validação de integridade (ex: verificação de assinatura, SBOM)
- [ ] Rejeição automática de imagens não assinadas em L2/L3
- [ ] Relatorios mensais de tentativas bloqueadas

:::

**🧾 Artefactos & evidências.**  
- `registry-allowlist.yaml` versionado no repositório
- Policy OPA/Kyverno aplicada e auditada
- Logs de Admission Controller com rejeições
- Exceções registadas com justificativa e prazo

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Aviso para registries não confiáveis |
| L2 | Sim | Allowlist com bloqueio por origem, digest recomendado |
| L3 | Sim | Allowlist restritivo + digest-only obrigatório + assinatura verificada |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy | Definição de workload | DevOps + AppSec | Antes do go-live |

**Ligações úteis.**  
[Assinatura e Cadeia de Trust](/sbd-toe/sbd-manual/containers-imagens/addon/assinatura-cadeia-trust), [Policies de Runtime OPA](/sbd-toe/sbd-manual/containers-imagens/addon/policies-runtime-opa)

---

### US-08 – Gestão de Segredos Fora da Imagem com OIDC e Workload Identity

**Contexto.**  
Segredos embebidos em imagens criam exposição difícil de revogar. Credenciais long-lived em pipelines são vulneráveis a comprometimento. Workload identity efémera é o padrão moderno.

:::userstory
**História.**   
Como **DevOps**, quero proibir credenciais estáticas em imagens e usar identidades efémeras via OIDC/Workload Identity, para eliminar exposição de segredos de longa duração.

**Critérios de aceitação (BDD).**  
- **Dado** que uma imagem é construída  
  **Quando** o pipeline analisa camadas  
  **Então** falha se encontrar credenciais (AWS keys, GCP tokens, DB passwords, API keys) embebidas
- **Dado** um container em execução  
  **Quando** necessita aceder recursos (AWS, GCP, Kubernetes API)  
  **Então** recebe token efémero via OIDC (TTL ≤ 1h) sem credenciais armazenadas
- **Dado** que a sessão do container termina  
  **Quando** o token expira  
  **Então** o container não pode reutilizar a credencial nem escalar privilégios

**Checklist.**  
- [ ] Secret scanning em camadas (ex: TruffleHog, Gitleaks)
- [ ] Falha automática do build se credencial for detectada
- [ ] OIDC/Workload Identity configurado (ex: GitHub OIDC, Kubernetes SA OIDC)
- [ ] TTL de token configurado para ≤ 1h
- [ ] `imagePullSecrets` auditados (nenhum secret hardcoded)
- [ ] Acesso a resources via role/service account dedicado (não default)
- [ ] Nenhuma credencial em variáveis de ambiente (usar mounted secrets no máximo)
- [ ] Rotação automática de credenciais long-lived se necessário

:::

**🧾 Artefactos & evidências.**  
- Relatórios de secret scanning no pipeline
- Configuração OIDC e Workload Identity
- Políticas IAM/RBAC mostrando acesso restritivo
- Logs de token issuance

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Secret scanning, credenciais não em env vars |
| L2 | Sim | Secret scanning obrigatório, OIDC com TTL curto |
| L3 | Sim | Secret scanning + OIDC + rotação automática + auditoria contínua |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Build/Deploy | Build e deploy | DevOps | Em cada execução |

**Ligações úteis.**  
[Runners e Isolamento](/sbd-toe/sbd-manual/containers-imagens/addon/runners-isolamento)

---

### US-09 – RBAC Mínimo e ServiceAccounts Dedicadas

**Contexto.**  
Workloads com permissões excessivas ou usando default ServiceAccount ampliam impacto de compromisso. RBAC mínimo reduz "blast radius" de falhas de segurança.

:::userstory
**História.**   
Como **DevOps + AppSec**, quero ***enforce* uso de ServiceAccounts dedicadas com RBAC mínimo por workload**, para reduzir impacto de credenciais comprometidas e isolar blast radius.

**Critérios de aceitação (BDD).**  
- **Dado** que um workload é definido  
  **Quando** especifico a ServiceAccount  
  **Então** uma SA dedicada é criada (não default) com permissões mínimas exigidas
- **Dado** um workload em L2/L3  
  **Quando** tenta usar default ServiceAccount  
  **Então** é rejeitado por política de Admission Control
- **Dado** uma SA dedicada  
  **Quando** é configurada  
  **Então** inclui apenas permissões necessárias (ex: read-only a configmaps específicos, sem escalada de privilégios)

**Checklist.**  
- [ ] ServiceAccount dedicada por workload (não reutilizada entre aplicações)
- [ ] Role/RoleBinding com permissões mínimas (principle of least privilege)
- [ ] Default SA proibido em L2/L3 por Admission Control
- [ ] Auditoria de permissões documentada (o que cada workload pode fazer)
- [ ] Nenhuma role com `*` wildcard em L2/L3
- [ ] Revisão periódica de permissões (quadrimestralmente)
- [ ] Métricas de SA usage (quais foram usadas, quais nunca)

:::

**🧾 Artefactos & evidências.**  
- Manifests ServiceAccount/Role/RoleBinding versionados
- Auditoria de permissões por SA
- Política OPA/Kyverno bloqueando default SA
- Dashboard de RBAC coverage

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | SA dedicadas, permissões razoáveis |
| L2 | Sim | SA dedicada obrigatória, RBAC mínimo validado |
| L3 | Sim | SA dedicada + RBAC mínimo + revisão periódica + no wildcard permissions |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy | Definição de workload | Plataforma | Antes do go-live |

**Ligações úteis.**  
[Kubernetes e Execução](/sbd-toe/sbd-manual/containers-imagens/addon/kubernetes-execucao)

---

### US-10 – Segmentação de Rede e NetworkPolicy

**Contexto.**  
Sem segmentação de rede, workloads comprometidos exfiltram dados e propagam ataques lateralmente. NetworkPolicy implementa zero-trust de rede, bloqueando fluxos não-autorizados.

:::userstory
**História.**   
Como **DevOps + Infraestrutura**, quero aplicar NetworkPolicy com ingress/egress explícito em cada namespace, para limitar comunicações ao estritamente necessário e detetar anomalias.

**Critérios de aceitação (BDD).**  
- **Dado** que um workload tenta contactar um serviço não-autorizado **Quando** o fluxo não está em NetworkPolicy **Então** a conexão é bloqueada e registada em logs de auditoria
- **Dado** que um novo namespace é criado **Quando** não existe NetworkPolicy por omissão **Então** deny-all é aplicado automaticamente (L2+)
- **Dado** que tráfego DNS é observado **Quando** nome não é resolvível **Então** a tentativa é bloqueada e alertada em SIEM

**Checklist.**  
- [ ] NetworkPolicy deny-all default por namespace (L2+)
- [ ] Whitelist de ingress por serviço/port (Ex: `from:\n  - podSelector: {app: payment}` port 443)
- [ ] Egress controlado para APIs externas (L3: digest-only registry, NTP, auditoria + SIEM)
- [ ] Exceções documentadas com expiração (Ex: manutenção, vencimento 30d)
- [ ] Validação em admission controller (Gatekeeper/Kyverno)
- [ ] Relatórios de fluxo bloqueado (10x/dia se volumoso → agregado)
- [ ] Teste de falhas: `nsenter` em pod, validar bloqueios

:::

**Artefactos & evidências.**  
- `networkpolicy/*.yaml` (organizados por namespace e tipo: deny-default, ingress, egress)
- Logs de rejeição em SIEM (volume de pacotes bloqueados, top 10 destinos não-autorizados)
- Métricas de Prometheus: `calico_denied_packets`, `cilium_policy_drop`
- Relatório de auditoria trimestral: conectividade vs prescrições
- Exceções documentadas com TTL e revisões

**Proporcionalidade L1–L3.**  
| Nível | Prescrição | Exemplos | SLA Validação |
|-------|-----------|----------|---------------|
| **L1** | Recomendado documentar fluxos | Manual; fluxos observados | Trimestral |
| **L2** | Deny-all default + ingress crítico | Namespace obrigatório; egress para registry+DNS | Mensal; auditoria anual |
| **L3** | Egress total + auditoria contínua | Whitelist per-service; no exceptions sem aprovação GRC | Semanal; alertas <1h |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Design | Levantamento de dependências | Dev Team | Antes de especificar pods |
| Deploy | Aplicação de manifesto | DevOps + Admission Controller | Antes de workload scheduling |
| Ops | Auditoria de fluxos | Plataforma + AppSec | 30d audit log retention |
| GRC | Exceções vs conformidade | GRC | Revisão trimestral |

**Ligações úteis.**  
[Kubernetes e Execução](/sbd-toe/sbd-manual/containers-imagens/addon/kubernetes-execucao)

---

### US-11 – Golden Base Images com Patching Automático

**Contexto.**  
Bases heterogéneas aumentam custo operacional e risco de configuração. SLA de patching assegura que vulnerabilidades não se propagam.

:::userstory
**História.**   
Como **DevOps + AppSec**, quero manter catálogo de Golden Base Images com versionamento semântico e SLA de patching, para padronizar segurança e reduzir configuração drift.

**Critérios de aceitação (BDD).**  
- **Dado** que uma base Ubuntu 22.04 recebe CVE crítico (CVSS≥9) **Quando** o patch está disponível **Então** nova tag é cut (Ex: ubuntu-22.04:v1.2.3→v1.2.4) e propagada em <7d (L3) ou <30d (L2)
- **Dado** que um microsserviço constrói com base descontinuada **Quando** validação do pipeline executa **Então** build falha com mensagem clara do end-of-life
- **Dado** que base node:20 é atualizada **Quando** nova release é publicada **Então** changelog é adicionado a `golden-images-catalog.md` com SBOM diff

**Checklist.**  
- [ ] Catálogo `golden-images-catalog.md` com versionamento semântico (ubuntu-22.04:v1.2.3, alpine:v3.19.1)
- [ ] Assinatura de cada golden image (Cosign + OIDC via Rekor)
- [ ] SLA de patching definido por criticidade (L1: recomendado, L2: 30d, L3: 7–14d)
- [ ] Integração com CVE feed (ex: Trivy API, Red Hat advisories)
- [ ] Deprecation policy com aviso 90d antes de remover tag
- [ ] Registo de cada push com SBOM (CycloneDX JSON no `image:tag@digest.sbom.json`)
- [ ] Dashboard: time-to-patch por criticidade, adoption rate de imagens antigas

:::

**Artefactos & evidências.**  
- `golden-images-catalog.md` (tabela: base, latest tag, release date, EOL date, SBOM, assinatura status)
- Changelog de segurança (Ex: "ubuntu-22.04:v1.2.4 – patch CVE-2024-12345 expat")
- SBOM de cada golden image (formato CycloneDX, armazenado em registry via tag `.sbom.json` ou atributo custom)
- Logs de patching: data/hora, criticidade, autor, link para upstream advisory
- Métricas de adoção (% aplicações usando latest, % usando deprecated)

**Proporcionalidade L1–L3.**  
| Nível | Prescrição | SLA Patch | Assinatura | Deprecation | Auditoria |
|-------|-----------|----------|-----------|------------|-----------|
| **L1** | Recomendado; catálogo informal | Ad-hoc | Não | Manual | Anual |
| **L2** | Obrigatório para prod; catálogo publicado | 30d crítico | Cosign recomendado | 90d aviso | Semestral |
| **L3** | Obrigatório; SLA rigoroso | 7–14d crítico | Cosign + OIDC obrigatório | 90d aviso + validação | Mensal |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Catalogação | Submissão de base | AppSec | Revisão em 5d |
| Patching | CVE publicado | DevOps (automático se via Dependabot) | Per SLA |
| Validação | Nova tag | Pipeline CI/CD | <2h para aprovação |
| Sunsetting | EOL atingido | Plataforma + GRC | Notificação 90d antes |

**Ligações úteis.**  
[Imagens Base Seguras](/sbd-toe/sbd-manual/containers-imagens/addon/imagens-base)

---

### US-12 – Builders e Runners Ephemerais, Assinados e com Auditoria

**Contexto.**  
Builders comprometidos comprometem todas as releases. Runners partilhados ou persistentes são pontos críticos de ataque na supply chain. Rastreabilidade é essencial para investigação pós-incidente.

:::userstory
**História.**   
Como **DevOps/AppSec**, quero que builders e runners sejam mínimos, ephemerais (destruídos após cada execução), assinados e auditados, para proteger o pipeline CI/CD e garantir rastreabilidade criptográfica de todas as execuções.

**Critérios de aceitação (BDD).**  
- **Dado** que o pipeline arranca **Quando** um runner executa jobs **Então** usa builder assinado (Cosign), mínimo, é destruído após conclusão e todas as operações são registadas com timestamp/actor
- **Dado** um runner em execução **Quando** tenta aceder a `/var/run/docker.sock`, privilégios elevados (CAP_SYS_ADMIN) ou rede não-autorizada **Então** é bloqueado pela configuração de segurança + gerado alerta
- **Dado** uma ferramenta necessária no runner **Quando** tenta ser instalada dinamicamente **Então** verifica contra allowlist antes de instalar e regista (sha256, source, timestamp)
- **Dado** um builder destroy event **Quando** ocorre **Então** regista: pod ID, exit status, duração, logs consolidados com hash de conteúdo

**Checklist.**  
- [ ] Runner ephemeral: criado por job, destruído obrigatoriamente após conclusão (max 24h TTL mesmo se bug)
- [ ] Runner com utilizador não-root (Ex: `runAsUser: 1000`, `runAsNonRoot: true`)
- [ ] Builder image assinada com Cosign + OIDC, versionada e imutável (digest-only)
- [ ] Builder image minimizada (ex: 50MB vs 500MB stock) com Dockerfile linting (Hadolint)
- [ ] Allowlist de ferramentas aprovadas (ex: `curl`, `git`, `gcc` apenas se necessário), bloqueio de shells interativas
- [ ] Nenhum acesso a Docker socket (`/var/run/docker.sock` blocked), nenhum `privileged: true`, nenhum `hostPath` mount
- [ ] Logs de builder assinados (gravidade ≥DEBUG, consolidados em journald ou stdout com JSON structuring)
- [ ] Cache de builder controlado e isolado por job (ex: cache key = `${CI_COMMIT_SHA}`, expiração 7d)
- [ ] Métricas: duração média, taxa de falha por tipo, volume de logs (alertar se >1GB)

:::

**Artefactos & evidências.**  
- Configuração de runners (YAML/HCL versionado em Git, signed tag para cada release)
- Manifest de builder image com assinatura Cosign (Ex: `builder:v2.1.0@sha256:abc123...`)
- Logs de criação e destruição de runners (retention 1+ anos, indexados em ELK/Splunk)
- Allowlist de ferramentas publicada (`tools-allowlist.yaml` com versionamento semântico)
- SBOM de builder image (CycloneDX JSON com dependências de build)
- Dashboard: tempo de build, falhas, logs volume, cache hit rate
- Auditoria trimestral: compliance vs política, incidentes de builders, recomendações de hardening

**Proporcionalidade L1–L3.**  
| Nível | Runners | Builder | Assinatura | Auditoria | Suporte Multiplataforma |
|-------|---------|---------|-----------|-----------|----------------------|
| **L1** | Recomendado ephemeral | Imagem pública | Não | Logs básicos | Não |
| **L2** | Obrigatório ephemeral, non-root | Imagem minimizada, versionada | Cosign recomendado | Logs centralizados, auditoria semestral | Sim (Intel + ARM) |
| **L3** | Obrigatório ephemeral, max 24h TTL, segmentado por team | Imagem minimizada + allowlist rigorosa | Cosign + OIDC obrigatório | Logs estruturados JSON, auditoria mensal + alertas <1h | Sim (Intel, ARM, IBM Z) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Definição | Criação de pipeline | Dev Team | Antes do go-live |
| Implementação | Configuração de runners | DevOps | Validação por AppSec |
| Execução | Cada job do pipeline | Runner (automático) | <2h para destruction cleanup |
| Auditoria | Revisão periódica | Plataforma + GRC | Trimestral; alertas imediatos para violações |

**Ligações úteis.**  
[Runners e Isolamento](/sbd-toe/sbd-manual/containers-imagens/addon/runners-isolamento)

---

### US-13 – Enforcement Centralizado e Auditável de Políticas no Runtime

**Contexto.**  
Para garantir que políticas são aplicadas de forma sistemática e que violações são rastreadas, é necessário enforcement formal com logs centralizados e revisão periódica.

:::userstory
**História.**  
Como **DevOps/AppSec**, quero que o enforcement de políticas de segurança seja **central, auditável e periódico**, para garantir que nenhuma execução escapa aos controlos e que todas as tentativas violadas são registadas e revisadas.

**Critérios de aceitação (BDD).**  
- **Dado** que políticas de runtime estão ativas  
  **Quando** um workload é criado  
  **Então** a política é avaliada, o resultado é registado em log centralizado e não pode ser ignorado
- **Dado** uma violação de política  
  **Quando** ocorre  
  **Então** é bloqueada, auditada com timestamp/actor/pod details e gera alerta
- **Dado** uma revisão periódica (ex: mensal)  
  **Quando** é executada  
  **Então** produz relatório de tentativas bloqueadas, taxa de conformidade e recomendações de ajuste

**Checklist.**  
- [ ] Logs centralizados de Admission Controller (ex: Prometheus, ELK, Datadog)
- [ ] Alertas automáticos para violações críticas
- [ ] Relatório mensal/trimestral de enforcement com métricas
- [ ] Rastreabilidade completa: pod, namespace, imagem, timestamp, actor
- [ ] Integração com SIEM ou plataforma de auditoria
- [ ] Políticas versionadas em Git, revisão por PR antes de aplicação
- [ ] Dashboard de conformidade público/acessível a auditores

:::

**🧾 Artefactos & evidências.**  
- Dashboard de Prometheus/Grafana com métricas de enforcement
- Logs estruturados de rejeições (JSON)
- Relatório mensal de conformidade
- Alertas configurados no sistema de notificações

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Logging básico, sem alertas automáticos |
| L2 | Sim | Logging + alertas para críticos |
| L3 | Sim | Logging + alertas + dashboard + revisão mensal |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy/Produção | Criação de workload | DevOps/AppSec + GRC | Contínuo |

**Ligações úteis.**  
[Policies de Runtime OPA](/sbd-toe/sbd-manual/containers-imagens/addon/policies-runtime-opa), [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)


---

### US-14 – Sandboxing Avançado com gVisor/Kata para Workloads Críticas

**Contexto.**  
Aplicações que processam dados críticos (pagamentos, dados pessoais) exigem isolamento reforçado para proteção contra escalada de privilégios ou acesso ao host.

:::userstory
**História.**  
Como **Infraestrutura + AppSec**, quero configurar sandboxes avançados (gVisor, Kata Containers, Firecracker) via RuntimeClass em workloads sensíveis, para garantir isolamento reforçado de syscalls e proteção contra escalada de privilégios.

**Critérios de aceitação (BDD).**  
- **Dado** que um pod sensível é criado (ex: com label `sandbox=required`)  
  **Quando** é agendado no cluster  
  **Então** usa RuntimeClass com sandbox avançado (`gvisor` ou `kata`)
- **Dado** um workload em sandbox  
  **Quando** tenta fazer syscall perigosa (ex: `ptrace`, `mount`)  
  **Então** é bloqueada pelo sandbox, não pelo host
- **Dado** um ataque de escape de container  
  **Quando** é tentado  
  **Então** o isolamento de sandbox rejeita, mesmo que securityContext deixe passar

**Checklist.**  
- [ ] RuntimeClass gVisor/Kata instalado no cluster
- [ ] Pods sensíveis label com `sandbox=required`
- [ ] CPU/memória extra alocada para overhead de sandbox
- [ ] Auditoria de pods que usam sandbox
- [ ] Performance testada e aprovada (overhead aceitável)
- [ ] Documentação de workloads que requerem sandbox (ex: processamento de pagamentos)

:::

**🧾 Artefactos & evidências.**  
- Manifests com `runtimeClassName: gvisor` ou `kata`
- Logs de sandbox de syscalls bloqueadas
- Testes de performance e escape
- Relatório de workloads em sandbox

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Não | Opcional, investigativo |
| L2 | Recomendado | Para workloads sensíveis |
| L3 | Obrigatório | Para workloads críticas (pagamentos, dados sensíveis, PII) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy | Criação de pod sensível | Infraestrutura + AppSec | Antes do deploy em produção |

**Ligações úteis.**  
[Kubernetes e Execução](/sbd-toe/sbd-manual/containers-imagens/addon/kubernetes-execucao)


## 📦 Artefactos esperados

Cada prática deixa uma pegada verificável - os artefactos.  
Sem eles, não há como provar conformidade nem realizar auditorias eficazes.  
A tabela seguinte consolida os principais outputs que devem estar presentes em qualquer projeto containerizado.

| Artefacto | Responsável | Evidência |
|-----------|-------------|-----------|
| `Dockerfile` com digest fixo | Dev Team | Repo Git |
| Relatórios de scanner SCA | DevOps | Pipeline logs |
| Proveniência + assinatura Cosign | AppSec | Metadata em registry, entrada Rekor |
| Policies OPA/Kyverno versionadas | DevOps | Repositório Git, manifests validados |
| Logs de Admission Controller | GRC | Relatórios de rejeições e aceitações |
| **SBOM da imagem (CycloneDX/SPDX)** | DevOps | Ficheiro anexo ao artefacto |
| **registry-allowlist.yaml** | DevOps | Policy de admissão aplicada |
| **Relatórios de secret scan** | DevOps | CI logs + bloqueios de secrets |
| **RBAC/SA manifests** | Plataforma | Auditoria de permissões |
| **networkpolicy/*.yaml** | Plataforma | Auditoria de fluxos intra-cluster |
| **golden-images-catalog.md** | Plataforma/AppSec | SLA de patching + changelog |
| **Config de runners/builders** | DevOps | Assinatura + ephemeral logs |
| **Dashboard de enforcement** | DevOps/AppSec | Prometheus/Grafana com métricas |
| **Relatório mensal de conformidade** | GRC | Tentativas bloqueadas, taxa de conformidade |
| **Manifests RuntimeClass (gVisor/Kata)** | Plataforma | Pod specs com sandbox configurado |
| **Auditoria de workloads sensíveis** | Plataforma/GRC | Relatório de pods em sandbox |

---

## ⚖️ Matriz de proporcionalidade L1–L3

A proporcionalidade garante que os controlos não são uniformes, mas sim ajustados ao risco real de cada aplicação.  
Uma aplicação L1 não exige o mesmo investimento que uma aplicação crítica (L3).  
A tabela seguinte mostra como escalar cada prática.

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Imagens base confiáveis | Sim | Sim | Sim |
| Pinagem por digest | Recomendado | Obrigatório | Obrigatório |
| Scanning de imagens | Aviso | Bloqueio High/Critical | Bloqueio Medium+ |
| Assinatura & proveniência | Opcional | Recomendado | Obrigatório |
| Políticas de runtime | Básico (non-root) | Restritivas | Completo + auditoria |
| Monitorização runtime | Básico | Crítico | Total + resposta automática |
| **SBOM por imagem** | Recomendado | Obrigatório | Obrigatório (+ com proveniência) |
| **Allowlist de registries/digest-only** | Aviso | Bloqueio por origem | Bloqueio + digest-only |
| **Segredos fora da imagem / OIDC** | Recomendado | Obrigatório | Obrigatório + rotação automática |
| **RBAC mínimo / SA dedicada** | Recomendado | Obrigatório | Obrigatório + revisão periódica |
| **NetworkPolicy (ingress/egress)** | Básico | Ingress+egress crítico | Ingress+egress total + auditoria |
| **Golden base + SLA patch** | Recomendado | Obrigatório | Obrigatório + rollout acelerado |
| **Builders/runners ephemerais/assinados** | Recomendado | Obrigatório | Obrigatório + segmentação rede |
| **Enforcement centralizado com auditoria** | Recomendado | Sim (logging + alertas) | Sim (logging + alertas + dashboard + revisão) |
| **Sandboxing avançado (gVisor/Kata)** | Opcional | Recomendado (workloads sensíveis) | Obrigatório (workloads críticas) |

---

## 🏁 Recomendações finais

A segurança de containers deve ser entendida como um **ciclo contínuo** e não como uma lista de verificações isoladas.  
Mais importante do que aplicar controlos dispersos é garantir que estão integrados entre si, desde a seleção da imagem base até à resposta a incidentes em produção.

- **Containers são artefactos de software críticos**: devem ser tratados com SBOM, proveniência, políticas de execução e auditoria como qualquer código de negócio.
- **Shift-left é imperativo**: integração de scanners, linters e policies em CI/CD reduz risco e custo exponencialmente.
- **Assinatura e proveniência (SLSA, Sigstore)** são práticas em rápida adoção - devem ser incluídas já em novos projetos, especialmente em L2/L3.
- **Enforcement formal com auditoria** garante que nenhuma execução escapa aos controlos; métricas centralizadas permitem revisão periódica e compliance reporting.
- **Isolamento reforçado** (sandboxes gVisor/Kata) é obrigatório em L3 para workloads críticas (pagamentos, PII) - a complexidade é justificada pelo risco.
- **Prevenção + deteção coexistem**: políticas restrictivas no cluster são essenciais, mas monitorização em runtime é igualmente crítica para resposta rápida.
- **Governação deve incluir métricas claras**: % imagens assinadas, % pipelines com scanners ativos, % incidentes detetados/resolvidos, taxa de conformidade com policies.
- **Golden base images + allowlist + builders ephemerais e assinados** são o tripé de segurança - padronização reduz risco de supply chain.

Em síntese: **containers são facilitadores de agilidade e portabilidade, mas apenas quando tratados com a mesma disciplina científica aplicada a qualquer outro artefacto crítico de software**. Segurança de containers não é apenas responsabilidade de DevOps: é uma preocupação transversal de Dev Team, AppSec, Plataforma e GRC.
---
