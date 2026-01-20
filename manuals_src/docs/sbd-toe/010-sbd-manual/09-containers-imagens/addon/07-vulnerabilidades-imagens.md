---
id: vulnerabilidades-imagens
title: Deteção e Tratamento de Vulnerabilidades em Imagens
description: Identificação e análise técnica de vulnerabilidades em containers como sinal de risco, não como decisão automática
tags: [containers, vulnerabilidades, cve, sca, trivy, syft, imagem]
---

# 🧨 Deteção e Tratamento de Vulnerabilidades em Imagens

## 🌟 Objetivo

Assegurar que todas as imagens de container utilizadas em pipelines, ambientes de teste ou produção **são analisadas quanto a vulnerabilidades conhecidas (CVEs)**, produzindo **sinais técnicos objetivos** que suportam decisões informadas sobre mitigação, aceitação ou bloqueio.

Este ficheiro define **como detetar e classificar vulnerabilidades**, não como decidir automaticamente a aceitabilidade do risco.

---

## 🧬 O que são vulnerabilidades em imagens

Cada imagem de container inclui **bibliotecas, runtimes e binários** potencialmente vulneráveis, introduzidos por diferentes vias:

- Herdados da imagem base;
- Introduzidos por dependências aplicacionais;
- Transitivos (dependências de dependências);
- Resultantes do próprio processo de build.

Uma vulnerabilidade identificada por um scanner indica:
- presença de um componente afetado,
- associação a uma CVE conhecida,
- potencial impacto técnico.

> ⚠️ A presença de uma CVE **não implica automaticamente risco explorável** no contexto real da aplicação.

---

## ⚠️ Deteção não é avaliação de risco

É fundamental evitar a seguinte equivalência incorreta:

- ✔️ CVE detetada → sinal técnico válido  
- ❌ CVE detetada ≠ risco automaticamente inaceitável  
- ❌ CVSS elevado ≠ impacto real garantido

A avaliação de risco exige contexto adicional:
- código efetivamente exposto;
- vetores de ataque disponíveis;
- permissões e hardening do runtime;
- criticidade da aplicação e dados tratados.

Este ficheiro trata da **deteção e classificação técnica**, não da decisão final.

---

## 📘 Ferramentas de análise (SCA para containers)

| Ferramenta        | Função técnica                                  | Papel no SbD-ToE                     |
|-------------------|-------------------------------------------------|--------------------------------------|
| **Trivy**         | Deteção rápida de CVEs                          | Sinal inicial                         |
| **Grype**         | Correlação SBOM ↔ vulnerabilidades              | Precisão e rastreabilidade            |
| **Snyk Container**| Contextualização adicional (SaaS)               | Apoio à triagem                       |
| **Docker Scout**  | Visualização de camadas e dependências           | Análise exploratória                  |

Estas ferramentas **detetam presença**, não explorabilidade nem impacto real.

---

## 🛠️ Como aplicar a deteção corretamente

1. **Gerar SBOM da imagem final** (ver `06-sbom-containers.md`);
2. **Executar scanner SCA** sobre a imagem real;
3. **Produzir relatório técnico**, incluindo:
   - CVE;
   - pacote afetado;
   - versão;
   - CVSS;
   - fix disponível ou não;
4. **Classificar tecnicamente as vulnerabilidades**:
   - com correção disponível;
   - sem correção disponível;
   - herdadas da base image;
5. **Preservar os resultados como evidência versionada**;
6. **Encaminhar os resultados para análise humana**, quando aplicável.

A automatização **não elimina a necessidade de interpretação**.

---

## 📂 Armazenamento e rastreabilidade dos resultados

Para garantir auditabilidade:

- Armazenar relatórios por imagem e digest;
- Versionar resultados por build;
- Associar scanner, base de dados e timestamp;
- Correlacionar com SBOM e assinatura da imagem.

Resultados não rastreáveis **não têm valor operacional nem auditável**.

---

## 🔍 Utilização correta dos resultados de scanning

No SbD-ToE, os resultados de vulnerabilidades devem ser usados para:

- Priorizar correções;
- Detetar regressões de segurança;
- Apoiar decisões documentadas de aceitação ou mitigação;
- Alimentar métricas de melhoria contínua.

Não devem ser usados como:
- substituto de análise de risco;
- prova de segurança;
- mecanismo único de bloqueio sem contexto.

---

## ✅ Boas práticas

- Definir **limiares técnicos iniciais** (ex.: CVSS ≥ 7) como *trigger*, não como veredicto;
- Distinguir vulnerabilidades exploráveis de teóricas;
- Rever vulnerabilidades herdadas da base image regularmente;
- Automatizar correção quando fix está disponível;
- Documentar aceitação de risco quando aplicável;
- Rever decisões após incidentes ou novas informações.

---

## 📎 Referências cruzadas

| Documento                         | Relação com vulnerabilidades                 |
|----------------------------------|----------------------------------------------|
| `01-imagens-base.md`             | Minimização reduz superfície de CVEs         |
| `06-sbom-containers.md`          | Scanner usa SBOM como base                   |
| `03-assinatura-cadeia-trust.md` | Integridade da imagem analisada              |
| `09-riscos-processo-imagens.md` | Scanners como sinal, não decisão             |
| `15-aplicacao-lifecycle.md`     | Integração no SSDLC                          |

> 🚨 Vulnerabilidades detetadas são **sinais técnicos**, não sentenças.  
> O risco real só existe quando o sinal é interpretado no contexto correto.
