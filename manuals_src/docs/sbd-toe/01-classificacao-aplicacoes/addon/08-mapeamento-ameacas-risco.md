---
id: mapeamento-ameacas-risco
title: Mapeamento de Ameaças por Nível de Risco
sidebar_position: 8
tags: [tipo:mapeamento, ameaças, risco, controlo]
---

<!--template: sbdtoe-core -->

# 🛠️ Mapeamento de Ameaças por Nível de Risco {classificacao-aplicacoes:addon:mapeamento-ameacas-risco}

A integração de **modelos de ameaças estruturados** na análise de risco é fundamental para garantir que os riscos considerados representam efetivamente a realidade técnica e operativa. Este ficheiro estabelece um modelo de referência para mapear ameaças conhecidas (como STRIDE ou MITRE ATT\&CK) aos riscos analisados no contexto de aplicações.

---

## 🛡️ Porquê mapear ameaças? {classificacao-aplicacoes:addon:mapeamento-ameacas-risco#porque_mapear_ameacas}

* Ajuda a **validar se os riscos analisados cobrem ameaças reais**.
* Permite uma abordagem sistemática e rastreável.
* Suporta a priorização de controlos baseados em exposição concreta.
* Facilita auditorias e revisões de arquitetura e threat modeling.

---

## 🧩 Modelos de ameaças relevantes {classificacao-aplicacoes:addon:mapeamento-ameacas-risco#modelos_de_ameacas_relevantes}

| Modelo        | Características principais                                                                          | Relevância para risco aplicacional                    |
| ------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| STRIDE        | Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege | Ideal para modelar aplicações desde o design          |
| MITRE ATT\&CK | Técnicas de ataque em sistemas reais (enterprise/cloud)                                             | Excelente para avaliar exposição e controle de ataque |
| CAPEC         | Catálogo de padrões de exploração de vulnerabilidades                                               | Bom para mapear controlos específicos                 |

> Em contexto aplicacional, STRIDE é ideal para threat modeling e ATT\&CK para validação de exposição e resposta.

---

## 📝 Exemplo de Mapeamento STRIDE → Risco {classificacao-aplicacoes:addon:mapeamento-ameacas-risco#exemplo_de_mapeamento_stride__risco}

| Categoria STRIDE       | Exemplo de Ameaça                | Risco Potencial                           | Controlos sugeridos                    |
| ---------------------- | -------------------------------- | ----------------------------------------- | -------------------------------------- |
| Spoofing               | Falsificação de identidade       | Acesso não autorizado a funções sensíveis | MFA, validação JWT, controle de sessão |
| Tampering              | Manipulação de dados em trânsito | Perda de integridade de informação        | TLS, HMAC, assinatura digital          |
| Information Disclosure | Exfiltração de dados sensíveis   | Violacão de confidencialidade             | Encriptação, RBAC, mascaramento        |
| Denial of Service      | Envio de tráfego malicioso       | Indisponibilidade de serviço              | Rate limiting, WAF, circuit breakers   |

---

## 📝 Mapeamento com MITRE ATT\&CK (resumo) {classificacao-aplicacoes:addon:mapeamento-ameacas-risco#mapeamento_com_mitre_attck_resumo}

| Técnica ATT\&CK           | Vetor de risco                 | Possível resposta / controlo                          |
| ------------------------- | ------------------------------ | ----------------------------------------------------- |
| Initial Access: Phishing  | Comprometimento de credenciais | Filtro SPF/DKIM, awareness, isolamento de credenciais |
| Execution: Scripting      | Execução de código remoto      | Controlo de macro, validação de input                 |
| Discovery: Cloud Services | Enumeração de recursos         | Hardening IAM, logging, segmentação                   |
| Impact: Data Destruction  | Perda deliberada de dados      | Backups protegidos, controlo de alterações            |

> A seleção das técnicas ATT\&CK deve refletir o contexto da aplicação (web, cloud, API, CI/CD, etc.).

---

## 📝 Mapeamento com OSC\&R (exemplos) {classificacao-aplicacoes:addon:mapeamento-ameacas-risco#mapeamento_com_oscr_exemplos}

| Tática OSC\&R     | Técnica ofensiva                             | Risco Aplicacional              | Controlos sugeridos                      |
| ----------------- | -------------------------------------------- | ------------------------------- | ---------------------------------------- |
| Initial Access    | Injeção de código em aplicação local         | Execução arbitrária no cliente  | Validação estrita de input, sandboxing   |
| Persistence       | Modificação de ficheiros locais persistentes | Injeção de DLL ou hooks         | File integrity monitoring, assinaturas   |
| Defense Evasion   | Inversão de execução ou nome de processo     | Bypass de controlos de execução | AppArmor, exec restrictions              |
| Credential Access | Dumping de credenciais em runtime            | Acesso a segredos em memória    | Proteção de segredos, encriptação em uso |

> OSC\&R é especialmente últil para aplicações com runtime local, agentes ou módulos instalados.

---

## 🔐 Ligacão com Risco Residual e Controlos {classificacao-aplicacoes:addon:mapeamento-ameacas-risco#ligacao_com_risco_residual_e_controlos}

* Cada ameaça identificada deve resultar na avaliação de um risco associado.
* Esse risco pode ser mitigado parcialmente → gerando **risco residual**.
* O controlo aplicado deve ser **rastreável para a ameaça e para o risco**.

---

## 🧩 Extensões para Contextos Específicos {classificacao-aplicacoes:addon:mapeamento-ameacas-risco#extensoes_para_contextos_especificos}

| Modelo      | Foco                                         | Quando usar                                                      |
| ----------- | -------------------------------------------- | ---------------------------------------------------------------- |
| **OSC\&R**  | Técnicas ofensivas contra software           | Aplicações em runtime, segurança ofensiva de aplicações          |
| **D3FEND**  | Técnicas defensivas documentadas             | Planeamento de controlos defensivos com base em ameaças          |
| **MASTR-S** | Ameaças à cadeia de fornecimento de software | Aplicações com pipelines CI/CD, dependências externas, automação |

> Estes modelos são especialmente relevantes para equipas com capacidades de threat modeling maduras ou ambientes com elevado risco técnico.

---

## 🚀 Recomendações para adoção {classificacao-aplicacoes:addon:mapeamento-ameacas-risco#recomendacoes_para_adocao}

* Usar STRIDE como modelo base em threat modeling.
* Usar ATT\&CK para validação de exposição e definição de prioridades.
* Usar OSC\&R para aplicações com componentes nativos, agentes ou execução local.
* Associar cada entrada na matriz de risco a pelo menos uma ameaça conhecida.
* Rever ameaças conhecidas com cada alteração de arquitetura.

> O mapeamento de ameaças não é apenas uma prática de threat modeling, mas um **instrumento fundamental para fundamentar e justificar a análise de risco**.
