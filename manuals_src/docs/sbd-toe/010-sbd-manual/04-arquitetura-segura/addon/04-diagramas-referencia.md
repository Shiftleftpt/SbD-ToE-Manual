---
id: diagramas-referencia
title: 🧹 Modelos de Arquitetura Segura Reutilizáveis
description: Modelos prescritivos com ligação a requisitos (ARC), risco e ameaças mitigadas
sidebar_position: 4
---

# 🧹 Modelos de Arquitetura Segura Reutilizáveis

Este documento apresenta modelos de referência que podem ser usados como base segura para novos projetos.  
Cada modelo está associado a:

- Um **nível de risco típico** (L1, L2 ou L3)
- Os **requisitos ARC aplicáveis**
- As **ameaças mitigadas**
- Os ficheiros `.drawio` ou PlantUML sugeridos

---

## 🧱 Modelo 1 - Monólito Web com Backend Interno (Risco L1)

### 📝 Descrição

- Aplicação tradicional com backend interno e base de dados local
- Sem APIs públicas
- Acesso controlado via rede privada

### ✔️ Requisitos aplicáveis

- `ARC-001` (Zonas de confiança)
- `ARC-003` (Fluxos representados)
- `ARC-007` (Uso de padrão aprovado)

### 🔑 Ameaças mitigadas

- STRIDE: Tampering, Information Disclosure
- OSC&R: ARC-01, ARC-03

### 🖼️ Diagrama sugerido

```plaintext
[UI] --> [Web Server] --> [Database]
```

> ⚠️ Neste modelo, o controlo é garantido sobretudo pela **simplicidade** e **restrição de exposição**.

---

## ☁️ Modelo 2 - Microserviços com APIs Externas (Risco L2)

### 📝 Descrição

- APIs expostas via Gateway autenticado
- Microserviços com segmentação lógica
- mTLS na comunicação interna

### ✔️ Requisitos aplicáveis

- `ARC-001`, `ARC-002`, `ARC-003`, `ARC-004`, `ARC-005`, `ARC-006`
- `ARC-007`, `ARC-008`, `ARC-009`, `ARC-010`

### 🔑 Ameaças mitigadas

- STRIDE: Elevation of Privilege, Spoofing, Repudiation
- OSC&R: ARC-03, ARC-06, GOV-01

### 🖼️ Diagrama sugerido

```plaintext
[API Gateway] <--> [Service A] <--> [Service B] <--> [DB]
                      |
                 [Auth Service]
```

> ✅ Requer validação técnica formal (ARC-005) e revisão de threat modeling (ARC-010).

---

## 🧐 Modelo 3 - Plataforma Crítica Regulada (Risco L3)

### 📝 Descrição

- Aplicação sujeita a regulação (ex: saúde, financeiro)
- Controlo estrito de fronteiras
- Segmentação física e lógica (Kubernetes namespaces, DMZs)

### ✔️ Requisitos aplicáveis

- Todos os requisitos ARC-001 a ARC-011

### 🔑 Ameaças mitigadas

- STRIDE: Todas
- OSC&R: ARC-01, ARC-03, GOV-01, GOV-02

### 🖼️ Diagrama sugerido

```plaintext
[Client] --> [Web Gateway] --> [Frontend Pod]
                            --> [Backend Pod] --> [Data Services]
```

> ✅ Este modelo exige aplicação completa do capítulo, incluindo exceções formalizadas (ARC-011) e rastreabilidade integral (ARC-008).

---

## 📁 Sugestões de reutilização

- Disponibilizar modelos em `.drawio` ou `.puml` no repositório interno
- Atribuir owner técnico por modelo
- Validar anualmente e associar a projetos reais como referência

> Estes modelos não substituem o design específico de cada aplicação, mas constituem **padrões mínimos obrigatórios a validar** em função do nível de risco.

---
