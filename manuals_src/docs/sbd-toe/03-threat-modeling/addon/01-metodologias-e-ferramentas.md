---
id: metodologias-e-ferramentas
title: Metodologias e Ferramentas de Threat Modeling
description: Comparação prática de abordagens e ferramentas recomendadas
tags: [stride, pasta, linddun, ferramentas, tooling, metodologias]
---

# 🛡️ Metodologias e Ferramentas de Threat Modeling {threat-modeling:addon:metodologias-e-ferramentas}

## 🌟 Objetivo {threat-modeling:addon:metodologias-e-ferramentas#objetivo}

Fornecer uma visão comparativa e orientada à decisão sobre as principais **metodologias e ferramentas** de Threat Modeling, ajudando equipas a:

- Selecionar o modelo adequado com base no tipo de sistema e criticidade;
- Avaliar ferramentas disponíveis por maturidade e contexto;
- Estruturar e versionar os artefactos de Threat Modeling de forma reutilizável.

---

## 🧠 Modelos existentes e quando aplicar {threat-modeling:addon:metodologias-e-ferramentas#modelos_existentes_e_quando_aplicar}

### ✅ Comparação de metodologias {threat-modeling:addon:metodologias-e-ferramentas#comparacao_de_metodologias}

| Modelo      | Foco Principal             | Quando usar                                      | Complexidade | Output típico                          |
| ----------- | -------------------------- | ------------------------------------------------ | ------------ | -------------------------------------- |
| **STRIDE**  | Ameaças técnicas           | Qualquer aplicação exposta ou com lógica crítica | Média        | Lista de ameaças por componente        |
| **LINDDUN** | Ameaças à privacidade      | Sistemas com dados pessoais, RGPD, consentimento | Média        | Avaliação de privacidade por fluxo     |
| **PASTA**   | Modelação baseada em risco | Sistemas regulados, críticos, exigência formal   | Alta         | Ameaças mapeadas para risco e controlo |

> 💡 STRIDE é versátil e o mais amplamente usado. LINDDUN complementa com foco em privacidade. PASTA é adequado para equipas maduras ou contextos regulatórios.

---

### ♻️ Aplicação recomendada {threat-modeling:addon:metodologias-e-ferramentas#aplicacao_recomendada}

- **STRIDE**: ideal como base para qualquer aplicação com interface exposta ou lógica sensível.
- **LINDDUN**: aplicar quando há dados pessoais, preocupações de privacidade ou requisitos legais (ex: RGPD).
- **PASTA**: usar em sistemas com requisitos regulatórios (ex: PCI-DSS, NIS2), ou onde se exige rastreio formal entre risco, ameaça e controlo.

---

### 🧮 Recomendação por tipo de sistema {threat-modeling:addon:metodologias-e-ferramentas#recomendacao_por_tipo_de_sistema}

| Tipo de sistema                | Modelo recomendado | Justificação técnica                                                               |
| ------------------------------ | ------------------ | ---------------------------------------------------------------------------------- |
| API crítica exposta            | STRIDE             | Foco técnico em spoofing, tampering, DoS; cobertura simples por componente         |
| Serviço com dados pessoais     | STRIDE + LINDDUN   | Cobertura técnica (STRIDE) e avaliação de privacidade (LINDDUN)                    |
| Aplicação regulada (PCI, NIS2) | PASTA (+ STRIDE)   | Exige rastreio formal ameaça → risco → controlo, mas STRIDE ajuda na identificação |
| Plataforma interna (privada)   | STRIDE ou LINDDUN  | Dependendo da criticidade e tipo de dados tratados                                 |
| Sistema legado em avaliação    | STRIDE             | Abordagem leve, compatível com falta de documentação ou diagramas completos        |

---

## 🛠️ Ferramentas disponíveis {threat-modeling:addon:metodologias-e-ferramentas#ferramentas_disponiveis}

### ✅ Comparação prática {threat-modeling:addon:metodologias-e-ferramentas#comparacao_pratica}

| Ferramenta          | Modelos Suportados | Colaboração | Características chave                          | Recomendado para…                    |
| ------------------- | ------------------ | ----------- | ---------------------------------------------- | ------------------------------------ |
| Microsoft TMT       | STRIDE             | ❌           | Modelo fixo, integração com diagramas Visio    | Arquitectos, equipas Microsoft       |
| OWASP Threat Dragon | STRIDE             | ✅           | Open source, online/offline, exporta diagramas | Equipas DevSecOps, equipas ágeis     |
| IriusRisk           | STRIDE / Custom    | ✅ (premium) | Gestão de risco, API, integração com Jira/Git  | Organizações com budget e GRC formal |
| Draw.io / Miro      | Todos (visuais)    | ✅           | Diagrama livre, plugins, exportação            | Visualização colaborativa            |
| Markdown + Mermaid  | Todos              | ✅           | Versionável, leve, integrável com GitHub       | Equipas técnicas e pipelines CI/CD   |

---

### 🧩 Recomendações por nível de maturidade {threat-modeling:addon:metodologias-e-ferramentas#recomendacoes_por_nivel_de_maturidade}

| Maturidade da equipa | Abordagem recomendada                           |
| -------------------- | ----------------------------------------------- |
| Baixa / início       | STRIDE com Threat Dragon ou diagramas simples   |
| Média / DevSecOps    | STRIDE com templates, Mermaid, ou Draw.io       |
| Alta / regulatória   | PASTA ou STRIDE + IriusRisk, com integração GRC |

---

## 📁 Organização de artefactos e templates {threat-modeling:addon:metodologias-e-ferramentas#organizacao_de_artefactos_e_templates}

Sugestão de estrutura para manter os modelos reutilizáveis e versionados:

```
📁 threat-model/
├── README.md            # Resumo do modelo, escopo e metodologia usada
├── dfd-diagram.drawio   # Diagrama de fluxo de dados
├── threats.csv          # Matriz de ameaças por componente (STRIDE)
├── mitigations.md       # Mitigações propostas e estado (em progresso, validado, etc.)
└── decisions.md         # Decisões tomadas e justificações (aceitação de risco, exceções)
```

Sempre que possível, os requisitos derivados das ameaças devem ser rastreáveis ao catálogo definido no Capítulo 2 — Requisitos de Segurança.

---

## ✅ Boas práticas {threat-modeling:addon:metodologias-e-ferramentas#boas_praticas}

- Escolher o modelo de análise com base na sensibilidade do sistema;
- Usar diagramas e artefactos versionáveis, legíveis e acessíveis à equipa;
- Garantir rastreabilidade entre ameaças, requisitos e controlos aplicados;
- Repetir o exercício em pontos de mudança: nova arquitetura, novas features ou incidentes.

---

## 📎 Referências cruzadas {threat-modeling:addon:metodologias-e-ferramentas#referencias_cruzadas}

| Documento                    | Relação com este ficheiro                         |
|------------------------------|---------------------------------------------------|
| `01-metodologia-base.md`     | Abordagem geral e objetivos do threat modeling    |
| `03-diagramas-ameacas.md`    | Apoio à criação de DFDs e representação visual    |
| `07-validacao-ameacas.md`    | Validação e cobertura dos modelos utilizados      |

---

## 🔗 Recursos úteis {threat-modeling:addon:metodologias-e-ferramentas#recursos_uteis}

- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
- [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/)
- [Microsoft Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool)
- [IriusRisk](https://www.iriusrisk.com/)
- [STRIDE Method - Microsoft SDL](https://learn.microsoft.com/en-us/security/engineering/stride-overview)
