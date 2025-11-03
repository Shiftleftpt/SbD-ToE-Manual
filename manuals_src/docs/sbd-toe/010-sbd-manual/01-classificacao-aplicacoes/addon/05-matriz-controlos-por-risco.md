---
id: matriz-controlos-por-risco
title: Matriz de Controlos por Nível de Risco
sidebar_position: 5
tags: [tipo:matriz, risco, controlos, proporcionalidade]
---

<!--template: sbdtoe-core -->

# 📊 Matriz de Controlos por Nível de Risco

Esta tabela resume os controlos mínimos esperados por domínio técnico, de acordo com a classificação de risco da aplicação.

Pode ser usada como referência independente ou integrada em modelos de aceitação, critérios de release ou políticas internas.

## 🛠️ Tabela de Controlos por Risco

| Domínio                          | Risco Baixo                                   | Risco Médio                                                 | Risco Elevado                                                         |
|----------------------------------|-----------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------|
| Requisitos (Cap. 2)              | ASVS N1 (adaptado)                            | ASVS N2 + critérios formais                                 | ASVS N2/N3 completo + validação por segurança                         |
| Threat Modeling (Cap. 3)         | Informal ou omitido                           | Sessões colaborativas regulares                            | Formal com DFDs + STRIDE e registo                                    |
| Arquitetura Segura (Cap. 4)      | Padrões mínimos                               | Revisão técnica + zonas de confiança                        | Revisão formal + documentação de mitigação                           |
| Dependências (Cap. 5)            | `npm audit` / `dotnet list`                   | SCA com política de severidade                              | SCA automatizado + SBOM + alertas                                    |
| Desenvolvimento (Cap. 6)         | Linters + revisão básica                      | Guias + regras de PR específicas                            | Revisão obrigatória + pair programming seguro                         |
| CI/CD (Cap. 7)                   | Credenciais protegidas                        | Validação de ambientes e segredos                          | Proveniência, SLSA + integrity checks                                |
| IaC (Cap. 8)                     | Scripts revistos manualmente                  | Scanners (ex: tfsec)                                        | Policies + enforcement no pipeline                                   |
| *containers* (Cap. 9)             | Imagens fiáveis + updates                     | Hardening + scanning de imagem                             | Assinatura, política formal, proteção runtime                         |
| Testes de Segurança (Cap. 10)    | Checklists manuais                            | SAST + DAST pontuais                                       | Fuzzing, regressão, DAST contínuo                                     |
| Deploy Seguro (Cap. 11)          | Checklist + reversibilidade básica            | Aprovação dupla + controlo de versões                      | Processo formal de validação de segurança                             |
| Operações (Cap. 12)              | Logging local                                 | Alertas básicos + SIEM leve                                | Integração com IRP + deteção em tempo real                           |
| Formação (Cap. 13)               | Sessão de onboarding breve                    | Formação anual + sessões práticas                          | Treino formal + avaliações periódicas                                |
| Governança (Cap. 14)             | Cláusulas simples de segurança                | Templates com conformidade                                 | Requisitos por risco + validação antes do onboarding                  |

> ℹ️ Esta matriz está alinhada com o modelo descrito no Capítulo 1 e deve ser mantida atualizada com base nas políticas e contexto organizacional.

