---
id: intro
title: Governança & Contratação
description: Estruturas, políticas e práticas para assegurar governação organizacional, integração de fornecedores e transparência no ciclo SbD-ToE
tags: [governanca, contratacao, fornecedores, excecoes, rastreabilidade, conformidade, KPIs]
sidebar_position: 0
---
import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: CP1.1, SM1.3, CMVM3.3</Badge>
  <Badge color="info">SSDF: PO.1, PO.4, GV.1</Badge>
  <Badge color="info">SLSA: Nível 3 / 4</Badge>
  <Badge color="info">DSOMM: 3 / 3 (Governance)</Badge>
  <a href="./achievable-maturity" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver análise de maturidade</a>
</div>

:::note Capítulo Organizacional
Este capítulo é considerado **organizacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **assegurar a adoção, governação e evolução sustentável** das práticas de segurança definidas nos capítulos basilares e operacionais.  

Os capítulos organizacionais estabelecem a estrutura humana e processual que permite consolidar o SbD-ToE na organização, incluindo:
- **Formação, sensibilização e capacitação contínua** (Cap. 13)  
- **Governança, contratação e controlo executivo** (Cap. 14)  

Sem estes elementos, a segurança por design torna-se pontual e dependente de indivíduos, perdendo a **consistência e resiliência organizacional** necessárias à maturidade de longo prazo.
:::


# Governança & Contratação

Este capítulo assume um papel **excecional** no SbD-ToE. Enquanto capítulos anteriores prescrevem práticas técnicas, aqui define-se **como estas práticas se tornam visíveis, auditáveis e governadas** ao nível organizacional.  

Fornece a estrutura para **unificar esforços dispersos** de equipas técnicas, garantindo que a segurança é vista e controlada pela organização, e introduz mecanismos de **exceções formais**, **cláusulas contratuais** e **KPIs**, que transformam segurança de um exercício local em um **sistema de governação e responsabilização corporativa**, através de:

- Definição de **modelos de governação** para segurança.  
- Processo formal de **gestão de exceções** com registo e aprovação.  
- Integração de **cláusulas contratuais de segurança** em procurement e outsourcing.  
- **Validação contínua de fornecedores** (auditorias, due diligence).  
- **Rastreabilidade organizacional**: visão consolidada de práticas por projeto.  
- Definição e recolha de **KPIs de governação** (exceções, incidentes, cobertura formativa, etc.).  

👉 É este capítulo que permite responder à pergunta crítica: *“A organização consegue demonstrar, com evidência, o que está a ser feito em segurança por todas as equipas e fornecedores?”*
---

## 🧪 2. Prescrição prática

- **O que fazer:**  
  - Criar modelo formal de governação de segurança.  
  - Estabelecer fluxo de exceções e aceitação de risco.  
  - Integrar cláusulas contratuais de SbD-ToE em fornecedores.  
  - Definir auditorias e validações de terceiros.  
  - Recolher e reportar KPIs de governação.  

- **Como fazer:**  
  - Documentos aprovados por direção.  
  - Ferramenta de GRC para rastrear exceções e métricas.  
  - Integração com jurídico/procurement em novos contratos.  
  - Reporting periódico à gestão.  

- **Quando:**  
  - Em todos os novos projetos e contratações.  
  - Sempre que há exceções aos controlos prescritos.  
  - Em ciclos trimestrais de governação.  

- **Porquê:**  
  - Transformar segurança em prática institucionalizada.  
  - Tornar visível e auditável o estado de adoção.  
  - Garantir conformidade normativa (ISO 27001, NIS2, SSDF).  

---

## 👥 Papéis envolvidos

- **Dev** → regista exceções e aplica práticas acordadas.  
- **AppSec** → valida exceções, supervisiona rastreabilidade.  
- **DevOps/SRE** → garante aplicação prática em pipelines e deploy.  
- **Gestão/PMO** → aprova risco residual e governa adoção.  
- **Jurídico/Procurement** → integra cláusulas de segurança em contratos.  
- **GRC/Conformidade** → recolhe evidências, gere métricas e auditorias.  

👉 Cada papel tem **user stories associadas** no `aplicacao-lifecycle.md`.

---

## 🔗 Integração no ciclo

A governação atua como camada **horizontal** que abrange todo o ciclo SbD-ToE:  
- **Planeamento:** definição de cláusulas, políticas e métricas.  
- **Execução:** registo de exceções, integração em contratos, reporting contínuo.  
- **Validação:** auditorias a fornecedores, verificação de KPIs.  
- **Operações:** integração com incidentes e monitorização.  
- **Auditoria organizacional:** evidência consolidada de adoção por capítulo.  

---

## 📊 Rastreabilidade organizacional

- **Exceções registadas e aprovadas** em ferramenta de GRC.  
- **Cláusulas contratuais rastreadas** em contratos de fornecedores.  
- **KPIs consolidados** em dashboard organizacional (ex.: % de equipas com champions, nº de exceções aprovadas, tempo médio de resolução).  
- **Ligação a frameworks normativos** (ISO, NIS2, SSDF) assegura completude e conformidade.  

---

## 🏁 Conclusão

Este capítulo é o que **fecha o ciclo do SbD-ToE**:  
- Transforma práticas isoladas em **processo organizacional audítavel**.  
- Dá **visibilidade e transparência** à gestão.  
- Permite **medir eficácia** através de KPIs.  
- Integra segurança em **fornecedores e contratos**.  

👉 Sem este capítulo, o SbD-ToE fica limitado à prática técnica local.  
👉 Com ele, torna-se um **sistema de governação organizacional**, credível e sustentável.

---

## 📚 Alinhamento com frameworks

- **OWASP SAMM** → Governance & Strategy.  
- **BSIMM** → CP1.1, SM1.3, CMVM3.3.  
- **SSDF** → PO.1, PO.4, GV.1.  
- **SLSA** → Nível 3 / 4 (contratos e supply chain).  
- **DSOMM** → Governance.  

---

## 📜 Políticas Organizacionais Relevantes

| Política | Obrigatória? | Aplicação | Conteúdo mínimo |
|----------|--------------|-----------|-----------------|
| Política de Exceções de Segurança | Sim | AppSec + Gestão | Fluxo formal de pedido, aprovação e prazo |
| Política de Contratação Segura | Sim | Jurídico/Procurement | Cláusulas SbD-ToE, validação contínua |
| Política de Rastreabilidade Organizacional | Sim | GRC | Registo centralizado, dashboards |
| Política de Auditoria de Fornecedores | Recomendado | Procurement + AppSec | Auditorias periódicas de segurança |
| Política de KPIs de Governação | Sim | GRC + Direção | Métricas, relatórios, objetivos |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do manual**, onde estas políticas estão consolidadas transversalmente.

---
