---
description: Organização dos requisitos por domínio técnico e tipo de rastreio necessário
id: taxonomia-rastreabilidade
tags:
- ALM
- domínios
- dsomm
- rastreabilidade
- requisitos
- ssdf
- taxonomia
title: Taxonomia de Rastreabilidade de Requisitos
---


# 🏷️ Taxonomia e Rastreabilidade de Requisitos de Segurança

## 🌟 Objetivo

Estabelecer um modelo normalizado de identificação e rastreabilidade de requisitos de segurança aplicacionais, através da utilização de **tags estruturadas** que podem ser aplicadas em backlog, código, testes, pipelines e documentação instanciadas a cada aplicação.

Esta taxonomia permite:

- Assegurar a **ligação entre risco, requisito e controlo implementado**;
- Suportar a **automação da conformidade** e cobertura de requisitos;
- Tornar rastreável a presença (ou ausência) de requisitos ao longo do ciclo de vida.

---

## 🧱 Estrutura das tags

| Componente     | Significado                                              | Exemplo            |
|----------------|----------------------------------------------------------|--------------------|
| `SEC`          | Prefixo fixo que indica requisito de segurança           | `SEC`              |
| `Lx`           | Nível de risco (L1, L2, L3) da aplicação                 | `L2`               |
| `DOMINIO`      | Domínio técnico (alinhado com o catálogo de requisitos) | `AUT`, `VAL`       |
| `CODIGO`       | Código semântico ou abreviado do requisito              | `MFA`, `VALID`     |

> Exemplo completo: `SEC-L2-AUT-MFA`

---

## 📘 Domínios técnicos suportados

Os domínios seguem os temas definidos no catálogo de requisitos (`addon/catalogo-requisitos`):

| Domínio   | Categoria técnica associada                     |
|-----------|--------------------------------------------------|
| `AUT`     | Autenticação e gestão de identidade              |
| `ACC`     | Controlo de acesso e autorização                 |
| `VAL`     | Validação e sanitização de dados                 |
| `CFG`     | Configuração segura e gestão de parâmetros       |
| `LOG`     | Registo, auditoria e monitorização               |
| `API`     | Segurança de APIs e serviços externos            |
| `DST`     | Distribuição de artefactos e publicações         |
| `REQ`     | Definição e gestão de requisitos                 |
| `ERR`     | Gestão de erros e mensagens                      |
| `SES`     | Sessões e gestão de estado                       |
| `ENC`     | Dados sensíveis e criptografia                   |
| `INT`     | Integrações e trocas de mensagens                |
| `IDE`     | Ferramentas e ambientes de desenvolvimento       |

---

## 🛠️ Como aplicar

### 1. **Backlog (user stories, épicos, tasks)**

- Incluir a tag na descrição ou título da história:
  - Ex: `SEC-L2-AUT-MFA`
- Permite filtrar e identificar requisitos ativos por sprint, release ou projeto.

### 2. **Código-fonte**

- Inserir como comentário técnico:
  - `// SEC-L3-VAL-SQLI`
- Permite rastreabilidade via análise de código ou revisão manual.

### 3. **CI/CD pipelines**

- Usar tags como triggers para:
  - Validações automáticas;
  - Gates de conformidade;
  - Rejeição de builds não conformes.

### 4. **Casos de teste e QA**

- Associar a tag aos critérios de validação;
- Suporta cobertura de requisitos por teste e rastreabilidade de evidência.

### 5. **Documentação e arquitetura**

- Incluir tags em decisões, fluxos, modelos de controlo e justificacões técnicas;
- Essencial para revisões formais e auditorias.

---

## 🔍 Verificação e manutenção

- As tags devem ser **validadas periodicamente** contra:
  - O [catálogo](./catalogo-requisitos);
  - A [matriz de risco](./matriz-controlos-por-risco).

- A organização deve manter um registo com:
  - Requisitos aplicados e respetivos IDs;
  - Implementações técnicas associadas;
  - Validações executadas e evidência gerada;
  - [Exceções documentadas] (addon/gestao-excecoes`).

---

## 📈 Benefícios operacionais

- Redução da ambiguidade: cada controlo tem identificação única;
- Suporte à automação e ao DevSecOps: integração com pipelines, scanners e dashboards;
- Transparência: facilita reporting técnico e de gestão;
- Escalabilidade: modelo simples e aplicável a múltiplas equipas, produtos e ferramentas.

---

## 🧹 Diferença entre ID normativo e tag operacional

No [catálogo de requisitos] (./addon/catalogo-requisitos), cada requisito é identificado por um **ID normativo genérico**, como:

| ID normativo | Nome resumido                         |
|--------------|----------------------------------------|
| `AUT-001`    | MFA obrigatório                        |
| `VAL-002`    | Validação de parâmetros de entrada     |

Estes IDs servem para normalizar e referenciar requisitos de forma única em toda a organização.

> ⚠️ Contudo, **estes IDs não devem ser usados diretamente na implementação de projetos ou produtos.**

---

## 🏷️ Instanciação para aplicação concreta

Cada requisito aplicável deve ser **instanciado com base no nível de risco da aplicação (L1, L2 ou L3)**, originando uma **tag operacional rastreável**, seguindo o padrão `SEC-Lx-DOMINIO-CODIGO`.

---

### ✅ Exemplo completo de rastreabilidade

| Elemento               | Exemplo                                          |
|------------------------|--------------------------------------------------|
| ID no catálogo         | `AUT-001`                                        |
| Nome do requisito      | MFA obrigatório                                  |
| Aplicação              | Portal Exemplo                                   |
| Classificação de risco | L2 (risco médio)                                 |
| Tag operacional        | `SEC-L2-AUT-MFA`                                 |

> Esta tag é o identificador que deve ser usado nos elementos de ciclo de vida (backlog, código, testes, pipelines, evidência).

---

## 🤪 Benefícios da distinção

- Os **IDs normativos** garantem consistência, governança e manutenção do catálogo;
- As **tags instanciadas (`SEC-Lx-*`)** permitem rastrear e verificar a aplicação efetiva dos requisitos **em contexto real e proporcional ao risco**.

> 📌 A distinção entre ambos permite manter **governança centralizada** com **implementação descentralizada, rastreável e auditável**.

---

> 📌 A utilização sistemática desta taxonomia permite rastrear, validar e justificar a aplicação (ou exceção) de requisitos de forma auditável e escalável em qualquer projeto.
