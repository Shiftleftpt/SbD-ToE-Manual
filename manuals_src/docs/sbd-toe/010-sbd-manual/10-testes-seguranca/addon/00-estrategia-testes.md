---
id: intro
title: Validação Contínua de Segurança
description: Estratégias e práticas para validar continuamente a segurança de aplicações através de testes automatizados, manuais e ofensivos.
tags: [testes, segurança, validação contínua, SAST, DAST, fuzzing, pentesting, DSOMM, SAMM, SSDF, SLSA]
sidebar_position: 0
---


# 🧭 Estratégia de Testes de Segurança no Ciclo de Vida

## 🌟 Objetivo

Estabelecer uma **estratégia integrada e proporcional** para a aplicação de testes de segurança ao longo do ciclo de vida de desenvolvimento (SDLC), garantindo que:

- Os testes certos são aplicados no momento certo;
- A profundidade e frequência de testes estão alinhadas com o risco da aplicação;
- As equipas compreendem o propósito e complementaridade de cada tipo de teste;
- A estratégia pode evoluir com a maturidade da organização.

> Uma estratégia eficaz evita tanto a **falsa confiança** (excesso de ferramentas sem cobertura real) como o **défice de validação** (assunções não testadas).

---

## 🔍 O que é uma estratégia de testes de segurança

Uma estratégia de testes de segurança define:

- **Quando** testar (ex: por fase do SDLC: coding, build, staging, produção);
- **O quê** testar (ex: código-fonte, binários, APIs, fluxos de negócio);
- **Como** testar (ex: estático, dinâmico, interativo, fuzzing, manual);
- **Quem** é responsável por interpretar resultados e responder;
- **Com que frequência** (ex: contínuo, por release, por risco);
- **Critérios de aceitação** e thresholds mínimos por tipo de teste.

---

## 🧬 Mapeamento SDLC → Testes

| Fase do SDLC        | Tipos de testes recomendados                            | Objetivo principal                    |
|---------------------|----------------------------------------------------------|----------------------------------------|
| Planeamento         | Threat modeling, revisão de requisitos                  | Prevenção e cobertura                  |
| Desenvolvimento     | Linters, SAST, IAST                                     | Detecção precoce no código             |
| Build/CI            | SAST, SCA, testes de regressão, geração de SBOM         | Validação contínua                     |
| Staging/Testes      | DAST, Fuzzing, IAST, validações manuais                 | Avaliação de comportamento real        |
| Produção/Operação   | Monitorização, validações por amostragem, pentest       | Verificação pós-deploy                 |

---

## 🛠️ Como aplicar na prática

1. **Classifica o risco da aplicação (L1–L2–L3)** conforme o Capítulo 01;
2. **Seleciona os tipos de teste apropriados** para o nível de risco:
   - L1: Linters + SAST + testes manuais básicos;
   - L2: Adição de DAST, regressão de segurança, IAST;
   - L3: Full pipeline com fuzzing, cobertura por tipo de API, testes diferenciais;
3. **Integra testes no pipeline** com gates, thresholds e artefactos rastreáveis;
4. **Documenta a estratégia de testes** no repositório/projeto (ex: ficheiro `SECURITY-TESTS.md`);
5. **Avalia regularmente a eficácia dos testes** com base em findings reais e incidentes.

---

## ✅ Boas práticas

- **Aplica testes shift-left** sempre que possível (ex: SAST no PR);
- Define **critérios claros de aprovação** (ex: cobertura mínima, 0 findings críticos);
- Adota **matrizes de risco vs tipo de teste** para cada repositório ou produto;
- Faz revisão periódica da estratégia com equipa AppSec;
- Inclui **feedback dos testes** no backlog e processos de melhoria contínua.

---

## 📎 Referências cruzadas

| Documento                       | Relevância estratégica                         |
|----------------------------------|------------------------------------------------|
| `01-sast.md`                     | Parte essencial do início da estratégia        |
| `02-dast.md`                     | Validação dinâmica - depende do contexto       |
| `06-cobertura-e-priorizacao.md` | Define alvos e profundidade dos testes         |
| `07-integracao-pipeline.md`     | Onde e como ligar a estratégia ao CI/CD        |
| Capítulo 01 - Gestão de Risco   | Define o nível de criticidade da aplicação     |
| Capítulo 02 - Requisitos        | Define o quê deve ser testado (REQs)           |
| Capítulo 06 - Desenvolvimento   | Define práticas seguras a validar              |
| Capítulo 07 - CI/CD Seguro      | Define como os testes se integram na entrega   |
| Capítulo 12 - Monitorização     | Observação pós-deploy e validações em runtime  |

---

> 🧠 Uma estratégia de testes de segurança **não é uma lista de ferramentas** - é uma decisão sobre como, quando e com que profundidade validar a segurança do que se constrói. É o reflexo direto do risco aceite pela organização.
