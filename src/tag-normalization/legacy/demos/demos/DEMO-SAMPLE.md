---
id: demo-sample
title: "Demo Sample - Teste de Validação e Recomendação"
description: "Ficheiro de demonstração para testar o sistema de tags"
tags: [cicd, sbom, sast, dast, design, arquitetura]
sidebar_position: 999
---

# Demo Sample - Sistema de Tags

Este é um ficheiro de demonstração para testar o sistema de validação e recomendação de tags.

## Segurança em Arquitetura

A arquitetura segura é fundamental para qualquer aplicação. Precisa considerar:

- Threat modeling desde o início
- Análise de dependências (SBOM)
- Gestão de vulnerabilidades
- Compliance e regulamentações
- Testing de segurança (SAST, DAST)

## CI/CD Seguro

O pipeline de deployment deve incluir:

- Scanning automático de código
- Testing de segurança integrado
- Validação de containers
- Verificação de assinaturas
- Compliance checks

## Monitorização e Observabilidade

Em produção, precisamos:

- Logging centralizado
- Alertas de segurança
- Auditing de operações
- Métricas de conformidade
- Dashboards de observabilidade

## Relações Semânticas

O sistema vai detectar relações entre:
- `sbom` ↔ `sca`, `supply-chain`, `dependencias`
- `threat-model` ↔ `arquitetura`, `design`
- `testing` ↔ `sast`, `dast`, `cicd`
- `cicd` ↔ `deployment`, `pipeline`, `automacao`
