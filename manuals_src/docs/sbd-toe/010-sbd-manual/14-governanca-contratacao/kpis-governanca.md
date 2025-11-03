---
id: kpis-governanca
title: KPIs e Métricas de Governação
sidebar_position: 90
description: Indicadores operacionais e de maturidade aplicáveis à governação de segurança por projeto e organização
tags: [kpi, metricas, governance, maturidade, controlo, excecoes]
---


# 📊 KPIs de Governança e Visibilidade Organizacional

Este anexo consolida os **indicadores operacionais, técnicos e de processo** que permitem avaliar a aplicação efetiva do modelo SbD-ToE em contexto organizacional.
Inclui também indicadores de **formação obrigatória** para funções críticas, como definido no Cap. 13.

---

## 📅 1. KPIs operacionais (por projeto ou aplicação)

| Indicador                                                     | Fonte              | Tipo   |
| ------------------------------------------------------------- | ------------------ | ------ |
| % de requisitos aplicados conforme risco                      | Cap. 2 + matriz Lx | %      |
| % de exceções documentadas com owner e prazo                  | Cap. 14.1 + 14.5   | %      |
| % de projetos com rastreabilidade completa (risco → controlo) | Cap. 14.4          | %      |
| % de owners com formação SbD ativa (\<12 meses)                | Cap. 13 + Cap. 14  | %      |
| Tempo médio para mitigar findings críticos                    | Cap. 12            | Tempo  |
| Nº de findings críticos abertos por aplicação                 | Cap. 10 + 12       | Quant. |

---

## 🔁 2. KPIs de processo (organizacionais)

| Indicador                                               | Fonte             | Tipo |
| ------------------------------------------------------- | ----------------- | ---- |
| % de fornecedores com validação de segurança anual      | Cap. 14.3 + 14.6  | %    |
| % de contratos com cláusulas de segurança proporcionais | Cap. 14.2         | %    |
| % de exceções aprovadas formalmente                     | Cap. 14.1 + 14.5  | %    |
| % de reviewers e validadores com formação obrigatória   | Cap. 13 + Cap. 14 | %    |
| % de aplicações com owner de segurança atribuído        | Cap. 14.1         | %    |
| Cobertura da formação anual por função crítica          | Cap. 13           | %    |

---

## 📈 3. KPIs estratégicos (resumo executivo)

| Indicador                                       | Observação                     |
| ----------------------------------------------- | ------------------------------ |
| Índice médio de maturidade por domínio SbD-ToE  | Agregado por capítulo e função |
| % de projetos críticos sem cobertura total      | Alerta de risco                |
| Evolução trimestral da cobertura SbD-ToE        | Por capítulo e unidade         |
| % de budget com segurança planeada desde início | Integração precoce             |
| % de relatórios com evidência rastreável        | Indicador de auditabilidade    |

---

## ✅ Recomendações

* Integrar os KPIs com dashboards (PowerBI, Grafana, Confluence);
* Associar cada indicador a owner e periodicidade de revisão;
* Usar como input para auditorias, GRC e melhoria contínua;
* Avaliar progressos trimestralmente e comunicar resultados;
* Validar se owners, reviewers e aprovadores têm formação SbD ativa.

---

## 🔗 Ligações cruzadas

* Cap. 1 + 2 — Fonte dos requisitos e risco por aplicação
* Cap. 13 — Formação e capacitação
* Cap. 14.1 a 14.6 — Onde os dados são registados
* Cap. 14.7 — Maturidade organizacional
