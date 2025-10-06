---
id: validacao-requisitos
title: Estratégias de Validação de Requisitos de Segurança
description: Formas recomendadas de testar e verificar requisitos definidos no catálogo
tags: [validação, requisitos, testes, evidência, ciclo de vida]
---

# ✅ Validação de Requisitos de Segurança {requisitos-seguranca:addon:validacao-requisitos}

## 🌟 Objetivo {requisitos-seguranca:addon:validacao-requisitos#objetivo}

Prescrever a forma de validar a aplicação dos **requisitos de segurança definidos no Capítulo 2**, com ênfase em mecanismos rastreáveis, contínuos e integráveis no ciclo de desenvolvimento.

A validação permite:

- Confirmar que os requisitos definidos foram **efetivamente aplicados**;
- Assegurar que os controlos estão **presentes, funcionais e eficazes**;
- Produzir **evidência verificável e auditável** da conformidade com os requisitos de segurança aplicacionais.

---

## 📌 Princípios orientadores {requisitos-seguranca:addon:validacao-requisitos#principios_orientadores}

A validação deve ser:

- **Sistemática**: associada a momentos bem definidos do ciclo de vida;
- **Proporcional ao risco**: validando com mais profundidade requisitos de maior criticidade;
- **Rastreável**: com ligação entre requisito, validação e resultado;
- **Repetível**: automatizável ou documentada de forma clara;
- **Independente**: sempre que possível, realizada por alguém fora da implementação direta.

---

## 🛠️ Como validar {requisitos-seguranca:addon:validacao-requisitos#como_validar}

A escolha do método depende do tipo de requisito e do momento em que é aplicado. Os métodos incluem:

### 1. Análise Estática (SAST) {requisitos-seguranca:addon:validacao-requisitos#1_analise_estatica_sast}

- Usada para requisitos que se traduzem em padrões de código, configurações ou estruturas previsíveis.
- Aplica-se durante o desenvolvimento e no pipeline de build.
- Deve abranger a verificação de:
  - presença de validações de entrada;
  - uso de bibliotecas aprovadas;
  - aplicação de controlos criptográficos mínimos;
  - controlo de fluxo de autenticação e autorização.
- Os resultados devem ser integrados com os identificadores de requisitos (ex: `SEC-L2-*`).

### 2. Análise Dinâmica (DAST) {requisitos-seguranca:addon:validacao-requisitos#2_analise_dinamica_dast}

- Aplica-se a requisitos que se manifestam na execução da aplicação.
- Deve ser usada em ambiente de teste ou pré-produção.
- Permite validar:
  - exposição de endpoints e headers;
  - comportamento perante entradas maliciosas;
  - ausência de erros ou divulgações indevidas;
  - resposta a falhas de autenticação ou autorizações mal configuradas.

### 3. Testes funcionais de segurança {requisitos-seguranca:addon:validacao-requisitos#3_testes_funcionais_de_seguranca}

- Complementam a análise dinâmica e verificam o comportamento do sistema com base nos critérios de aceitação de cada requisito.
- Devem incluir:
  - Verificação do comportamento esperado (positivo);
  - Exploração de comportamentos indevidos ou bypasses (negativo);
  - Cobertura de casos-limite, restrições e falhas previstas no requisito.

### 4. Revisão técnica estruturada {requisitos-seguranca:addon:validacao-requisitos#4_revisao_tecnica_estruturada}

- Realizada por analistas, arquitetos ou elementos da equipa de segurança.
- Foca-se em requisitos cujo controlo seja distribuído ou implícito (ex: segregação lógica, dependências, controlo de sessão).
- Deve ocorrer após marcos relevantes: release candidate, pull request crítico, auditoria interna.

### 5. Validação contínua em CI/CD {requisitos-seguranca:addon:validacao-requisitos#5_validacao_continua_em_cicd}

- Requisitos críticos e rastreáveis devem estar ligados a mecanismos de bloqueio na pipeline.
- Isso inclui:
  - Avaliações automáticas do código e da configuração;
  - Rejeição de builds que violem critérios mínimos (ex: falta de MFA, falta de logging, hardcoded secrets);
  - Revalidação dos requisitos com cada alteração de risco (ex: nova feature, nova integração).

---

## 📆 Quando validar {requisitos-seguranca:addon:validacao-requisitos#quando_validar}

| Fase SDLC               | Objetivo da validação                          | Método primário                        |
|-------------------------|-----------------------------------------------|----------------------------------------|
| Planeamento e definição | Confirmação da aplicabilidade dos requisitos  | Análise técnica + validação manual     |
| Desenvolvimento         | Detecção precoce de incumprimento             | SAST + revisão de código               |
| Testes                  | Verificação do comportamento previsto         | Testes funcionais + DAST               |
| Pré-release / entrega   | Validação de conformidade total               | Validação cruzada + CI/CD gates        |
| Produção / operação     | Monitorização contínua de requisitos ativos   | Revalidação, logging, alertas          |

---

## 🧬 Resultados esperados da validação {requisitos-seguranca:addon:validacao-requisitos#resultados_esperados_da_validacao}

Cada requisito validado deve gerar:

- **Evidência de execução** (relatório, log, artefacto de validação);
- **Resultado binário ou graduado** (ex: conforme / não conforme / parcial);
- **Ligação ao identificador do requisito** (ex: `SEC-L2-INPUT-VALID`);
- **Recomendação ou medida corretiva**, se necessário.

---

## 📎 Referências cruzadas {requisitos-seguranca:addon:validacao-requisitos#referencias_cruzadas}

Este documento complementa os seguintes artefactos do capítulo:

| Documento                             | Relação com a validação                    |
|--------------------------------------|--------------------------------------------|
| `addon/01-catalogo-requisitos.md`    | Define os requisitos a validar             |
| `addon/06-matriz-controlos-por-risco.md` | Aponta os requisitos por nível de risco |
| `canon/20-checklist-revisao.md`      | Checklist binário de verificação por projeto |

---

## 🔁 Melhoria contínua {requisitos-seguranca:addon:validacao-requisitos#melhoria_continua}

A validação de requisitos deve ser incorporada num ciclo de melhoria contínua, onde os métodos são:

- **Revistos com base em incidentes ou findings reais**;
- **Atualizados com novas técnicas** ou alterações ao catálogo;
- **Automatizados sempre que possível**, para reforçar a escalabilidade e cobertura;
- **Monitorizados com indicadores de conformidade** ao longo do tempo (ex: % requisitos validados por release).

---

> 📌 A validação eficaz transforma requisitos em proteção real.  
> Não basta definir — é preciso confirmar, medir, melhorar.
