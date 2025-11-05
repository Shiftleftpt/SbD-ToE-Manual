---

id: pre-note
title: ℹ️ Fundamentação
description: Porquê Determinação da criticidade de aplicações para aplicar proporcionalidade nos controlos de segurança
tags: [base, classificacao, risco, proporcionalidade, ciclo-vida]
---

# Classificação da Criticidade Aplicacional

A classificação de criticidade aplicacional proposta neste capítulo segue uma abordagem **pragmática, rápida e iterativa**, adequada a contextos ágeis e com ciclo de vida contínuo. É especialmente útil em organizações onde:

- Existe uma lacuna na gestão formal de risco, ou  
- A abordagem tradicional de GRC não se adequa à realidade do portfólio aplicacional.

Porquê? Porque nem sempre há um alinhamento entre a **capilaridade exigida por GRC** e a **natureza prática dos sistemas de software em desenvolvimento**. Em muitos casos, o modelo organizacional de risco é demasiado genérico ou complexo para apoiar decisões ágeis no contexto das equipas de desenvolvimento.

> Esta proposta, compatível com o conceito de *risk categorization*, está totalmente alinhada com o domínio **Risk Management** do **OWASP SAMM**, com os princípios de **DSOMM**, **BSIMM**, **SSDF (RM.1)**, **ISO 27005** e **SLSA**, assegurando integração com modelos de maturidade amplamente aceites.

Importa sublinhar: **esta abordagem não substitui métodos formais** de análise de risco (como ISO 27005, NIST 800-30 ou FAIR). O objetivo é garantir que **todas as aplicações recebem, desde o início, uma decisão clara e justificável sobre o seu nível de risco**, evitando dois cenários frequentes:

- **Under-engineering**: aplicações expostas sem controlos mínimos;
- **Over-engineering**: excesso de controlo desnecessário, com desperdício de esforço.

Esta classificação inicial permite aplicar práticas de segurança com **proporcionalidade, rastreabilidade e foco na ação concreta**.

Quando existam **artefactos organizacionais previamente definidos** - como BIA (Business Impact Analysis), DRP (Disaster Recovery Plan), BCP (Business Continuity Plan) ou outras formas de categorização - **estes podem (e devem) ser aproveitados como base factual para a classificação**. Mesmo que não sejam exatos, oferecem uma referência válida e suficiente, conforme descrito no [Alternativa - adoção de DRP, BIA ou outras Classificações Existentes](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia).

## 🎯 Modelo proposto: simples, participativo e pragmático

Este manual propõe um modelo de classificação **empírico e simplificado**, inspirado na **OWASP Risk Rating**, mas adaptado a contextos práticos onde a decisão rápida é essencial. O modelo assenta em três eixos principais:

- **E (Exposição)**: acessibilidade externa e vetores de ataque;
- **D (Tipo de Dados)**: sensibilidade, privacidade e enquadramento regulamentar;
- **I (Impacto Potencial)**: consequências técnicas, operacionais e reputacionais em caso de falha ou violação.

Este modelo é influenciado por abordagens amplamente reconhecidas:

- **OWASP SAMM** - domínio *Threat Assessment*, especialmente a atividade A.2 (Assess Risk);
- **OWASP Risk Rating Methodology** - baseada em impacto e probabilidade;
- **NIST 800-30** e **ISO 27005** - que sustentam metodologias formais de análise de risco.

Contudo, assume-se aqui uma abordagem **mais acessível e pragmática**, que privilegia:

- Rapidez de aplicação (poucos minutos por aplicação);
- Participação direta de stakeholders técnicos e de negócio;
- Decisão empírica, iterativa e fácil de rever ao longo do tempo.

> ⚠️ Esta classificação serve apenas como ponto de partida. Sempre que possível, deve existir **ligação formal ao processo de gestão de risco organizacional**.  
> Quando tal processo não existir ou não for adequado ao contexto aplicacional, esta abordagem serve como alternativa viável e eficaz.

Como detalhado em [Modelo de Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos), a classificação por aplicação é feita atribuindo **valores entre 1 e 3 em cada eixo**, com base na perceção informada dos principais stakeholders.

**Quão acessível está a aplicação ou sistema, com base no seu contexto de rede e interface?**

|   |                                                    |
| - | -------------------------------------------------- |
| ☐ | Apenas acessível internamente (sem acesso externo) |
| ☐ | Acessível externamente, mas com autenticação       |
| ☐ | Público (acesso aberto ou não autenticado)         |

---

**Como classifica a natureza e criticidade da informação processada?**

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
| ☐ | Dados públicos, sem sensibilidade ou impacto legal                     |
| ☐ | Dados pessoais, identificáveis, ou confidenciais internos              |
| ☐ | Dados regulados ou altamente sensíveis (bancários, saúde, localização) |

---

**Qual seria o impacto que uma violação teria, em caso extremo, para a organização?**

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
| ☐ | Impacto nulo ou irrelevante                                            |
| ☐ | Impacto limitado, reversível ou com pouco alcance                      |
| ☐ | Impacto elevado: reputacional, regulatório ou financeiro significativo |

---
o valor da Criticidade é determinado pela soma da "quantificação qualitativa" empirica dos 3 eixos:
```md
Criticidade Total (C) = E + D + I
```

A soma aritmética define o nível de criticidade da aplicação:

| Soma | Classificação | Nível de Risco |
| ---- | ------------- | -------------- |
| 3–4  | L1            | Baixo          |
| 5–6  | L2            | Médio          |
| 7–9  | L3            | Elevado        |

> A classificação deve ser revista por segurança, arquitetura ou GRC, considerando:
>
> * Casos regulatórios;
> * Integrações externas;
> * Contextos técnicos relevantes.

---
