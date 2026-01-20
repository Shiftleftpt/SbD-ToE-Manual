---
id: validacao-codigo
title: Validação de Código como Controlo de Risco de Processo
description: Porque a validação de código é um mecanismo central de controlo de risco no desenvolvimento moderno
---

# 🛠️ Validação de Código como Controlo de Risco de Processo

No desenvolvimento moderno, o principal risco já não reside apenas na **complexidade do código**, mas na **forma como esse código é introduzido no sistema**.

À medida que as equipas recorrem a reutilização extensiva, automação, geração assistida e refatorações frequentes, o ato de “escrever código” deixa de ser um processo exclusivamente deliberado e passa a ser, em muitos casos, um processo **mediado**, **acelerado** e **não linear**.

Neste contexto, a validação de código deixa de ser uma boa prática opcional e passa a desempenhar um papel central:  
**controlar o risco do processo de desenvolvimento**.

---

## Código não é confiança — é input

Um dos pressupostos fundamentais deste capítulo é simples, mas estrutural:

> **Código não é confiável por defeito, independentemente da sua origem.**

A origem do código — autoria humana, reutilização interna, bibliotecas externas ou ferramentas de apoio — não é um critério válido de confiança.  
O único fator que transforma código em artefacto aceitável é a **validação técnica adequada ao risco**.

Este princípio é coerente com o tratamento dado a:
- dependências externas (Cap. 5),
- decisões arquiteturais (Cap. 4),
- e requisitos de segurança (Cap. 2).

O desenvolvimento seguro estende essa lógica ao próprio código produzido internamente.

---

## Validação como processo, não como evento

Outro erro comum é tratar a validação como um **evento pontual** — tipicamente uma revisão final antes do merge.

No SbD-ToE, a validação é entendida como um **processo progressivo**, onde o código atravessa estados bem definidos, cada um reduzindo o risco introduzido:

1. **Código proposto**  
   Código ainda não compreendido nem validado, sujeito a erro plausível.

2. **Código revisto**  
   Código analisado por um humano com conhecimento técnico, mas ainda não validado empiricamente.

3. **Código validado**  
   Código sujeito a validações técnicas relevantes (testes, análise estática, verificações automáticas).

4. **Código aceite**  
   Código cuja incorporação é uma decisão explícita, assumida por um role identificável.

A ausência de qualquer uma destas transições **não é neutra**: representa risco não mitigado.

---

## Erro plausível: o maior inimigo do desenvolvimento seguro

Grande parte das vulnerabilidades modernas não resulta de código obviamente incorreto, mas de **erro plausível**:
- lógica que “faz sentido” mas falha em casos limite;
- suposições implícitas não documentadas;
- uso incorreto de APIs seguras;
- omissões subtis de validação ou controlo de erro.

Estes erros passam facilmente despercebidos quando:
- a revisão é superficial;
- a confiança na origem do código é excessiva;
- a validação empírica é insuficiente.

Por isso, a validação no desenvolvimento seguro não procura apenas *bugs*, mas **entendimento**.

---

## Evidência como critério de aceitação

No SbD-ToE, nenhuma validação existe sem evidência.

Aceitar código implica conseguir responder, a posteriori:
- quem reviu;
- que validações foram executadas;
- com que resultados;
- e com base em que critérios foi tomada a decisão.

Essa evidência não existe para “auditorias futuras”;  
existe para **disciplinar o processo presente** e reduzir erro sistémico.

---

## Ligação ao ciclo de vida

Este addon define o **racional técnico** da validação de código.  
A sua aplicação prática — gates, responsabilidades e artefactos — é descrita no `15-aplicacao-lifecycle.md` do capítulo.

A validação não substitui outras práticas do manual;  
funciona como **ponto de convergência** entre desenvolvimento, testes e governação.

---
