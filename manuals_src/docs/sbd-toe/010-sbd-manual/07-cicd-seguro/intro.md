---
id: intro
title: CI/CD Seguro
description: Práticas de segurança para pipelines de integração e entrega contínua, com foco em automação, rastreabilidade e controlo proporcional ao risco
tags: [cicd, segurança, pipelines, automação, proveniência, devsecops, risco]
sidebar_position: 0
---

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua e mensurável.  

Os capítulos operacionais implementam o SbD-ToE em contextos técnicos específicos. Estes capítulos traduzem as prescrições basilares em práticas de **execução verificável**, promovendo a **integração contínua da segurança** ao longo do ciclo de vida do software.
:::

# CI/CD Seguro

Os pipelines de **integração e entrega contínua (CI/CD)** são hoje a **espinha dorsal da engenharia de software**.  
Através deles flui código, são construídos artefactos, aplicadas validações e finalmente promovidas versões a produção.  
Se um pipeline for comprometido, o impacto é devastador: **todas as aplicações e serviços que dele dependem herdam esse risco**.

Este capítulo parte de uma constatação inequívoca: **a segurança do pipeline é a segurança do produto**.  
Não basta proteger o código-fonte ou o runtime da aplicação - é o pipeline que garante que tudo o resto chega a produção de forma íntegra, auditável e confiável.

Por isso, o SbD-ToE estabelece aqui um corpo prescritivo para pipelines: **como devem ser concebidos, governados e auditados para resistirem a ataques, prevenirem falhas e suportarem a confiança organizacional**.

---

## 🧭 O que cobre tecnicamente

A segurança de CI/CD abrange um conjunto vasto de domínios técnicos e organizacionais:

- **Definição e versionamento de pipelines** (YAML, scripts, templates)  
- **Ambientes de execução**: runners, agentes e containers de build  
- **Gestão de segredos e credenciais** utilizadas nos jobs  
- **Integração de scanners de segurança** (SAST, IaC, secrets, containers, SBOM)  
- **Assinatura e proveniência de artefactos** para garantir integridade  
- **Políticas de promoção e gates proporcionais ao risco**  
- **Rastreabilidade ponta-a-ponta** commit → pipeline → release  

---

## 📌 O que deve ser feito

Para que os pipelines CI/CD sejam confiáveis e auditáveis, a organização deve:

1. **Endurecer e isolar runners** por projeto, aplicação ou nível de risco.  
2. **Integrar scanners automáticos** em fases proporcionais ao impacto esperado.  
3. **Proibir segredos estáticos** e substituir por OIDC, tokens de curta duração e logs mascarados.  
4. **Assinar e registar proveniência** de todos os artefactos e releases.  
5. **Impor gates de promoção** configurados por classificação de risco (L1, L2, L3).  
6. **Registar exceções** de forma formal, temporária e auditável.  
7. **Garantir rastreabilidade completa** para suportar auditorias e resposta a incidentes.

---

## ⚙️ Como deve ser feito

Os mecanismos técnicos que permitem implementar estas práticas incluem:

- Versionamento de pipelines em repositórios Git com revisão por PR  
- Uso de runners **ephemerais, não privilegiados e segregados**  
- Integração de ferramentas como `semgrep`, `trivy`, `cosign`, `scorecard` e scanners de IaC/containers  
- Configuração de **OIDC e TTL curto** para segredos, eliminando chaves long-lived  
- Assinatura automática de artefactos e proveniência conforme **SLSA**  
- Retenção estruturada de logs, metadados e correlações commit→pipeline→release  

---

## 📆 Quando aplicar

A disciplina de CI/CD Seguro não se ativa pontualmente: acompanha toda a vida do projeto.  
Deve ser aplicada:

- **Desde o arranque de um novo pipeline**, mesmo em MVPs  
- **Sempre que há promoção de releases** para ambientes superiores  
- **Quando se alteram runners, tooling ou segredos**  
- **Em auditorias regulares**, para garantir rastreabilidade e conformidade  

---

## 👥 Quem está envolvido

A segurança de CI/CD depende de papéis distintos, mas complementares:

| Papel/Função     | Contributo principal |
|------------------|----------------------|
| **Dev Team**     | Desenvolver pipelines, reagir a findings e manter qualidade do código |
| **DevOps**       | Endurecer runners, gerir automação e aplicar controlos operacionais |
| **AppSec**       | Definir políticas, thresholds de scanners e gates por risco |
| **GRC/Auditoria**| Verificar rastreabilidade, exceções e conformidade organizacional |

---

## 🎯 Para quê

- **Prevenir ataques à supply chain** explorando pipelines ou runners inseguros  
- **Proteger artefactos críticos**, garantindo que apenas código confiável é promovido  
- **Dar confiança organizacional**, demonstrando rastreabilidade a gestores, auditores e reguladores  
- **Permitir releases rápidas e seguras**, sem comprometer integridade nem conformidade  

---

## 📜 Políticas Organizacionais Relevantes

| Política organizacional         | Obrigatória | Aplicação | Conteúdo mínimo |
|---------------------------------|-------------|-----------|-----------------|
| Política de CI/CD Seguro        | Sim         | Todos os projetos | Revisão por PR, runners seguros, scanners obrigatórios, gestão de segredos, assinatura/proveniência |
| Política de Gestão de Segredos  | Sim         | DevOps, AppSec | OIDC/TTL curto, proibição de segredos estáticos, rotação periódica |
| Política de Rastreabilidade     | Recomendado | GRC/Auditoria | Logs correlacionados commit→pipeline→release, retenção mínima, export imutável |
| Política de Exceções CI/CD      | Sim         | AppSec, GRC | Registo formal, aprovações, prazo e compensações |

As políticas organizacionais relevantes encontram-se descritas no **Anexo de Políticas do Manual**, incluindo: CI/CD Seguro, Gestão de Segredos, Rastreabilidade e Exceções.

---
