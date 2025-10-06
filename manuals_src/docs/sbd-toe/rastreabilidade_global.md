...

### ✅ Conclusão

O SbD-ToE fornece **cobertura quase total** das práticas do NIST SSDF. As lacunas são residuais e técnicas (ex.: assinatura formal de artefactos, RCA estruturado), não comprometendo a conformidade geral com o modelo. O SbD-ToE pode ser usado como evidência de implementação dos requisitos SSDF, incluindo cenários regulatórios.

---

## 🔹 ISO/IEC 27001 & ISO/IEC 27034

### 🧾 Síntese Técnica

A ISO/IEC 27001 define requisitos para Sistemas de Gestão de Segurança da Informação (ISMS), com foco organizacional e baseado em risco. A ISO/IEC 27034 complementa com orientações específicas para segurança de aplicações, incluindo frameworks normativos e controlos reutilizáveis (ONF/ANF).

### 📊 Mapeamento — ISO 27001/27034 vs. SbD-ToE

*As Tabelas 4 e 5 mantêm-se inalteradas.*

### 📌 Análise de Cobertura

* **ISO 27001**: o SbD-ToE cobre integralmente os controlos ligados ao SDLC (ex.: A.14), fornecendo políticas, processos e práticas para desenvolvimento seguro. Controlos como gestão de ativos (A.8) e gestão de incidentes (A.16) são parcialmente abordados no contexto de aplicações.
* **ISO 27034**: o SbD-ToE funciona como ONF aplicável, contendo políticas, controlos (ASCs), e práticas reutilizáveis. A aplicação proporcional por risco (equivalente ao ANF) está contemplada via classificação de criticidade. A certificação de aplicações é operacionalizada através dos gates do CI/CD.

### ✅ Conclusão

O SbD-ToE oferece **cobertura completa dos requisitos ISO/IEC 27034** e **cobertura plena dos controlos ISO 27001 relevantes ao desenvolvimento seguro**. Lacunas em domínios fora de AppSec (gestão de ativos geral, gestão corporativa de incidentes) são esperadas e não afetam a conformidade do SDLC.

---

## 🔹 SLSA v1.0 (Supply Chain Levels for Software Artifacts)

### 🧾 Síntese Técnica

O SLSA define níveis (0–3) de integridade da cadeia de fornecimento de software, centrados em proveniência, build seguro, verificação e distribuição confiável.

### 📊 Mapeamento — SLSA vs. SbD-ToE

*A Tabela 6 mantém-se inalterada.*

### 📌 Análise de Cobertura

* **SLSA L1**: totalmente coberto – SbD inclui SBOM, registo de build, rastreabilidade e validação de componentes.
* **SLSA L2**: parcialmente coberto – pipelines seguros são previstos, mas a assinatura formal da proveniência não é exigida explicitamente.
* **SLSA L3**: parcialmente apoiado – práticas de isolamento, imutabilidade e pinning de dependências existem, mas não se atinge reprodução ou verificação externa.

### ✅ Conclusão

O SbD-ToE suporta **conformidade robusta com SLSA níveis 1 e 2**, com fundamentos técnicos para alcançar L3 mediante extensões. As lacunas relacionam-se com assinatura de builds e certificações formais, que podem ser complementadas pela organização.

---

## 🔹 CIS Controls v8

### 🧾 Síntese Técnica

Os CIS Controls são 18 controlos críticos para proteger ativos, dados e software. O Controlo 16 é dedicado à segurança de software aplicacional. Os controlos são organizados por grupos de implementação (IG1–IG3).

### 📊 Mapeamento — CIS Controls vs. SbD-ToE

*A Tabela 7 mantém-se inalterada.*

### 📌 Análise de Cobertura

O SbD-ToE cobre totalmente os controlos ligados ao SDLC:

* **Completa**: CIS 4, 5, 6, 7, 8, 14, 15, 16, 18 – segurança de código, pipelines, formação, dependências, gestão de vulnerabilidades, pentests.
* **Parcial**: CIS 2, 3, 12, 13, 17 – aplicados ao contexto AppSec, mas não à infraestrutura geral.
* **Fora de escopo**: CIS 1, 9, 10, 11 – domínio de TI corporativo, não abordado pelo SbD-ToE.

### ✅ Conclusão

O SbD-ToE fornece **cobertura completa de todos os controlos CIS relacionados com desenvolvimento seguro**. Para IG2/IG3, o SbD-ToE serve como base sólida, especialmente no Controlo 16. As lacunas identificadas estão fora do escopo do manual (infraestrutura TI, endpoints).

---

## 🔹 ENISA — SDLC & DevSecOps Guidelines

### 🧾 Síntese Técnica

As diretrizes da ENISA descrevem práticas para integrar segurança no ciclo de vida de desenvolvimento e DevOps, incluindo governação, supply chain, automação, testes e operações.

### 📊 Mapeamento — ENISA vs. SbD-ToE

*A Tabela 8 mantém-se inalterada.*

### 📌 Análise de Cobertura

O SbD-ToE cobre todas as áreas ENISA com elevada correspondência:

* **Governança**: política formal, papéis, maturidade, integração com gestão de risco.
* **Supply Chain**: SBOM, SCA, contratos seguros.
* **Operações**: gestão de vulnerabilidades, infraestrutura como código, configuração segura.
* **DevSecOps**: CI/CD automatizado, testes contínuos, métricas e critérios de segurança.
* **Design & Dev Seguro**: threat modeling, requisitos, princípios de arquitetura, privacidade.
* **Testes & Deployment**: code review, testes multi-nível, deployment seguro, eliminação de dados de teste.

### ✅ Conclusão

O SbD-ToE está **totalmente alinhado com as diretrizes da ENISA**, cobrindo todas as áreas propostas para SDLC seguro e DevSecOps. Pode ser utilizado como base de conformidade com NIS2 e outros requisitos europeus emergentes.

---

## ✅ Conclusão Geral

A rastreabilidade global demonstra que o SbD-ToE apresenta **elevada correspondência com os principais frameworks e normas de segurança de software**, tanto em modelos de maturidade (SAMM, BSIMM), como em requisitos normativos (SSDF, ISO, ENISA) e controlos técnicos (CIS, SLSA).

O manual pode ser adotado como framework único de implementação para organizações que pretendem:

* Alcançar níveis avançados de maturidade em segurança de software;
* Demonstrar conformidade com requisitos regulatórios e normativos;
* Integrar segurança de forma transversal no ciclo de vida de desenvolvimento;
* Consolidar práticas DevSecOps, supply chain e AppSec com rastreabilidade comprovada.

As lacunas identificadas são marginais, técnicas ou fora do escopo natural do manual (por exemplo, gestão de ativos de hardware ou resposta organizacional a incidentes), e podem ser complementadas facilmente. O SbD-ToE afirma-se assim como um **pilar estruturante para programas de segurança de software robustos, auditáveis e sustentáveis**.
