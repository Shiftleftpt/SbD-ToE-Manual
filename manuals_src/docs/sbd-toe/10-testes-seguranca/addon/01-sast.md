---
id: sast
title: Validação Estática de Código (SAST)
description: Aplicação de testes estáticos ao código-fonte para deteção precoce de vulnerabilidades e falhas de segurança.
tags: [sast, validação, segurança, código, análise estática]
sidebar_position: 2
---

# 🛠️ Testes Estáticos de Segurança (SAST) {testes-seguranca:addon:sast}

## 🌟 Objetivo {testes-seguranca:addon:sast#objetivo}

Detetar vulnerabilidades de segurança no **código fonte** antes da execução da aplicação, através de **análise estática automática**, garantindo:

- Feedback precoce e contínuo para as equipas de desenvolvimento;
- Rastreabilidade entre código, findings e requisitos de segurança;
- Integração automatizada com o ciclo de desenvolvimento e CI/CD;
- Redução de risco sem impacto na produtividade.

> O SAST é a base da validação shift-left — deteta falhas sem necessidade de executar a aplicação.

---

## 🔍 O que é SAST {testes-seguranca:addon:sast#o_que_e_sast}

O SAST (Static Application Security Testing) analisa o **código-fonte ou bytecode** para identificar padrões perigosos, más práticas, falhas lógicas e potenciais vulnerabilidades — sem executar a aplicação.

Pode ser realizado por:

- Ferramentas linguísticas (linters com regras de segurança);
- Scanners genéricos (ex: ferramentas de mercado);
- Motores semânticos configuráveis (ex: com regras personalizadas).

> ⚠️ O SAST é complementar a testes dinâmicos e manuais — não substitui validações em tempo de execução.

---

## ⚙️ Como aplicar {testes-seguranca:addon:sast#como_aplicar}

1. **Selecionar a ferramenta adequada** por stack (ex: Node, Java, .NET, Python);
2. **Definir regras e thresholds mínimos** de aceitação (ex: falhas críticas bloqueiam build);
3. **Executar automaticamente em cada pull request e pipeline de build**;
4. **Emitir findings com rastreabilidade por linha de código e commit**;
5. **Manter baseline de findings aceite vs findings novos**;
6. **Documentar exceções e justificar false positives**, com acompanhamento AppSec.

> 💡 Sugestão: usar tags nos findings para associar requisitos (ex: `REQ-205`) e mitigações.

---

## ✅ Boas práticas {testes-seguranca:addon:sast#boas_praticas}

- Executar o SAST localmente (pré-commit) e no pipeline (CI);
- Afinar regras para reduzir falsos positivos e ruído;
- Estabelecer política clara de findings bloqueantes por severidade;
- Integrar com backlog (ex: Jira, Azure Boards) para triagem e gestão;
- Validar cobertura da análise (ex: ficheiros ignorados, exclusões);
- Reavaliar configurações com cada evolução tecnológica.

---

## 📎 Referências cruzadas {testes-seguranca:addon:sast#referencias_cruzadas}

| Documento                       | Relação com o SAST                            |
|--------------------------------|-----------------------------------------------|
| Capítulo 02 — Requisitos       | Valida `REQ-203`, `REQ-205`, `REQ-303`        |
| Capítulo 06 — Desenvolvimento  | Reforça práticas de secure coding             |
| Capítulo 07 — CI/CD Seguro     | Ver `07-integracao-validacoes.md`             |
| `06-cobertura-e-priorizacao.md`| Define targets e prioridades de análise       |
| `08-gestao-findings.md`        | Garante tratamento eficaz dos resultados      |
| `09-feedback-equipa.md`        | Envolvimento das equipas na validação         |

---

> 🔒 O SAST permite reduzir o custo de correção de vulnerabilidades ao agir antes da execução — mas só é eficaz quando configurado com critério, mantido atualizado e gerido em conjunto com os developers.
