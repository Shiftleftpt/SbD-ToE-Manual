---
id: intro
title: Classificação da Criticidade Aplicacional
description: Determinação da criticidade de aplicações para aplicar proporcionalidade nos controlos de segurança
tags: [base, classificacao, risco, proporcionalidade, ciclo-vida]
---

<!--web-only-->

import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  <Badge color="warning">Capítulo Basilar</Badge>
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: SR1.1, SR1.5</Badge>
  <Badge color="info">SSDF: RM.1, RM.2</Badge>
  <Badge color="info">SLSA: Nível 1 / 4</Badge>
  <Badge color="info">DSOMM: 2 / 3 (média)</Badge>
  [📄 Ver análise de maturidade](xref:sbd-toe:toe:01-classificacao-aplicacoes:maturidade)
</div>
<!--end-web-only-->

<!--print-only-->

📘 Capítulo Basilar · SAMM 2/3 · BSIMM SR1.1, SR1.5 · SSDF RM.1, RM.2 · SLSA 1/4 · DSOMM 2/3
📄 Ver análise de maturidade (ficheiro `canon/10-maturidade.md`)

<!--end-print-only-->

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo SbD-ToE. A sua não aplicação **inviabiliza** a adoção coerente das restantes práticas de segurança por falta de fundação em análise de risco.
:::

# Classificação da Criticidade Aplicacional {classificacao-aplicacoes:intro}

## 1. 🧭 O que cobre tecnicamente {classificacao-aplicacoes:intro#1__o_que_cobre_tecnicamente}

Este capítulo trata da definição e aplicação de critérios para classificar aplicações segundo a sua criticidade. Serve como base para aplicar controlos proporcionais e garantir rastreabilidade técnica e normativa.

> > 📌 A classificação da criticidade é o ponto de entrada para os capítulos:
> > [Capítulo 02 – Requisitos](xref:sbd-toe:toe:intro:intro), [Capítulo 04 – Arquitetura](xref:sbd-toe:toe:intro:intro), [Capítulo 07 – CI/CD](xref:sbd-toe:toe:intro:intro) e [Capítulo 10 – Testes](xref:sbd-toe:toe:intro:intro).

---

## 2. 🧪 Prescrição prática: o quê, quem, como, quando, porquê e para quê {classificacao-aplicacoes:intro#2__prescricao_pratica_o_que_quem_como_quando_porque_e_para_que}

### 📌 O que deve ser feito {classificacao-aplicacoes:intro#o_que_deve_ser_feito}

1. Classificar a aplicação segundo **exposição, dados sensíveis e impacto**;
2. Documentar a classificação e as evidências utilizadas;
3. Aplicar controlos mínimos com base no nível atribuído;
4. Rever a classificação em pontos-chave do ciclo de vida;
5. Aplicar critérios formais para aceitação de risco, quando necessário.

### ⚙️ Como deve ser feito {classificacao-aplicacoes:intro#como_deve_ser_feito}

* Usar o [Modelo de Classificação](xref:sbd-toe:toe:01-classificacao-aplicacoes:modelo-classificacao-eixos);
* Adotar [Adoção de DRP/BIA](xref:sbd-toe:toe:01-classificacao-aplicacoes:adopcao-drp-bia)
* Incorporar o [Ciclo de Vida da Classificação de Risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:ciclo-vida-risco);
* Aplicar os [Critérios para Aceitação de Risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:criterios-aceitacao-risco);
* Considerar ameaças reais através do [Mapeamento de Ameaças por Nível de Risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:mapeamento-ameacas-risco);
* Registar decisões em repositório versionado, ferramenta de risco ou documentação rastreável.

### 📆 Quando aplicar {classificacao-aplicacoes:intro#quando_aplicar}

* Durante a fase inicial do projeto ou arquitetura;
* Sempre que houver alterações relevantes: nova feature, mudança de dados, exposição ou integração;
* Em releases principais ou milestones críticos (ex: produção);
* Após incidentes de segurança relevantes;
* No mínimo a cada **6 meses** ou **em cada revisão de arquitetura ou roadmap de segurança**.

> A revisão periódica da classificação de risco suporta diretamente as práticas de **maturidade 2** em **SAMM**, **DSOMM** e **SSDF**.

### 👥 Quem está envolvido e como {classificacao-aplicacoes:intro#quem_esta_envolvido_e_como}

| Papel              | Contributo                                                                |
| ------------------ | ------------------------------------------------------------------------- |
| Dev / Tech Lead      | Propor classificação, registar alterações                         |
| AppSec / Segurança   | Validar modelo aplicado, ajustar nível de risco, aplicar matriz   |
| Arquitetura          | Rever implicações técnicas e exposição                            |
| Produto / Gestão     | Aprovar aceitação de risco, rever impacto de exceções             |
| GRC / Compliance     | Assegurar rastreabilidade, validação de critérios normativos      |
| QA / Testes          | Validar cumprimento de requisitos por nível de risco antes do go-live |


> ✅ *Todos os contributos devem ser registados e versionados para efeitos de rastreabilidade e auditoria.*

### 🎯 Porquê / Para quê {classificacao-aplicacoes:intro#porque__para_que}

* Garantir proporcionalidade nos controlos de segurança aplicados;
* Reduzir custos evitando sobreproteção ou exposição desnecessária;
* Suportar conformidade com requisitos normativos e auditorias;
* Informar decisões estratégicas (roadmap, orçamentação, outsourcing);
* Promover uma cultura de melhoria contínua e visibilidade do risco.

> 📌 A aplicação proporcional de controlos pode ser guiada pela [Matriz de Controlos por Risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:matriz-controlos-por-risco).
> 📌 Exemplos práticos estão disponíveis em:
> [Casos Práticos](xref:sbd-toe:toe:01-classificacao-aplicacoes:casos-praticos), [Avaliação Semiquantitativa](xref:sbd-toe:toe:01-classificacao-aplicacoes:avaliacao-semiquantitativa), [Risco Residual](xref:sbd-toe:toe:01-classificacao-aplicacoes:risco-residual).

---

## 🧪 Ciclo de Vida da Classificação de Risco {classificacao-aplicacoes:intro#ciclo_de_vida_da_classificacao_de_risco}

A classificação de risco **não é um evento único**, mas um processo contínuo. Deve ser revista:

* Em alterações de arquitetura, exposição ou dados;
* Antes de releases críticos;
* Periodicamente (ex: a cada 6 meses);
* Após incidentes ou deteções relevantes.

> 📌 Ver [Ciclo de Vida da Classificação de Risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:ciclo-vida-risco).

Esta reavaliação contínua assegura que os controlos aplicados se mantêm proporcionais e atualizados.

---

## ✅ Critérios para Aceitação de Risco {classificacao-aplicacoes:intro#criterios_para_aceitacao_de_risco}

Nem todos os riscos identificados requerem mitigação adicional. Alguns podem ser **aceites formalmente**, desde que respeitem critérios claros:

* Compatibilidade com o nível L1–L3 da aplicação;
* Valor residual do risco dentro dos limiares definidos;
* Existência de evidência de controlos aplicados;
* Documentação formal da decisão e prazo de revisão.

> 📌 Ver [Critérios para Aceitação de Risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:criterios-aceitacao-risco).

A aceitação consciente e rastreável de risco é um componente essencial da maturidade em segurança.

---

## 🛡️ Mapeamento de Ameaças a Riscos {classificacao-aplicacoes:intro#mapeamento_de_ameacas_a_riscos}

Para garantir que a classificação de risco é representativa da realidade técnica, é essencial mapear ameaças conhecidas (ex: STRIDE, MITRE ATT\&CK) ao modelo de risco adotado.

> 📌 Ver [Mapeamento de Ameaças por Nível de Risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:mapeamento-ameacas-risco).

Este mapeamento facilita a definição de controlos proporcionais e justifica a análise feita.

---

## 📜 Políticas Organizacionais Relevantes {classificacao-aplicacoes:intro#politicas_organizacionais_relevantes}

A aplicação prática deste capítulo requer a existência das seguintes políticas formais para assegurar a normalização e adoção da classificação, aceitação, revisão e rastreabilidade de risco:

| Política                                        | Obrigatória? | Aplicação                                | Conteúdo mínimo esperado                                                             |
| ----------------------------------------------- | ------------ | ---------------------------------------- | ------------------------------------------------------------------------------------ |
| Política de Classificação de Risco Aplicacional | ✅ Sim        | Todos os projetos e equipas de produto   | Modelo de classificação (exposição, dados, impacto); momentos de aplicação; registo. |
| Política de Aceitação de Risco Residual         | ✅ Sim        | Segurança, gestão, donos de produto      | Critérios de aceitação; responsáveis; validade; evidência e rastreabilidade formal.  |
| Política de Revisão Periódica de Risco          | ✅ Sim        | Toda a organização                       | Frequência mínima (ex: 6 meses); triggers obrigatórios; documentação obrigatória.    |
| Política de Rastreabilidade de Decisões         | ⚠️ Opcional  | Organizações com exigências de auditoria | Versionamento; ligação com arquitetura, requisitos e controlos de segurança.         |

<!--web-only-->
> 🔗 Ver também: [Políticas Organizacionais Relevantes](xref:sbd-toe:toe:01-classificacao-aplicacoes:policies-relevantes)
<!--end-web-only-->

<!--print-only-->
> 📌 Ver detalhes no anexo de políticas do manual.
<!--end-print-only-->
