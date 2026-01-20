---
id: riscos-processo-arquitetura
title: Riscos de Processo na Arquitetura de Software
description: Identificação e mitigação dos riscos inerentes ao processo de decisão arquitetural
tags: [arquitetura, risco-processo, decisao, baseline, dependencias]
---

# 🛠️ Riscos de Processo na Arquitetura de Software

A arquitetura de um sistema é o resultado de um **conjunto de decisões técnicas** que determinam a sua estrutura, propriedades de segurança, capacidade de evolução e impacto operacional.

Independentemente do estilo arquitetural, tecnologia ou domínio, o **processo de decisão arquitetural** está sujeito a riscos próprios que, se não forem explicitamente tratados, comprometem a segurança do sistema entregue.

---

## 1. Arquitetura como desenho vs arquitetura como decisão

Um risco recorrente é tratar a arquitetura como um exercício de desenho técnico (diagramas, caixas e setas), em vez de um processo decisional explícito.

Consequências típicas:
- ausência de responsáveis pelas decisões;
- impossibilidade de justificar trade-offs aceites;
- dificuldade em reavaliar decisões quando o contexto muda.

No SbD-ToE, **arquitetura é decisão**, e deve ser tratada como tal.

---

## 2. Decisões arquiteturais sem responsável explícito

Decisões arquiteturais sem *owner* claro introduzem:
- ambiguidade de responsabilidade;
- dificuldade de auditoria;
- risco de deriva arquitetural ao longo do tempo.

Toda a decisão arquitetural relevante deve ter um responsável identificado e uma data/contexto de aprovação.

---

## 3. Dependências externas tratadas como infraestrutura neutra

Serviços externos, plataformas geridas, APIs de terceiros ou componentes fora do controlo direto da organização **são decisões arquiteturais**, não meros detalhes de implementação.

Riscos associados:
- dependência de terceiros como *single point of failure*;
- exposição de dados e metadados;
- limitações de controlo, auditoria e saída (*exit strategy*).

A aceitação de uma dependência externa deve ser tratada como **decisão arquitetural explícita**.

---

## 4. Fluxos de dados implícitos não modelados

Além dos fluxos funcionais explícitos, arquiteturas modernas geram fluxos implícitos, tais como:
- logs;
- métricas;
- telemetria;
- eventos e sinais de observabilidade.

Ignorar estes fluxos conduz a:
- exposição inadvertida de dados sensíveis;
- incumprimento de requisitos de retenção e minimização;
- lacunas na análise de ameaças.

Estes fluxos fazem parte da arquitetura e devem ser tratados como tal.

---

## 5. Componentes opacos ou não determinísticos

Componentes cujo comportamento:
- não é totalmente previsível,
- depende de estado externo,
- ou não é totalmente observável,

introduzem risco arquitetural adicional.

A arquitetura deve prever:
- contenção de impacto;
- validação de outputs críticos;
- mecanismos de degradação segura;
- observabilidade suficiente para detetar desvios.

---

## 6. Reutilização acrítica de arquiteturas anteriores

Reutilizar arquiteturas existentes é prática comum, mas torna-se arriscado quando:
- o contexto mudou;
- o perfil de risco é diferente;
- novas dependências ou fluxos foram introduzidos.

Arquiteturas herdadas devem ser tratadas como **hipóteses iniciais**, não como verdades validadas.

---

## 7. Divergência entre arquitetura documentada e arquitetura real

Quando a arquitetura documentada não reflete o sistema efetivamente implementado:
- decisões tornam-se inválidas;
- ameaças deixam de estar cobertas;
- a evidência perde valor.

Este risco exige mecanismos de revisão periódica e *gates* arquiteturais explícitos.

---

## 8. Implicações para o SbD-ToE

O SbD-ToE assume que:
- decisões arquiteturais são falíveis;
- riscos de processo arquitetural devem ser explicitamente tratados;
- mitigação exige decisão humana, validação e evidência verificável.

Os critérios de decisão e evidência são definidos no ficheiro de decisão arquitetural deste capítulo.
