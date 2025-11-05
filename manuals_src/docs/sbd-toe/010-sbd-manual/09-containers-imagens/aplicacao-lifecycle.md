---
id: aplicacao-lifecycle
title: Como Fazer
description: Como aplicar as práticas prescritas de segurança em containers ao longo do ciclo de vida de desenvolvimento e operação
tags: [containers, imagens, segurança, isolamento, ciclo-de-vida, sbom, supply-chain]
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
| **DevOps / Plataforma** | Manter repositórios de imagens confiáveis, configurar pipelines, enforcing Admission Control |
| **AppSec** | Definir políticas, rever alertas críticos, validar conformidade com baseline de segurança |
| **GRC / Auditoria** | Validar registos de conformidade, exceções e governação sobre imagens e runtime |

---

## 📖 User Stories Reutilizáveis

### US-01 – Construção de imagens seguras
**Contexto.**  
A base de uma imagem insegura compromete todo o ciclo de vida.

**📖 Rationale científico.**  
Frameworks como **SSDF PW.4/PS.3/RV.3**, **SAMM (Construction & Verification)** e **BSIMM CMVM1.1/SE2.5** prescrevem a seleção de bases confiáveis. O **SLSA** coloca a proveniência como fator de confiança obrigatório.  
Mitiga ameaças como **CWE-829 (Inclusão de componentes não confiáveis)** e **OSC&R: Compromise Base Image**.  
Estudos da **Sonatype** e da **Sysdig** mostram que o uso de *pinning* por digest e imagens oficiais reduz drasticamente a taxa de CVEs críticos em produção.  

:::userstory
**História.**   
Como **Dev Team**, quero construir imagens a partir de bases confiáveis e **pinned**, para reduzir risco de vulnerabilidades e supply chain.  

**Critérios de aceitação (BDD).**  
- Dado que inicio a construção da imagem  
- Quando seleciono a base  
- Então a imagem deve vir de um repositório oficial confiável e com digest fixo  

**Checklist.**  
- [ ] Imagem base de repositório confiável  
- [ ] Versão pinada por digest SHA256  
- [ ] Sem pacotes desnecessários instalados  

:::

**Artefactos & evidências.**  
- `Dockerfile` com digest fixo  
- Relatório de scanner  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Imagens oficiais | Digest fixo + scanner High/Critical | Digest fixo + scanner Medium+ + SBOM |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Desenvolvimento | Construção inicial da imagem | Dev Team | Imediato |

**Ligações úteis.**  
xref:sbd-toe:cap07:intro  

---

### US-02 – Scanning automático em CI/CD
**Contexto.**  
Identificar vulnerabilidades cedo reduz risco em produção.  

**📖 Rationale científico.**  
**SSDF RV.2/RV.3**, **SAMM Verification** e **BSIMM SE2.5** reforçam a necessidade de scanners integrados no pipeline.  
Mitiga riscos como **CWE-1104** e **OSC&R: Image Vulnerabilities**.  
Relatórios da **ENISA** mostram que pipelines com *gating* reduzem até 70% de vulnerabilidades em produção.  

:::userstory
**História.**   
Como **DevOps**, quero integrar scanners de imagens em pipelines CI/CD, para bloquear builds com vulnerabilidades críticas.  

**Critérios de aceitação (BDD).**  
- Dado que executo o pipeline  
- Quando a imagem é construída  
- Então o scanner deve bloquear vulnerabilidades acima do threshold definido  

**Checklist.**  
- [ ] Scanner configurado no pipeline  
- [ ] Threshold definido (High/Critical em L2/L3)  
- [ ] Pipeline falha se vulnerabilidade acima do threshold  

:::

**Artefactos & evidências.**  
- Logs do scanner  
- Relatório anexado ao PR  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Aviso | Bloqueio High/Critical | Bloqueio Medium+ |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Build da imagem | DevOps | Automático |

**Ligações úteis.**  
xref:sbd-toe:cap05:intro  

---

### US-03 – Assinatura e proveniência de imagens
**Contexto.**  
Sem proveniência confiável, imagens podem ser alteradas maliciosamente.  

**📖 Rationale científico.**  
O **SLSA v1.0** exige proveniência auditável. O **SSDF RV.3** e o **BSIMM CMVM/CP1.2** reforçam atestados de integridade.  
Mitiga **CWE-353/494**, **OSC&R: Artifact Tampering**.  
Exemplos como SolarWinds mostram impacto devastador de ausência de assinatura.  

:::userstory
**História.**   
Como **AppSec**, quero que todas as imagens sejam assinadas e tenham proveniência verificável, para garantir integridade no deploy.  

**Critérios de aceitação (BDD).**  
- Dado que a imagem foi construída  
- Quando é publicada no registry  
- Então deve ser assinada e validada antes do deploy  

**Checklist.**  
- [ ] Imagem assinada com chave confiável  
- [ ] Proveniência atestada (SLSA L3+)  
- [ ] Admission Control rejeita imagens não assinadas  

:::

**Artefactos & evidências.**  
- Metadata de assinatura (`cosign verify`)  
- Proveniência (`in-toto`)  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Pré-produção | Publicação em registry | AppSec + DevOps | Antes do deploy |

**Ligações úteis.**  
xref:sbd-toe:cap07:intro  

---

### US-04 – Políticas de execução em runtime
**Contexto.**  
Um container sem restrições expande a superfície de ataque.  

**📖 Rationale científico.**  
Referências: **NIST SP 800-190**, **Kubernetes Pod Security Standards**.  
Mitiga **CWE-250**, **OSC&R: Privileged Container**.  
Relatórios **Sysdig** provam eficácia de `runAsNonRoot` e *capabilities drop*.  

:::userstory
**História.**   
Como **DevOps**, quero aplicar políticas de runtime (OPA/Kyverno), para garantir que containers correm com mínimos privilégios.  

**Critérios de aceitação (BDD).**  
- Dado que um container é criado  
- Quando a política de admissão é aplicada  
- Então apenas containers conformes são aceites  

**Checklist.**  
- [ ] `runAsNonRoot` aplicado  
- [ ] Capabilities reduzidas  
- [ ] `readOnlyRootFilesystem` configurado  
- [ ] Policies enforcement no cluster  

:::

**Artefactos & evidências.**  
- Manifestos validados  
- Logs Admission Controller  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Non-root básico | Capabilities reduzidas | Policies completas + auditoria |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Produção | Criação de pod | DevOps | Imediato |

**Ligações úteis.**  
xref:sbd-toe:cap12:intro  

---

### US-05 – Monitorização e resposta a incidentes
**Contexto.**  
Ataques de runtime só são detetados com monitorização ativa.  

**📖 Rationale científico.**  
Referências: **NIST SP 800-137**, **SSDF RV.1**, **DSOMM Ops**.  
Mitiga **CWE-778 (Insufficient Logging)**, **OSC&R: Runtime Threats**.  
Relatórios mostram que ferramentas como **Falco** reduzem *MTTD/MTTR* drasticamente.  

:::userstory
**História.**   
Como **SecOps**, quero monitorizar containers em execução e gerar alertas, para permitir resposta rápida a incidentes.  

**Critérios de aceitação (BDD).**  
- Dado que um container está em execução  
- Quando ocorre comportamento suspeito  
- Então o evento deve ser registado e gerado alerta  

**Checklist.**  
- [ ] Monitorização runtime ativa  
- [ ] Alertas configurados  
- [ ] Processo de resposta documentado  

:::

**Artefactos & evidências.**  
- Logs runtime security  
- Relatório de incidentes  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Alertas críticos configurados | Cobertura total + resposta auto |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Produção | Execução de containers | SecOps + GRC | Imediato |

**Ligações úteis.**  
xref:sbd-toe:cap12:intro  

---

### US-06 – SBOM de imagens
**Contexto.**  
Sem SBOM, não há visibilidade rápida sobre CVEs presentes.  

**📖 Rationale científico.**  
**SSDF PW.4/RV.3**, **SLSA Provenance**, **BSIMM CMVM**.  
Mitiga **CWE-1104**, **OSC&R: Inaccurate Inventory**.  
Estudos **DBIR** e **Sonatype** provam aceleração de resposta a CVEs com SBOM CycloneDX/SPDX.  

:::userstory
**História.**   
Como **DevOps**, quero gerar SBOM a cada imagem construída, para permitir rastreabilidade de componentes.  

**Critérios de aceitação (BDD).**  
- Dado que uma imagem é construída  
- Quando o pipeline conclui  
- Então gera SBOM e armazena-o com a imagem  

**Checklist.**  
- [ ] SBOM gerado (Syft, etc.)  
- [ ] SBOM anexado ao artefacto  
- [ ] Consulta disponível para auditoria  

:::

**Artefactos & evidências.**  
- `sbom.json`  
- Labels no registry  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| SBOM básico | Completo + retenção | Completo + integração SLSA |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Build de imagem | DevOps | Em cada build |

**Ligações úteis.**  
xref:sbd-toe:cap05:intro  

---

### US-07 – Governação de registries
**Contexto.**  
Pulls de registries não confiáveis expõem a supply chain.  

**📖 Rationale científico.**  
**SSDF RV.3/GV.2**, **SLSA Provenance**, **BSIMM CMVM**.  
Mitiga **CWE-494/353**, **OSC&R: Registry Poisoning**.  
Estudos **OpenSSF** mostram que allowlists reduzem significativamente risco de typosquatting.  

:::userstory
**História.**   
Como **DevOps**, quero impor allowlist de registries e digest-only, para impedir uso de fontes não confiáveis.  

**Critérios de aceitação (BDD).**  
- Dado que um workload referencia imagem  
- Quando a política verifica a origem  
- Então apenas imagens aprovadas por digest são aceites  

**Checklist.**  
- [ ] Lista de registries aprovados  
- [ ] Digest-only obrigatório  
- [ ] Bloqueio de tags mutáveis  

:::

**Artefactos & evidências.**  
- `registry-allowlist.yaml`  
- Logs Admission Controller  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Aviso | Bloqueio origem | Bloqueio origem + digest-only |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy | Definição de workload | DevOps | Antes do go-live |

---

### US-08 – Segredos fora da imagem
**Contexto.**  
Segredos embebidos em imagens criam exposição difícil de revogar.  

**📖 Rationale científico.**  
**SSDF PW.6/PS.3**, **BSIMM SE2.x**.  
Mitiga **CWE-798**, **OSC&R: Secret Exposure**.  
Relatórios pós-incidente mostram que OIDC/TTL curto reduz impacto de *secret sprawl*.  

:::userstory
**História.**   
Como **DevOps**, quero proibir segredos na imagem e usar pull-secrets dinâmicos, para reduzir exposição.  

**Critérios de aceitação (BDD).**  
- Dado que uma imagem é construída  
- Quando o pipeline analisa camadas  
- Então falha se encontrar credenciais embebidas  

**Checklist.**  
- [ ] Secret scanning em camadas  
- [ ] OIDC/Workload Identity com TTL curto  
- [ ] `imagePullSecrets` auditados  

:::

**Artefactos & evidências.**  
- Relatórios de secret scan  
- Políticas de rotação  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + rotação automática |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Build/Deploy | Build/Deploy | DevOps | Em cada execução |

---

### US-09 – RBAC mínimo e ServiceAccounts
**Contexto.**  
Workloads com permissões excessivas ampliam impacto de compromisso.  

**📖 Rationale científico.**  
**NIST SP 800-190**, **SSDF PS.2**, **OWASP K8s Top Ten**.  
Mitiga **CWE-269/284**, **OSC&R: Abuse of Default SA**.  
Relatórios **Sysdig** mostram que abuso de SA por omissão é frequente.  

:::userstory
**História.**   
Como **Plataforma**, quero ServiceAccount dedicada com RBAC mínimo, para reduzir impacto de credenciais comprometidas.  

**Critérios de aceitação (BDD).**  
- Dado que um workload é definido  
- Quando atribuo SA dedicada  
- Então apenas permissões necessárias são concedidas  

**Checklist.**  
- [ ] SA dedicada por workload  
- [ ] RBAC mínimo aplicado  
- [ ] Default SA proibido em L2/L3  

:::

**Artefactos & evidências.**  
- Manifests RBAC/SA  
- Auditoria de permissões  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + revisão periódica |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy | Definição de workload | Plataforma | Antes do go-live |

---

### US-10 – NetworkPolicy
**Contexto.**  
Sem segmentação de rede, workloads comprometidos exfiltram dados.  

**📖 Rationale científico.**  
**NIST SP 800-190**, **CIS K8s Benchmark**.  
Mitiga **OSC&R: Lateral Movement**, **CAPEC-601**.  
Estudos mostram que NetworkPolicies reduzem o *blast radius*.  

:::userstory
**História.**   
Como **Plataforma**, quero aplicar NetworkPolicy com egress controlado, para limitar comunicações ao estritamente necessário.  

**Critérios de aceitação (BDD).**  
- Dado que o namespace é criado  
- Quando aplico NetworkPolicies  
- Então apenas destinos permitidos são alcançados  

**Checklist.**  
- [ ] NetworkPolicy por namespace  
- [ ] Lista de dependências explícitas  
- [ ] Auditoria de fluxos  

:::

**Artefactos & evidências.**  
- `networkpolicy/*.yaml`  
- Relatórios de fluxo  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Ingress básico | Ingress + egress crítico | Ingress + egress total + auditoria |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Design/Deploy | Criação de namespaces | Plataforma | Antes da abertura de tráfego |

---

### US-11 – Golden Base Images
**Contexto.**  
Bases heterogéneas aumentam custo e risco.  

**📖 Rationale científico.**  
**SSDF RV.3/PS.3**, **BSIMM CMVM**, **SLSA Baselines**.  
Mitiga **CWE-1104**, **OSC&R: Outdated Base Images**.  
Estudos mostram que imagens curadas + SLA (7/30 dias) reduzem MTTR.  

:::userstory
**História.**   
Como **Plataforma/AppSec**, quero manter catálogo de Golden Base Images com SLA de patching, para padronizar segurança.  

**Critérios de aceitação (BDD).**  
- Dado que uma base recebe CVE crítico  
- Quando o SLA é atingido  
- Então a base é atualizada ou descontinuada  

**Checklist.**  
- [ ] Catálogo publicado  
- [ ] SLA definido (30d L2, 7–15d L3)  
- [ ] Processo de depreciação  

:::

**Artefactos & evidências.**  
- `golden-images-catalog.md`  
- Changelog de segurança  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + rollout acelerado |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Operação | CVE / revisão | Plataforma + AppSec | 7–30 dias |

---

### US-12 – Governação de builders e runners
**Contexto.**  
Builders comprometidos comprometem todas as releases.  

**📖 Rationale científico.**  
**SLSA Build L2–L3**, **SSDF PW.7/RV.3**, **BSIMM CMVM1.3**.  
Mitiga **OSC&R: Poisoned Pipeline Execution**.  
Estudos mostram que runners ephemerais e assinados reduzem persistência e adulteração.  

:::userstory
**História.**   
Como **DevOps**, quero que builders e runners sejam mínimos, ephemerais e assinados, para proteger o pipeline.  

**Critérios de aceitação (BDD).**  
- Dado que o pipeline arranca  
- Quando um runner executa jobs  
- Então usa builder assinado, mínimo e é destruído no fim  

**Checklist.**  
- [ ] Runner ephemeral e não privilegiado  
- [ ] Builder assinado e mínimo  
- [ ] Allowlist de ferramentas  

:::

**Artefactos & evidências.**  
- Configuração de runners  
- Logs de assinatura  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + segmentação rede |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Execução de pipeline | DevOps | Em cada pipeline |

---

## 📦 Artefactos esperados

Cada prática deixa uma pegada verificável - os artefactos.  
Sem eles, não há como provar conformidade nem realizar auditorias eficazes.  
A tabela seguinte consolida os principais outputs que devem estar presentes em qualquer projeto containerizado.

| Artefacto | Responsável | Evidência |
|-----------|-------------|-----------|
| `Dockerfile` com digest fixo | Dev Team | Repo Git |
| Relatórios de scanner | DevOps | Pipeline logs |
| Proveniência + assinatura | AppSec | Metadata em registry |
| Policies de runtime | DevOps | Manifestos validados |
| Logs de runtime security | GRC | Relatórios de incidentes |
| **SBOM da imagem** | DevOps | Ficheiro CycloneDX/SPDX anexo/associado |
| **registry-allowlist.yaml** | DevOps | Policy de admissão aplicada |
| **Relatórios de secret scan** | DevOps | CI logs + bloqueios |
| **RBAC/SA manifests** | Plataforma | Auditoria de permissões |
| **networkpolicy/*.yaml** | Plataforma | Auditoria de fluxos |
| **golden-images-catalog.md** | Plataforma/AppSec | SLA de patching + changelog |
| **Config de runners/builders** | DevOps | Assinatura + ephemeral logs |

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

---

## 🏁 Recomendações finais

A segurança de containers deve ser entendida como um **ciclo contínuo** e não como uma lista de verificações isoladas.  
Mais importante do que aplicar controlos dispersos é garantir que estão integrados entre si, desde a seleção da imagem base até à resposta a incidentes em produção.

- Containers devem ser tratados como **artefactos de software completos**, com SBOM, proveniência e políticas de execução.  
- A integração de scanners e linters em CI/CD é **não-negociável** em ambientes modernos.  
- A assinatura e proveniência (SLSA, Sigstore) são práticas em rápida adoção - devem ser incluídas já em novos projetos.  
- Monitorização de runtime não substitui políticas preventivas: **prevenção + deteção** devem coexistir.  
- A governação deve incluir métricas claras: % imagens assinadas, % pipelines com scanners ativos, % incidentes detetados/resolvidos.  
- **Padroniza a segurança** com *golden base images* e **allowlist**; reforça pipeline com **builders ephemerais** e assinados.  

Em síntese: containers só são um facilitador de agilidade e portabilidade **se forem tratados com a mesma disciplina científica aplicada a qualquer outro artefacto crítico de software**.