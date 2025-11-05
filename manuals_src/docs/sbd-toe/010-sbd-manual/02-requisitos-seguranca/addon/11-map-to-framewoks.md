---
id: map-to-framewoks
title: Rastreabilidade do Catalogo com Frameworks de Segurança
description: Mapeamento dos temas de requisitos do catálogo com frameworks normativas e de maturidade
tags: [rastreabilidade, frameworks, asvs, samm, bsimm, nist, cis, slsa, dsomm]
sidebar_position: 3
---

## 🎯 Rastreabilidade com Frameworks de Referência

Este documento apresenta a matriz de rastreabilidade entre os **20 temas de requisitos aplicacionais** definidos neste manual e as **principais frameworks de segurança e maturidade** utilizadas como base para a sua definição.

A rastreabilidade visa:

- Demonstrar o **alinhamento das práticas prescritas** com normas e frameworks reconhecidas;
- Facilitar a **integração com programas de conformidade** e avaliação de maturidade existentes;
- Apoiar na **comunicação com auditores, equipas de GRC, arquitetos e clientes**;
- Permitir que cada requisito ou tema seja facilmente mapeado para **referenciais internacionais consolidados**.

As frameworks consideradas são:

| Abreviatura | Framework / Referencial                                | Versão       |
|-------------|----------------------------------------------------------|--------------|
| ASVS        | OWASP Application Security Verification Standard         | v5.0         |
| SAMM        | OWASP Software Assurance Maturity Model                  | v2.1         |
| BSIMM       | Building Security In Maturity Model                      | v13          |
| NIST        | NIST SP 800-53 – Security and Privacy Controls           | Rev. 5       |
| SLSA        | Supply-chain Levels for Software Artifacts               | v1.0         |
| CIS         | CIS Controls (Center for Internet Security)              | v8           |

---

## 📘 Matriz de Mapeamento

A tabela abaixo apresenta o **alinhamento entre os 20 temas definidos neste manual** e os domínios / controlos das frameworks de referência.

Cada célula inclui o(s) identificador(es) do(s) controlo(s), prática(s) ou domínio(s) correspondente(s) da framework. Quando o alinhamento é parcial, é indicado com `~`.

| # | Tema de Requisito Aplicacional                            | ASVS v5.0 | SAMM v2.1 | BSIMM13 | NIST 800-53 Rev.5 | SLSA v1.0 | CIS v8 |
|---|------------------------------------------------------------|-----------|-----------|---------|--------------------|-----------|--------|
| 1 | 🔐 Autenticação e Gestão de Identidade                    | V2        | AA2.1     | AA1.1   | IA-2, IA-5         | —         | 6.2    |
| 2 | 🧾 Controlo de Acesso                                      | V4        | AA1.2     | AA2.1   | AC-2, AC-3         | —         | 6.1    |
| 3 | 📈 Registo, Auditoria e Monitorização                      | V10       | OM2.2     | CR2.2   | AU-2, AU-6, AU-12  | —         | 8.2    |
| 4 | 🧠 Gestão de Sessões                                       | V3        | AA2.2     | AA2.3   | SC-23, AC-12       | —         | 6.3    |
| 5 | 🔒 Proteção de Dados em Trânsito                          | V9        | CM1.1     | DR3.1   | SC-12, SC-13       | —         | 13.1   |
| 6 | 🗃️ Proteção de Dados em Repouso                           | V9        | CM1.2     | DR2.1   | SC-28, SC-28(1)    | —         | 3.4    |
| 7 | 🧾 Validação e Saneamento de Dados                         | V5, V6    | AA1.3     | SR2.3   | SI-10, SI-11       | —         | 10.4   |
| 8 | 🔍 Tratamento de Erros e Segurança na Comunicação          | V10       | OM1.1     | CR3.2   | SC-7, SI-11        | —         | 8.7    |
| 9 | 🔐 Criação e Gestão de Credenciais                        | V2, V15   | AA2.1     | AA1.2   | IA-5, IA-6         | —         | 5.1    |
|10 | 🧰 Configuração Segura                                     | V1, V18   | CM2.2     | CM1.1   | CM-2, CM-6         | —         | 4.3    |
|11 | 🐞 Tratamento de Vulnerabilidades                          | V1        | PO3.1     | VT1.1   | SI-2, RA-5         | —         | 7.1    |
|12 | 📦 Gestão de Dependências e SBOM                           | V11       | CM2.1     | SR1.2   | CM-8, CM-8(2)      | L1–L4     | 2.3    |
|13 | 🔄 CI/CD Seguro                                            | V13       | OE2.3     | CM1.4   | CM-5, AC-19        | L2–L4     | 4.6    |
|14 | ⚙️ Segurança da Infraestrutura como Código                | V13       | OE2.2     | CM1.3   | CM-6, SC-15        | L2–L4     | 11.4   |
|15 | 🐳 *containers* e Execução Isolada                          | V14       | OE2.2     | SR1.4   | SC-39, SC-38       | L3–L4     | 5.2    |
|16 | 🧪 Testes de Segurança (DAST, fuzzing, etc.)               | V7        | TE2.1     | PT1.2   | CA-8, RA-5         | —         | 18.2   |
|17 | 🚀 Deploy Seguro                                           | V1, V15   | OE3.1     | CM1.5   | CM-6, SA-10        | L4        | 4.7    |
|18 | 📊 Monitorização e Alertas Operacionais                    | V10       | OM2.3     | CR3.3   | AU-6, IR-5         | —         | 8.1    |
|19 | 👥 Formação, Onboarding e Sensibilização                   | V1        | EDU1.1    | T1.1    | AT-2, AT-3         | —         | 14.2   |
|20 | 📋 Governança, Revisões e Contratação                      | V1        | PO1.1     | SM1.1   | PM-1, SA-4         | —         | 17.1   |

> **Notas**:
> - Quando aplicável, os níveis do SLSA (L1–L4) são indicados em faixas, pois não existe mapeamento direto 1:1.
> - A coluna “ASVS v5.0” representa os controlos principais correspondentes, sendo possível que alguns temas estejam associados a múltiplos domínios ASVS.
> - A cobertura é intencionalmente abrangente, mas pode ser adaptada conforme o contexto de cada organização.

---

## 🔗 Ligação à Matriz de Aplicação por Risco

O mapeamento feito neste anexo mostra como cada uma das nossas 20 categorias de requisitos se relaciona com frameworks de referência como OWASP ASVS, NIST 800-53, BSIMM, SAMM, entre outras.

Para saber **quais destas categorias são obrigatórias consoante o nível de risco de uma aplicação**, consulta o anexo seguinte:

👉 [06-matriz-controlos-por-risco.md](matriz-controlos-por-risco)

Este cruzamento permite à organização aplicar requisitos de forma proporcional e fundamentada, alinhada com as suas necessidades, contexto e maturidade.

--- 

## 📚 Utilização da Matriz

Esta matriz pode ser usada para:

- Apoiar auditorias, análises de gap e assessments;
- Justificar a adoção de requisitos específicos num projeto ou programa;
- Alinhar os controlos de segurança com iniciativas de certificação;
- Demonstrar maturidade organizacional perante clientes ou reguladores.

---

