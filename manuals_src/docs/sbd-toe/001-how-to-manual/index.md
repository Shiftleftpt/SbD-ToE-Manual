---
id: index
title: Security by Design – Teoria de Tudo
hide_title: false
hide_table_of_contents: false
---

# Introdução ao Manual SbD – Theory of Everything

O manual **Security by Design – Theory of Everything (SbD-ToE)** foi criado com um propósito claro:  
oferecer um **quadro prático e proporcional** para a adoção de segurança no desenvolvimento de software, ajustado ao risco real de cada aplicação.

Nem todas as aplicações são iguais.  
Nem todas as organizações têm os mesmos recursos, contexto ou requisitos regulatórios.

Por isso, este manual parte de um princípio fundamental:

> **A segurança deve ser aplicada com base numa análise de risco - e não de forma cega ou uniforme.**

---

## 🧭 Precedência lógica entre capítulos

Há uma ordem lógica na leitura e aplicação dos capítulos:  
a **análise de risco e a classificação de aplicações** são sempre o ponto de partida. Só depois se definem requisitos, modelam ameaças e desenha a arquitetura.

Esta precedência é intencional - garante que todas as práticas seguintes são **proporcionais, relevantes e ajustadas ao contexto real** de cada aplicação.

---

## ⚖️ Fundamento: risco como critério orientador

Inspirado nos princípios do [NIS2](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX%3A32022L2555) <!-- Precisa revisão manual -->, e em frameworks como o **ISO/IEC 27005**, **OWASP SAMM** e **Microsoft SDL**, este manual propõe uma **classificação de risco simplificada**, que serve de base para todas as decisões.

- A avaliação de risco define o **nível de exigência** aplicável.
- Cada nível determina **quais os controlos mandatórios, recomendados ou opcionais**.
- A matriz de risco assegura **proporcionalidade e foco nos riscos reais**.

> Este modelo canaliza esforço para onde ele é mais necessário - nem tudo precisa de tudo.

---

## 🛠️ Prescritivo, mas adaptável

O SbD-ToE é um manual **prescritivo**:  
diz-te **o que fazer, quando, como e com que ferramentas**.

Mas é também:

- **Modular** - podes adotar os domínios mais críticos primeiro (ex: "Controlo de Dependências", "CI/CD Seguro")
- **Extensível** - suporta evolução progressiva com frameworks como SAMM, ASVS ou roadmaps internos
- **Pragmático** - recomendações orientadas à prática, compatíveis com equipas reais em funcionamento

O objetivo **não é "cumprir um checklist"**, mas sim:

- Fazer sentido para quem executa
- Ser compreendido pelas equipas técnicas e de produto
- Não bloquear, mas **acelerar com segurança**

---

## 🧩 Um manual para todas as organizações

Qualquer organização - independentemente da sua dimensão, orçamento ou contexto - pode usar este manual como base para:

- Avaliar e melhorar a sua maturidade de segurança
- Tomar decisões informadas com base no risco
- Alinhar desenvolvimento, segurança e operação
- Implementar melhorias incrementais, realistas e sustentáveis

Este manual foi construído para:

- **Evitar ambiguidade**
- **Facilitar a integração com práticas existentes**
- **Apoiar tecnicamente sem ruturas**
- **Promover mudança estrutural com realismo**

---

## 🧠 Aplicar com inteligência, não por obrigação

> No limite, aplica-se o bom senso.  
> A segurança é para servir a organização - **não para a atrapalhar**.

Este manual **não impõe - propõe**:  
fornece um caminho claro, estruturado e aplicável, deixando sempre espaço para **adaptação, maturidade e contexto**.

É uma **ferramenta de capacitação, não de controlo**.

---

## 🌐 A base de todos os outros manuais

O SbD-ToE é a fundação onde assentam todos os conteúdos especializados da ShiftLeft:

- **Segurança na utilização de IA**
- **Supply Chain Security**
- **ASPM – Application Security Posture Management**
- **Mitigação de Ameaças (OSC&R)**

Todos partem deste núcleo comum:  
um ciclo de vida de desenvolvimento **seguro, proporcional, auditável - e humano**.

---

## 🚀 O que se consegue com o SbD-ToE

Ao aplicar de forma consistente as 14 áreas técnicas do SbD-ToE, a organização alcança níveis elevados de maturidade, alinhados com frameworks internacionais:

| Framework | Maturidade Esperada |
|----------|----------------------|
| **OWASP SAMM** | Nível 2–3 (Managed/Defined) |
| **BSIMM** | Domínio 2–3 (Defined/Measured) |
| **ISO/IEC 27001/27034** | Implementação e melhoria contínua de controlos |
| **SLSA** | Nível 3 ou superior |
| **NIST SSDF** | Alinhamento com Prepare, Protect, Produce, Respond |
| **CIS Controls** | Cumprimento de controlos aplicáveis ao SDLC |

Este posicionamento permite:

- Demonstrar conformidade
- Assegurar rastreabilidade
- Sustentar auditorias e certificações
- Melhorar continuamente a postura de segurança

E, acima de tudo, **obter resultados práticos e mensuráveis desde o início**, independentemente do ponto de partida.

---

## 📌 Sobre a Cobertura e os Gaps

O manual **SbD-ToE** está alinhado com frameworks internacionais como **OWASP SAMM**, **BSIMM**, **NIST SSDF** e **SLSA**.  
Esta correspondência é apresentada de forma explícita em:

- [Cobertura por Framework](xref:sbd-toe:toe:coverage-frameworks.md:coverage-frameworks)
- [Gaps e Delimitações](xref:sbd-toe:toe:gaps-por-framework.md:gaps-por-framework)

> **Nota:** Os gaps listados **não representam fragilidades** da abordagem SbD-ToE.  
> São, na sua maioria, **delimitações intencionais** para manter o manual:
> - Prático e aplicável na realidade das equipas  
> - Proporcional ao risco e ao contexto  
> - Modular, permitindo evolução por fases

Temas mais avançados, contínuos ou transversais são tratados em **secções complementares** do manual:

| Secção                       | Foco Principal                                                                 |
|-----------------------------|--------------------------------------------------------------------------------|
| 📦 `Supply Chain Security`  | Rigor na proveniência, integridade e rastreabilidade no ciclo de vida do software |
| 📊 `ASPM`                   | Gestão contínua da postura de segurança aplicacional                           |
| 🔐 `Segurança na IA`        | Uso seguro e controlado de ferramentas, modelos e pipelines com IA              |
| 🛡️ `Mitigação de Ameaças`   | Resposta estruturada a ameaças com base na framework OSC&R                      |

Estas secções complementam o SbD-ToE e podem ser adotadas **progressivamente**, com base nas necessidades e maturidade de cada organização.

---

## 🙏 Nota de Agradecimento

> *"We stand on the shoulders of giants."*

Este manual é fruto do trabalho coletivo de comunidades, autores e equipas técnicas ao longo de décadas.  
A sua origem está na prática - não na teoria - com mais de 10 anos de experiência real aplicada.

Desde a primeira “ShiftLeft Framework for Security by Design & by Default” até hoje, procurámos sempre **soluções simples, exequíveis e adaptáveis**.

A todos os que partilham, desafiam e fazem evoluir este campo: o nosso agradecimento.

