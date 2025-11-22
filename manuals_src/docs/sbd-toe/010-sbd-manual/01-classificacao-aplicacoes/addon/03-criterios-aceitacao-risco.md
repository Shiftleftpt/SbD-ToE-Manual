---
id: criterios-aceitacao-risco
title: Critérios para Aceitação de Risco
sidebar_position: 3
tags: [aceitacao, excecao, rastreabilidade, tipo:criterios]
---

<!--template: sbdtoe-core -->

# 🛠️ Critérios para Aceitação de Risco

A aceitação formal de risco é uma etapa fundamental no processo de gestão de risco, e deve ser suportada por **critérios claros, objetivos e documentados**. Estes critérios determinam quando um risco é considerado aceitável, com ou sem mitigação adicional.

Este ficheiro define um conjunto mínimo de critérios de aceitação de risco, adaptados ao modelo SbD-ToE e alinhados com os níveis de aplicação L1–L3.

---

## 📌 Parâmetros para avaliação

A decisão de aceitar um risco deve considerar:

* **Valor residual do risco** (pós-controlos)
* **Criticidade da aplicação** (L1, L2 ou L3)
* **Tipo de impacto associado** (negócio, legal, operacional, reputacional)
* **Confiança nos controlos existentes**
* **Reversibilidade ou impacto de falha**
* **Disponibilidade de planos de contingência**

---

## ⚖️ Limiares de aceitação por nível

| Nível da aplicação         | Risco Residual Máximo Aceitável | Observações                                     |
| -------------------------- | ------------------------------- | ----------------------------------------------- |
| **L1** (baixa criticidade) | ≤ 9 (médio)                     | Aceitação informal possível                     |
| **L2** (média criticidade) | ≤ 6 (baixo a médio)             | Requer validação formal e registo               |
| **L3** (alta criticidade)  | ≤ 4 (baixo)                     | Exceção apenas com aprovação de gestor de risco |

---

## 🧾 Exemplos de critérios formais de aceitação

* Risco residual avaliado como **baixo** por pelo menos dois perfis (ex: AppSec + PO).
* Controlos compensatórios estão em execução, embora não idealmente desenhados.
* Risco com impacto exclusivamente **operacional interno** e cobertura por DRP.
* Existência de workaround ou rollback eficaz validado.
* Decisão de aceitação devidamente **documentada e com prazo de revisão**.

---

## ❌ Critérios para rejeição ou mitigação obrigatória

* Risco residual **acima do limiar definido** para o nível da aplicação.
* Impacto potencial **legal ou regulatório** grave.
* Inexistência de planos de contingência ou rollback.
* Não conformidade com controlo obrigatório (ex: ASVS, NIST, ISO, RGPD).
* Ameaça altamente explorável com exposição real (ex: mapeada em ATT\&CK ou OSC\&R).

---

## 🏡 Processo recomendado de aceitação

1. **Identificação clara** do risco e do seu valor residual.
2. Validação dos controlos aplicados e da sua eficácia.
3. Aplicação dos limiares definidos por nível (L1–L3).
4. Documentação da decisão de aceitação (template ou GRC).
5. Revisão periódica e reavaliação obrigatória em caso de alteração substancial.

---

## 📌 Recomendações finais

* Formalizar uma **policy de aceitação de risco aplicacional**, com papéis e responsabilidades.
* Integrar decisão de aceitação nos **artefactos de release**.
* Registar riscos aceites num **repositório com visibilidade GRC**.
* Associar data de revisão, decisor e contexto organizacional da decisão.

> A aceitação de risco não é uma omissão de responsabilidade, mas uma **decisão consciente, formal e rastreável**.
