---
id: riscos-processo-threat-modeling
title: Riscos de Processo no Threat Modeling
description: Identificação e tratamento dos riscos inerentes ao processo de Threat Modeling, independentemente do método utilizado
tags: [threat-modeling, risco-processo, decisao, validacao]
---

# 🛠️ Riscos de Processo no Threat Modeling

O Threat Modeling é um **processo de decisão estruturada** que visa identificar, analisar e priorizar ameaças relevantes para um sistema concreto, num determinado contexto.

Como qualquer processo decisional complexo, está sujeito a **riscos próprios**, independentes:
- do método utilizado (STRIDE, PASTA, LINDDUN, etc.),
- das ferramentas de apoio,
- da experiência individual dos participantes.

A não identificação explícita destes riscos compromete a fiabilidade do modelo de ameaças produzido.

---

## 1. Omissão estrutural de ameaças

Nem todas as ameaças relevantes são necessariamente identificadas durante uma sessão de Threat Modeling.

As omissões podem resultar de:
- limitações do método adotado;
- foco excessivo em componentes visíveis;
- desconhecimento de domínios adjacentes;
- reutilização acrítica de modelos anteriores.

A ausência de uma ameaça num modelo **não constitui evidência da sua inexistência**.

---

## 2. Enviesamento de perspetiva

O Threat Modeling reflete inevitavelmente as perspetivas, experiências e pressupostos dos participantes.

Riscos comuns incluem:
- subvalorização de ameaças fora do domínio técnico imediato;
- normalização de riscos conhecidos (“sempre foi assim”);
- sobrevalorização de cenários improváveis em detrimento de falhas sistémicas.

Este enviesamento deve ser assumido como **risco inerente**, não como falha excecional.

---

## 3. Confusão entre análise intermédia e decisão formal

Durante o processo são produzidos múltiplos artefactos intermédios:
- listas de ameaças potenciais;
- notas de sessão;
- diagramas exploratórios;
- hipóteses de ataque.

Estes artefactos **não constituem, por si só**, um modelo de ameaças aprovado.

A ausência de distinção clara entre:
- material de apoio,
- e decisão validada,

introduz ambiguidade e fragiliza a governação do risco.

---

## 4. Dependência acrítica de modelos prévios

A reutilização de modelos anteriores é prática comum e legítima, mas introduz riscos quando:
- o contexto mudou;
- a arquitetura evoluiu;
- novas dependências foram introduzidas;
- o perfil de risco foi alterado.

Modelos herdados devem ser tratados como **hipóteses de partida**, nunca como verdade validada.

---

## 5. Uso não controlado de informação sensível

O processo de Threat Modeling envolve frequentemente:
- diagramas arquiteturais detalhados;
- fluxos de dados sensíveis;
- decisões de mitigação críticas.

Estes artefactos constituem **ativos de alto valor**, sujeitos a requisitos de confidencialidade, controlo de acesso e retenção.

---

## 6. Resultados plausíveis mas incorretos

Um modelo de ameaças pode parecer:
- coerente,
- completo,
- tecnicamente bem articulado,

e ainda assim estar incorreto ou incompleto.

A plausibilidade não substitui validação, revisão e evidência.

---

## 7. Implicações para o SbD-ToE

O SbD-ToE assume explicitamente que:
- o Threat Modeling é um processo falível;
- os riscos de processo devem ser tratados de forma sistemática;
- a mitigação destes riscos exige validação humana, decisão explícita e evidência verificável.

Os controlos associados a estas exigências são definidos no ficheiro de validação e evidência deste capítulo.
