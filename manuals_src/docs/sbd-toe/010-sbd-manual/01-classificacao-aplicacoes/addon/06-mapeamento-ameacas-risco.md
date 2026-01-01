---
id: mapeamento-ameacas-risco
title: Mapeamento de Ameaças para Validação do Risco
sidebar_position: 6
tags: [tipo:mapeamento, ameacas, risco, validacao, controlo]
---

<!--template: sbdtoe-core -->

# 🛠️ Mapeamento de Ameaças para Validação do Risco

O mapeamento de ameaças conhecidas é um **mecanismo essencial de validação da análise de risco**, garantindo que os riscos identificados refletem **vetores de ataque reais, plausíveis e documentados**.

No *Security by Design – Theory of Everything (SbD-ToE)*, as ameaças **não determinam o nível de risco da aplicação**, mas são usadas para:

- validar a classificação de risco efetuada (E/D/I);
- identificar lacunas na análise ou nos controlos aplicados;
- justificar reforços de controlo ou rejeição de aceitação de risco;
- fundamentar decisões com base em catálogos reconhecidos.

---

## 🧠 Enquadramento no modelo SbD-ToE

O papel do mapeamento de ameaças no SbD-ToE é **complementar e validatório**:

1. A aplicação é classificada segundo o modelo **E/D/I**.
2. São identificados riscos relevantes e respetivos atributos.
3. As ameaças conhecidas são mapeadas para esses riscos.
4. Os controlos são definidos ou ajustados.
5. O risco residual é avaliado e, se aplicável, aceite.

> 📌 A ausência de ameaças mapeáveis para um risco identificado  
> é um **sinal de alerta** que exige revisão da análise.

---

## 🛡️ Porque mapear ameaças

O mapeamento sistemático de ameaças permite:

- confirmar que os riscos analisados **correspondem a cenários reais**;
- reduzir subjetividade na avaliação de risco;
- aumentar rastreabilidade entre risco, ameaça e controlo;
- suportar auditorias, revisões de arquitetura e decisões de exceção.

---

## 🧩 Catálogos de ameaças relevantes

Os seguintes modelos são reconhecidos no SbD-ToE como fontes válidas de ameaça:

| Modelo        | Papel no SbD-ToE                                              | Quando usar                                   |
|---------------|---------------------------------------------------------------|-----------------------------------------------|
| **STRIDE**    | Modelação de ameaças ao nível da aplicação                    | Design, arquitetura, threat modeling inicial  |
| **MITRE ATT&CK** | Validação de vetores de ataque reais e exposição operacional | Aplicações expostas, cloud, APIs, enterprise  |
| **CAPEC**     | Padrões de exploração de vulnerabilidades                     | Justificação de controlos técnicos específicos|
| **OSC&R**     | Técnicas ofensivas contra software                            | Runtime local, agentes, clientes, SDKs        |
| **D3FEND**    | Técnicas defensivas associadas a ameaças                      | Planeamento e justificação de controlos       |

> Estes catálogos **não são mutuamente exclusivos** e devem ser usados conforme o contexto técnico.

---

## 🧩 Exemplo: STRIDE como validação de risco

| Categoria STRIDE       | Ameaça típica                    | Risco validado                       | Controlos associados                |
|------------------------|----------------------------------|--------------------------------------|------------------------------------|
| Spoofing               | Falsificação de identidade       | Acesso indevido a funções críticas   | MFA, gestão de sessão              |
| Tampering              | Manipulação de dados             | Perda de integridade                 | Assinatura, validação de input     |
| Information Disclosure | Exfiltração de dados             | Violação de confidencialidade        | Encriptação, RBAC                  |
| Denial of Service      | Saturação de recursos            | Indisponibilidade                    | Rate limiting, proteção perimetral |

Este mapeamento confirma que os riscos identificados **têm correspondência direta com vetores de ataque conhecidos**.

---

## 🧩 Uso de ATT&CK para validação de exposição

| Técnica ATT&CK            | Vetor de ataque                | Risco associado                 | Controlos típicos                 |
|---------------------------|-------------------------------|----------------------------------|----------------------------------|
| Initial Access: Phishing  | Compromisso de credenciais     | Acesso não autorizado            | MFA, awareness                   |
| Execution: Scripting      | Execução remota                | Execução arbitrária              | Hardening, validação             |
| Discovery: Cloud Services | Enumeração de recursos         | Exposição excessiva              | IAM restritivo, logging          |
| Impact: Data Destruction  | Sabotagem de dados             | Perda de integridade             | Backups, controlo de alterações  |

ATT&CK é particularmente útil para validar se **a exposição assumida no modelo E/D/I é realista**.

---

## 🔐 Ligação com controlos e risco residual

Cada ameaça mapeada deve resultar em:

- um ou mais **riscos associados**;
- definição de **controlos mitigadores**;
- avaliação do **risco residual** após controlo.

Quando uma ameaça relevante **não tem controlo eficaz**, o risco residual:
- aumenta,
- ou torna-se **não aceitável**, especialmente em aplicações L3.

---

## ⚠️ Regras normativas

- Todo o risco identificado **deve ser validável** por pelo menos uma ameaça conhecida.
- A aceitação de risco **não é válida** se ameaças plausíveis permanecerem sem controlo eficaz.
- Em aplicações L3, ameaças mapeadas em catálogos reconhecidos **exigem mitigação explícita ou justificação formal de exceção**.

---

## 🔄 Integração no ciclo de vida

O mapeamento de ameaças deve ser revisto:

- sempre que haja alterações de arquitetura, dados ou exposição;
- quando são introduzidos novos mecanismos de automação ou delegação;
- após incidentes ou descobertas relevantes;
- antes de decisões formais de aceitação de risco residual.

---

## 📌 Nota final

O mapeamento de ameaças não serve para “listar ataques”,  
serve para **ancorar a análise de risco na realidade técnica**.

No SbD-ToE, ameaças são **instrumentos de validação**,  
não mecanismos de classificação automática de risco.
