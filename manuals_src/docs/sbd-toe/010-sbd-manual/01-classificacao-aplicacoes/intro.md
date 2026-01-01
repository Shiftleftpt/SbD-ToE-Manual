---
id: intro
title: Classificação da Criticidade Aplicacional
description: Determinação da criticidade de aplicações para aplicar proporcionalidade nos controlos de segurança
tags: [base, classificacao, risco, proporcionalidade, ciclo-vida]
---

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.

Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo.  
A ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE, tornando inviável a adoção coerente das práticas operacionais e de governação.
:::

# Classificação da Criticidade Aplicacional

Este capítulo define e prescreve **como classificar aplicações segundo a sua criticidade**, de forma a permitir a **aplicação proporcional de requisitos, controlos, validações e evidência de segurança** ao longo de todo o ciclo de vida.

No SbD-ToE, a classificação **não visa rotular tecnologias ou ferramentas**, mas sim **caracterizar o risco aplicacional de forma suficiente para suportar decisões técnicas e organizacionais consistentes**.

Ferramentas de automação e de apoio à decisão (incluindo IA) são tratadas como **parte normal do SDLC moderno** e devem ser consideradas na classificação **sempre que alterem exposição, dados, impacto ou a forma como decisões e validações são realizadas**.  
A sua presença **não cria novas categorias de risco**, mas influencia os **atributos internos do risco** e, consequentemente, os controlos necessários.

Neste capítulo é sugerido um **modelo de classificação simples, direto e economicamente viável**, adequado à maioria dos contextos aplicacionais.  
A organização pode, contudo, optar por um modelo alternativo já existente (por exemplo DRP/BIA ou outro método formal de análise de risco), desde que seja possível **mapear os seus resultados para o contexto do desenvolvimento aplicacional**.

O objetivo central do manual é:
1. **Classificar aplicações de forma consistente**, para assegurar proporcionalidade adequada;  
2. **Disponibilizar mecanismos claros, rápidos e rastreáveis** para o fazer, sem dependência excessiva de processos pesados ou ferramentas específicas.

> 📌 A classificação da criticidade é o ponto de entrada para os capítulos:  
> [Capítulo 02 – Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/intro),  
> [Capítulo 04 – Arquitetura](/sbd-toe/sbd-manual/arquitetura-segura/intro),  
> [Capítulo 07 – CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro) e  
> [Capítulo 10 – Testes](/sbd-toe/sbd-manual/testes-seguranca/intro).

---

## 🧠 Nota conceptual: risco e atributos

O SbD-ToE trata o **risco como um conceito único**, independentemente da sua origem técnica ou processual.  
O que varia são os **atributos do risco** — como origem, mecanismo, detetabilidade, reprodutibilidade e evidenciabilidade — que influenciam diretamente os requisitos e controlos aplicáveis.

> 📌 Ver: [Atributos do Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/atributos-risco)

---

## 🧪 Prescrição prática: o quê, quem, como, quando, porquê e para quê

### 📌 O que deve ser feito

1. Classificar a aplicação segundo **exposição, dados sensíveis e impacto**, conforme proposto no manual, ou adotar outro modelo equivalente;
2. Considerar explicitamente como **automação e apoio à decisão (incl. IA)** influenciam os **atributos do risco** relevantes;
3. Documentar a classificação, pressupostos e evidência utilizada;
4. Aplicar controlos mínimos com base no nível atribuído;
5. Rever a classificação em pontos-chave do ciclo de vida;
6. Aplicar critérios formais para aceitação de risco, quando necessário.

---

### ⚙️ Como deve ser feito

- Usar o [Modelo de Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos);  
- Ou um modelo alternativo adotado pela organização (ex.: [Adoção de DRP/BIA](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia));  
- Quando existir tooling automatizado/assistivo (incl. IA), **avaliar o seu impacto nos atributos do risco** e calibrar E/D/I em conformidade;  
- Incorporar o [Ciclo de Vida da Classificação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco);  
- Aplicar os [Critérios para Aceitação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/criterios-aceitacao-risco);  
- Considerar ameaças reais através do [Mapeamento de Ameaças por Nível de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco);  
- Registar decisões em repositório versionado, ferramenta de risco ou documentação rastreável.

---

### 📆 Quando aplicar

- Durante a fase inicial do projeto ou definição de arquitetura;
- Sempre que houver alterações relevantes: novas funcionalidades, dados, exposição ou integrações;
- Quando se introduzam ou alterem mecanismos de automação/assistência (incl. IA) com impacto nos atributos do risco;
- Em releases principais ou milestones críticos (ex.: produção);
- Após incidentes de segurança relevantes;
- No mínimo a cada **6 meses** ou **em cada revisão de arquitetura ou roadmap de segurança**.

> A revisão periódica da classificação de risco suporta diretamente práticas de **maturidade intermédia** em **SAMM**, **DSOMM** e **SSDF**.

---

### 👥 Quem está envolvido e como

| Papel                | Contributo                                                                 |
| -------------------- | -------------------------------------------------------------------------- |
| Dev / Tech Lead      | Propor classificação, identificar alterações relevantes                    |
| AppSec / Segurança   | Validar modelo aplicado, ajustar nível de risco, aplicar matriz             |
| Arquitetura          | Rever implicações técnicas, fluxos e exposição                               |
| Produto / Gestão     | Aprovar aceitação de risco, avaliar impacto de exceções                     |
| GRC / Compliance     | Assegurar rastreabilidade e alinhamento normativo                           |
| QA / Testes          | Validar cumprimento de requisitos por nível de risco antes do go-live       |

> ✅ *Todos os contributos devem ser registados e versionados para efeitos de rastreabilidade e auditoria.*

---

### 🎯 Porquê / Para quê

- Garantir proporcionalidade nos controlos de segurança aplicados;
- Reduzir custos evitando sobreproteção ou exposição desnecessária;
- Suportar conformidade normativa e auditorias;
- Informar decisões estratégicas (roadmap, orçamentação, outsourcing);
- Promover melhoria contínua e visibilidade do risco.

> 📌 A aplicação proporcional de controlos pode ser guiada pela  
> [Matriz de Controlos por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/matriz-controlos-por-risco).

---

## 🧪 Ciclo de Vida da Classificação de Risco

A classificação de risco **não é um evento único**, mas um processo contínuo. Deve ser revista:

- Em alterações de arquitetura, exposição, dados ou automação/assistência;
- Antes de releases críticos;
- Periodicamente (ex.: a cada 6 meses);
- Após incidentes ou deteções relevantes.

> 📌 Ver: [Ciclo de Vida da Classificação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco)

Esta reavaliação contínua assegura que os controlos aplicados se mantêm proporcionais e atualizados.

---

## ✅ Critérios para Aceitação de Risco

Nem todos os riscos identificados requerem mitigação adicional. Alguns podem ser **aceites formalmente**, desde que respeitem critérios claros:

- Compatibilidade com o nível L1–L3 da aplicação;
- Valor residual dentro dos limiares definidos;
- Evidência suficiente de controlos aplicados;
- Documentação formal da decisão e prazo de revisão.

> 📌 Ver: [Critérios para Aceitação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/criterios-aceitacao-risco)

---

## 🛡️ Mapeamento de Ameaças a Riscos

Para garantir que a classificação reflete a realidade técnica, é essencial mapear ameaças conhecidas (ex.: STRIDE, MITRE ATT&CK) ao modelo de risco adotado.

> 📌 Ver: [Mapeamento de Ameaças por Nível de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco)

---

## 📜 Políticas Organizacionais Relevantes

A aplicação prática deste capítulo requer políticas formais que assegurem normalização, rastreabilidade e governação do risco:

| Política                                        | Obrigatória? | Aplicação                                | Conteúdo mínimo esperado                                                             |
| ----------------------------------------------- | ------------ | ---------------------------------------- | ------------------------------------------------------------------------------------ |
| Política de Classificação de Risco Aplicacional | ✅ Sim        | Todos os projetos e equipas de produto   | Modelo de classificação; momentos de aplicação; registo formal.                      |
| Política de Aceitação de Risco Residual         | ✅ Sim        | Segurança, gestão, donos de produto      | Critérios de aceitação; responsáveis; validade; evidência rastreável.                |
| Política de Revisão Periódica de Risco          | ✅ Sim        | Toda a organização                       | Frequência mínima; triggers obrigatórios; documentação.                              |
| Política de Rastreabilidade de Decisões         | ⚠️ Opcional  | Contextos regulados ou auditáveis        | Versionamento; ligação a arquitetura, requisitos e controlos.                        |

> 📌 Ver detalhes no **anexo de políticas do manual**.
