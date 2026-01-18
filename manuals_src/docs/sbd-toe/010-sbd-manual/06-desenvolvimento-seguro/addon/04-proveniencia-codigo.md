---
id: proveniencia-codigo
title: Origem e Proveniência do Código
description: Tratamento do código como artefacto de proveniência controlada no desenvolvimento seguro
---

# 🧬 Origem e Proveniência do Código

Durante muitos anos, o desenvolvimento seguro partiu de um pressuposto implícito:  
o código era escrito maioritariamente pela própria equipa, de forma deliberada e compreendida.

Esse pressuposto já não é válido.

Hoje, uma base de código típica resulta da combinação de:
- código escrito localmente;
- código reutilizado entre projetos;
- exemplos adaptados;
- transformações automáticas;
- sugestões e aceleração por ferramentas de apoio.

O resultado é que **o código passa a ter proveniência múltipla**, mesmo quando reside no mesmo repositório.

---

## Porque a proveniência importa

A proveniência do código não é uma questão filosófica; é uma questão de risco.

Sem compreensão clara da origem e contexto de um fragmento de código, surgem riscos como:
- uso inadvertido de padrões inseguros;
- introdução de dependências implícitas;
- incompatibilidades com decisões arquiteturais;
- conflitos com requisitos de segurança existentes;
- riscos legais ou de licenciamento.

Tratar código sem proveniência conhecida como “normal” é equivalente a aceitar uma dependência externa sem análise — algo que o SbD-ToE explicitamente rejeita.

---

## Código interno como supply chain interno

Este addon introduz um conceito-chave:

> **O código produzido internamente deve ser tratado como parte da supply chain interna.**

Tal como dependências externas:
- o código tem origem,
- contexto,
- histórico,
- e risco associado.

A diferença é apenas o perímetro de controlo, não a necessidade de validação.

Esta perspetiva cria coerência direta com o Capítulo 05 — Dependências e Supply Chain, sem duplicar os seus mecanismos.

---

## Proveniência não é autoria

É importante distinguir:
- **autoria**: quem escreveu o código;
- **proveniência**: em que contexto surgiu, com que pressupostos, e com que grau de compreensão.

Um fragmento de código pode ser:
- corretamente escrito,
- funcional,
- e ainda assim inadequado ao contexto onde é incorporado.

O desenvolvimento seguro preocupa-se com **adequação**, não apenas com correção sintática.

---

## Implicações práticas no desenvolvimento

Assumir proveniência implica que:
- código incorporado deve ser compreendido, não apenas testado;
- decisões de incorporação devem ser explícitas;
- exceções devem ser registadas quando o entendimento é parcial;
- a revisão humana passa a ser um mecanismo de governação, não apenas de qualidade.

Estas implicações refletem-se diretamente:
- nas regras de validação,
- nos gates do lifecycle,
- e na evidência exigida para aceitação.

---

## Encerramento

Ao tratar o código como artefacto de proveniência controlada, o desenvolvimento seguro deixa de depender da “qualidade média” das contribuições e passa a depender de **processos robustos e verificáveis**.

Este é o único modelo que escala quando o desenvolvimento se torna rápido, distribuído e assistido por tooling avançado.

---
