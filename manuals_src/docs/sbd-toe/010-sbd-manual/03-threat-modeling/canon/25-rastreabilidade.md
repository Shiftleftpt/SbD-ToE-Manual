---
id: rastreabilidade
title: Rastreabilidade Top-Down – Capítulo 03
sidebar_position: 25
---

# 📎 Rastreabilidade contra Frameworks - Capítulo 03: Threat Modeling

Este ficheiro estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks de segurança relacionados com threat modeling e avaliação de ameaças aplicacionais.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre de forma sistemática os requisitos normativos e de maturidade técnica associados ao threat modeling.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                       | Prática do Capítulo 03 que responde                         | Nível de Cobertura |
|-------------------------------------------------------|--------------------------------------------------------------|--------------------|
| **NIST SSDF** – PW.2 (Threat Modeling)                | Metodologias de threat modeling sistemático                  | ✅ Completo         |
| **NIST SSDF** – PW.4 (Revisão de requisitos)          | Ligação explícita entre ameaças e requisitos (Addon 07)      | ✅ Parcial          |
| **OWASP SAMM v2.1** – Design → Threat Assessment      | Processo estruturado de threat modeling com integração contínua no SDLC | ✅ Nível 3          |
| **BSIMM13** – Architecture Analysis (AA1.1–AA1.3)     | Modelação contínua, estruturada e metodologias específicas (STRIDE, OCTAVE) | ✅ Nível 3          |
| **BSIMM13** – Architecture Analysis (AA2.1–AA2.2)     | Validação formal e documentada da segurança da arquitetura (Addon 09) | ✅ Completo         |
| **ISO/IEC 27034** – Application Security Control      | Validação formal e técnica da arquitetura resultante de TM   | ✅ Parcial          |
| **OWASP ASVS v5** – V1.1–V1.9 (Threat Modeling)       | Modelação de ameaças para derivação e validação de requisitos de segurança | ✅ Parcial          |
| **NIST SP 800-53** – SA-11 (Security Testing)         | Validação e teste contínuo baseado em modelos de ameaça      | ✅ Completo         |
| **NIST SP 800-53** – SA-17 (Architecture & Design)    | Modelação e validação contínua da arquitetura segura (Addon 09) | ✅ Completo         |
| **CIS Controls v8** – Control 16.8                    | Threat modeling formal e sistemático                         | ✅ Completo         |
| **ENISA DevSecOps** – Threat Modeling em CI/CD        | Integração contínua do TM em pipelines de desenvolvimento (Addon 06) | ✅ Completo         |
| **OWASP DSOMM** – Design & Development | Modelação de ameaças integrada no SDLC e rastreabilidade com controlos e requisitos | ✅ Completo |


---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

O capítulo cobre integralmente a prática PW.2, oferecendo:
- Metodologias sistemáticas documentadas
- Aplicação contínua ao longo do SDLC
- Evidências rastreáveis e auditáveis

A ligação explícita entre threat modeling e revisão de requisitos (PW.4) é parcialmente coberta pelo Addon 07, dependendo da articulação com o Capítulo 02.

---

### 🧱 OWASP SAMM v2.1

O capítulo atinge **nível 3** em *Threat Assessment*:
- Processo formal, estruturado e rastreável
- Aplicação contínua durante o ciclo de vida
- Metodologias técnicas alinhadas (ex.: STRIDE)

---

### 📊 BSIMM13

Cobertura total das práticas de análise da arquitetura contínua:
- AA1.1–AA1.3 (Modelação de ameaças estruturada)
- AA2.1–AA2.2 (Validação da arquitetura explícita)

Este nível corresponde ao nível mais elevado (nível 3 BSIMM), com práticas consistentes e rastreáveis documentadas no capítulo.

---

### 🏛️ ISO/IEC 27034

Cobertura parcial através da validação da arquitetura derivada de threat modeling:
- Validação explícita da arquitetura segura documentada no Addon 09
- Necessária integração com práticas adicionais do capítulo 04 (Arquitetura Segura)

---

### 🔐 OWASP ASVS v5

Cobertura parcial das práticas de threat modeling (V1.1–V1.9):
- Modelação técnica estruturada presente
- Depende da integração formal com requisitos do Capítulo 02 para uma cobertura completa.

---

### 📐 NIST SP 800-53

Cobertura integral dos requisitos:
- **SA-11**: validação contínua por threat modeling técnico e testes associados
- **SA-17**: validação formal e técnica da segurança da arquitetura

---

### 📘 CIS Controls v8

A prática (Control 16.8) é integralmente coberta:
- Processo formal, documentado e auditável
- Aplicação sistemática durante todo o SDLC

---

### 🔄 ENISA DevSecOps

Threat modeling aplicado explicitamente em pipelines CI/CD:
- Metodologia técnica contínua (Addon 06)
- Integração formal com validação técnica e documentação rastreável

---
### 🧱 OWASP DSOMM

O capítulo cobre diretamente o domínio **Design & Development**, através de:

- Integração contínua do threat modeling nas fases de design;
- Rastreabilidade entre ameaças, requisitos (Cap. 2) e controlos aplicados;
- Adoção de metodologias formais e ferramentas automatizadas (ex: IriusRisk).

**Cobertura adicional recomendada**:

- Referenciar a articulação do threat modeling como input do domínio *Risk Management* (por exemplo, via Catálogo de Riscos do Cap. 1);
- Reforçar a ligação com práticas de *Verification & Test*, evidenciada no Addon 09 e Cap. 4.
---

## 🔗 Ligações com outros capítulos

As práticas de threat modeling descritas no capítulo 03:

- Dependem diretamente da classificação de risco (Capítulo 01)
- São fundamentais para a definição e validação de requisitos de segurança (Capítulo 02)
- Suportam diretamente a validação de arquitetura segura (Capítulo 04)
- Integram-se formalmente com processos CI/CD (Capítulo 07)
- Estabelecem requisitos técnicos e validação contínua de testes (Capítulo 10)

> 📌 Esta rastreabilidade assegura que as práticas de threat modeling descritas neste capítulo **não são isoladas**, mas fornecem uma resposta técnica robusta e auditável aos principais frameworks e normas de segurança.
