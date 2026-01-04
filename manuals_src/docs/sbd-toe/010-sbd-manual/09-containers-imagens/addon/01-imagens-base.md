---
id: imagens-base
title: Imagens Base Seguras e Minimalistas
description: Seleção, reforço e validação de imagens base seguras para containers
tags: [containers, imagens base, hardening, runtime, supply chain]
---

# 🧱 Imagens Base Seguras e Minimalistas

## 🌟 Objetivo

Garantir que todas as aplicações, pipelines e serviços que utilizam containers **partem de imagens base seguras, controladas e minimizadas**, reduzindo a superfície de ataque e estabelecendo um **ponto de confiança explícito** na cadeia de execução.

Num contexto de SSDLC moderno, imagens base são frequentemente **selecionadas, herdadas ou reutilizadas automaticamente** por pipelines, templates ou geradores de código.  
Por isso, a sua escolha **não pode ser implícita nem tácita**: deve ser uma **decisão humana inicial**, suportada por validação técnica e sujeita a reavaliação periódica.

Uma imagem base segura permite:

- Reduzir significativamente a exposição a vulnerabilidades conhecidas (CVE);
- Minimizar o número de binários e bibliotecas carregadas;
- Aplicar controlos de integridade e proveniência;
- Garantir coerência e previsibilidade nos ambientes de execução;
- Suportar políticas organizacionais de execução segura.

---

## 🧬 O que é uma imagem base segura

Uma **imagem base segura** é aquela que:

- É mantida e atualizada por uma fonte confiável, interna ou explicitamente aprovada;
- Contém apenas o necessário para a aplicação funcionar (ex.: distroless, alpine);
- Evita ferramentas interativas (`curl`, `wget`, `bash`, `ping`) que ampliam a superfície de ataque;
- Utiliza um utilizador não-root por omissão;
- É submetida a **validação técnica automática** (SCA, scanners de containers);
- É **avaliada e aprovada por decisão humana explícita** antes da sua adoção;
- É assinada e rastreável ao longo do pipeline.

> ⚠️ Imagens genéricas como `ubuntu`, `node`, `python` ou `debian` podem conter centenas de pacotes desnecessários.  
> A sua utilização em produção **não deve ser implícita** e requer justificação e validação reforçadas.

---

## 📘 Exemplos de imagens recomendadas

| Tipo               | Exemplo                                  | Notas                                                                 |
|--------------------|------------------------------------------|-----------------------------------------------------------------------|
| Distroless         | `gcr.io/distroless/static`               | Sem shell nem package manager; reduz drasticamente a superfície       |
| Alpine minimalista | `alpine:3.19`                            | Imagem pequena; requer validação de compatibilidade                   |
| Builder + runtime  | Multi-stage `golang:alpine` → `distroless` | Compila num estágio, executa noutro                                    |
| Imagem própria     | `registry.corp.com/base/api`             | Controlada pela organização, com baseline e SLA de manutenção          |

Estes exemplos **não constituem autorização automática**.  
Cada imagem deve ser **avaliada, aprovada e registada** como imagem base válida.

---

## 🛠️ Como aplicar

A aplicação correta de imagens base seguras exige disciplina e rastreabilidade:

1. **Selecionar a imagem base em função da linguagem e do tipo de aplicação**, assumindo que a escolha pode ser reutilizada automaticamente;
2. **Avaliar a imagem candidata** (scanner SCA, composição, superfície de ataque);
3. **Decidir explicitamente a sua aprovação** como imagem base organizacional;
4. **Fixar versão ou digest**, evitando referências flutuantes;
5. **Eliminar ferramentas de debug e shells interativos**;
6. **Executar como utilizador não-root**, definido no `Dockerfile`;
7. **Assinar a imagem após validação** (ver `03-assinatura-cadeia-trust.md`);
8. **Integrar a validação e o enforcement na pipeline**, sem substituir decisão humana (ver `05-policies-runtime-opa.md`);
9. **Publicar a imagem num registry controlado**, com rastreabilidade e controlo de acesso.

---

## 📂 Onde manter imagens base aprovadas

Imagens base aprovadas devem ser tratadas como **ativos de confiança organizacional**:

- Registry interno ou controlado (Artifactory, Harbor, ECR, GCR);
- Catálogo mantido por equipa de plataforma/AppSec;
- Referências fixas (versão ou digest), nunca `latest`;
- Documentação associada com:
  - origem,
  - critérios de aprovação,
  - data de revisão,
  - responsáveis.

A ausência deste catálogo implica **impossibilidade de auditoria efetiva**.

---

## 🔁 Reavaliação e ciclo de vida

A aprovação de uma imagem base **não é permanente**.

Deve existir:
- Reavaliação periódica (ex.: por idade, CVEs relevantes, mudança de contexto);
- Processo de depreciação e substituição;
- Capacidade de revogação rápida em caso de incidente.

A reutilização automática de imagens **não dispensa** esta revalidação.

---

## ✅ Boas práticas

- Evitar `latest`: usar versões ou digests auditáveis;
- Preferir multi-stage builds;
- Reduzir camadas e dependências;
- Reavaliar imagens base após CVEs críticos;
- Associar SBOM à imagem base;
- Definir TTL para revisão obrigatória de imagens antigas.

---

## 📎 Referências cruzadas

| Documento                         | Relação com imagens base                                  |
|----------------------------------|-----------------------------------------------------------|
| `03-assinatura-cadeia-trust.md`  | Assinatura e verificação de integridade                   |
| `05-policies-runtime-opa.md`    | Enforcement técnico de imagens aprovadas                  |
| `06-sbom-containers.md`         | Inventário e composição das imagens                       |
| `07-vulnerabilidades-imagens.md`| Análise contínua de vulnerabilidades                      |
| `09-riscos-processo-imagens.md` | Separação entre validação automática e decisão humana     |

> 🧩 A imagem base é o **primeiro ponto de decisão consciente** na cadeia de execução de containers.  
> Sem essa decisão explícita, todo o restante controlo perde significado.
