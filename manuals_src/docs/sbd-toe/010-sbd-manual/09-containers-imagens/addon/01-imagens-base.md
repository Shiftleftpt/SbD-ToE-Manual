---
description: Seleção, reforço e validação de imagens base seguras para *containers*
id: imagens-base
tags:
- cicd
- containers
- hardening
- imagens base
- runtime
- supply chain
- supply-chain
title: Imagens Base Seguras e Minimalistas
---


# 🧱 Imagens Base Seguras e Minimalistas

## 🌟 Objetivo

Garantir que todas as aplicações, pipelines e serviços que utilizam *containers* **partem de imagens base seguras, controladas e minimizadas**, reduzindo a superfície de ataque e aumentando a confiança no runtime.

Uma imagem base segura permite:

- Reduzir significativamente as vulnerabilidades conhecidas (CVE);
- Minimizar o número de binários e bibliotecas carregadas;
- Aplicar controlos de assinatura e verificação de integridade;
- Garantir coerência nos ambientes de execução;
- Suportar políticas organizacionais de execução segura.

---

## 🧬 O que é uma imagem base segura

Uma **imagem base segura** é aquela que:

- É mantida e atualizada por uma fonte confiável;
- Contém apenas o necessário para a aplicação funcionar (distroless, alpine, etc.);
- Evita ferramentas interativas (ex: `curl`, `wget`, `bash`, `ping`) que ampliam a superfície de ataque;
- Utiliza um utilizador não-root por omissão;
- É submetida a **validação estática** (SCA, scanners de container);
- É assinada e rastreável.

> ⚠️ Imagens genéricas como `ubuntu`, `node`, `python`, `debian` podem conter centenas de pacotes desnecessários - devem ser evitadas em produção.

---

## 📘 Exemplos de imagens recomendadas

| Tipo              | Exemplo                       | Notas                                                    |
|-------------------|-------------------------------|-----------------------------------------------------------|
| Distroless        | `gcr.io/distroless/static`     | Sem shell nem package manager, ideal para binários únicos |
| Alpine minimalista| `alpine:3.19`                  | Apenas 5MB; requer validação de compatibilidade           |
| Builder + runtime | Multi-stage com `golang:alpine` + `distroless` | Compila num, executa noutro                               |
| Imagem própria    | `registry.corp.com/base/api`   | Controlada pela organização, com baseline de segurança     |

---

## 🛠️ Como aplicar

1. **Selecionar imagem base com base na linguagem e tipo de aplicação** (ex: Node.js com Alpine, Go com Distroless);
2. **Evitar imagens com múltiplas camadas e dependências transversais**;
3. **Validar a imagem antes do uso com scanners SCA** (Syft, Grype, Trivy);
4. **Remover ferramentas de debug e shells interativos**;
5. **Executar sempre como utilizador não-root**, definido na imagem (`USER` no `Dockerfile`);
6. **Assinar a imagem após validação** (ver `03-assinatura-cadeia-trust.md`);
7. **Integrar a validação da imagem na pipeline de CI/CD** (ver `05-policies-runtime-opa.md`);
8. **Versionar e publicar a imagem num registry controlado**.

---

## 📂 Onde manter imagens base aprovadas

- **Registry interno validado** (ex: Artifactory, Harbor, ECR, GCR);
- **Catálogo controlado por equipa de plataforma/AppSec**, com lista de imagens autorizadas;
- Tags fixas (ex: `node:18.17.0`) em vez de flutuantes (ex: `node:latest`);
- Documento ou `README` com hashes e políticas de atualização.

---

## ✅ Boas práticas

- Evitar `latest`: usar sempre versões fixas e auditáveis;
- Fazer **multi-stage builds** e eliminar resíduos;
- Reduzir camadas (`layers`) e evitar ferramentas desnecessárias;
- Validar periodicamente se as imagens base contêm CVEs críticos;
- Associar SBOM à imagem (`syft docker:imagem`), incluindo no CI/CD;
- Aplicar política de time-to-live (TTL) para revisão obrigatória de imagens antigas.

---

## 📎 Referências cruzadas

| Documento                      | Relação com imagens base                       |
|-------------------------------|------------------------------------------------|
| `03-assinatura-cadeia-trust.md`   | Imagens devem ser assinadas e verificadas     |
| `05-policies-runtime-opa.md`     | Enforcement de uso apenas de imagens aprovadas|
| `06-sbom-containers.md`          | Geração de SBOM de imagens                    |
| `07-vulnerabilidades-imagens.md` | Análise de vulnerabilidades nas imagens       |
| `achievable-maturity`               | Utilização de imagens validadas como critério de maturidade |

> 🧩 A imagem base é o alicerce de segurança de qualquer *container*. A sua escolha e validação impactam diretamente a exposição a vulnerabilidades e o controlo de execução.

