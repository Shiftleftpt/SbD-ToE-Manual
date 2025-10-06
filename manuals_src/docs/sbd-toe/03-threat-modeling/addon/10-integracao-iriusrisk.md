---
id: integracao-iriusrisk
title: Integração com IriusRisk e Ferramentas Automatizadas
description: Como substituir o mapeamento manual threat → requisito usando plataformas como IriusRisk, mantendo a rastreabilidade com o Capítulo 2
tags: [iriusrisk, integração, ameaças, requisitos, rastreabilidade, capitulo2]
---

# 🧠 Integração com IriusRisk e Ferramentas Automatizadas {threat-modeling:addon:integracao-iriusrisk}

## 🌟 Objetivo {threat-modeling:addon:integracao-iriusrisk#objetivo}

Demonstrar como aplicar os princípios normativos deste capítulo utilizando **plataformas automatizadas de Threat Modeling**, como o **IriusRisk**, substituindo os ficheiros manuais e mantendo a rastreabilidade com os requisitos definidos no **Capítulo 2 — Requisitos de Segurança**.

Esta integração visa:

- Automatizar o mapeamento threat → requisito → controlo;
- Eliminar a necessidade de ficheiros manuais (`yaml`, `md`, `csv`);
- Permitir validação contínua via CI/CD, mantendo coerência com o modelo SbD-ToE.

---

## 🧭 O que é substituído pela ferramenta {threat-modeling:addon:integracao-iriusrisk#o_que_e_substituido_pela_ferramenta}

| Ficheiro manual (modelo local) | Equivalente em IriusRisk                                    |
| ------------------------------ | ----------------------------------------------------------- |
| `threats.yaml`                 | Threats geradas automaticamente por templates               |
| `requisitos.yaml`              | Security Requirements atribuídos por ameaça                 |
| `mitigations.md`               | Lista de controlos com estado (implemented / planned / n/a) |
| `decisions.md`                 | Risk Decisions documentadas com justificação e data         |
| `mapeamento.md`                | Exportação de mappings threat → requisito → controlo        |

---

## 🔗 Ligação com o Capítulo 2 — Requisitos de Segurança {threat-modeling:addon:integracao-iriusrisk#ligacao_com_o_capitulo_2__requisitos_de_seguranca}

Para manter consistência e rastreabilidade, os requisitos definidos no IriusRisk devem:

- Referenciar os **mesmos códigos de requisito do Cap. 2**, ex: `REQ-AUT-003`, `REQ-AC-010`;
- Ser classificados na mesma **categoria funcional** (autenticação, controlo de acesso, privacidade);
- Ter criticidade associada (baixa / média / alta) conforme contexto do risco;
- Indicar o **estado atual** da implementação.

### Exemplo de correspondência: {threat-modeling:addon:integracao-iriusrisk#exemplo_de_correspondencia}

| Ameaça (IriusRisk)               | Requisito derivado (Cap. 2)           | Estado       |
| -------------------------------- | ------------------------------------- | ------------ |
| JWT token não assinado           | `REQ-AUT-003`: Assinatura obrigatória | Implementado |
| Endpoint `/admin/config` exposto | `REQ-AC-010`: RBAC obrigatório        | Em curso     |
| Claims excessivos no JWT         | `REQ-DAT-005`: Claims mínimos         | Justificado  |

---

## 📁 Estrutura de exportação no projeto {threat-modeling:addon:integracao-iriusrisk#estrutura_de_exportacao_no_projeto}

```
📁 threat-model/
├── iriusrisk-export/
│   ├── threats.json         # Lista de ameaças exportadas via API
│   ├── requirements.csv     # Requisitos de segurança atribuídos por ameaça
│   ├── controls.csv         # Estado de controlos aplicados
│   ├── decisions.csv        # Justificações de risco
├── threat-model.yml         # Metadados (última sincronização, projeto, versão)
```

---

## 🛠️ Como aplicar com IriusRisk no CI/CD {threat-modeling:addon:integracao-iriusrisk#como_aplicar_com_iriusrisk_no_cicd}

A pipeline pode incluir validações como:

- Verificar que todas as ameaças com criticidade alta têm:
  - controlo aplicado **OU**
  - justificação documentada;
- Confirmar que requisitos do Cap. 2 com `estado != implemented` têm ticket associado;
- Exportar relatório resumido com percentagem de ameaças cobertas.

### Exemplo (pseudocódigo bash): {threat-modeling:addon:integracao-iriusrisk#exemplo_pseudocodigo_bash}

```bash
# Verifica se há threats sem mitigação nem justificação {threat-modeling:addon:integracao-iriusrisk}

cat threats.json | jq '.[] | select(.criticality == "High")' |
  while read threat; do
    REQ=$(jq '.requirement_id' <<< "$threat")
    STATUS=$(grep $REQ requirements.csv | cut -d',' -f3)
    if [[ "$STATUS" != "Implemented" && "$STATUS" != "Justified" ]]; then
      echo "❌ Ameaça $REQ sem controlo válido"
      exit 1
    fi
  done
```

---

## ✅ Benefícios da Integração {threat-modeling:addon:integracao-iriusrisk#beneficios_da_integracao}

| Benefício                          | Impacto                                                   |
| ---------------------------------- | --------------------------------------------------------- |
| Elimina ficheiros manuais          | Reduz risco de desatualização, aumenta confiabilidade     |
| Mantém ligação direta a requisitos | Facilita auditorias e validação cruzada com Cap. 2        |
| Permite validação no CI/CD         | Automatiza segurança por design como requisito de release |
| Suporta decisões de risco formais  | Justificações com responsável, data e contexto            |

---

## ✅ Boas práticas {threat-modeling:addon:integracao-iriusrisk#boas_praticas}

- Reutilizar templates de threats e requisitos oferecidos pela ferramenta;
- Manter naming e códigos de requisito sincronizados com o Capítulo 2;
- Incluir a exportação automática no CI/CD para auditoria contínua;
- Utilizar dashboards da ferramenta para medir cobertura e estado;
- Validar exportações com scripts locais e integrar com backlog.

---

## 📎 Referências cruzadas {threat-modeling:addon:integracao-iriusrisk#referencias_cruzadas}

| Documento                        | Relação com este ficheiro                                 |
|----------------------------------|-----------------------------------------------------------|
| `addon/07-mapeamento-threats-requisitos.md` | Alternativa manual ao mapeamento entre ameaças e requisitos |
| `addon/06-threat-modeling-ci.md` | Validação de threat modeling em pipelines CI/CD           |
| `canon/25-rastreabilidade.md`    | Rastreabilidade formal com frameworks e requisitos         |
| `canon/15-aplicacao-lifecycle.md`| Integração com o ciclo de vida do projeto                 |

---

> A adoção de ferramentas como IriusRisk deve ser acompanhada de processos que garantam coerência com a taxonomia e requisitos de segurança definidos no manual SbD-ToE. A ferramenta **não substitui** a responsabilidade pela rastreabilidade — apenas a sistematiza e automatiza.
