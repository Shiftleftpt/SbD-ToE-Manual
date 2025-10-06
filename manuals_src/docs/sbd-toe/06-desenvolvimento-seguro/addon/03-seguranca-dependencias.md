---
id: seguranca-dependencias
title: Segurança de Dependências
sidebar_position: 3
description: Práticas de gestão e validação de dependências externas para garantir integridade, atualização e segurança no código
tags: [dependências, segurança, sbom, gestão, validação]
---

# 📦 Segurança de Dependências {desenvolvimento-seguro:addon:seguranca-dependencias}

> 💡 **Nota prática**:  
> Ferramentas como **Snyk**, **OWASP Dependency-Check**, **Sonatype**, **Xygeni**, entre outras, já permitem detetar **vulnerabilidades conhecidas (CVEs)** em bibliotecas e pacotes usados em tempo de build, execução ou testes.  
> Estas ferramentas são úteis para aplicar uma política de validação contínua e enforcement automático, mas **não substituem a análise crítica da equipa técnica** quanto à legitimidade, necessidade e atualidade das dependências utilizadas.

---

## 📌 Objetivos {desenvolvimento-seguro:addon:seguranca-dependencias#objetivos}

- Reduzir o risco de exploração via bibliotecas desatualizadas ou comprometidas.
- Garantir que todas as dependências têm justificação técnica e validação de segurança.
- Estabelecer um processo rastreável de aprovação e controlo de versões.
- Facilitar a automação de verificações (SCA) e bloqueios em CI/CD.
- Apoiar auditorias internas e externas com evidência de controlo técnico.

---

Este documento define os critérios mínimos para a utilização segura de dependências externas (e internas reutilizadas), garantindo que são:

- **Validadas quanto a vulnerabilidades conhecidas**
- **Legitimadas tecnicamente pela equipa**
- **Atualizadas e rastreáveis no tempo**

---

## 👥 Quem deve aplicar {desenvolvimento-seguro:addon:seguranca-dependencias#quem_deve_aplicar}

- **Desenvolvedores**: ao adicionar ou atualizar pacotes.
- **Tech leads / revisores técnicos**: ao aprovar PRs com alterações a `package.json`, `pom.xml`, `requirements.txt`, etc.
- **Equipa de segurança / AppSec**: ao definir listas permitidas ou regras de aprovação.

---

## ⏱️ Quando aplicar {desenvolvimento-seguro:addon:seguranca-dependencias#quando_aplicar}

- Sempre que for introduzida ou atualizada uma dependência.
- Periodicamente, por via automatizada (ex: nightly scans).
- Antes de cada release ou entrega a produção.
- Durante auditorias ou revisões de segurança.

---

## 🧱 Requisitos obrigatórios {desenvolvimento-seguro:addon:seguranca-dependencias#requisitos_obrigatorios}

1. **Validação de CVEs por SCA (Software Composition Analysis)**
   - Scans automáticos com alertas e relatórios por PR ou build.
   - Integração com CI/CD.

2. **Lista aprovada (allowlist) e política de exclusão (denylist)**
   - Evitar bibliotecas não auditadas, não mantidas, ou abandonadas.
   - Obrigatório para projetos com classificação L2/L3.

3. **Validação técnica explícita em PRs**
   - Justificação da inclusão.
   - Avaliação da manutenção da biblioteca e da sua origem.

4. **Atualização regular de pacotes**
   - Exigir atualização de pacotes obsoletos, vulneráveis ou deprecated.
   - Automatizar alertas por dependência com CVE conhecido não mitigado.

5. **Gestão diferenciada de dependências de runtime vs. dev/test**
   - Aplicar validação proporcional ao risco de exploração em produção.

---

## 🚨 Sinais de risco {desenvolvimento-seguro:addon:seguranca-dependencias#sinais_de_risco}

- Bibliotecas sem manutenção há mais de 1 ano.
- Pacotes com menos de 10 estrelas e nenhum release oficial.
- Scripts ou binários incluídos sem validação.
- Forks privados sem atualização de upstream.

---

## ✅ Como validar {desenvolvimento-seguro:addon:seguranca-dependencias#como_validar}

- Scans automatizados em cada commit/PR (`dependency-check`, `snyk test`, etc.).
- Aprovação manual de cada novo pacote.
- Gatilhos de bloqueio no pipeline por vulnerabilidade severa.
- Revisão do changelog e do repositório da dependência.

---

## 🧾 Como evidenciar {desenvolvimento-seguro:addon:seguranca-dependencias#como_evidenciar}

- Logs de execução dos scanners de dependências.
- Ficheiro `.approved-deps.yml` ou equivalente, versionado.
- Comentário no PR com a validação e justificativa da nova dependência.
- Histórico de atualização no repositório ou sistema de gestão de pacotes.

---

## 🔄 Ligação a outras práticas {desenvolvimento-seguro:addon:seguranca-dependencias#ligacao_a_outras_praticas}

| Tema                                    | Ficheiro associado               |
|-----------------------------------------|----------------------------------|
| Linters e validações no pipeline        | `addon/02-linters-validacoes.md` |
| Justificação de exceções                | `addon/05-excecoes-e-justificacoes.md` |
| Validação integrada na revisão de código| `addon/08-validacoes-codigo.md` |
| Rastreabilidade no código e PRs         | `addon/09-anotacoes-evidencia.md` |

---

> 📌 A inclusão de dependências inseguras é uma das causas mais comuns de compromissos aplicacionais.  
> O processo de validação deve ser sistemático, rastreável e bloqueante nos casos críticos.
