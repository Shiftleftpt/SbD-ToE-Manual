---
id: intro
title: Classificação da Criticidade Aplicacional
description: Determinação da criticidade de aplicações para aplicar proporcionalidade nos controlos de segurança
tags: [base, classificacao, risco, proporcionalidade, ciclo-vida]
---

import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: SR1.1, SR1.5</Badge>
  <Badge color="info">SSDF: RM.1, RM.2</Badge>
  <Badge color="info">SLSA: Nível 1 / 4</Badge>
  <Badge color="info">DSOMM: 2 / 3 (média)</Badge>
  [📄 Ver análise de maturidade](./achievable-maturity)
</div>

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.  

Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo, cobrindo:
- **Classificação de risco e proporcionalidade** (Cap. 01)  
- **Definição estruturada de requisitos de segurança** (Cap. 02)  
- **Modelação de ameaças e priorização de controlos** (Cap. 03)  
- **Desenho e validação de arquitetura segura** (Cap. 04)  
- **Implementação disciplinada e revisão de código seguro** (Cap. 06)  

A ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE, tornando inviável a adoção coerente das práticas operacionais e de governação.
:::


# Classificação da Criticidade Aplicacional

Este capítulo trata da definição e aplicação de critérios para classificar aplicações segundo a sua criticidade. Serve como base para aplicar controlos proporcionais e garantir rastreabilidade técnica e normativa.
Neste capitulo é sugerido um modelo de classificação simples, direto e rápido, mas a organização pode optar por outro já existente ou até escolher outra forma de classificar as aplicações. O Manual explica como pode ser efetuada essa adoção, e.g., [Adoção de DRP/BIA](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia). Ou outro modelo que sejá necessário.
O que interessa, e o que este manual tenta prover, é 1º classificar as aplicações - para assegurar a proporcionalidade adequada, e 2º ter mecanismos bem claro, rápidos e económicos de o fazer.

>> 📌 A classificação da criticidade é o ponto de entrada para os capítulos:
>> [Capítulo 02 – Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Capítulo 04 – Arquitetura](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Capítulo 07 – CI/CD](/sbd-toe/sbd-manual/cicd-seguro/intro) e [Capítulo 10 – Testes](/sbd-toe/sbd-manual/testes-seguranca/intro).

---

## 2. 🧪 Prescrição prática: o quê, quem, como, quando, porquê e para quê

### 📌 O que deve ser feito

1. Classificar a aplicação segundo **exposição, dados sensíveis e impacto** conforme proposto no manual,  ou adoptar um outro modelo de classificação (e.g. com base na avaliação se existente de DRP, ou usar outro metodo mais formal de analise de risco, desde que se consiga transferir para o "universo" do desenvolvimento aplicacional). 
2. Documentar a classificação e as evidências utilizadas;
3. Aplicar controlos mínimos com base no nível atribuído;
4. Rever a classificação em pontos-chave do ciclo de vida;
5. Aplicar critérios formais para aceitação de risco, quando necessário.

### ⚙️ Como deve ser feito

* Usar o [Modelo de Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos);
* ou usar outro que faça sentido à organização (por exemplo [Adoção de DRP/BIA](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia))
* Incorporar o [Ciclo de Vida da Classificação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco);
* Aplicar os [Critérios para Aceitação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/criterios-aceitacao-risco);
* Considerar ameaças reais através do [Mapeamento de Ameaças por Nível de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco);
* Registar decisões em repositório versionado, ferramenta de risco ou documentação rastreável.

### 📆 Quando aplicar

* Durante a fase inicial do projeto ou arquitetura;
* Sempre que houver alterações relevantes: nova feature, mudança de dados, exposição ou integração;
* Em releases principais ou milestones críticos (ex: produção);
* Após incidentes de segurança relevantes;
* No mínimo a cada **6 meses** ou **em cada revisão de arquitetura ou roadmap de segurança**.

> A revisão periódica da classificação de risco suporta diretamente as práticas de **maturidade 2** em **SAMM**, **DSOMM** e **SSDF**.

### 👥 Quem está envolvido e como

| Papel              | Contributo                                                                |
| ------------------ | ------------------------------------------------------------------------- |
| Dev / Tech Lead      | Propor classificação, registar alterações                         |
| AppSec / Segurança   | Validar modelo aplicado, ajustar nível de risco, aplicar matriz   |
| Arquitetura          | Rever implicações técnicas e exposição                            |
| Produto / Gestão     | Aprovar aceitação de risco, rever impacto de exceções             |
| GRC / Compliance     | Assegurar rastreabilidade, validação de critérios normativos      |
| QA / Testes          | Validar cumprimento de requisitos por nível de risco antes do go-live |


> ✅ *Todos os contributos devem ser registados e versionados para efeitos de rastreabilidade e auditoria.*

### 🎯 Porquê / Para quê

* Garantir proporcionalidade nos controlos de segurança aplicados;
* Reduzir custos evitando sobreproteção ou exposição desnecessária;
* Suportar conformidade com requisitos normativos e auditorias;
* Informar decisões estratégicas (roadmap, orçamentação, outsourcing);
* Promover uma cultura de melhoria contínua e visibilidade do risco.

> 📌 A aplicação proporcional de controlos pode ser guiada pela [Matriz de Controlos por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/matriz-controlos-por-risco).
> 📌 Exemplos práticos estão disponíveis em:
> [Casos Práticos](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/casos-praticos), [Avaliação Semiquantitativa](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/avaliacao-semiquantitativa), [Risco Residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual).

---

## 🧪 Ciclo de Vida da Classificação de Risco

A classificação de risco **não é um evento único**, mas um processo contínuo. Deve ser revista:

* Em alterações de arquitetura, exposição ou dados;
* Antes de releases críticos;
* Periodicamente (ex: a cada 6 meses);
* Após incidentes ou deteções relevantes.

> 📌 Ver [Ciclo de Vida da Classificação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco).

Esta reavaliação contínua assegura que os controlos aplicados se mantêm proporcionais e atualizados.

---

## ✅ Critérios para Aceitação de Risco

Nem todos os riscos identificados requerem mitigação adicional. Alguns podem ser **aceites formalmente**, desde que respeitem critérios claros:

* Compatibilidade com o nível L1–L3 da aplicação;
* Valor residual do risco dentro dos limiares definidos;
* Existência de evidência de controlos aplicados;
* Documentação formal da decisão e prazo de revisão.

> 📌 Ver [Critérios para Aceitação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/criterios-aceitacao-risco).

A aceitação consciente e rastreável de risco é um componente essencial da maturidade em segurança.

---

## 🛡️ Mapeamento de Ameaças a Riscos

Para garantir que a classificação de risco é representativa da realidade técnica, é essencial mapear ameaças conhecidas (ex: STRIDE, MITRE ATT\&CK) ao modelo de risco adotado.

> 📌 Ver [Mapeamento de Ameaças por Nível de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco).

Este mapeamento facilita a definição de controlos proporcionais e justifica a análise feita.

---

## 📜 Políticas Organizacionais Relevantes

A aplicação prática deste capítulo requer a existência das seguintes políticas formais para assegurar a normalização e adoção da classificação, aceitação, revisão e rastreabilidade de risco:

| Política                                        | Obrigatória? | Aplicação                                | Conteúdo mínimo esperado                                                             |
| ----------------------------------------------- | ------------ | ---------------------------------------- | ------------------------------------------------------------------------------------ |
| Política de Classificação de Risco Aplicacional | ✅ Sim        | Todos os projetos e equipas de produto   | Modelo de classificação (exposição, dados, impacto); momentos de aplicação; registo. |
| Política de Aceitação de Risco Residual         | ✅ Sim        | Segurança, gestão, donos de produto      | Critérios de aceitação; responsáveis; validade; evidência e rastreabilidade formal.  |
| Política de Revisão Periódica de Risco          | ✅ Sim        | Toda a organização                       | Frequência mínima (ex: 6 meses); triggers obrigatórios; documentação obrigatória.    |
| Política de Rastreabilidade de Decisões         | ⚠️ Opcional  | Organizações com exigências de auditoria | Versionamento; ligação com arquitetura, requisitos e controlos de segurança.         |

> 🔗 Ver também: [Políticas Organizacionais Relevantes](/sbd-toe/sbd-manual/classificacao-aplicacoes/policies-relevantes)
> 📌 Ver detalhes no anexo de políticas do manual.
