---
id: isolamento-runners
title: Isolamento e Proteção de Runners
sidebar_position: 4
description: Medidas para segregar runners por aplicação, evitar persistência e garantir ambientes de execução efémeros e controlados.
tags: [cicd, runners, isolamento, segurança, execução, infraestrutura]
---

# 🖥️ Isolamento e proteção de runners {cicd-seguro:addon:isolamento-runners}

Os runners (ou agentes de execução) são os ambientes onde os pipelines CI/CD são realmente processados. Se um runner for comprometido, toda a cadeia de build e entrega pode ser manipulada — desde a introdução de backdoors, à exfiltração de segredos ou sabotagem de artefactos.

> A segurança dos runners define os limites de confiança da execução automatizada.

---

## 🎯 Objetivos {cicd-seguro:addon:isolamento-runners#objetivos}

- Garantir que os pipelines são executados em ambientes **seguros, controlados e efémeros**;
- Impedir que código malicioso comprometa o runner ou escape do contexto do pipeline;
- Reduzir a superfície de ataque associada a runners partilhados, persistentes ou mal configurados.

---

## 🛠️ Práticas {cicd-seguro:addon:isolamento-runners#praticas}

1. **Execução em runners efémeros ou reimagináveis**  
   - Cada job deve correr num ambiente isolado (ex: VM, container);
   - Os runners devem ser destruídos, restaurados ou validados após cada execução.

2. **Segregação por nível de risco e por projeto**  
   - Aplicações L2 e L3 não devem partilhar runners com projetos externos ou menos críticos;
   - Runners para produção devem ser dedicados e isolados dos ambientes de desenvolvimento.

3. **Hardening dos ambientes de execução**  
   - Os runners devem ser minimalistas, atualizados e com a menor superfície de ataque possível;
   - O sistema base deve ter controlo rigoroso sobre binários, permissões e serviços ativos.

4. **Verificação de integridade dos agentes e imagens base**  
   - As imagens devem ser assinadas e de origem validada;
   - Os binários e scripts utilizados devem ser verificados por hash ou assinatura digital.

5. **Proibição de execução privilegiada**  
   - Jobs de pipeline não devem correr como `root` nem com permissões elevadas;
   - Deve ser bloqueada a execução de comandos como `sudo`, `setcap`, ou acesso direto a `docker`.

---

## ⚖️ Aplicação proporcional por nível de risco {cicd-seguro:addon:isolamento-runners#aplicacao_proporcional_por_nivel_de_risco}

| Nível | Requisitos obrigatórios                                   | Requisitos reforçados                                       |
|-------|------------------------------------------------------------|--------------------------------------------------------------|
| **L1** | Runners atualizados; isolamento básico por job             | —                                                            |
| **L2** | Runners dedicados por projeto; imagem hardened             | Verificação periódica de integridade                         |
| **L3** | Runners efémeros, segregados por criticidade; imagens assinadas | Hardening formal; sem root; auditoria contínua         |

---

## 📌 Exemplos práticos {cicd-seguro:addon:isolamento-runners#exemplos_praticos}

- **GitHub Actions**  
  - Uso de `self-hosted runners` dedicados por projeto ou aplicação crítica;  
  - Validação de imagens com `act`, `cosign` ou `sigstore`.

- **GitLab Runners**  
  - `autoscaling runners` (em Kubernetes, EC2 spot) para isolamento por job;  
  - Execução via `docker+machine` ou `k8s` com destruição automática.

- **Azure DevOps**  
  - Pools dedicados por projeto; uso de imagens minimalistas com hardening pré-aplicado;  
  - Bloqueio de acesso a recursos locais e desativação de privilégios elevados.

- **Jenkins**  
  - Agentes controlados por labels e restrição de nós (isolamento lógico);  
  - Pipelines com `agent { docker { image: "signed" } }` e hardening prévio.

---

## 📉 Riscos mitigados {cicd-seguro:addon:isolamento-runners#riscos_mitigados}

- Persistência de malware entre execuções (OSC&R: CI0009);
- Exfiltração de segredos via runners contaminados (OSC&R: CI0003, CI0016);
- Escalada de privilégios via permissões excessivas (OSC&R: SC0006);
- Compromisso da build por manipulação do ambiente (OSC&R: CI0005).

---

## 🧭 Referências {cicd-seguro:addon:isolamento-runners#referencias}

- [SLSA – Build Isolation Requirements](https://slsa.dev/spec/v1.0/)
- [OWASP CI/CD Security – 4. Execution Environment](https://owasp.org/www-project-cicd-security/#4-execution-environment)
- [NIST SSDF – PW.5: Harden Execution Environment](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [BSIMM – SE2.2, SE2.4]
- [SAMM – Secure Build – Environment Hardening, Deployment Isolation]
