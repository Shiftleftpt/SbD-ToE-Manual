---
id: mapeamento-threats-requisitos
title: Mapeamento de Ameaças para Requisitos de Segurança
description: Como ligar ameaças identificadas a requisitos formais definidos no Capítulo 2
tags: [mapeamento, requisitos, threats, stride, capitulo2, rastreabilidade]
---

# 🧩 Mapeamento de Ameaças para Requisitos de Segurança

## 🌟 Objetivo

Estabelecer uma abordagem sistemática para mapear ameaças identificadas no *Threat Modeling* com os **requisitos de segurança** definidos no Capítulo 2 do manual SbD-ToE, assegurando que:

- Cada ameaça origina pelo menos um requisito técnico ou organizacional;
- A derivação de requisitos é rastreável, auditável e documentada;
- A ligação entre ameaça → requisito → controlo está explícita.

---

## 🧭 Como mapear ameaças a requisitos

O mapeamento deve ser feito com base em identificadores únicos e formatos consistentes:

| Threat ID | Descrição da Ameaça                                | Requisito Gerado                             | Categoria Cap. 2       | Estado       |
| --------- | -------------------------------------------------- | -------------------------------------------- | ---------------------- | ------------ |
| TM-001    | JWT com `alg: none` permite falsificação de sessão | REQ-AUT-003: Assinatura JWT obrigatória      | Autenticação e Sessões | Mitigado     |
| TM-002    | Endpoint `/admin/config` acessível a todos         | REQ-AC-010: RBAC obrigatório por endpoint    | Controlo de Acesso     | Em validação |
| TM-003    | Claims excessivos no JWT expõem dados sensíveis    | REQ-DAT-005: Minimizar claims por contexto   | Privacidade e Dados    | Justificado  |
| TM-004    | Falta de logging de ações administrativas          | REQ-LOG-001: Logging estruturado obrigatório | Logging e Auditoria    | Em curso     |

> ⚠️ Cada linha do mapeamento deve estar documentada no repositório ou no ficheiro `mitigations.md`.

---

## ✅ Exemplos de requisitos derivados

| Categoria de Requisito (Cap. 2) | Tipo de ameaça típica                           | Exemplo de requisito derivado                                      |
| ------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------ |
| Autenticação e Sessões          | Reutilização de JWTs não expirados              | REQ-AUT-004: TTL máximo de 15min nos tokens                        |
| Controlo de Acesso              | Acesso não controlado a funções administrativas | REQ-AC-012: Verificação explícita de `role` no backend             |
| Privacidade e Dados             | Claims desnecessários em tokens                 | REQ-DAT-006: Scoping dinâmico de claims por operação               |
| Logging e Auditoria             | Ações sem registo estruturado                   | REQ-LOG-002: Registo de todas ações sensíveis com ID de utilizador |
| Proteção contra DoS             | Abuse de endpoints públicos (ex: `/login`)      | REQ-DOS-001: Rate limiting + CAPTCHA                               |

---

## 🔗 Integração com o processo de validação

Durante a fase de validação de segurança de cada projeto, este mapeamento deve ser usado para:

- Confirmar se cada ameaça identificada tem uma resposta (requisito ou justificação);
- Verificar se o requisito está implementado, testado ou em exceção formal;
- Rastrear a origem do requisito (de onde surgiu a necessidade real).

---

## 📁 Organização sugerida

```
📁 threat-model/
├── threats.yaml        # Lista de ameaças com threat_id, descrição, requisito associado
├── requisitos.yaml     # Requisitos com id, descrição, categoria, estado
└── mitigations.md      # Estado e histórico das decisões de segurança
```

---

## ✅ Boas práticas

- Utilizar sempre identificadores únicos e rastreáveis (ex: `TM-001`, `REQ-AC-010`);
- Garantir consistência entre os ficheiros `threats.yaml`, `requisitos.yaml` e `mitigations.md`;
- Atualizar o mapeamento sempre que novas ameaças forem introduzidas ou requisitos alterados;
- Usar o mapeamento como input obrigatório em validações de segurança e auditorias técnicas;
- Integrar este processo com ferramentas de ALM, CI/CD ou GRC sempre que possível.

---

## 📎 Referências cruzadas

| Documento                        | Relação com este ficheiro                            |
|----------------------------------|------------------------------------------------------|
| [threat-modeling-ci](./threat-modeling-ci) | Validação automatizada do modelo em pipelines CI/CD |
| [metodo base](./addon/metodologia-base)  | Princípios gerais de threat modeling no SbD-ToE     |

---

> Este mapeamento permite consolidar a ligação entre *análise de ameaças* e *exigências formais de segurança*, tornando o processo verificável, justificável e auditável.
