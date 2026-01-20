---
id: governanca-automatismos
title: Governação do Uso de Automatismos e Assistentes no SSDLC
description: Prescrição para o uso controlado de ferramentas de geração automatizada (incluindo IA) no desenvolvimento, sem alteração dos requisitos aplicacionais
tags: [governanca, automatizacao, ia, sdlc, requisitos, validacao, rastreabilidade]
---

# 🛠️ Governação do Uso de Automatismos no Desenvolvimento

Este anexo define **princípios, regras e obrigações mínimas** para o uso de **ferramentas de automatização e geração assistida** (incluindo assistentes baseados em IA, low-code/no-code e geração automática de código) no contexto do *Secure Software Development Lifecycle* (SSDLC).

O seu objetivo é **assegurar que a adoção destas ferramentas não compromete**:
- a validade dos **requisitos de segurança** definidos no Capítulo 2;
- a **rastreabilidade** entre risco, requisito, controlo e evidência;
- a **verificabilidade prática** e a responsabilização humana.

> ⚠️ Este anexo **não define novos requisitos aplicacionais** nem altera o catálogo T01–T20.  
> Define apenas **condições de governação e validação** para a correta aplicação dos requisitos existentes quando são usados automatismos.

---

## 🎯 Âmbito e enquadramento

Este anexo aplica-se sempre que, no processo de desenvolvimento, sejam utilizados:

- Assistentes de código baseados em IA (ex.: *code assistants*, *copilots*);
- Plataformas *low-code / no-code*;
- Ferramentas de geração automática de código, configurações ou testes;
- Automatismos que produzam *artefactos executáveis* ou logicamente relevantes.

Não se aplica:
- a sistemas cujo **produto final seja um sistema de IA** (ver manual SbD-AI-ToE);
- a ferramentas puramente informativas sem impacto no código, configuração ou lógica.

---

## 🧠 Princípios fundamentais (normativos)

As regras seguintes são **invariantes** no modelo SbD-ToE:

1. **A responsabilidade é sempre humana**  
   Nenhuma decisão técnica ou de segurança pode ser atribuída a uma ferramenta.

2. **Output automatizado não é evidência**  
   Código, testes ou configurações geradas automaticamente **não constituem evidência de cumprimento** de requisitos.

3. **Código gerado é tratado como código de terceiros**  
   Está sujeito às mesmas validações, revisões e controlos.

4. **A validação é obrigatória e explícita**  
   Todo o output relevante deve ser validado por mecanismos humanos e/ou automatizados.

5. **A rastreabilidade não é opcional**  
   A utilização de automatismos **não quebra nem simplifica** as exigências de rastreabilidade.

---

## 🔗 Impacto nos temas de requisitos existentes

O uso de automatismos **reforça** (não substitui) as obrigações nos seguintes temas do catálogo:

| Tema | Impacto específico |
|---|---|
| **T11 – Segurança do Código e Build** | Revisão humana obrigatória de código gerado |
| **T12 – Dependências e SBOM** | Identificação de dependências implícitas introduzidas |
| **T13 – CI/CD Seguro** | Gates automáticos tornam-se críticos |
| **T17 – Testes de Segurança** | Testes não podem assumir confiança implícita |
| **T20 – Governação e Conformidade** | Uso deve ser conhecido, autorizado e auditável |

> Estes impactos são operacionalizados no ficheiro `aplicacao-lifecycle.md` através de user stories e gates específicos.

---

## ⚙️ Regras mínimas de governação

### 1. Uso autorizado e conhecido
- A organização **deve saber** que ferramentas são usadas;
- O uso deve estar coberto por política interna (ver Cap. 14).

### 2. Proteção de informação
- É **proibido** introduzir segredos, chaves, dados sensíveis ou informação confidencial em prompts;
- A violação constitui incidente de segurança.

### 3. Revisão humana obrigatória
- Todo o código/configuração gerada deve ser:
  - revisto por um developer qualificado;
  - sujeito aos mesmos critérios de *code review*.

### 4. Validação técnica independente
- SAST, SCA, testes e validações **não podem ser desativados** por “confiança na ferramenta”.

### 5. Gestão de exceções
- Qualquer atalho ou não aplicação de controlo segue o **processo formal de exceções** do Capítulo 14, com TTL.

---

## 🧪 Evidência e auditoria

A evidência **não é o uso da ferramenta**, mas sim:

- Resultados de testes;
- Logs de pipelines CI/CD;
- Aprovações humanas documentadas;
- Rastreabilidade entre:
  - risco → requisito → controlo → validação.

Quando relevante, deve existir referência explícita de que **foi usado automatismo**, sem necessidade de detalhar prompts ou modelos.

---

## 📚 Alinhamento normativo e referências

Este anexo está alinhado com as seguintes referências:

- **NIST SP 800-218A** — Secure Software Development Framework Profile for GenAI  
- **NIST AI Risk Management Framework 1.0**  
- **ISO/IEC 42001:2023** — AI Management System  
- **OpenSSF – Secure Use of AI Code Assistants**

Estas referências **não criam novos requisitos aplicacionais**, mas reforçam princípios de governação, responsabilização e validação já existentes no SbD-ToE.

---

## 🧭 Relação com outros capítulos

- Capítulo 1 — Classificação de risco: o uso de automatismos **não altera L1–L3**;
- Capítulo 2 — Requisitos de Segurança: requisitos mantêm-se inalterados;
- Capítulo 7 — CI/CD Seguro: gates automáticos tornam-se críticos;
- Capítulo 14 — Governação e Exceções: políticas, formação e controlo formal.

---

## ✅ Conclusão

O SbD-ToE **compreende e aceita a IA como ferramenta poderosa**, mas rejeita qualquer modelo onde:
- a confiança substitua validação;
- a automação substitua responsabilidade;
- a conveniência comprometa evidência.

Este anexo assegura que a adoção de automatismos **reforça** — e nunca fragiliza — a aplicação rigorosa dos requisitos de segurança definidos neste manual.

