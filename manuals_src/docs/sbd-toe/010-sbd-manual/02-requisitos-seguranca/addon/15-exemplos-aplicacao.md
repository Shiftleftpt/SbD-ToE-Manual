---
description: Estudo de caso que ilustra a aplicação dos requisitos ao longo do ciclo
  de vida
id: exemplos-aplicacao
tags:
- aplicação
- ciclo-vida
- exemplos
- rastreabilidade
- requisitos
- validacao
- validação
title: Exemplo Prático de Aplicação de Requisitos
---


# Exemplos de Aplicação de Requisitos de Segurança

Este anexo ilustra, de forma prática, como aplicar os requisitos de segurança ao longo do ciclo de vida de uma nova funcionalidade, com base na classificação de risco da aplicação.

> ℹ️ Este documento apresenta um **exemplo prático completo** da aplicação dos requisitos de segurança definidos no Capítulo 2, demonstrando como aplicá-los a uma nova funcionalidade ao longo do ciclo de vida do desenvolvimento.  
> Não se trata de um documento prescritivo, mas sim de um **estudo de caso reutilizável** que segue a lógica:  
> **classificação → seleção → rastreabilidade → validação**.  
> Pode ser adaptado e replicado noutros contextos, mantendo os princípios da proporcionalidade e da rastreabilidade.

## Cenário: Nova funcionalidade de upload de documentos numa aplicação web B2B

### 🧩 1. Contexto

- Aplicação: Portal web de gestão de contratos
- Tipo: Aplicação web com autenticação federada
- Dados: Contratuais e pessoais (alguns sensíveis)
- Classificação: Nível 2 (risco médio), conforme Capítulo 1
- Nova funcionalidade: Permitir upload de documentos PDF por utilizadores autenticados

---

### 🔎 2. Revisão da classificação de risco

Antes de definir requisitos, a equipa revê a classificação da aplicação à luz da nova funcionalidade:

| Fator                          | Alteração com a nova feature         |
|-------------------------------|--------------------------------------|
| Superfície de exposição       | ↑ Upload direto de utilizador final |
| Sensibilidade dos dados       | ↔ Igual (dados já eram sensíveis)    |
| Dependência de terceiros      | ↔ Sem alterações                     |

**Decisão**: Mantém-se como Nível 2, mas a exposição aumenta.

---

### 📝 3. Identificação dos requisitos relevantes

Com base nos temas do catálogo (Cap. 2) e nos domínios impactados pela feature (input, ficheiros, autenticação, registos), são selecionados os seguintes requisitos:

| ID       | Descrição                                                                 | Tema                            |
|----------|---------------------------------------------------------------------------|---------------------------------|
| REQ-003  | Sessões com timeout de 15 minutos de inatividade                          | Sessões e Estado                |
| REQ-010  | Validação de tipo, extensão e tamanho no upload de ficheiros             | Validação de Input e Output     |
| REQ-011  | Análise de malware antes do armazenamento de ficheiros                   | Antivírus e Malware             |
| REQ-015  | Logging de tentativas de upload e erros associados                        | Registo e Auditoria             |
| REQ-018  | Criação de testes automáticos para inputs malformados no endpoint de API | Testes de Segurança             |

---

### 🔗 4. Rastreabilidade (risco → requisito → controlo → validação)

| Risco identificado                          | Requisito | Controlo implementado                       | Validação                     |
|--------------------------------------------|-----------|----------------------------------------------|-------------------------------|
| Upload de ficheiros maliciosos             | REQ-011   | Integração com antivírus no pipeline         | CI/CD com scan automático     |
| Abuso do endpoint com ficheiros grandes    | REQ-010   | Limite de 10 MB + verificação de MIME type   | Teste funcional + logs        |
| Sessões abusivamente longas                | REQ-003   | Timeout de 15 min com reautenticação         | Teste de UI + script Selenium |
| Falta de visibilidade sobre ações críticas | REQ-015   | Logging com nível de alerta e centralização  | Revisão de logs + alertas     |

---

### 👥 5. Papéis envolvidos

| Papel                 | Contributo                                  |
|----------------------|---------------------------------------------|
| Dev Team             | Integração dos controlos nos endpoints/API  |
| QA/Testes            | Escrita dos testes automatizados            |
| Segurança (AppSec)   | Validação de requisitos e rastreabilidade   |
| Product Owner        | Inclusão dos critérios no backlog e user stories |

---

### 📆 6. Ponto de verificação no ciclo de vida

- Os requisitos foram incluídos nas **histórias de utilizador**
- Os critérios de aceitação foram definidos em Gherkin
- Os testes foram validados na fase de integração contínua (CI)
- A validação da rastreabilidade foi feita durante a sprint review com apoio de segurança

---

## Conclusão

Este exemplo demonstra a aplicação prática dos requisitos de segurança desde a identificação do risco até à validação técnica, garantindo rastreabilidade, proporcionalidade e integração com os processos de desenvolvimento ágil.

> Este mesmo processo pode ser reutilizado noutros casos com adaptações mínimas, desde que se mantenha a lógica: **classificação → seleção → rastreabilidade → validação**.
