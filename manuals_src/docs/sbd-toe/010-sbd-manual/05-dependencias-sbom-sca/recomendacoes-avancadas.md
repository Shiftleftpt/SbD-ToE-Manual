---
id: recomendacoes-avancadas
title: Práticas Avançadas - Gestão de Dependências e Supply Chain
description: Recomendações reforçadas para contextos críticos ou ambientes com elevada maturidade
tags: [avancadas, maturidade, supply-chain, dependencias, sbom, sca]
sidebar_position: 30

---

# 🧠 Práticas Avançadas - Gestão de Dependências e Supply Chain

Este anexo apresenta práticas de segurança reforçadas aplicáveis a contextos com requisitos elevados de maturidade, conformidade regulatória exigente (ex: NIS2, CRA, ISO 27001) ou aplicações críticas (ex: finanças, infraestruturas, defesa).

> 📌 Estas recomendações não substituem os controlos principais, mas aumentam significativamente a visibilidade, confiabilidade e resiliência da cadeia de fornecimento.

---

## 🔐 1. Validação de SBOM em runtime

- Integrar SBOM como artefacto verificável durante a execução (ex: embed como label em container, sidecar de validação)
- Comparar SBOM runtime com imagem oficial para deteção de drift
- Bloquear execução se o binário contiver bibliotecas não previstas

> Ferramentas: `tern`, `in-toto`, `Sigstore`, `Cosign`, `KubeClarity`

---

## 🧬 2. Política “Zero Unknowns”

- **Nenhuma dependência transitiva pode ser desconhecida ou não catalogada**
- SBOMs devem conter `purl` ou identificador único por componente
- Dependências obsoletas ou sem origem clara são bloqueadas automaticamente

> Exige SBOMs completos e atualizados + integração com repositórios internos e políticas de CI

---

## 🧪 3. Sandboxing determinístico para build e SCA

- Executar build e análise SCA em ambiente **sandboxed, imutável e auditável**
- Usar file system de só leitura e isolamento de rede para prevenir scripts maliciosos
- Controlar hashes dos artefactos gerados antes do deploy

> Ex: Containers Docker com `--read-only`, `--no-new-privileges` e `seccomp`

---

## 🧰 4. Empacotamento e selagem de bibliotecas críticas

- Criação de bundles internos de bibliotecas já verificadas e seladas
- Uso de assinaturas digitais (`cosign`, `gpg`) para garantir integridade e origem
- Exposição via repositório privado interno com `promotion pipeline`

> Ideal para dependências partilhadas entre equipas ou projetos regulados

---

## 🧼 5. Remoção sistemática de código não utilizado (dependency hygiene)

- Verificação periódica de pacotes não utilizados (ex: `depcheck`, `pip-check`, `npm-prune`)
- Foco em reduzir a superfície de ataque associada a código morto
- Processo de aprovação reversa: tudo o que não for explicitamente necessário é removido

> Prática crítica em imagens de containers e funções serverless

---

## 📊 6. Métricas de maturidade para dependências

- % de findings SCA resolvidos em < 5 dias
- % de dependências com SBOM completo e versionado
- Nº médio de dependências por serviço / por imagem
- Nº de exceções de risco ativas e expiração associada

> Estas métricas podem ser usadas para dashboards de risco, SLA internos e auditorias externas

---
## 🧮 7. Análise da cadeia transitiva de dependências

- Avaliação do **comportamento completo da cadeia de dependências**, incluindo scripts pós-instalação, hooks e toolchains
- Aplicação de scanners que avaliem `package.json`, `requirements.txt`, `setup.py`, `postinstall`, etc.
- Validação de pacotes que executam código na instalação (ex: `npm`, `pip`, `cargo`)

> Ferramentas úteis: `socket.dev`, `npm-lockfile-linter`, `PyUp`, `NodeSecure`, `Chain-bench`

---

## 🌐 8. Reputação e origem confiável de componentes

- Aplicar política de **score mínimo de reputação** para pacotes públicos
- Apenas permitir bibliotecas com:
  - Múltiplos maintainers ativos
  - Repositório público com releases assinadas
  - Histórico de atualizações regulares
- Integração com ferramentas de scoring como `OSSF Scorecard`, `deps.dev`, `libraries.io`

> Ideal para filtrar riscos em pacotes de baixo uso ou não mantidos

---

## 🧱 9. Fallback hardened para registries externos

- O fallback para repositórios externos (ex: `npmjs`, `PyPI`, `DockerHub`) **deve ser controlado e justificado**
- Requisitos mínimos:
  - Verificação de assinatura ou hash
  - Acesso apenas a partir de proxy autenticado
  - Justificação de ausência em mirror interno

> Esta prática reduz o risco de *supply chain injection* durante builds

---

## 🛰️ 10. Validação cruzada de SBOM com threat intelligence externo

- Enriquecer SBOMs com dados de risco provenientes de fontes como:
  - CISA KEV (Known Exploited Vulnerabilities)
  - OSV (Open Source Vulnerability)
  - VulnCheck, Risk Ledger, entre outros
- Automatizar bloqueios baseados em `exploit-in-the-wild` ou `CVSS > threshold`
- Integrar enriquecimento no pipeline CI/CD antes de aprovação de build

> Aumenta a capacidade de **resposta proativa a exploits em circulação**, complementando o SCA tradicional.

---

## 🧯 11. Análise de blast radius por dependência crítica

- Identificar bibliotecas cujo compromisso teria alto impacto organizacional
- Calcular blast radius com base em:
  - Uso transversal por serviços
  - Nível de exposição externa
  - Capacidades críticas (ex: auth, parsing, crypto)
- Aplicar medidas reforçadas:
  - Releases com staging + aprovação explícita
  - Verificação multi-equipa
  - Atualização prioritária forçada

> Permite gerir risco não só por vulnerabilidade, mas pelo **impacto sistémico de cada dependência**.

## 🔗 Ligações com outras práticas reforçadas

| Domínio técnico      | Recomendações avançadas relacionadas                |
|----------------------|----------------------------------------------------|
| Containers           | Imagens mínimas + SBOM embedded + scanning isolado |
| CI/CD                | Build reprodutível + assinatura + proveniência     |
| Requisitos           | Rastreabilidade bidirecional + critérios de aceitação automatizados |

---

> 🧭 Estas recomendações devem ser aplicadas de forma gradual e proporcional à criticidade do sistema. Em ambientes L3, pelo menos 2 destas práticas devem ser adotadas como baseline de maturidade elevada.
