---
id: matriz-controlos-por-risco
title: Matriz de Controlos Mínimos por Nível de Risco
sidebar_position: 5
tags: [tipo:matriz, risco, controlos, proporcionalidade]
---

<!--template: sbdtoe-core -->

# 📊 Matriz de Controlos Mínimos por Nível de Risco

Esta matriz define o **patamar mínimo de controlos de segurança esperados**, por domínio técnico, em função do **nível de risco da aplicação (L1–L3)**, conforme determinado no Capítulo 01.

Os controlos aqui indicados constituem uma **baseline obrigatória** para cada nível de risco e devem ser entendidos como **mínimos exigíveis**, não como um limite máximo de aplicação.

A matriz pode ser usada:
- como referência técnica independente;
- como base para critérios de release;
- como input para modelos de aceitação de risco;
- como instrumento de controlo, auditoria ou KPI organizacional.

---

## 🧠 Enquadramento normativo

No *Security by Design – Theory of Everything (SbD-ToE)*, o nível de risco da aplicação determina **o grau mínimo de rigor** esperado na aplicação de controlos de segurança.

Contudo:

- o nível **L1–L3** resulta de uma **projeção simplificada** do risco (modelo E/D/I);
- os **atributos do risco** (detetabilidade, evidenciabilidade, reprodutibilidade, delegação, impacto real) podem exigir **reforços adicionais**;
- a ausência de evidência adequada **invalida a aplicação efetiva do controlo**, mesmo que este esteja “previsto”.

Esta matriz deve, por isso, ser aplicada **em conjunto** com:
- o modelo de classificação de risco;
- os critérios de aceitação;
- a análise de risco residual;
- e o ciclo de vida do risco.

---

## 🛠️ Matriz de Controlos por Nível de Risco

| Domínio                          | Risco Baixo (L1)                              | Risco Médio (L2)                                           | Risco Elevado (L3)                                                      |
|----------------------------------|-----------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|
| Requisitos (Cap. 2)              | ASVS N1 (adaptado)                            | ASVS N2 + critérios formais                                 | ASVS N2/N3 completo + validação por segurança                            |
| Threat Modeling (Cap. 3)         | Informal ou omitido                           | Sessões colaborativas regulares                             | Formal com DFDs + STRIDE e registo                                       |
| Arquitetura Segura (Cap. 4)      | Padrões mínimos                               | Revisão técnica + zonas de confiança                        | Revisão formal + documentação de mitigação                               |
| Dependências (Cap. 5)            | `npm audit` / `dotnet list`                   | SCA com política de severidade                              | SCA automatizado + SBOM + alertas                                        |
| Desenvolvimento (Cap. 6)         | Linters + revisão básica                      | Guias + regras de PR específicas                            | Revisão obrigatória + práticas reforçadas de revisão segura              |
| CI/CD (Cap. 7)                   | Credenciais protegidas                        | Validação de ambientes e segredos                           | Proveniência, SLSA + controlos de integridade                            |
| IaC (Cap. 8)                     | Scripts revistos manualmente                  | Scanners (ex.: tfsec)                                       | Policies formais + enforcement obrigatório no pipeline                  |
| Containers (Cap. 9)              | Imagens fiáveis + updates                     | Hardening + scanning de imagem                              | Assinatura, política formal, proteção em runtime                          |
| Testes de Segurança (Cap. 10)    | Checklists manuais                            | SAST + DAST pontuais                                        | Fuzzing, regressão, DAST contínuo                                         |
| Deploy Seguro (Cap. 11)          | Checklist + reversibilidade básica            | Aprovação dupla + controlo de versões                       | Processo formal de validação de segurança                                 |
| Operações (Cap. 12)              | Logging local                                 | Alertas básicos + SIEM leve                                 | Integração com IRP + deteção em tempo real                                |
| Formação (Cap. 13)               | Sessão de onboarding breve                    | Formação anual + sessões práticas                           | Treino formal + avaliações periódicas                                    |
| Governança (Cap. 14)             | Cláusulas simples de segurança                | Templates com conformidade                                  | Requisitos por risco + validação antes do onboarding                     |

---

## ⚠️ Regra de reforço obrigatório de controlos

> ⚠️ **Nota normativa essencial**

Sempre que os **atributos do risco** indiquem:
- baixa detetabilidade;
- baixa evidenciabilidade;
- comportamento não determinístico;
- elevada delegação ou execução automática com impacto real  
  (incluindo automação avançada ou apoio à decisão),

devem ser aplicados **controlos equivalentes ao nível imediatamente superior**,  
**independentemente** da classificação L1–L3 inicialmente atribuída.

Esta regra aplica-se a qualquer tecnologia ou prática de desenvolvimento e **não depende da presença explícita de IA**.

---

## 🔄 Atualização e manutenção da matriz

Esta matriz deve ser:
- revista sempre que ocorram alterações relevantes no manual;
- ajustada ao contexto regulatório e organizacional;
- mantida coerente com as políticas internas de segurança e risco.

A sua utilização não dispensa:
- análise contextual;
- produção de evidência;
- registo formal das decisões tomadas.

---

## 📌 Nota final

Esta matriz **não define “o máximo a fazer”**,  
define **o mínimo aceitável** para cada nível de risco.

A segurança efetiva resulta da **aplicação consciente, evidenciável e proporcional** dos controlos —  
não da mera conformidade com uma tabela.

---

## 🔗 Ligações úteis

- [Capítulo 01 – Classificação da Criticidade Aplicacional](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Modelo de Classificação por Eixos (E/D/I)](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos)
- [Critérios para Aceitação de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/criterios-aceitacao-risco)
- [Análise de Risco Residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual)
