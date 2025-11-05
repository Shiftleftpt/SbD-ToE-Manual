---
id: matriz-controlos-por-risco
title: Aplicação de Requisitos por Classificação
description: Requisitos mínimos obrigatórios por classificação de criticidade da aplicação
tags: [proporcionalidade, risco, requisitos, matriz, controlo]
---

# 🧩 Matriz de Aplicação de Requisitos por Nível de Risco

Esta matriz resume, por **tema técnico de segurança**, quais os domínios onde existem **requisitos obrigatórios** para cada nível de risco (L1, L2, L3).

> ⚠️ **Importante:** A marcação ✔ indica que **existem requisitos obrigatórios dentro desse tema para o nível de risco em causa** - **não implica que todos os requisitos do tema se apliquem** a todos os níveis.  
> Consulte o [catálogo completo de requisitos aplicacionais](./catalogo-requisitos) para ver os detalhes por requisito e nível.

---

| Tema de Requisitos                                | L1 | L2 | L3 |
|---------------------------------------------------|:--:|:--:|:--:|
| 🔐 1. Autenticação e Gestão de Identidade         | ✔ | ✔ | ✔ |
| 🧾 2. Controlo de Acesso                          | ✔ | ✔ | ✔ |
| 📈 3. Registo, Auditoria e Monitorização          |    | ✔ | ✔ |
| 📮 4. Gestão de Sessão                            | ✔ | ✔ | ✔ |
| 🧱 5. Validação de Entrada                        | ✔ | ✔ | ✔ |
| 🪪 6. Proteção de Dados Sensíveis                 |    | ✔ | ✔ |
| 🧮 7. Criptografia e Gestão de Chaves             |    | ✔ | ✔ |
| 🚧 8. Tratamento de Erros e Comportamentos Invulgares | ✔ | ✔ | ✔ |
| 🧯 9. Segurança na API e Interface                | ✔ | ✔ | ✔ |
| 🧼 10. Sanitização e Output Seguro                | ✔ | ✔ | ✔ |
| 🛡️ 11. Segurança do Código e Ciclo de Build       | ✔ | ✔ | ✔ |
| 🪪 12. Segurança de Terceiros e Bibliotecas       | ✔ | ✔ | ✔ |
| 📦 13. Gestão de Dependências (SBOM, SCA)         |    | ✔ | ✔ |
| 🐳 14. *containers* e Ambientes Isolados           |    | ✔ | ✔ |
| ⚙️ 15. Configuração Segura                        | ✔ | ✔ | ✔ |
| 🏁 16. Deploy, Release e Runtime Controls         |    | ✔ | ✔ |
| 🔍 17. Testes de Segurança e Validações           |    | ✔ | ✔ |
| 📊 18. Monitorização Contínua e Alertas           |    | ✔ | ✔ |
| 👥 19. Onboarding, Perfis e Segregação de Acessos | ✔ | ✔ | ✔ |
| 📜 20. Governança, Conformidade e Ciclo de Vida   | ✔ | ✔ | ✔ |

---

> A matriz acima deve ser usada em conjunto com os anexos:
> - [catalogo de requisitos](./catalogo-requisitos)
> - [criterios aceitação](./criterios-aceitacao)
> - [rastreabilidade](./rastreabilidade-controlo)

