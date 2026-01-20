---
id: criterios-aceitacao-risco
title: Critérios para Aceitação de Risco
sidebar_position: 3
tags: [tipo:criterios, aceitacao, excecao, rastreabilidade]
---

<!--template: sbdtoe-core -->

# 🛠️ Critérios para Aceitação de Risco

A aceitação formal de risco é uma etapa fundamental no processo de gestão de risco e deve ser suportada por **critérios claros, objetivos e documentados**.

No *Security by Design – Theory of Everything (SbD-ToE)*, aceitar risco **não significa ignorá-lo**, mas sim assumir explicitamente que, dadas as condições atuais, o risco residual é considerado tolerável para o nível de criticidade da aplicação.

Este ficheiro define os **critérios mínimos** para aceitação de risco, alinhados com o modelo SbD-ToE e com os níveis aplicacionais **L1–L3**.

---

## 🧠 Princípio fundamental

Um risco **só pode ser aceite** quando:

- os seus **atributos são compreendidos**;
- os **controlos aplicados são conhecidos e verificáveis**;
- existe **evidência suficiente** da sua eficácia;
- o impacto residual é **compatível com o nível da aplicação**.

Sempre que estes pressupostos não se verifiquem, a aceitação de risco **não é válida**, independentemente da urgência, custo ou maturidade da equipa.

---

## 📌 Parâmetros para avaliação

A decisão de aceitação de risco deve considerar, no mínimo:

- **Valor residual do risco** (após aplicação de controlos);
- **Nível de criticidade da aplicação** (L1, L2 ou L3);
- **Tipo de impacto associado** (negócio, legal, operacional, reputacional);
- **Confiança nos controlos existentes**, incluindo a sua verificabilidade;
- **Reversibilidade do impacto** ou capacidade de rollback;
- **Disponibilidade de planos de contingência**;
- **Evidência objetiva** que suporte a avaliação efetuada.

---

## ⚖️ Limiares de aceitação por nível

| Nível da aplicação         | Risco Residual Máximo Aceitável | Observações                                     |
| -------------------------- | ------------------------------- | ----------------------------------------------- |
| **L1** (baixa criticidade) | ≤ 9 (médio)                     | Aceitação informal possível                     |
| **L2** (média criticidade) | ≤ 6 (baixo a médio)             | Requer validação formal e registo               |
| **L3** (alta criticidade)  | ≤ 4 (baixo)                     | Exceção apenas com aprovação de gestor de risco |

> 📌 Estes limiares assumem **controlo efetivo e evidência adequada**.  
> A ausência de evidência invalida automaticamente a aceitação.

---

## 🧩 Condições adicionais em contextos de automação e apoio à decisão

A utilização de automação ou apoio à decisão (incluindo IA) **não invalida por si só** a aceitação de risco.

Contudo, a aceitação **fica condicionada** quando esses mecanismos alteram atributos relevantes do risco, nomeadamente:

- **reduzem a detetabilidade** de erros ou falhas;
- **diminuem a evidenciabilidade** das decisões;
- **introduzem não determinismo** relevante;
- **executam ações com impacto real** sem validação humana obrigatória.

### ❌ Situações em que a aceitação de risco **não é permitida**

Não é aceitável aceitar risco quando:

- decisões ou ações automatizadas com impacto real são aplicadas **sem revisão humana efetiva**;
- os resultados não são reprodutíveis ou não podem ser validados de forma independente;
- não existe evidência clara do funcionamento correto dos controlos;
- o impacto potencial é legal, regulatório ou reputacional significativo;
- o risco se enquadra em aplicação **L3** e depende exclusivamente de confiança implícita no mecanismo automatizado.

---

## 🧾 Exemplos de critérios formais de aceitação válidos

A aceitação pode ser considerada quando, cumulativamente:

- o risco residual é avaliado como **baixo** por pelo menos dois perfis independentes (ex.: AppSec + Product Owner);
- existem **controlos compensatórios** ativos e monitorizados;
- o impacto é **estritamente operacional interno** e existe plano de recuperação validado;
- a automação é **assistiva**, com validação humana obrigatória antes de qualquer efeito real;
- a decisão está **documentada**, com responsável identificado e **prazo de revisão definido**.

---

## 🏡 Processo recomendado de aceitação

1. **Identificação clara** do risco e dos seus atributos relevantes.
2. Validação dos controlos aplicados e da evidência disponível.
3. Avaliação do risco residual face aos limiares L1–L3.
4. Decisão formal de aceitação, rejeição ou mitigação adicional.
5. Registo da decisão, incluindo racional, responsável e data de revisão.
6. Reavaliação obrigatória sempre que ocorram alterações relevantes.

---

## 📌 Recomendações finais

- Formalizar uma **policy de aceitação de risco aplicacional**, com papéis e responsabilidades definidos.
- Integrar decisões de aceitação nos **artefactos de release e governação**.
- Registar riscos aceites num repositório com **visibilidade GRC**.
- Nunca aceitar risco **sem evidência suficiente**, independentemente do nível da aplicação.

> A aceitação de risco não é uma omissão de responsabilidade,  
> mas uma **decisão consciente, informada e rastreável**.
