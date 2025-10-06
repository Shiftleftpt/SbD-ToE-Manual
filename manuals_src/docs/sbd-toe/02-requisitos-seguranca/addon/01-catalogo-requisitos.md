---
id: catalogo-requisitos
title: Catálogo de Requisitos Aplicacionais
description: Lista essencial de requisitos de segurança organizados por categoria e nível de risco
tags: [tipo:catalogo, tema:requisitos, rastreabilidade, criticidade, ASVS]
---

<!--template: sbdtoe-addon -->

# 🛠️ Catálogo de Requisitos Aplicacionais {requisitos-seguranca:addon:catalogo-requisitos}

O **catálogo de requisitos de segurança** é um dos pilares do modelo SbD-ToE, funcionando como referência estruturada para garantir que cada aplicação, projeto ou sistema adota controlos adequados ao seu nível de risco, tipologia e contexto operacional.

A existência de um catálogo formal permite:
- Garantir **proporcionalidade** das exigências (L1, L2, L3), evitando sobrecarga ou lacunas;
- Assegurar **rastreabilidade** entre risco, requisito, controlo e evidência;
- Integrar os requisitos de segurança nos processos de desenvolvimento, auditoria e manutenção;
- Servir de base comum para curadoria, evolução e adaptação organizacional.

Este catálogo foi consolidado a partir de múltiplas fontes reconhecidas (ASVS, MSTG, NIST SSDF, IEC 62443, BSIMM, entre outras) e destina-se a ser **adaptado e curado por cada organização ou projeto**, de modo a garantir alinhamento com o contexto e o estado da arte.

---

## 📌 Como aplicar este catálogo no SbD-ToE {requisitos-seguranca:addon:catalogo-requisitos#como_aplicar_este_catalogo_no_sbd_toe}

1. **Seleção proporcional**:  
   Cada requisito tem a indicação do(s) nível(is) de risco em que é obrigatório ou recomendado (L1, L2, L3).

2. **Curadoria contínua**:  
   Recomenda-se a revisão e adaptação periódica destes requisitos, acrescentando ou ajustando conforme o tipo de aplicação, ameaças emergentes e contexto do negócio.

3. **Integração operacional**:  
   O catálogo deve ser incorporado nos processos de backlog, definição de critérios de aceitação, testes e validação, bem como na documentação técnica e auditorias.

4. **Evolução e cobertura**:  
   Novos requisitos podem (e devem) ser acrescentados com base em lições aprendidas, incidentes, novos standards ou alterações de contexto.

---

<!--web-only-->
## 📚 Consulta rápida dos requisitos base {requisitos-seguranca:addon:catalogo-requisitos#consulta_rapida_dos_requisitos_base}

Consulte a aplicação proporcional dos requisitos por domínio técnico no  
[Catálogo Base de Requisitos (anexo deste capítulo)](xref:sbd-toe:toe:02-requisitos-seguranca:lista-requisitos-base):

- [AUT — Autenticação e Identidade](xref:cap02#aut) <!-- Precisa revisão manual -->
- [ACC — Controlo de Acesso](xref:cap02#acc) <!-- Precisa revisão manual -->
- [LOG — Registo e Monitorização](xref:sbd-toe:toe:02-requisitos-seguranca:rationale-catalogo)
- [SES — Sessões e Estado](xref:cap02#ses) <!-- Precisa revisão manual -->
- [VAL — Validação de Dados](xref:sbd-toe:toe:01-classificacao-aplicacoes:avaliacao-semiquantitativa)
- [ERR — Gestão de Erros](xref:sbd-toe:toe:03-threat-modeling:metodologias-e-ferramentas)
- [CFG — Configuração Segura](xref:cap02#cfg) <!-- Precisa revisão manual -->
- [API — Segurança de APIs](xref:sbd-toe:toe:capitulos-basilares:capitulos-basilares)
- [INT — Mensagens e Integrações](xref:sbd-toe:toe:intro:intro)
- [REQ — Definição de Requisitos](xref:sbd-toe:toe:02-requisitos-seguranca:aplicacao-lifecycle)
- [DST — Distribuição de Artefactos](xref:cap02#dst) <!-- Precisa revisão manual -->
- [IDE — Ferramentas de Desenvolvimento](xref:sbd-toe:toe:06-desenvolvimento-seguro:guidelines-equipa)
<!--end-web-only-->

<!--print-only-->
Para consulta rápida da aplicação proporcional dos requisitos por nível de risco, ver o anexo “Catálogo Base de Requisitos” no final deste capítulo.
<!--end-print-only-->

---

## 📖 Fontes e referências principais {requisitos-seguranca:addon:catalogo-requisitos#fontes_e_referencias_principais}

- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/) <!-- Precisa revisão manual -->
- [OWASP Mobile Security Testing Guide (MSTG)](https://owasp.org/www-project-mobile-security-testing-guide/) <!-- Precisa revisão manual -->
- [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/publications/detail/sp/800-218/final) <!-- Precisa revisão manual -->
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) <!-- Precisa revisão manual -->
- [IEC 62443 — Segurança em Sistemas Industriais](https://webstore.iec.ch/publication/7033) <!-- Precisa revisão manual -->
- [BSIMM — Building Security In Maturity Model](https://www.bsimm.com/) <!-- Precisa revisão manual -->
- [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/) <!-- Precisa revisão manual -->

---

## 📌 Nota Final {requisitos-seguranca:addon:catalogo-requisitos#nota_final}

O catálogo deve ser entendido como **referência viva e adaptável** — ponto de partida para a definição dos requisitos concretos de cada organização ou projeto, e para a integração efetiva da segurança em todo o ciclo de vida do software.

> Para validação, critérios de aceitação e evidências, consultar a secção de [validação de requisitos](xref:sbd-toe:toe:02-requisitos-seguranca:validacao-requisitos).
