---
id: exemplo-pipeline-container
title: Caso Prático – Pipeline Containerizado com Execução Segura
description: Exemplo completo de pipeline CI/CD com execução de *containers* em ambiente seguro e validado
tags: [exemplo, pipeline, containers, cicd, segurança, execucao]
---

# 💪 Caso Prático – Pipeline Containerizado com Execução Segura

Este exemplo ilustra a aplicação prática das prescrições do Capítulo 09 - desde a construção segura da imagem base, até à sua execução controlada num pipeline CI/CD e em Kubernetes.

O pipeline em causa é responsável por **compilar, testar, assinar e publicar um microserviço Node.js**, com execução **100% containerizada** e alinhada com as práticas do SbD-ToE.

---

## 📦 Estrutura da pipeline

```text
.
├── /.github/workflows/build.yml
├── /Dockerfile
├── /.sbom/
├── /k8s/deployment.yaml
└── /policies/
```

---

## 🔐 Passos principais implementados

| Etapa                         | Implementação real                           | Documentação associada                    |
|-------------------------------|-----------------------------------------------|-------------------------------------------|
| Imagem base segura            | `FROM node:18.17.0-alpine` + `USER node`      | `01-imagens-base.md`                      |
| Assinatura da imagem          | `cosign sign` com GitHub OIDC                | `03-assinatura-cadeia-trust.md`           |
| Geração de SBOM               | `syft . -o cyclonedx-json > .sbom/container.json` | `06-sbom-containers.md`               |
| Scanner de vulnerabilidades   | `trivy image` com bloqueio por CVSS > 7       | `07-vulnerabilidades-imagens.md`          |
| Runners isolados              | `runs-on: [self-hosted, ephemeral]`           | `02-runners-isolamento.md`                |
| Execução com enforcement      | Kyverno `validate` para labels, UID, origem   | `05-policies-runtime-opa.md`              |
| Deploy controlado em K8s      | Pod com `securityContext` e PSA: `restricted` | `08-kubernetes-execucao.md`               |

---

## 📜 Exemplo resumido do pipeline (GitHub Actions)

```yaml
jobs:
  build-and-push:
    runs-on: [self-hosted, hardened]
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t registry/project/app:1.0.0 .
      - name: Generate SBOM
        run: syft docker:registry/project/app:1.0.0 -o cyclonedx-json > sbom.json
      - name: Scan for CVEs
        run: trivy image --exit-code 1 --severity HIGH registry/project/app:1.0.0
      - name: Sign image
        run: cosign sign --key env://COSIGN_KEY registry/project/app:1.0.0
      - name: Push image
        run: docker push registry/project/app:1.0.0
```

---

## ☸️ Execução controlada no Kubernetes

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: microservico
    sbom: "true"
spec:
  securityContext:
    runAsNonRoot: true
    readOnlyRootFilesystem: true
    allowPrivilegeEscalation: false
  containers:
    - name: app
      image: registry/project/app:1.0.0
      ports: [ { containerPort: 3000 } ]
```

> 🔐 Este pod só será aceite em clusters com Pod Security Admission (`restricted`) + policies Kyverno a validar origem e UID.

---

## ✅ Resultados obtidos

- Execução de pipeline **100% rastreável** e alinhada com políticas;
- Imagem final com **SBOM, CVE scan e assinatura verificável**;
- Deploy em Kubernetes com enforcement de segurança à entrada;
- Processo auditável, versionado e reaplicável a outros projetos.

---

## 🧹 Lições aprendidas

- A utilização de *containers* exige disciplina e automatização contínua;
- O enforcement no runtime é tão importante quanto o build seguro;
- A validação da origem da imagem e do seu conteúdo deve ser feita *antes* da execução - não depois;
- A separação clara entre build, validação e execução reduz significativamente a superfície de ataque.

---

## 📌 Referências cruzadas

- Capítulo 07 – `addon/10-sbd-no-proprio-pipeline.md`
- Capítulo 05 – `06-validacao-dependencias.md`
- Capítulo 10 – `intro.md` (testes de execução containerizada)

> ✅ Este exemplo mostra como aplicar, de forma integrada e realista, as práticas do SbD-ToE ao ciclo de vida completo de execução containerizada.
