---
id: assinatura-cadeia-trust
title: Assinatura de Imagens e Cadeia de Confiança
description: Validação da proveniência e integridade de imagens de containers como evidência técnica, não como decisão de execução
tags: [containers, assinatura, trust, notary, cosign, rekor, supply-chain]
---

# 🔏 Assinatura de Imagens e Cadeia de Confiança

## 🌟 Objetivo

Assegurar que todas as imagens de container utilizadas em pipelines, ambientes de execução e produção **têm a sua proveniência e integridade tecnicamente verificáveis**, através de mecanismos de assinatura digital e registo auditável.

A assinatura e a cadeia de confiança **não concedem autorização de execução**.  
Elas fornecem **evidência objetiva** que suporta decisões humanas sobre aceitação, promoção e execução de imagens.

Este ficheiro define como produzir e verificar essa evidência de forma consistente.

---

## 🧬 O que é a cadeia de confiança em imagens

A **cadeia de confiança** aplicada a imagens de containers permite responder, de forma verificável, a questões fundamentais:

- Quem produziu esta imagem?
- Em que contexto foi construída?
- A imagem foi modificada após o build?
- Existe continuidade entre build, assinatura e execução?

Tecnicamente, a cadeia de confiança inclui:

- **Assinatura digital da imagem** no momento do build;
- **Verificação da assinatura** antes da sua utilização;
- **Registo imutável da assinatura** (ex.: transparency log);
- **Associação entre imagem, pipeline e entidade produtora**.

> 🎯 A assinatura garante **integridade e proveniência**.  
> A decisão de executar a imagem depende de critérios de risco, contexto e governação, tratados noutros pontos do manual.

---

## ⚠️ Assinatura não é autorização

É essencial evitar uma interpretação incorreta, mas comum:

- ✔️ *Imagem assinada* → integridade comprovada  
- ❌ *Imagem assinada* ≠ imagem automaticamente aprovada

Uma imagem pode ser:
- tecnicamente íntegra,
- proveniente de uma fonte legítima,
- corretamente assinada,

e **ainda assim não ser adequada** ao contexto onde pretende ser executada.

A decisão de aceitação deve considerar:
- o ambiente (DEV, QA, PROD);
- a criticidade da aplicação (L1–L3);
- os dados tratados;
- o risco residual identificado noutros controlos.

Esta separação é fundamental para evitar **confiança implícita induzida por automação**.

---

## 📘 Ferramentas e mecanismos recomendados

| Componente          | Ferramenta / Padrão | Função técnica                                             |
|--------------------|---------------------|-------------------------------------------------------------|
| Assinatura         | Cosign              | Assinar imagens com chave ou identidade federada (OIDC)     |
| Transparency Log   | Rekor               | Registo imutável e auditável de assinaturas                 |
| Verificação        | Cosign + controllers| Verificação técnica antes da execução                       |
| Alternativa OCI    | Notary v2           | Assinatura nativa de artefactos OCI                         |

Estas ferramentas **produzem evidência criptográfica**, não decisões.

---

## 🛠️ Como aplicar assinatura e verificação

A aplicação correta da cadeia de confiança deve seguir uma sequência clara:

1. **Assinar a imagem no momento do build**, usando chave privada ou identidade federada;
2. **Publicar a assinatura juntamente com a imagem**, como metadados OCI;
3. **Registar a assinatura num transparency log**, garantindo imutabilidade;
4. **Verificar tecnicamente a assinatura** antes de qualquer utilização;
5. **Associar a verificação a políticas técnicas**, sem substituir governação;
6. **Disponibilizar a evidência** para suporte à decisão humana;
7. **Proteger chaves e identidades** usadas para assinatura.

A verificação automática **não elimina** a necessidade de avaliação contextual.

---

## 📂 Armazenamento, versionamento e rastreabilidade

- Assinaturas devem residir **junto da imagem** no registry;
- Utilizar digests e identificadores estáveis;
- Correlacionar assinatura com:
  - commit,
  - pipeline,
  - build ID;
- Opcionalmente referenciar assinatura no SBOM.

A rastreabilidade deve permitir reconstruir o percurso completo da imagem.

---

## ✅ Boas práticas

- Preferir identidades OIDC para reduzir gestão manual de chaves;
- Proibir execução de imagens não assinadas em L2/L3;
- Separar claramente:
  - verificação técnica (automática),
  - aceitação de risco (humana);
- Usar políticas de execução para **bloquear ausência de evidência**, não para conceder confiança implícita;
- Rever assinaturas e critérios de aceitação em caso de incidente ou mudança de contexto.

---

## 📎 Referências cruzadas

| Documento                         | Relação com a cadeia de confiança              |
|----------------------------------|------------------------------------------------|
| `01-imagens-base.md`             | Assinatura após aprovação da imagem base       |
| `05-policies-runtime-opa.md`    | Enforcement técnico de verificação             |
| `06-sbom-containers.md`         | Ligação entre composição e integridade         |
| `09-riscos-processo-imagens.md` | Separação entre evidência e decisão            |
| `25-rastreabilidade.md`         | Demonstração auditável de integridade          |

> 🔐 A assinatura de imagens é um **pilar técnico da confiança**,  
> mas a **confiança operacional só existe quando há decisão humana explícita suportada por evidência**.
