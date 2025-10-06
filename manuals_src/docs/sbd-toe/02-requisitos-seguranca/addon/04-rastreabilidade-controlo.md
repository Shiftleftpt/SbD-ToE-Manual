---
id: rastreabilidade-controlo
title: Rastreabilidade entre Requisitos e Controlos Técnicos
description: Ligação entre requisitos definidos, testes aplicáveis e controlos implementados
tags: [rastreabilidade, requisitos, controlos, testes, cobertura]
---

# 🔗 Modelo de Rastreabilidade de Requisitos {requisitos-seguranca:addon:rastreabilidade-controlo}

## 🌟 Objetivo {requisitos-seguranca:addon:rastreabilidade-controlo#objetivo}

Permitir a documentação e manutenção da **rastreabilidade entre riscos identificados, requisitos de segurança aplicados, respetivos controlos técnicos, mecanismos de validação e evidência associada**.  
Este modelo apoia:

- A verificação sistemática da cobertura de segurança ao longo do ciclo de vida;
- A preparação de auditorias internas e externas;
- A integração com ferramentas de desenvolvimento, gestão de risco e conformidade.

> Pode ser usado como template em Markdown, Excel, Jira, Confluence ou outras ferramentas ALM.

---

## 🧱 Estrutura Sugerida {requisitos-seguranca:addon:rastreabilidade-controlo#estrutura_sugerida}

| Risco (ID) | Requisito (ID) | Descrição do Requisito                          | Tipo de Controlo | Validação                     | Evidência                          |
|------------|----------------|--------------------------------------------------|-------------------|-------------------------------|-------------------------------------|
| RSK-001    | REQ-001        | Autenticação multifator com hardware token       | Preventivo        | Teste automatizado em CI/CD   | Captura de ecrã do fluxo de login   |
| RSK-002    | REQ-002        | Logging centralizado com retenção de 180 dias    | Detetivo          | Revisão manual + script       | Output de `logrotate` + configuração |
| RSK-003    | REQ-003        | Validação de input com base em schema definido   | Preventivo        | Testes unitários e integração | Logs de execução dos testes         |
| RSK-004    | REQ-004        | Passwords com requisitos conforme NIST 800-63B   | Preventivo        | Análise estática (regex)      | Código fonte + screenshot           |

---

## 🛠️ Como aplicar {requisitos-seguranca:addon:rastreabilidade-controlo#como_aplicar}

- Cada linha da matriz representa uma ligação direta entre um **risco identificado** e o **requisito de segurança correspondente**.
- O tipo de controlo deve ser classificado como: `Preventivo`, `Detetivo` ou `Corretivo`.
- A validação deve ser objetiva e comprovável: testes automatizados, revisão manual, análise estática, etc.
- A evidência pode incluir logs, capturas de ecrã, ficheiros de configuração, ou outputs de ferramentas.

> 🧩 Este modelo complementa a aplicação dos capítulos `01-gestao-risco`, `02-requisitos-seguranca` e `20-checklist-revisao.md`.

---

## 📘 Exemplos por Tema {requisitos-seguranca:addon:rastreabilidade-controlo#exemplos_por_tema}

| Tema                    | Requisito (Resumo)                                           | Tipo de Controlo   | Validação                      | Evidência                       |
|-------------------------|--------------------------------------------------------------|--------------------|-------------------------------|----------------------------------|
| Autenticação            | Sessões com timeout inativo de 15 min                        | Preventivo         | Teste manual + script browser | Configuração + gravação da sessão |
| Controlo de Acesso      | RBAC com separação de funções (SoD)                          | Preventivo         | Revisão de roles + testes     | Printscreen de matrix de roles  |
| Logging e Monitorização | Alertas em tempo real para falhas de login                   | Detetivo           | Simulação de falha            | Captura de alerta no SIEM        |
| Gestão de Erros         | Mensagens de erro sem exposição de stack trace               | Preventivo         | Testes automatizados          | Output de testes de integração   |
| Segurança de Código     | Linters e análise estática com política personalizada        | Preventivo         | Pipeline CI/CD                | Relatório de análise             |
| SCA / Dependências      | Política de atualização crítica < 48h                        | Preventivo/Corretivo| Verificação de SLA            | Issue criada + commit            |
| Dados Sensíveis         | Encriptação AES-256 em repouso para dados críticos           | Preventivo         | Revisão da configuração       | Output de KMS ou vault           |
| Comunicação Segura      | TLS 1.2+ obrigatório para APIs internas                      | Preventivo         | Testes automatizados          | Scanner + resultado de verificação |
| Ciclo de Vida de Sessão | Logout automático após X minutos de inatividade              | Preventivo         | Teste com navegador/script    | Gravação de sessão + logs        |

---

## 📂 Organização recomendada {requisitos-seguranca:addon:rastreabilidade-controlo#organizacao_recomendada}

Este modelo pode ser estruturado por aplicação, por release ou por funcionalidade crítica.  
Sugestão de organização prática:

1. **Resumo e finalidade**
2. **Legenda de colunas (risco, requisito, controlo, validação, evidência)**
3. **Tabela rastreável (como as apresentadas acima)**
4. **Referência cruzada com os requisitos definidos no Capítulo 2**
5. **Apontadores para evidência (diretórios, commits, screenshots, pipelines)**

Formatos sugeridos:

- `.md` para rastreabilidade em Git;
- `.csv` ou `.xlsx` para exportação e análise rápida;
- Integração com campos personalizados em Jira, ADO, Confluence ou ferramentas ALM.

---

## 🔗 Integração com o ciclo de vida {requisitos-seguranca:addon:rastreabilidade-controlo#integracao_com_o_ciclo_de_vida}

Este modelo deve ser aplicado:

- Durante **revisões técnicas** e de **segurança de release**
- Como suporte ao processo de **aceitação de riscos**
- Em checkpoints formais como **go/no-go** ou auditorias ISO/PCI
- Para registo de evidência técnica e validação contínua de requisitos

---

## 📎 Ferramentas recomendadas {requisitos-seguranca:addon:rastreabilidade-controlo#ferramentas_recomendadas}

| Finalidade                    | Ferramenta sugerida                |
|-------------------------------|------------------------------------|
| Versionamento leve            | Git + Markdown                     |
| Análise e filtros             | Excel / CSV                        |
| Integração no fluxo DevOps    | Jira, Azure DevOps, GitHub Issues  |
| Validação e scanning          | SonarQube, ZAP, Trivy, scanners SAST/DAST |
| Gestão de segredos / config   | Vault, KMS, parameter stores       |
| Evidência de logs / alertas   | SIEM (ELK, Splunk, Sentinel...)    |

---

## ✅ Boas práticas {requisitos-seguranca:addon:rastreabilidade-controlo#boas_praticas}

- Criar e manter **uma matriz por aplicação ou projeto crítico**
- Usar o modelo como **trilho de auditoria interno**
- **Versionar todas as alterações** à matriz e à evidência associada
- Rever a matriz em todos os ciclos de release
- Incluir campos com referências aos requisitos (`REQ-XXX`) e riscos (`RSK-XXX`)

---

