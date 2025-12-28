---
id: 02-historia
title: História e Justificação
description: Porque é que a segurança nunca vive num único capítulo
sidebar_label: 2️⃣ História e Justificação
sidebar_position: 3
ai_generated: false
---

# A História dos Cross-Cutting Concerns no SbD-ToE

## Porque a segurança nunca vive num único capítulo

Durante muito tempo, a engenharia de software foi ensinada como uma linha reta. Primeiro analisava‑se, depois desenhava‑se, a seguir programava‑se, testava‑se no fim e, algures, alguém "tratava da segurança". Cada fase tinha o seu lugar. Cada problema tinha o seu capítulo.

Essa narrativa foi confortável. Simples. E, durante algum tempo, suficientemente eficaz.

Mas o software que hoje construímos já não cabe nessa história.

---

## A Complexidade Real do Software Moderno

Hoje, o software nasce de **sistemas sociotécnicos complexos**:

- Pessoas e equipas distribuídas
- Automação contínua em pipelines
- Cadeias de dependências globais
- Plataformas cloud e serviços externos
- **Assistência inteligente integrada no próprio ato de desenvolver**

As decisões deixaram de estar concentradas num momento ou numa pessoa. **Estão espalhadas**.

E quando as decisões se espalham, a segurança deixa de poder ser local.

---

## Quando a segurança aparece nas interseções

Na prática, os problemas mais sérios de segurança raramente surgem porque "faltou um capítulo". Surgem porque algo **atravessou vários capítulos** sem nunca ser verdadeiramente assumido por nenhum.

### Exemplos do quotidiano

- Um **segredo que apareceu num log**
  - Não é apenas um problema de desenvolvimento (código)
  - É também um problema de arquitetura (onde fluem dados)
  - É um problema de operações (retenção de logs)
  - É um problema de processo (quem tem acesso aos logs)

- Um **pipeline com mais permissões do que devia**
  - Não é apenas um problema de CI/CD
  - É um problema de IAM (identidades técnicas)
  - É um problema de segregação de funções
  - É um problema de governação (quem aprova essas permissões)

- Uma **dependência introduzida "só para resolver isto rápido"**
  - Não pertence apenas a requirements ou código
  - Afeta supply chain, vulnerabilidades, compatibilidade
  - Afeta conformidade e auditoria

- Uma **decisão automatizada que ninguém se lembra de ter tomado**
  - Não é apenas um problema de automação
  - É um problema de rastreabilidade, responsabilidade, reversibilidade

Nada disto pertence exclusivamente a requisitos, código, testes ou operações. **Pertence às interseções.**

---

## Por que o SbD-ToE os torna explícitos

Quando estes concerns não são assumidos de forma explícita, acontece quase sempre uma de duas coisas:

1. **Cada equipa resolve o mesmo problema à sua maneira**
   - Inconsistência
   - Falta de padronização
   - Esforço duplicado

2. **Ou ninguém o resolve por completo**
   - Porque "isso devia estar noutro lado"
   - Porque "não é responsabilidade de quem está aqui"
   - Porque "não ficou explícito em nenhum checklist"

O SbD-ToE parte de uma ideia simples, mas exigente:

> **Aquilo que atravessa muitas decisões não pode viver escondido.**

Ao tornar estes concerns explícitos, o manual não acrescenta burocracia. **Remove ambiguidade.**

---

## Uma viagem pelos concerns que atravessam tudo

### 🎯 O risco como narrativa contínua

No SbD-ToE, o risco não é um formulário inicial. É uma conversa permanente entre intenção e realidade.

O risco decide:
- Quanta validação é necessária
- Quanta evidência é exigida
- Quanta governação faz sentido

E, crucialmente, o risco não pertence apenas ao que o software faz — **pertence também a como é construído**.

### 📋 Requisitos como promessas

Os requisitos de segurança, vistos de fora, parecem listas. Vistos por dentro, são **promessas**.

Promessas de que:
- Certos limites não serão ultrapassados
- Certas decisões terão sempre validação
- Certos erros não escalarão silenciosamente

Quando tratados como concern transversal, os requisitos deixam de ser documentos estáticos e passam a ser **contratos vivos** entre equipas, tecnologia e organização.

### 🔐 Identidade e privilégio: quem pode fazer acontecer

À medida que a automação cresce, a pergunta muda subtilmente:

- Era: "Quem fez isto?"
- Tornou-se: "Quem tinha permissão para isto acontecer?"

Identidades humanas, contas técnicas, pipelines e agentes partilham o mesmo espaço de decisão. **Onde os privilégios são excessivos, os erros amplificam-se.**

### 💾 Dados: o ativo inquieto

Os dados raramente ficam quietos. Circulam por:
- Ambientes
- Logs
- Testes
- Integrações
- Fornecedores

Tratar dados como cross-cutting concern é aceitar que a segurança da informação não é um ponto de controlo isolado, mas uma **disciplina contínua de intenção e contenção**.

### 🔗 Supply chain: o software que não escrevemos

Grande parte do software moderno não é escrita por quem a mantém. **É composta.**

Dependências, imagens, ferramentas e código gerado entram no sistema trazendo consigo pressupostos invisíveis. A segurança da cadeia de fornecimento é, por isso, uma história que **atravessa todo o manual**.

### 📊 Evidência: a memória da segurança

Sem memória não há governação. Sem evidência não há confiança.

A rastreabilidade liga:
- Decisões a práticas
- Práticas a artefactos
- Artefactos a responsabilidades

É o que permite **aprender com o passado** e **justificar o presente**.

### ✂️ Separar para proteger

Os sistemas mais frágeis são aqueles onde a mesma entidade pode decidir, executar e aprovar.

A segregação de funções não nasce da desconfiança, mas do **reconhecimento dos limites humanos e técnicos**. Como concern transversal, **impede que erros isolados se tornem sistémicos**.

### ⚙️ Automação: decisões à velocidade da máquina

A automação não substitui decisões humanas — **executa-as à escala.**

Quando pipelines, scripts ou agentes passam a agir em nome das pessoas, a governação tem de acompanhar essa delegação. **Automação segura é automação consciente.**

### 🤝 Terceiros: confiança por extensão

Cada serviço externo é uma **extensão implícita do sistema**. Cada fornecedor transporta riscos, pressupostos e dependências.

Gerir terceiros como concern transversal é aceitar que a **fronteira do sistema é difusa** e que a confiança precisa de ser continuamente renovada.

### 👥 Pessoas: o elo que nunca desaparece

No fim, nenhum modelo sobrevive sem pessoas capazes de o aplicar.

Formação, competência e consciência não são notas de rodapé. São o **tecido que liga todos os outros concerns** e que permite que a segurança seja sustentável ao longo do tempo.

---

## O que esta história muda

Ao assumir explicitamente os cross-cutting concerns, o SbD-ToE deixa de ser apenas um manual de práticas. Torna-se um **modelo de pensamento** sobre engenharia de software segura.

Um modelo onde:

> **A segurança não vive num capítulo, mas na forma como os capítulos se ligam.**
