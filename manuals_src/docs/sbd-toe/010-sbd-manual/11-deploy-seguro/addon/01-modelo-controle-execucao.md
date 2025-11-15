---
id: 01-modelo-controle-execucao
title: Modelo de Controlo de Execução
description: Estratégia para garantir que todo o código executado em produção foi previamente validado e autorizado.
tags: [tipo:anexo, grupo:execucao, tema:pipeline, segurança, deploy]
---


# 🧠 Modelo de Controlo de Execução em Runtime

## 🌟 Objetivo

Garantir que a aplicação, após o deploy, **executa de forma segura, controlada e reversível**, através de mecanismos que permitem limitar impacto, reagir a falhas, ativar ou desativar funcionalidades e prevenir execuções perigosas em produção.

Estes controlos funcionam **durante a execução** da aplicação, complementando os testes pré-deploy e os controlos de CI/CD, sendo fundamentais para suportar:

- Reversibilidade e contenção de impacto;
- Monitorização ativa e capacidade de reação;
- Deploy progressivo e segurança em tempo real.

---

## 🧬 O que é controlo de execução

Controlo de execução refere-se a todos os mecanismos aplicáveis **em runtime** que permitem condicionar, bloquear, ajustar ou desligar funcionalidades da aplicação **sem novo deploy**.

São exemplos típicos:

| Tipo                     | Descrição                                                                                   | Exemplo prático                                       |
|--------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------|
| **Feature Toggle**       | Ativação ou desativação dinâmica de funcionalidades                                         | Lançar nova feature para 5% dos utilizadores          |
| **Circuit Breaker**      | Interrupção automática de chamadas externas em caso de falha repetida                      | Parar chamadas a API externa após 3 timeouts          |
| **Timeout / Quota**      | Limitação de tempo ou uso de recursos                                                       | Timeout de 2s para chamadas internas                  |
| **Kill Switch**          | Desligar funcionalidades em caso de incidente ou risco                                     | Desativar envio de notificações após anomalia         |
| **Runtime Guard**        | Verificação de pré-condições antes de executar lógica sensível                             | Verificar se token está assinado antes de usar        |

---

## 🛠️ Como aplicar

1. **Identificar pontos de risco ou controlo dinâmico** no código:
   - Chamadas externas, novas funcionalidades, operações críticas;

2. **Aplicar mecanismos de execução condicional**, com controlo externo:
   - Variáveis de ambiente, configuração centralizada, painéis de toggles;

3. **Incluir monitorização ativa** sobre os efeitos do controlo:
   - Métricas, alertas, logs de ativação/desativação, rastreio de falhas;

4. **Documentar fallback behavior** de cada controlo:
   - O que acontece se for ativado/desativado - impacto esperado;

5. **Testar periodicamente os mecanismos de controlo**:
   - Simular falhas, incidentes, carga, e validações de rollback.

---

## ✅ Boas práticas

- Usar **feature toggles com validade temporal** (ex: 30 dias);
- Documentar a lógica de cada controlo e garantir reversibilidade;
- Incluir **runtime guards para dados críticos** (ex: validação antes de executar);
- Tratar *circuit breakers* como medidas de segurança, não só de resiliência;
- Garantir que toggles e switches são **auditáveis e versionados**;
- Preferir **configuração centralizada e segura** (ex: HashiCorp Consul, AWS AppConfig);
- Validar se o código executado condiz com o ambiente (ex: staging ≠ produção).

---

## 📎 Referências cruzadas

| Documento / Capítulo               | Relação com este tema                              |
|------------------------------------|----------------------------------------------------|
| Cap. 07 – CI/CD Seguro             | Validação de ambientes e execução por pipeline     |
| Cap. 10 – Testes de Segurança      | Testes funcionais a toggles, guards e fallbacks    |
| Cap. 12 – Monitorização e Alertas  | Observabilidade de runtime e resposta a falhas     |
| SLSA L3/L4                         | Execução verificada, ambientes controlados         |
| NIST SSDF PR.AC-3                  | Controlo de execução autorizado                    |

---

> 🔐 O controlo de execução em runtime é um **elemento crítico de segurança operacional**, permitindo prevenir, conter ou mitigar o impacto de alterações sem requerer novo deploy - essencial para ambientes de alta criticidade e disponibilidade.
