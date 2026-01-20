---
id: decisao-evidencia-arquitetural
title: Decisão e Evidência Arquitetural
description: Critérios de decisão, validação e evidência mínima para arquitetura segura
tags: [arquitetura, decisao, evidencia, adr, baseline]
---

# 🛠️ Decisão e Evidência Arquitetural

Uma arquitetura só é operacionalmente válida quando as suas decisões:
- são explícitas;
- têm responsável identificado;
- produzem evidência verificável;
- podem ser revistas ou invalidadas.

Diagramas ou descrições isoladas **não constituem decisão arquitetural**.

---

## 1. O que constitui uma decisão arquitetural

Uma decisão arquitetural é qualquer escolha técnica que:
- afete propriedades de segurança, isolamento ou confiança;
- introduza ou remova dependências externas;
- condicione requisitos de segurança ou mitigação de ameaças;
- seja dispendiosa ou difícil de reverter.

Detalhes puramente locais de implementação não constituem, por si só, decisões arquiteturais.

---

## 2. Critérios mínimos de aceitação de uma decisão

Uma decisão arquitetural é considerada válida quando, no mínimo:

- o contexto e o problema estão claramente descritos;
- as principais alternativas foram identificadas;
- a decisão tomada é explícita;
- os trade-offs aceites estão documentados;
- existe ligação a ameaças (Cap. 3) e requisitos (Cap. 2);
- há um responsável identificado pela decisão.

---

## 3. Evidência mínima obrigatória

A evidência associada a decisões arquiteturais deve incluir:

- registo de decisão (ex.: ADR ou equivalente);
- diagramas arquiteturais versionados;
- referência à versão do sistema/contexto;
- ligação a ameaças e requisitos relevantes;
- data e responsável pela aprovação.

A evidência deve ser:
- versionada;
- reproduzível;
- auditável.

---

## 4. Baseline arquitetural

O conjunto de decisões aprovadas constitui a **baseline arquitetural** do sistema.

A baseline:
- é válida apenas para o contexto/versionamento aprovado;
- serve de referência para desenvolvimento, testes e operação;
- deve ser facilmente identificável e consultável.

---

## 5. Invalidação e revisão de decisões

Uma decisão arquitetural deve ser revista ou invalidada quando ocorre:

- alteração significativa da arquitetura;
- introdução de novas dependências externas;
- mudança relevante nos fluxos de dados;
- reclassificação do nível de risco (L1–L3);
- identificação de novas ameaças críticas.

Decisões não revistas devem ser consideradas **potencialmente inválidas**.

---

## 6. Integração com outros capítulos

As decisões arquiteturais:
- materializam mitigação de ameaças identificadas no Cap. 3;
- justificam requisitos do Cap. 2;
- condicionam práticas de desenvolvimento, testes e operação.

A ausência de ligação explícita compromete a coerência do modelo SbD-ToE.
