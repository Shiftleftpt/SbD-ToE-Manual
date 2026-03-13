# Classificação da Criticidade Aplicacional


## Versão curada (síntese para impressão)

### Nota basilar
> **Capítulo basilar.** Este capítulo é considerado **basilar** no modelo Security by Design – Theory of Everything (SbD-ToE).
> A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.
> Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo.
> A ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE,
> tornando inviável a adoção coerente das práticas operacionais e de governação.

### Enquadramento e objetivo
A classificação de criticidade aplicacional proposta neste capítulo segue uma abordagem **pragmática, rápida e iterativa**, adequada a contextos ágeis e com ciclo de vida contínuo.
É especialmente útil em organizações onde:

- Existe uma lacuna na gestão formal de risco, ou
- A abordagem tradicional de GRC não se adequa à realidade do portfólio aplicacional.

Importa sublinhar: **esta abordagem não substitui métodos formais** de análise de risco.
O objetivo é garantir que **todas as aplicações recebem, desde o início, uma decisão clara e justificável sobre o seu nível de risco**,
evitar **under-engineering** e **over-engineering**, e assegurar **proporcionalidade, rastreabilidade e foco na ação concreta**.

No SbD-ToE, a classificação **não visa rotular tecnologias ou ferramentas**, mas sim **caracterizar o risco aplicacional**
para suportar decisões técnicas e organizacionais consistentes.
Ferramentas de automação e apoio à decisão (incl. IA) são parte normal do SDLC moderno
e devem ser consideradas **sempre que alterem exposição, dados, impacto ou a forma como decisões e validações são realizadas**.

O objetivo central do manual é:
1. **Classificar aplicações de forma consistente**, para assegurar proporcionalidade adequada.
2. **Disponibilizar mecanismos claros, rápidos e rastreáveis** para o fazer.

### Modelo de classificação (E/D/I)
O modelo proposto é empírico e simplificado, inspirado na OWASP Risk Rating, baseado em três eixos:

- **E (Exposição)**: acessibilidade externa e vetores de ataque.
- **D (Tipo de Dados)**: sensibilidade, privacidade e enquadramento regulamentar.
- **I (Impacto Potencial)**: consequências técnicas, operacionais e reputacionais.

**Risco Classificado (R) = E + D + I**

**Classificação por pontuação**
| Soma Total | Classificação de Risco | Código |
|------------|------------------------|--------|
| 3–4        | **Baixo**              | L1     |
| 5–6        | **Médio**              | L2     |
| 7–9        | **Elevado**            | L3     |

**Exposição (E)**
| Nível | Descrição                                          | Pontos |
|-------|----------------------------------------------------|--------|
| 1     | Apenas acessível internamente (sem acesso externo) | 1      |
| 2     | Acessível externamente, com autenticação           | 2      |
| 3     | Público ou amplamente exposto                      | 3      |

**Tipo de Dados (D)**
| Nível | Descrição                                                              | Pontos |
|-------|------------------------------------------------------------------------|--------|
| 1     | Dados públicos ou sem sensibilidade                                    | 1      |
| 2     | Dados pessoais, identificáveis ou confidenciais internos               | 2      |
| 3     | Dados regulados ou altamente sensíveis                                 | 3      |

**Impacto Potencial (I)**
| Nível | Descrição                                                                  | Pontos |
|-------|----------------------------------------------------------------------------|--------|
| 1     | Impacto nulo ou irrelevante                                                 | 1      |
| 2     | Impacto limitado, localizado ou reversível                                 | 2      |
| 3     | Impacto elevado: financeiro, regulatório, operacional ou reputacional significativo | 3 |

### Prescrição prática: o que, como, quando, quem, porquê
#### O que deve ser feito
1. Classificar a aplicação segundo exposição, dados sensíveis e impacto, conforme proposto no manual, ou adotar outro modelo equivalente.
2. Considerar explicitamente como automação e apoio à decisão (incl. IA) influenciam os atributos do risco relevantes.
3. Documentar a classificação, pressupostos e evidência utilizada.
4. Aplicar controlos mínimos com base no nível atribuído.
5. Rever a classificação em pontos-chave do ciclo de vida.
6. Aplicar critérios formais para aceitação de risco, quando necessário.

#### Como deve ser feito
- Usar o Modelo de Classificação.
- Ou um modelo alternativo adotado pela organização (ex.: adoção de DRP/BIA).
- Quando existir tooling automatizado/assistivo (incl. IA), **avaliar o seu impacto nos atributos do risco** e calibrar E/D/I em conformidade.
- Incorporar o Ciclo de Vida da Classificação de Risco.
- Aplicar os Critérios para Aceitação de Risco.
- Considerar ameaças reais através do Mapeamento de Ameaças por Nível de Risco.
- Registar decisões em repositório versionado, ferramenta de risco ou documentação rastreável.

#### Quando aplicar
- Durante a fase inicial do projeto ou definição de arquitetura.
- Sempre que houver alterações relevantes: novas funcionalidades, dados, exposição ou integrações.
- Quando se introduzam ou alterem mecanismos de automação/assistência (incl. IA) com impacto nos atributos do risco.
- Em releases principais ou milestones críticos (ex.: produção).
- Após incidentes de segurança relevantes.
- No mínimo a cada **6 meses** ou **em cada revisão de arquitetura ou roadmap de segurança**.

#### Quem está envolvido e como
| Papel                | Contributo                                                                 |
| -------------------- | -------------------------------------------------------------------------- |
| Dev / Tech Lead      | Propor classificação, identificar alterações relevantes                    |
| AppSec / Segurança   | Validar modelo aplicado, ajustar nível de risco, aplicar matriz             |
| Arquitetura          | Rever implicações técnicas, fluxos e exposição                               |
| Produto / Gestão     | Aprovar aceitação de risco, avaliar impacto de exceções                     |
| GRC / Compliance     | Assegurar rastreabilidade e alinhamento normativo                           |
| QA / Testes          | Validar cumprimento de requisitos por nível de risco antes do go-live       |

#### Porquê / Para quê
- Garantir proporcionalidade nos controlos de segurança aplicados.
- Reduzir custos evitando sobreproteção ou exposição desnecessária.
- Suportar conformidade normativa e auditorias.
- Informar decisões estratégicas (roadmap, orçamentação, outsourcing).
- Promover melhoria contínua e visibilidade do risco.

### Ciclo de vida e triggers de reavaliação
O risco deve ser reavaliado sempre que ocorra qualquer evento que altere o seu perfil ou atributos, nomeadamente:

- Introdução de novas funcionalidades ou fluxos relevantes.
- Alterações à arquitetura (nova exposição API, integrações externas, mudança de trust boundaries).
- Mudanças de contexto legal, regulatório ou contratual.
- Introdução ou modificação de mecanismos de automação ou apoio à decisão (incluindo IA) quando alterem pressupostos de validação, evidência ou reprodutibilidade.
- Deteção de vulnerabilidades críticas ou recorrentes.
- Resultados relevantes de auditorias, testes de segurança ou avaliações independentes.

Proporcionalidade por nível:
- Em aplicações **L3**, reavaliação obrigatória a cada release ou alteração relevante.
- Em aplicações **L2**, reavaliação sempre que existam mudanças significativas de arquitetura, dados ou processo.
- Em aplicações **L1**, reavaliação baseada em eventos de risco identificados ou num calendário fixo.

### Critérios de aceitação e risco residual
**Princípio fundamental:** um risco só pode ser aceite quando os seus atributos são compreendidos, os controlos aplicados são conhecidos e verificáveis, existe evidência suficiente e o impacto residual é compatível com o nível da aplicação.

**Risco residual** é o risco que permanece após a aplicação efetiva dos controlos definidos, considerando eficácia real e evidência disponível.

**Limiares de aceitação por nível**
| Nível da aplicação         | Risco Residual Máximo Aceitável | Observações                                     |
| -------------------------- | ------------------------------- | ----------------------------------------------- |
| **L1** (baixa criticidade) | ≤ 9 (médio)                     | Aceitação informal possível                     |
| **L2** (média criticidade) | ≤ 6 (baixo a médio)             | Requer validação formal e registo               |
| **L3** (alta criticidade)  | ≤ 4 (baixo)                     | Exceção apenas com aprovação de gestor de risco |

Não é aceitável considerar risco residual como tolerável quando:
- os controlos não estão comprovadamente ativos;
- a decisão depende exclusivamente de confiança implícita em automação ou tooling;
- os resultados não são reprodutíveis ou verificáveis;
- existe impacto legal, regulatório ou reputacional significativo;
- a aplicação é **L3** e o risco residual depende de validação não determinística.

### Matriz de controlos mínimos e regra de reforço
A matriz define o **patamar mínimo de controlos de segurança esperados** por domínio técnico, em função do nível L1–L3.
Os controlos constituem uma **baseline obrigatória** e devem ser entendidos como **mínimos exigíveis**, não como limite máximo.

**Regra de reforço obrigatório de controlos:**
Sempre que os atributos do risco indiquem baixa detetabilidade, baixa evidenciabilidade, comportamento não determinístico,
ou elevada delegação/execução automática com impacto real, devem ser aplicados **controlos equivalentes ao nível imediatamente superior**,
independentemente da classificação L1–L3 inicialmente atribuída.

### Mapeamento de ameaças
O mapeamento de ameaças conhecidas é um mecanismo essencial de validação da análise de risco, garantindo correspondência com vetores reais e documentados.

Catálogos reconhecidos no SbD-ToE:
| Modelo        | Papel no SbD-ToE                                              | Quando usar                                   |
|---------------|---------------------------------------------------------------|-----------------------------------------------|
| **STRIDE**    | Modelação de ameaças ao nível da aplicação                    | Design, arquitetura, threat modeling inicial  |
| **MITRE ATT&CK** | Validação de vetores de ataque reais e exposição operacional | Aplicações expostas, cloud, APIs, enterprise  |
| **CAPEC**     | Padrões de exploração de vulnerabilidades                     | Justificação de controlos técnicos específicos|
| **OSC&R**     | Técnicas ofensivas contra software                            | Runtime local, agentes, clientes, SDKs        |
| **D3FEND**    | Técnicas defensivas associadas a ameaças                      | Planeamento e justificação de controlos       |

Regras normativas:
- Todo o risco identificado **deve ser validável** por pelo menos uma ameaça conhecida.
- A aceitação de risco **não é válida** se ameaças plausíveis permanecerem sem controlo eficaz.
- Em aplicações L3, ameaças mapeadas exigem mitigação explícita ou justificação formal de exceção.

### Validação assistida por ferramentas (invariantes)
- **I1 — Separação entre sugestão e decisão:** ferramentas sugerem; a decisão final é humana.
- **I2 — Evidência acima de plausibilidade:** resultados plausíveis não substituem evidência verificável.
- **I3 — Reprodutibilidade e auditabilidade:** toda a sugestão deve ser reproduzível e rastreável.
- **I4 — Proteção de ativos críticos:** ferramentas externas são risco de supply chain; aprovação explícita em L2/L3.
- **I5 — Rastreabilidade de decisão e execução:** quem decidiu, com base em quê, que validações e evidência suportam.

### Artefactos e evidência mínimos
| Fase         | Artefacto                          | Quem produz         | Onde fica                  | Evidência mínima                              |
|--------------|------------------------------------|---------------------|----------------------------|-----------------------------------------------|
| Início       | `classificacao-aplicacao.yaml`     | Developer / Team Lead     | Repo `security/`           | Commit + revisão AppSec Engineer |
| Planeamento  | `matriz-controlos.md`              | Developer / Team Lead     | Backlog / wiki             | REQ-XXX referenciados (Cap. 02); aprovado AppSec |
| Revisão      | `classificacao-revisao.md`         | AppSec Engineer      | Repo `docs/`               | Issue/ata datada; decisão justificada |
| Release      | `checklist-go-live.md`             | QA                  | Pipeline CI/CD             | Aprovação formal AppSec Engineer + Gestão (L3) |
| Operação     | `risco-residual.md`                | GRC/Compliance    | Ferramenta GRC / repo      | Owner + TTL + critérios encerramento; aprovação |
| Periódico    | `classificacao-revisao-anual.md` (L1), `semestral.md` (L2), `trimestral.md` (L3) | AppSec Engineer + GRC/Compliance | Repo docs / GRC | Data revisão, justificação manter/alterar, próxima data |
| Aceitação    | `aceitacoes-risco.md` com TTL      | GRC/Compliance    | Ferramenta GRC / repo      | TTL definido, owner, critério encerramento, alertas |
| Artefactos   | `artefactos-tecnicos.md`           | DevOps/SRE + Arquitetos | Repo `platform/docs` | Classificação por artefacto, rastreamento REQ, aprovação AppSec |
| Contínuo     | `kpi-classificacao-YYYY-MM.md`    | GRC/Compliance    | Dashboard / Repositório de reporting | KPI 1-7, série temporal, alertas, recomendações |
| Governação   | `politicas-organizacionais.md` (4 políticas) | GRC/Compliance + AppSec | Docs / Wiki / Política | Aprovação Gestão Executiva, treinamento + attestation, auditoria |

> **Formato canónico de evidência (sugestão):** `id`, `data`, `eixos` (E/D/I), `nivel`, `decisão`, `owner`, `ligações` (issues/PRs), `aprovadores`, `expiração` (se aplicável).

### Políticas organizacionais
| Nome da Política                                   | Obrigatória? | Aplicação                             | Conteúdo mínimo esperado                                                                                      |
|----------------------------------------------------|--------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Política de Classificação de Risco Aplicacional    | Sim       | Todos os projetos e equipas de produto | Modelo de classificação obrigatório; momentos de aplicação; registo e rastreio.                              |
| Política de Aceitação de Risco Residual            | Sim       | Segurança, gestão, donos de produto    | Critérios formais para aceitação; responsáveis; validade temporal; registo e rastreabilidade.                |
| Política de Revisão Periódica de Risco             | Sim       | Toda a organização                     | Frequência mínima; triggers obrigatórios; evidência exigida.                                                  |
| Política de Rastreabilidade de Decisões de Segurança | Opcional  | Organizações sujeitas a auditoria      | Versionamento de classificações; ligação com arquitetura, requisitos e controlos.                            |

### Maturidade e alinhamento
| Framework         | Domínios Relevantes                         | Práticas ou Objetos Cobertos                                  | Avaliação de Maturidade             |
|------------------|----------------------------------------------|----------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Governance → Risk Management                 | Classificação de risco por eixos, integração no SDLC           | **2 / 3**                           |
| OWASP DSOMM      | Risk, Security Requirements, Compliance      | Derivação de requisitos, rastreabilidade, decisão proporcional | **2 / 3** (média dos domínios)      |
| NIST SSDF v1.1   | RM.1, RM.2                                   | Classificação e avaliação de risco                             | **RM.1, RM.2**                      |
| BSIMM13          | Strategy and Metrics                         | SR1.1, SR1.5: decisão por criticidade                          | Contributo parcial                  |
| SLSA v1.0        | Supply Chain Risk Awareness                  | Definição proporcional de requisitos à criticidade             | **Nível 1 / 4**                     |

**Nota de extensão:** user stories, casos práticos, recomendações avançadas e detalhes operacionais completos constam na versão integral deste documento.
---

## Versão integral (corpo completo)

A classificação de criticidade aplicacional proposta neste capítulo segue uma abordagem **pragmática, rápida e iterativa**, adequada a contextos ágeis e com ciclo de vida contínuo. É especialmente útil em organizações onde:

- Existe uma lacuna na gestão formal de risco, ou  
- A abordagem tradicional de GRC não se adequa à realidade do portfólio aplicacional.

Porquê? Porque nem sempre há um alinhamento entre a **capilaridade exigida por GRC** e a **natureza prática dos sistemas de software em desenvolvimento**. Em muitos casos, o modelo organizacional de risco é demasiado genérico ou complexo para apoiar decisões ágeis no contexto das equipas de desenvolvimento.

> Esta proposta, compatível com o conceito de *risk categorization*, está totalmente alinhada com o domínio **Risk Management** do **OWASP SAMM**, com os princípios de **DSOMM**, **SSDF (RM.1)**, **ISO 27005** e **SLSA**, assegurando integração com modelos de maturidade amplamente aceites.

Importa sublinhar: **esta abordagem não substitui métodos formais** de análise de risco (como ISO 27005, NIST 800-30 ou FAIR). O objetivo é garantir que **todas as aplicações recebem, desde o início, uma decisão clara e justificável sobre o seu nível de risco**, evitando dois cenários frequentes:

- **Under-engineering**: aplicações expostas sem controlos mínimos;
- **Over-engineering**: excesso de controlo desnecessário, com desperdício de esforço.

Esta classificação inicial permite aplicar práticas de segurança com **proporcionalidade, rastreabilidade e foco na ação concreta**.

Quando existam **artefactos organizacionais previamente definidos** - como BIA (Business Impact Analysis), DRP (Disaster Recovery Plan), BCP (Business Continuity Plan) ou outras formas de categorização - **estes podem (e devem) ser aproveitados como base factual para a classificação**. Mesmo que não sejam exatos, oferecem uma referência válida e suficiente, conforme descrito no Alternativa - adoção de DRP, BIA ou outras Classificações Existentes.

## 🎯 Modelo proposto: simples, participativo e pragmático

Este manual propõe um modelo de classificação **empírico e simplificado**, inspirado na **OWASP Risk Rating**, mas adaptado a contextos práticos onde a decisão rápida é essencial. O modelo assenta em três eixos principais:

- **E (Exposição)**: acessibilidade externa e vetores de ataque;
- **D (Tipo de Dados)**: sensibilidade, privacidade e enquadramento regulamentar;
- **I (Impacto Potencial)**: consequências técnicas, operacionais e reputacionais em caso de falha ou violação.

Este modelo é influenciado por abordagens amplamente reconhecidas:

- **OWASP SAMM** - domínio *Threat Assessment*, especialmente a atividade A.2 (Assess Risk);
- **OWASP Risk Rating Methodology** - baseada em impacto e probabilidade;
- **NIST 800-30** e **ISO 27005** - que sustentam metodologias formais de análise de risco.

Contudo, assume-se aqui uma abordagem **mais acessível e pragmática**, que privilegia:

- Rapidez de aplicação (poucos minutos por aplicação);
- Participação direta de stakeholders técnicos e de negócio;
- Decisão empírica, iterativa e fácil de rever ao longo do tempo.

> ⚠️ Esta classificação serve apenas como ponto de partida. Sempre que possível, deve existir **ligação formal ao processo de gestão de risco organizacional**.  
> Quando tal processo não existir ou não for adequado ao contexto aplicacional, esta abordagem serve como alternativa viável e eficaz.

Como detalhado em Modelo de Classificação, a classificação por aplicação é feita atribuindo **valores entre 1 e 3 em cada eixo**, com base na perceção informada dos principais stakeholders.

**Quão acessível está a aplicação ou sistema, com base no seu contexto de rede e interface?**

|   |                                                    |
| - | -------------------------------------------------- |
| ☐ | Apenas acessível internamente (sem acesso externo) |
| ☐ | Acessível externamente, mas com autenticação       |
| ☐ | Público (acesso aberto ou não autenticado)         |

---

**Como classifica a natureza e criticidade da informação processada?**

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
| ☐ | Dados públicos, sem sensibilidade ou impacto legal                     |
| ☐ | Dados pessoais, identificáveis, ou confidenciais internos              |
| ☐ | Dados regulados ou altamente sensíveis (bancários, saúde, localização) |

---

**Qual seria o impacto que uma violação teria, em caso extremo, para a organização?**

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
| ☐ | Impacto nulo ou irrelevante                                            |
| ☐ | Impacto limitado, reversível ou com pouco alcance                      |
| ☐ | Impacto elevado: reputacional, regulatório ou financeiro significativo |

---
o valor da Criticidade é determinado pela soma da "quantificação qualitativa" empirica dos 3 eixos:
```md
Criticidade Total (C) = E + D + I
```

A soma aritmética define o nível de criticidade da aplicação:

| Soma | Classificação | Nível de Risco |
| ---- | ------------- | -------------- |
| 3–4  | L1            | Baixo          |
| 5–6  | L2            | Médio          |
| 7–9  | L3            | Elevado        |

> A classificação deve ser revista por segurança, arquitetura ou GRC, considerando:
>
> * Casos regulatórios;
> * Integrações externas;
> * Contextos técnicos relevantes.

---

---

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.

Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo.  
A ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE, tornando inviável a adoção coerente das práticas operacionais e de governação.
:::

# Classificação da Criticidade Aplicacional

Este capítulo define e prescreve **como classificar aplicações segundo a sua criticidade**, de forma a permitir a **aplicação proporcional de requisitos, controlos, validações e evidência de segurança** ao longo de todo o ciclo de vida.

No SbD-ToE, a classificação **não visa rotular tecnologias ou ferramentas**, mas sim **caracterizar o risco aplicacional de forma suficiente para suportar decisões técnicas e organizacionais consistentes**.

Ferramentas de automação e de apoio à decisão (incluindo IA) são tratadas como **parte normal do SDLC moderno** e devem ser consideradas na classificação **sempre que alterem exposição, dados, impacto ou a forma como decisões e validações são realizadas**.  
A sua presença **não cria novas categorias de risco**, mas influencia os **atributos internos do risco** e, consequentemente, os controlos necessários.

Neste capítulo é sugerido um **modelo de classificação simples, direto e economicamente viável**, adequado à maioria dos contextos aplicacionais.  
A organização pode, contudo, optar por um modelo alternativo já existente (por exemplo DRP/BIA ou outro método formal de análise de risco), desde que seja possível **mapear os seus resultados para o contexto do desenvolvimento aplicacional**.

O objetivo central do manual é:
1. **Classificar aplicações de forma consistente**, para assegurar proporcionalidade adequada;  
2. **Disponibilizar mecanismos claros, rápidos e rastreáveis** para o fazer, sem dependência excessiva de processos pesados ou ferramentas específicas.

> 📌 A classificação da criticidade é o ponto de entrada para os capítulos:  
> Capítulo 02 – Requisitos,  
> Capítulo 04 – Arquitetura,  
> Capítulo 07 – CI/CD e  
> Capítulo 10 – Testes.

---

## 🧠 Nota conceptual: risco e atributos

O SbD-ToE trata o **risco como um conceito único**, independentemente da sua origem técnica ou processual.  
O que varia são os **atributos do risco** — como origem, mecanismo, detetabilidade, reprodutibilidade e evidenciabilidade — que influenciam diretamente os requisitos e controlos aplicáveis.

> 📌 Ver: Atributos do Risco

---

## 🧪 Prescrição prática: o quê, quem, como, quando, porquê e para quê

### 📌 O que deve ser feito

1. Classificar a aplicação segundo **exposição, dados sensíveis e impacto**, conforme proposto no manual, ou adotar outro modelo equivalente;
2. Considerar explicitamente como **automação e apoio à decisão (incl. IA)** influenciam os **atributos do risco** relevantes;
3. Documentar a classificação, pressupostos e evidência utilizada;
4. Aplicar controlos mínimos com base no nível atribuído;
5. Rever a classificação em pontos-chave do ciclo de vida;
6. Aplicar critérios formais para aceitação de risco, quando necessário.

---

### ⚙️ Como deve ser feito

- Usar o Modelo de Classificação;  
- Ou um modelo alternativo adotado pela organização (ex.: Adoção de DRP/BIA);  
- Quando existir tooling automatizado/assistivo (incl. IA), **avaliar o seu impacto nos atributos do risco** e calibrar E/D/I em conformidade;  
- Incorporar o Ciclo de Vida da Classificação de Risco;  
- Aplicar os Critérios para Aceitação de Risco;  
- Considerar ameaças reais através do Mapeamento de Ameaças por Nível de Risco;  
- Registar decisões em repositório versionado, ferramenta de risco ou documentação rastreável.

---

### 📆 Quando aplicar

- Durante a fase inicial do projeto ou definição de arquitetura;
- Sempre que houver alterações relevantes: novas funcionalidades, dados, exposição ou integrações;
- Quando se introduzam ou alterem mecanismos de automação/assistência (incl. IA) com impacto nos atributos do risco;
- Em releases principais ou milestones críticos (ex.: produção);
- Após incidentes de segurança relevantes;
- No mínimo a cada **6 meses** ou **em cada revisão de arquitetura ou roadmap de segurança**.

> A revisão periódica da classificação de risco suporta diretamente práticas de **maturidade intermédia** em **SAMM**, **DSOMM** e **SSDF**.

---

### 👥 Quem está envolvido e como

| Papel                | Contributo                                                                 |
| -------------------- | -------------------------------------------------------------------------- |
| Dev / Tech Lead      | Propor classificação, identificar alterações relevantes                    |
| AppSec / Segurança   | Validar modelo aplicado, ajustar nível de risco, aplicar matriz             |
| Arquitetura          | Rever implicações técnicas, fluxos e exposição                               |
| Produto / Gestão     | Aprovar aceitação de risco, avaliar impacto de exceções                     |
| GRC / Compliance     | Assegurar rastreabilidade e alinhamento normativo                           |
| QA / Testes          | Validar cumprimento de requisitos por nível de risco antes do go-live       |

> ✅ *Todos os contributos devem ser registados e versionados para efeitos de rastreabilidade e auditoria.*

---

### 🎯 Porquê / Para quê

- Garantir proporcionalidade nos controlos de segurança aplicados;
- Reduzir custos evitando sobreproteção ou exposição desnecessária;
- Suportar conformidade normativa e auditorias;
- Informar decisões estratégicas (roadmap, orçamentação, outsourcing);
- Promover melhoria contínua e visibilidade do risco.

> 📌 A aplicação proporcional de controlos pode ser guiada pela  
> Matriz de Controlos por Risco.

---

## 🧪 Ciclo de Vida da Classificação de Risco

A classificação de risco **não é um evento único**, mas um processo contínuo. Deve ser revista:

- Em alterações de arquitetura, exposição, dados ou automação/assistência;
- Antes de releases críticos;
- Periodicamente (ex.: a cada 6 meses);
- Após incidentes ou deteções relevantes.

> 📌 Ver: Ciclo de Vida da Classificação de Risco

Esta reavaliação contínua assegura que os controlos aplicados se mantêm proporcionais e atualizados.

---

## ✅ Critérios para Aceitação de Risco

Nem todos os riscos identificados requerem mitigação adicional. Alguns podem ser **aceites formalmente**, desde que respeitem critérios claros:

- Compatibilidade com o nível L1–L3 da aplicação;
- Valor residual dentro dos limiares definidos;
- Evidência suficiente de controlos aplicados;
- Documentação formal da decisão e prazo de revisão.

> 📌 Ver: Critérios para Aceitação de Risco

---

## 🛡️ Mapeamento de Ameaças a Riscos

Para garantir que a classificação reflete a realidade técnica, é essencial mapear ameaças conhecidas (ex.: STRIDE, MITRE ATT&CK) ao modelo de risco adotado.

> 📌 Ver: Mapeamento de Ameaças por Nível de Risco

---

## 📜 Políticas Organizacionais Relevantes

A aplicação prática deste capítulo requer políticas formais que assegurem normalização, rastreabilidade e governação do risco:

| Política                                        | Obrigatória? | Aplicação                                | Conteúdo mínimo esperado                                                             |
| ----------------------------------------------- | ------------ | ---------------------------------------- | ------------------------------------------------------------------------------------ |
| Política de Classificação de Risco Aplicacional | ✅ Sim        | Todos os projetos e equipas de produto   | Modelo de classificação; momentos de aplicação; registo formal.                      |
| Política de Aceitação de Risco Residual         | ✅ Sim        | Segurança, gestão, donos de produto      | Critérios de aceitação; responsáveis; validade; evidência rastreável.                |
| Política de Revisão Periódica de Risco          | ✅ Sim        | Toda a organização                       | Frequência mínima; triggers obrigatórios; documentação.                              |
| Política de Rastreabilidade de Decisões         | ⚠️ Opcional  | Contextos regulados ou auditáveis        | Versionamento; ligação a arquitetura, requisitos e controlos.                        |

> 📌 Ver detalhes no **anexo de políticas do manual**.

---

## 🎯 Objetivo

Este documento define um **modelo unificado de caracterização do risco** no contexto do **Security by Design – Theory of Everything (SbD-ToE)**.

O objetivo **não é criar categorias distintas de risco** (ex.: “risco técnico” vs. “risco de processo”), mas sim estabelecer um **conjunto de atributos internos** que permitam:

- descrever rigorosamente qualquer risco relevante;
- compreender a sua origem e mecanismo de materialização;
- determinar **requisitos, controlos e validações proporcionais**;
- manter o modelo **intemporal**, extensível e tecnologicamente neutro.

Este modelo aplica-se a **todo o ciclo de vida da aplicação** e a **todos os capítulos do manual**.

---

## 🧠 Princípio fundamental

No SbD-ToE, **o risco é tratado como um conceito único e indivisível**.

Um risco pode ter origem técnica, processual, organizacional ou externa, mas **o seu impacto materializa-se sempre no sistema entregue**, na sua operação ou na sua conformidade.

O que varia **não é o tipo de risco**, mas sim:
- **como surge**;
- **como se manifesta**;
- **como pode (ou não) ser observado, validado e mitigado**.

Essas variações são capturadas através de **atributos do risco**.

---

## 🧩 Modelo de atributos do risco

Cada risco identificado no âmbito do SbD-ToE deve ser descrito, explícita ou implicitamente, através dos atributos abaixo.

### 1️⃣ Origem do risco

Identifica **onde o risco se introduz** no sistema ou no processo.

Valores típicos (não exclusivos):
- Técnica (arquitetura, código, configuração)
- Processual (decisão, omissão, automação)
- Organizacional (governação, responsabilidades)
- Externa (fornecedores, dependências, serviços)

> Exemplo:  
> Um erro introduzido por geração automática de código tem **origem processual**, mesmo que se materialize como vulnerabilidade técnica.

---

### 2️⃣ Mecanismo de introdução

Descreve **como o risco é introduzido**.

Exemplos comuns:
- Vulnerabilidade técnica conhecida
- Erro humano
- Omissão de análise ou validação
- Decisão inadequada
- Confiança excessiva em resultados automatizados
- Configuração implícita ou herdada

Este atributo é crítico para definir **controlos preventivos vs. detetivos**.

---

### 3️⃣ Superfície de materialização

Indica **onde o impacto se manifesta** quando o risco se concretiza.

Valores típicos:
- Produto (software, dados, interfaces)
- Operação (disponibilidade, integridade, continuidade)
- Conformidade (legal, regulatória, contratual)
- Reputação / negócio

Um mesmo risco pode materializar-se em **mais do que uma superfície**.

---

### 4️⃣ Detetabilidade

Caracteriza **a facilidade com que o risco pode ser identificado** antes ou após a sua materialização.

- Alta – facilmente detetável por testes ou controlos objetivos
- Média – requer análise especializada ou correlação
- Baixa – dificilmente observável sem incidentes ou auditorias profundas

Riscos de baixa detetabilidade exigem **controlos mais fortes a montante**.

---

### 5️⃣ Reprodutibilidade

Indica se o comportamento associado ao risco é:

- Determinístico – reproduzível de forma consistente
- Parcialmente determinístico – dependente de contexto
- Não determinístico – resultados variáveis para o mesmo input

Este atributo é particularmente relevante em contextos de:
- automação avançada;
- sistemas de apoio à decisão;
- análise baseada em heurísticas.

Baixa reprodutibilidade **aumenta o risco operacional e de validação**.

---

### 6️⃣ Evidenciabilidade

Descreve **o grau em que o risco e a sua mitigação podem ser suportados por evidência verificável**.

- Elevada – evidência objetiva, versionada e auditável
- Limitada – evidência indireta ou interpretativa
- Fraca – baseada em plausibilidade ou confiança implícita

No SbD-ToE, **risco sem evidência adequada não pode ser considerado mitigado**, independentemente da sofisticação da análise.

---

## 🧪 Exemplo ilustrativo (não normativo)

Um risco identificado através de uma análise assistida por IA pode ser caracterizado como:

- Origem: Processual  
- Mecanismo: Decisão assistida com validação insuficiente  
- Superfície: Produto e conformidade  
- Detetabilidade: Média  
- Reprodutibilidade: Baixa  
- Evidenciabilidade: Limitada  

👉 A consequência **não é rejeitar a ferramenta**, mas **exigir controlos adicionais**, como:
- revisão humana explícita;
- validação empírica independente;
- registo da decisão e da evidência utilizada.

Este exemplo é equivalente, do ponto de vista do modelo, a:
- um ORM mal configurado;
- uma pipeline CI com gates implícitos;
- um scanner com regras excessivamente permissivas.

---

## 🔗 Relação com outros elementos do SbD-ToE

- A **classificação L1–L3** continua a refletir **impacto e criticidade do sistema**, não atributos internos do risco.
- Os **atributos do risco** influenciam:
  - requisitos de segurança (Cap. 02);
  - threat modeling (Cap. 03);
  - decisões arquiteturais (Cap. 04);
  - critérios de aceitação e evidência;
  - governação e auditoria (Cap. 14).

Este modelo permite que o manual evolua **sem necessidade de redefinir conceitos-base** sempre que surgem novas formas de automação ou abstração.

---

## ✅ Conclusão

O SbD-ToE trata o risco como um **conceito único**, rico em atributos, capaz de capturar tanto riscos técnicos clássicos como riscos introduzidos por práticas modernas de desenvolvimento.

Esta abordagem:
- evita fragmentação conceptual;
- suporta definição proporcional de controlos;
- mantém o manual intemporal;
- reforça a exigência de responsabilidade, validação e evidência.

Os capítulos seguintes assumem este modelo como **pressuposto canónico**.

---

# 📎 Modelo de Classificação por Eixos de Risco

## 🎯 Objetivo

Fornecer um modelo **prático, proporcional e aplicável** ao contexto do desenvolvimento de software, para avaliar o **nível de risco de uma aplicação** com base em três eixos fundamentais:

- **Exposição (E)**
- **Tipo de Dados (D)**
- **Impacto Potencial (I)**

Este modelo permite decisões rápidas e documentadas sobre os controlos mínimos de segurança a aplicar, com rastreabilidade ao longo do ciclo de vida.

---

## 🧠 Enquadramento conceptual

No *Security by Design – Theory of Everything (SbD-ToE)*, o risco é tratado como um **conceito único**, caracterizado por múltiplos **atributos internos** (origem, mecanismo, detetabilidade, evidenciabilidade, reprodutibilidade, entre outros).

O modelo **E/D/I** constitui uma **projeção simplificada e operacional** desse risco, focada nos fatores que mais diretamente influenciam:
- a exposição técnica do sistema,
- a natureza dos dados tratados,
- e o impacto potencial de uma falha ou abuso.

Este modelo **não pretende capturar a totalidade do risco**, mas fornecer uma base consistente e suficiente para classificação aplicacional e aplicação proporcional de controlos.

---

## 🧮 Fórmula do Modelo Simplificado

A classificação de risco é feita com base na soma dos três eixos:

**Risco Classificado (R) = E + D + I**

**Onde:**

- **E (Exposição)**: Grau de acessibilidade técnica e operacional da aplicação
- **D (Tipo de Dados)**: Sensibilidade, valor e enquadramento legal dos dados processados
- **I (Impacto Potencial)**: Consequência expectável de uma falha, violação ou decisão incorreta

### Classificação por Pontuação

| Soma Total | Classificação de Risco | Código |
|------------|------------------------|--------|
| 3–4        | **Baixo**              | L1     |
| 5–6        | **Médio**              | L2     |
| 7–9        | **Elevado**            | L3     |

Esta classificação representa o **nível mínimo de rigor** a aplicar em requisitos, controlos, validações e evidência.

---

## 🧱 Detalhe dos Eixos

### 🧭 Exposição (E)

Avalia quão acessível está a aplicação ou sistema, considerando superfícies de ataque, interfaces e contexto de rede.

| Nível | Descrição                                          | Pontos |
|-------|----------------------------------------------------|--------|
| 1     | Apenas acessível internamente (sem acesso externo) | 1      |
| 2     | Acessível externamente, com autenticação           | 2      |
| 3     | Público ou amplamente exposto (acesso aberto ou não autenticado) | 3 |

---

### 📑 Tipo de Dados (D)

Classifica a natureza, sensibilidade e enquadramento legal dos dados processados.

| Nível | Descrição                                                              | Pontos |
|-------|------------------------------------------------------------------------|--------|
| 1     | Dados públicos ou sem sensibilidade                                    | 1      |
| 2     | Dados pessoais, identificáveis ou confidenciais internos               | 2      |
| 3     | Dados regulados ou altamente sensíveis (ex.: saúde, financeiros, localização) | 3 |

---

### ⚠️ Impacto Potencial (I)

Avalia o impacto expectável para a organização caso o risco se materialize.

| Nível | Descrição                                                                  | Pontos |
|-------|----------------------------------------------------------------------------|--------|
| 1     | Impacto nulo ou irrelevante                                                 | 1      |
| 2     | Impacto limitado, localizado ou reversível                                 | 2      |
| 3     | Impacto elevado: financeiro, regulatório, operacional ou reputacional significativo | 3 |

---

## 🧩 Critérios complementares em contextos de automação e apoio à decisão

A utilização de mecanismos de automação ou apoio à decisão (incluindo IA) **não cria novos eixos de risco**, nem implica, por si só, alteração da criticidade da aplicação.

Esses mecanismos devem ser considerados **exclusivamente quando modificam atributos relevantes do risco**, nomeadamente exposição, tipo de dados tratados ou impacto efetivo das decisões e ações realizadas.

### 🧭 Regra de aplicação obrigatória

A reavaliação dos eixos **E**, **D** e **I** é **obrigatória** sempre que a automação ou apoio à decisão:

- introduza nova superfície de exposição ou integração externa;
- envolva tratamento adicional de dados pessoais, regulados, segredos ou informação confidencial;
- aumente delegação, alcance ou velocidade de decisões com impacto real no sistema, nos dados ou no negócio.

Sempre que **qualquer uma destas condições se verifique**, a equipa **deve** ajustar os eixos afetados e **registar explicitamente o racional da decisão**.

A manutenção da classificação original **só é aceitável** quando exista:
- validação humana obrigatória e efetiva;
- controlo explícito dos outputs automatizados;
- evidência suficiente de que os atributos do risco não foram alterados.

### 🔎 Orientação prática mínima

| Situação observada                                                                 | Ajuste esperado |
|-----------------------------------------------------------------------------------|-----------------|
| Integração com serviços externos de automação ou IA                                | Avaliar E       |
| Envio de dados pessoais, regulados ou IP em prompts, contexto ou artefactos        | D ≥ 2           |
| Execução automática de código, infraestrutura ou decisões sem revisão humana       | I = 3           |
| Resultados não determinísticos aceites como evidência final                        | I = 3           |

> 📌 Esta orientação é prescritiva quanto à necessidade de avaliação, não quanto ao resultado final, que deve ser sempre contextual e documentado.

---

## 🔎 Porquê somar os eixos?

A opção pela **soma simples** dos eixos privilegia:

- simplicidade operacional;
- facilidade de adoção por equipas técnicas;
- consistência entre projetos;
- clareza e transparência em auditorias.

Modelos mais complexos foram considerados, mas tendem a introduzir variabilidade excessiva e dificultar a padronização organizacional.

Este modelo é empírico e prescritivo, adequado a contextos ágeis e DevSecOps, mantendo proporcionalidade e rastreabilidade.

---

## ⚠️ Considerações finais

- Este modelo **não substitui** threat modeling nem análises de risco formais;
- Deve ser usado como **mecanismo rápido de classificação** e ponto de partida para decisões;
- Deve ser revisto sempre que ocorram alterações relevantes a funcionalidades, dados, exposição ou pressupostos de processo.

Apesar da sua simplicidade, o modelo permite determinar, de forma rápida e fundamentada, **o nível de rigor de segurança a aplicar**, assegurando coerência ao longo do ciclo de vida.

---

## 🔗 Ligações úteis

- Modelo alternativo: Adoção de classificações existentes (DRP/BIA)
- Capítulo 01 – Classificação da Criticidade Aplicacional

---

# 🛠️ Ciclo de Vida da Classificação de Risco

A gestão de risco em software não deve ser encarada como um evento pontual, mas sim como um **processo iterativo e evolutivo** ao longo do ciclo de vida da aplicação.

No SbD-ToE, o risco é tratado como um **conceito único**, cuja relevância e severidade podem variar ao longo do tempo em função de alterações técnicas, organizacionais ou processuais.  
A capacidade de **identificar, reavaliar e tratar riscos de forma contextual** é determinante para garantir que os controlos aplicados permanecem proporcionais, eficazes e justificados.

Este ficheiro descreve as **práticas mínimas** para integrar a classificação e reavaliação de risco no ciclo de vida da aplicação.

---

## 📅 Integração por Fase do Ciclo de Vida

| Fase                     | Ações de Gestão de Risco                                                                 |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| Planeamento / Requisitos | Identificação inicial de riscos com base em impacto, dados, exposição, arquitetura prevista e pressupostos de processo |
| Design / Arquitetura     | Avaliação preliminar dos riscos e respetivos **atributos**; mapeamento para controlos de arquitetura |
| Desenvolvimento          | Reavaliação de riscos existentes face a novas funcionalidades; validação de pressupostos e requisitos de controlo |
| Testes / Validação       | Confirmação da aplicação dos controlos definidos; verificação de evidência e revisão de risco pré-release |
| Release / Operacional    | Registo formal de aceitação de risco residual; monitorização contínua e deteção de regressões |

> 📌 Em todas as fases, alterações nos **atributos do risco** (ex.: detetabilidade, evidenciabilidade ou reprodutibilidade) devem desencadear reavaliação explícita.

---

## 📅 Triggers para Reavaliação de Risco

O risco deve ser reavaliado sempre que ocorra qualquer evento que altere o seu **perfil ou atributos**, nomeadamente:

- Introdução de novas funcionalidades ou fluxos relevantes;
- Alterações à arquitetura (ex.: nova exposição API, integrações externas, mudança de trust boundaries);
- Mudanças de contexto legal, regulatório ou contratual;
- Introdução ou modificação de mecanismos de automação ou apoio à decisão (incluindo IA), **quando estes alterem pressupostos de validação, evidência ou reprodutibilidade**;
- Deteção de vulnerabilidades críticas ou recorrentes;
- Resultados relevantes de auditorias, testes de segurança ou avaliações independentes.

---

## 👥 Responsabilidades ao Longo do Ciclo

| Papel                  | Responsabilidades na gestão de risco                                                |
| ---------------------- | ----------------------------------------------------------------------------------- |
| Product Owner          | Avaliar impacto do risco no negócio e na priorização                                 |
| Arquitetura / Dev Lead | Aplicar o modelo de risco, identificar alterações de atributos e propor controlos   |
| Sec / AppSec           | Validar classificação, controlos aplicados e risco residual                          |
| Equipa de Operações    | Monitorizar risco em runtime e detetar regressões de controlo ou contexto            |

> ✅ As decisões e revisões de risco devem ser sempre **registadas, atribuídas a responsáveis e rastreáveis**.

---

## 🛠️ Mecanismos de Suporte

A operacionalização do ciclo de vida do risco pode ser suportada por:

- Integração da classificação e estado do risco em ferramentas de backlog (ex.: Jira);
- Registo versionado de riscos, pressupostos e decisões (ex.: YAML ou Markdown em Git);
- Dashboards de risco baseados em métricas objetivas e scoring transparente;
- Gates explícitos de validação de risco em pipelines de CI/CD, proporcionais ao nível L1–L3.

---

## ⚖️ Ligação com os Limiares L1–L3

O ciclo de vida da classificação de risco deve ser aplicado de forma proporcional ao **nível de criticidade da aplicação**:

- Em aplicações **L3**, a reavaliação de risco deve ser obrigatória a cada release ou alteração relevante;
- Em aplicações **L2**, deve ocorrer sempre que existam mudanças significativas de arquitetura, dados ou processo;
- Em aplicações **L1**, pode ser baseada em eventos de risco identificados ou num calendário fixo.

Esta proporcionalidade permite equilíbrio entre rigor, custo operacional e eficácia.

---

## 🚀 Recomendações para Maturidade

- Formalizar a reavaliação cíclica de risco através de checklist, workflow ou policy;
- Monitorizar explicitamente o risco residual ao longo do tempo;
- Integrar decisões de risco com registo de auditoria (*audit trail*);
- Envolver decisores não técnicos sempre que o risco tenha impacto legal, reputacional ou estratégico.

> O risco não é um valor estático: é um **processo vivo**, que deve acompanhar a evolução da aplicação, do contexto e das práticas de desenvolvimento.

---

# 🛠️ Critérios para Aceitação de Risco

A aceitação formal de risco é uma etapa fundamental no processo de gestão de risco e deve ser suportada por **critérios claros, objetivos e documentados**.

No *Security by Design – Theory of Everything (SbD-ToE)*, aceitar risco **não significa ignorá-lo**, mas sim assumir explicitamente que, dadas as condições atuais, o risco residual é considerado tolerável para o nível de criticidade da aplicação.

Este ficheiro define os **critérios mínimos** para aceitação de risco, alinhados com o modelo SbD-ToE e com os níveis aplicacionais **L1–L3**.

---

## 🧠 Princípio fundamental

Um risco **só pode ser aceite** quando:

- os seus **atributos são compreendidos**;
- os **controlos aplicados são conhecidos e verificáveis**;
- existe **evidência suficiente** da sua eficácia;
- o impacto residual é **compatível com o nível da aplicação**.

Sempre que estes pressupostos não se verifiquem, a aceitação de risco **não é válida**, independentemente da urgência, custo ou maturidade da equipa.

---

## 📌 Parâmetros para avaliação

A decisão de aceitação de risco deve considerar, no mínimo:

- **Valor residual do risco** (após aplicação de controlos);
- **Nível de criticidade da aplicação** (L1, L2 ou L3);
- **Tipo de impacto associado** (negócio, legal, operacional, reputacional);
- **Confiança nos controlos existentes**, incluindo a sua verificabilidade;
- **Reversibilidade do impacto** ou capacidade de rollback;
- **Disponibilidade de planos de contingência**;
- **Evidência objetiva** que suporte a avaliação efetuada.

---

## ⚖️ Limiares de aceitação por nível

| Nível da aplicação         | Risco Residual Máximo Aceitável | Observações                                     |
| -------------------------- | ------------------------------- | ----------------------------------------------- |
| **L1** (baixa criticidade) | ≤ 9 (médio)                     | Aceitação informal possível                     |
| **L2** (média criticidade) | ≤ 6 (baixo a médio)             | Requer validação formal e registo               |
| **L3** (alta criticidade)  | ≤ 4 (baixo)                     | Exceção apenas com aprovação de gestor de risco |

> 📌 Estes limiares assumem **controlo efetivo e evidência adequada**.  
> A ausência de evidência invalida automaticamente a aceitação.

---

## 🧩 Condições adicionais em contextos de automação e apoio à decisão

A utilização de automação ou apoio à decisão (incluindo IA) **não invalida por si só** a aceitação de risco.

Contudo, a aceitação **fica condicionada** quando esses mecanismos alteram atributos relevantes do risco, nomeadamente:

- **reduzem a detetabilidade** de erros ou falhas;
- **diminuem a evidenciabilidade** das decisões;
- **introduzem não determinismo** relevante;
- **executam ações com impacto real** sem validação humana obrigatória.

### ❌ Situações em que a aceitação de risco **não é permitida**

Não é aceitável aceitar risco quando:

- decisões ou ações automatizadas com impacto real são aplicadas **sem revisão humana efetiva**;
- os resultados não são reprodutíveis ou não podem ser validados de forma independente;
- não existe evidência clara do funcionamento correto dos controlos;
- o impacto potencial é legal, regulatório ou reputacional significativo;
- o risco se enquadra em aplicação **L3** e depende exclusivamente de confiança implícita no mecanismo automatizado.

---

## 🧾 Exemplos de critérios formais de aceitação válidos

A aceitação pode ser considerada quando, cumulativamente:

- o risco residual é avaliado como **baixo** por pelo menos dois perfis independentes (ex.: AppSec + Product Owner);
- existem **controlos compensatórios** ativos e monitorizados;
- o impacto é **estritamente operacional interno** e existe plano de recuperação validado;
- a automação é **assistiva**, com validação humana obrigatória antes de qualquer efeito real;
- a decisão está **documentada**, com responsável identificado e **prazo de revisão definido**.

---

## 🏡 Processo recomendado de aceitação

1. **Identificação clara** do risco e dos seus atributos relevantes.
2. Validação dos controlos aplicados e da evidência disponível.
3. Avaliação do risco residual face aos limiares L1–L3.
4. Decisão formal de aceitação, rejeição ou mitigação adicional.
5. Registo da decisão, incluindo racional, responsável e data de revisão.
6. Reavaliação obrigatória sempre que ocorram alterações relevantes.

---

## 📌 Recomendações finais

- Formalizar uma **policy de aceitação de risco aplicacional**, com papéis e responsabilidades definidos.
- Integrar decisões de aceitação nos **artefactos de release e governação**.
- Registar riscos aceites num repositório com **visibilidade GRC**.
- Nunca aceitar risco **sem evidência suficiente**, independentemente do nível da aplicação.

> A aceitação de risco não é uma omissão de responsabilidade,  
> mas uma **decisão consciente, informada e rastreável**.

---

# 🛠️ Análise de Risco Residual

O **risco residual** representa o risco que **permanece após a aplicação efetiva dos controlos definidos**, e constitui a base factual para qualquer decisão consciente de aceitação, mitigação adicional ou rejeição.

No *Security by Design – Theory of Everything (SbD-ToE)*, o risco residual **não é um valor abstrato**, mas o resultado de uma avaliação contextual que considera:
- o nível de criticidade da aplicação (L1–L3),
- os **atributos do risco**,
- a **eficácia real dos controlos**,
- e a **evidência disponível**.

Este ficheiro complementa o modelo de classificação e aceitação de risco, introduzindo a lógica de **“antes e depois dos controlos”**, de forma operacional e auditável.

---

## 🔢 Definições fundamentais

- **Risco Bruto (inerente)**  
  Risco identificado **antes da aplicação de controlos**, resultante da combinação de exposição, dados e impacto.

- **Risco Residual**  
  Risco remanescente **após a aplicação efetiva dos controlos**, considerando:
  - redução real de impacto,
  - aumento de detetabilidade,
  - melhoria de evidenciabilidade,
  - e limitação de alcance ou superfície.

- **Risco Aceitável**  
  Limite máximo de risco residual tolerado pela organização, dependente do nível da aplicação (L1–L3).

> 📌 No SbD-ToE, o risco residual **não resulta de uma subtração matemática simples**, mas de uma **reavaliação consciente dos atributos do risco após controlo**.

---

## 🧠 Relação com o modelo E/D/I

A análise de risco residual deve ser sempre coerente com a classificação **E/D/I** da aplicação:

- os controlos **não alteram retroativamente a exposição ou os dados tratados**;
- os controlos podem:
  - reduzir impacto,
  - limitar probabilidade de exploração,
  - aumentar deteção,
  - e melhorar evidência.

Sempre que a aplicação de controlos **não altere materialmente os atributos relevantes do risco**, o risco residual **permanece elevado**, mesmo que existam controlos “teóricos”.

---

## 🧩 Avaliação prática do risco residual

A avaliação do risco residual deve responder explicitamente às seguintes perguntas:

- Os controlos estão **implementados e ativos**?
- A sua eficácia é **verificável e evidenciável**?
- Existe **validação humana efetiva**, quando aplicável?
- O comportamento residual é **determinístico e reproduzível**?
- O impacto residual é **compatível com o nível da aplicação**?

A ausência de resposta positiva a qualquer uma destas questões **impede a aceitação válida do risco**.

---

## 📝 Exemplo ilustrativo (não normativo)

**Cenário:** API exposta com autenticação forte

| Dimensão avaliada            | Antes dos controlos | Após controlos efetivos                  |
|-----------------------------|---------------------|------------------------------------------|
| Exposição (E)               | 3                   | 3 (permanece exposta)                    |
| Tipo de Dados (D)           | 2                   | 2                                        |
| Impacto (I)                 | 3                   | 2 (limitação de abuso, rate limiting)    |
| Detetabilidade              | Baixa               | Alta (alertas, logging)                  |
| Evidenciabilidade           | Limitada            | Elevada (logs, métricas)                 |

👉 O risco residual é **reduzido**, mas **não eliminado**.  
A sua aceitação depende do nível da aplicação e da evidência disponível.

---

## ⚖️ Papel do risco residual na decisão

O risco residual deve ser comparado com os **limiares de aceitação definidos por nível de aplicação**:

| Nível da Aplicação         | Risco Residual Máximo Aceitável |
|---------------------------|----------------------------------|
| **L1** (baixa criticidade) | até 9                            |
| **L2** (média criticidade) | até 6                            |
| **L3** (alta criticidade)  | até 4                            |

> 📌 Estes valores **assumem evidência adequada e controlo efetivo**.  
> Sem evidência suficiente, o risco residual **não pode ser considerado baixo**, independentemente do valor estimado.

---

## ❌ Situações em que o risco residual **não é aceitável**

Não é aceitável considerar risco residual como tolerável quando:

- os controlos não estão comprovadamente ativos;
- a decisão depende exclusivamente de confiança implícita em automação ou tooling;
- os resultados não são reprodutíveis ou verificáveis;
- existe impacto legal, regulatório ou reputacional significativo;
- a aplicação é **L3** e o risco residual depende de validação não determinística.

---

## 🔄 Integração com o ciclo de vida e com GRC

- O risco residual deve ser **reavaliado sempre que ocorra alteração relevante**:
  - arquitetura,
  - dados,
  - exposição,
  - automação ou processo.
- Deve integrar:
  - gates de release,
  - artefactos de revisão de segurança,
  - e sistemas de GRC com thresholds explícitos.
- O risco residual **não é permanente**: tem prazo, contexto e responsáveis.

---

## 📌 Recomendação final

Toda a decisão de aceitação de risco residual deve ser:

- **formalmente registada**;
- **justificada com evidência técnica**;
- **compatível com o nível da aplicação**;
- **limitada no tempo e sujeita a reavaliação**.

> O risco residual não é um “resto inevitável”,  
> é uma **decisão consciente sobre o que a organização está disposta a assumir, aqui e agora**.

---

# 📊 Matriz de Controlos Mínimos por Nível de Risco

Esta matriz define o **patamar mínimo de controlos de segurança esperados**, por domínio técnico, em função do **nível de risco da aplicação (L1–L3)**, conforme determinado no Capítulo 01.

Os controlos aqui indicados constituem uma **baseline obrigatória** para cada nível de risco e devem ser entendidos como **mínimos exigíveis**, não como um limite máximo de aplicação.

A matriz pode ser usada:
- como referência técnica independente;
- como base para critérios de release;
- como input para modelos de aceitação de risco;
- como instrumento de controlo, auditoria ou KPI organizacional.

---

## 🧠 Enquadramento normativo

No *Security by Design – Theory of Everything (SbD-ToE)*, o nível de risco da aplicação determina **o grau mínimo de rigor** esperado na aplicação de controlos de segurança.

Contudo:

- o nível **L1–L3** resulta de uma **projeção simplificada** do risco (modelo E/D/I);
- os **atributos do risco** (detetabilidade, evidenciabilidade, reprodutibilidade, delegação, impacto real) podem exigir **reforços adicionais**;
- a ausência de evidência adequada **invalida a aplicação efetiva do controlo**, mesmo que este esteja “previsto”.

Esta matriz deve, por isso, ser aplicada **em conjunto** com:
- o modelo de classificação de risco;
- os critérios de aceitação;
- a análise de risco residual;
- e o ciclo de vida do risco.

---

## 🛠️ Matriz de Controlos por Nível de Risco

| Domínio                          | Risco Baixo (L1)                              | Risco Médio (L2)                                           | Risco Elevado (L3)                                                      |
|----------------------------------|-----------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|
| Requisitos (Cap. 2)              | ASVS N1 (adaptado)                            | ASVS N2 + critérios formais                                 | ASVS N2/N3 completo + validação por segurança                            |
| Threat Modeling (Cap. 3)         | Informal ou omitido                           | Sessões colaborativas regulares                             | Formal com DFDs + STRIDE e registo                                       |
| Arquitetura Segura (Cap. 4)      | Padrões mínimos                               | Revisão técnica + zonas de confiança                        | Revisão formal + documentação de mitigação                               |
| Dependências (Cap. 5)            | `npm audit` / `dotnet list`                   | SCA com política de severidade                              | SCA automatizado + SBOM + alertas                                        |
| Desenvolvimento (Cap. 6)         | Linters + revisão básica                      | Guias + regras de PR específicas                            | Revisão obrigatória + práticas reforçadas de revisão segura              |
| CI/CD (Cap. 7)                   | Credenciais protegidas                        | Validação de ambientes e segredos                           | Proveniência, SLSA + controlos de integridade                            |
| IaC (Cap. 8)                     | Scripts revistos manualmente                  | Scanners (ex.: tfsec)                                       | Policies formais + enforcement obrigatório no pipeline                  |
| Containers (Cap. 9)              | Imagens fiáveis + updates                     | Hardening + scanning de imagem                              | Assinatura, política formal, proteção em runtime                          |
| Testes de Segurança (Cap. 10)    | Checklists manuais                            | SAST + DAST pontuais                                        | Fuzzing, regressão, DAST contínuo                                         |
| Deploy Seguro (Cap. 11)          | Checklist + reversibilidade básica            | Aprovação dupla + controlo de versões                       | Processo formal de validação de segurança                                 |
| Operações (Cap. 12)              | Logging local                                 | Alertas básicos + SIEM leve                                 | Integração com IRP + deteção em tempo real                                |
| Formação (Cap. 13)               | Sessão de onboarding breve                    | Formação anual + sessões práticas                           | Treino formal + avaliações periódicas                                    |
| Governança (Cap. 14)             | Cláusulas simples de segurança                | Templates com conformidade                                  | Requisitos por risco + validação antes do onboarding                     |

---

## ⚠️ Regra de reforço obrigatório de controlos

> ⚠️ **Nota normativa essencial**

Sempre que os **atributos do risco** indiquem:
- baixa detetabilidade;
- baixa evidenciabilidade;
- comportamento não determinístico;
- elevada delegação ou execução automática com impacto real  
  (incluindo automação avançada ou apoio à decisão),

devem ser aplicados **controlos equivalentes ao nível imediatamente superior**,  
**independentemente** da classificação L1–L3 inicialmente atribuída.

Esta regra aplica-se a qualquer tecnologia ou prática de desenvolvimento e **não depende da presença explícita de IA**.

---

## 🔄 Atualização e manutenção da matriz

Esta matriz deve ser:
- revista sempre que ocorram alterações relevantes no manual;
- ajustada ao contexto regulatório e organizacional;
- mantida coerente com as políticas internas de segurança e risco.

A sua utilização não dispensa:
- análise contextual;
- produção de evidência;
- registo formal das decisões tomadas.

---

## 📌 Nota final

Esta matriz **não define “o máximo a fazer”**,  
define **o mínimo aceitável** para cada nível de risco.

A segurança efetiva resulta da **aplicação consciente, evidenciável e proporcional** dos controlos —  
não da mera conformidade com uma tabela.

---

## 🔗 Ligações úteis

- Capítulo 01 – Classificação da Criticidade Aplicacional
- Modelo de Classificação por Eixos (E/D/I)
- Critérios para Aceitação de Risco
- Análise de Risco Residual

---

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

---

# 📎 Modelo alternativo via Adoção de Classificações Existentes (e.g. DRP/BIA)


## 🎯 Objetivo

Orientar a reutilização de classificações já existentes - nomeadamente **DRP (Disaster Recovery Plan)** e **BIA (Business Impact Analysis)** - como base para a **classificação de risco aplicacional**, evitando duplicação de esforço e promovendo consistência na avaliação de criticidade.

---

## 📘 Contexto

Muitas organizações já realizam uma **classificação de impacto** com base na continuidade do negócio, no âmbito de processos como o DRP ou BIA, ou outras. Essas classificações incluem geralmente atributos como:

- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)
- Impacto financeiro, reputacional ou operacional
- Prioridade de recuperação

Embora não tenham foco direto na segurança, estes dados são **fortemente correlacionáveis** com o risco aplicacional e podem ser utilizados como **input inicial ou justificação** da classificação de risco prescrita no SbD-ToE.

---

## 🔁 Mapeamento prático entre DRP/BIA e risco de segurança

| Classificação DRP/BIA     | Interpretação no contexto SbD-ToE |
|---------------------------|------------------------------------|
| **Crítico**               | Risco Elevado                     |
| **Importante / Médio**    | Risco Médio                       |
| **Não essencial / Baixo** | Risco Baixo                       |

> ⚠️ Este mapeamento deve ser **confirmado por análise de segurança**, considerando a natureza dos dados e exposição da aplicação.

---

## 📝 Exemplo prático

Um sistema classificado como **Crítico** no DRP, com os seguintes parâmetros:

- **RTO:** < 4h  
- **RPO:** < 1h  
- Dados pessoais e de faturação  
- Integração com terceiros  
- Exposto à internet

→ Deve ser automaticamente classificado como **Risco Elevado**, exigindo:

- Threat Modeling formal  
- Requisitos de segurança completos  
- Testes automatizados contínuos  
- Monitorização ativa

---

## 📌 Recomendações

- Validar se a classificação DRP/BIA está atualizada e corresponde ao âmbito da aplicação atual
- Anexar ou referenciar a classificação de impacto no repositório onde for documentada a classificação de risco
- Se a aplicação for composta por múltiplos módulos, considerar a classificação **por componente**, não apenas global
- Em caso de divergência entre a classificação DRP e a observada em segurança, registar ambos os racionales e discutir com as equipas envolvidas

---

## 🧩 Integração operacional

Na prática, a reutilização destas classificações pode ser feita de três formas:

1. **Importação direta dos dados** no registo de risco (ex: ficheiro, wiki, ferramenta)
2. **Ligação cruzada** entre artefactos (ex: link para a ficha DRP no registo de risco)
3. **Template único** que inclua campos de impacto de negócio e risco de segurança

> Uma boa prática é incluir esta validação como um dos critérios do *checklist* de classificação.

---

---

# 🧪 Casos Práticos de Classificação de Risco

Os exemplos seguintes ilustram **diferentes formas legítimas de classificar aplicações** no SbD-ToE, demonstrando:

- aplicação direta do modelo **E/D/I**;
- impacto de **dados e contexto regulatório**;
- uso de **classificação conservadora por criticidade operacional**;
- influência de **automação avançada (incl. IA)** quando relevante.

O objetivo não é encontrar a “classificação perfeita”,  
mas **assegurar o nível adequado de cuidado e controlo**.

---

## 📝 Caso 1 — Plataforma de E-commerce Pública

**Contexto**  
Plataforma de vendas online, com pagamentos diretos e integração com terceiros.

- **Exposição (E)**: Pública (web + app móvel) → **3**  
- **Tipo de Dados (D)**: Dados pessoais + dados de pagamento → **3**  
- **Impacto (I)**: Financeiro, reputacional e legal → **3**

**Classificação:**  
**E + D + I = 9 → L3 (Risco Elevado)**

**Racional**  
Mesmo sem considerar incidentes passados, a combinação de exposição pública, dados sensíveis e impacto direto no negócio justifica **máximo rigor**.

**Implicações práticas**:
- Requisitos de segurança completos e rastreáveis  
- Threat modeling formal  
- SBOM e SCA contínuo  
- DAST contínuo, fuzzing e validação de regressões  

---

## 📝 Caso 2 — Portal Interno de RH Hospitalar

**Contexto**  
Aplicação interna, acessível apenas na rede hospitalar, usada para gestão de RH.

- **Exposição (E)**: Interna → **1**  
- **Tipo de Dados (D)**: Dados clínicos e financeiros de colaboradores → **3**  
- **Impacto (I)**: Legal (RGPD), confidencialidade sensível → **3**

**Classificação:**  
**E + D + I = 7 → L3 (Risco Elevado)**

**Racional**  
A baixa exposição **não compensa** a natureza dos dados nem o impacto legal.  
Este é um exemplo clássico de erro comum evitado pelo modelo SbD-ToE.

**Nota importante**  
Este caso demonstra que:
> *“interno” não significa “baixo risco”*.

---

## 📝 Caso 3 — Sistema de Faturação B2B

**Contexto**  
Sistema usado por clientes empresariais autenticados, com integração ERP.

- **Exposição (E)**: Acesso externo autenticado → **2**  
- **Tipo de Dados (D)**: Dados financeiros e de clientes → **2**  
- **Impacto (I)**: Operacional e financeiro → **2**

**Classificação:**  
**E + D + I = 6 → L2 (Risco Médio)**

**Racional**  
Sistema relevante, mas com impacto controlável e sem dados regulados críticos.

**Implicações práticas**:
- Requisitos de segurança formais, mas proporcionais  
- Threat modeling simplificado  
- SCA com política de severidade  
- Testes de segurança regulares, não contínuos  

---

## 📝 Caso 4 — Ferramenta Interna de Gestão de Tarefas

**Contexto**  
Aplicação simples, usada internamente para gestão de tarefas.

- **Exposição (E)**: Interna → **1**  
- **Tipo de Dados (D)**: Não sensíveis → **1**  
- **Impacto (I)**: Baixo → **1**

**Classificação:**  
**E + D + I = 3 → L1 (Risco Baixo)**

**Racional**  
Baixa exposição, baixo impacto e ausência de dados sensíveis justificam controlos mínimos.

**Implicações práticas**:
- Linters e revisão básica de código  
- Boas práticas gerais de segurança  
- Sem exigência de testes avançados  

---

## 📝 Caso 5 — Serviço Core com DRP Crítico (Classificação Conservadora)

**Contexto**  
Serviço central de negócio, classificado como **Crítico no DRP**:

- RTO < 1h  
- RPO ≈ 0  
- Interrupção paralisa operações da organização  

**Análise técnica estrita**:
- Exposição controlada  
- Dados moderadamente sensíveis  

**Decisão adotada**:
- **Classificação direta como L3**, por criticidade operacional

**Racional**  
Mesmo que o risco técnico pudesse ser L2, o custo de falha justifica  
**tratamento como aplicação de risco elevado**.

> Este é um exemplo explícito de *over-classification deliberada*,  
> aceite e recomendada no SbD-ToE.

---

## 📝 Caso 6 — Aplicação com Automação Avançada (incl. IA)

**Contexto**  
Aplicação interna que utiliza automação assistiva para:
- gerar código,
- aprovar alterações de configuração,
- executar ações com impacto real.

- **Exposição (E)**: Interna, mas com integrações externas → **2**  
- **Tipo de Dados (D)**: Código, configurações, segredos ocasionais → **2**  
- **Impacto (I)**: Alterações automáticas com efeito real → **3**

**Classificação:**  
**E + D + I = 7 → L3 (Risco Elevado)**

**Racional**  
A classificação **não é elevada por “usar IA”**,  
mas porque existe:
- delegação,
- velocidade,
- e impacto sem validação humana obrigatória.

---

## 📌 Conclusão

Estes exemplos demonstram que:

- a classificação de risco **não é mecânica**;
- o SbD-ToE aceita decisões conservadoras e pragmáticas;
- o objetivo final é sempre:
  > **aplicar o nível certo de cuidado, controlo e validação**.

A coerência do modelo está na **proporcionalidade**,  
não na obsessão pela pontuação perfeita.

---

# 🛠️ Validação Assistida por Ferramentas — Risco de Processo

## 🎯 Objetivo

Este documento prescreve como gerir **riscos de processo** quando ferramentas automatizadas (algoritmos de scoring, sistemas de análise, ou outras formas de assistência) participam na **classificação de aplicações, deteção de alterações, ou mapeamento de ameaças**.

O objetivo **não é proibir ferramentas**, mas sim:

- garantir que **sugestões de ferramentas nunca substituem decisões humanas**;
- identificar **erros plausíveis** que máquinas podem introduzir;
- exigir **validação obrigatória** e **rastreabilidade explícita**;
- estabelecer **trilhos de escalação** em caso de discordância;
- manter **evidência auditável** de todas as decisões.

---

## 📋 Invariantes Fundamentais (do agent.md)

Independentemente do tipo de ferramenta ou fase do ciclo de vida, **todo o uso de automação na classificação deve respeitar**:

### I1 — Separação entre Sugestão e Decisão

- Ferramentas **sugerem, analisam, ou correlacionam**.
- A **decisão final é sempre humana**, atribuída a um role explícito (Developer, AppSec Engineer, GRC/Compliance).
- A sugestão pode ser ignorada, modificada, ou aceite — mas a responsabilidade é sempre do decisor humano.

### I2 — Evidência Acima de Plausibilidade

- Um resultado **plausível** (ex: "L2 porque E=2, D=2, I=1") não substitui **evidência verificável**.
- Exemplos de evidência:
  - Arquitetura técnica documentada e revisada.
  - Dados especificados e classificados manualmente.
  - Ameaças validadas por especialistas de domínio.
  - Exceções aprovadas formalmente.

### I3 — Reprodutibilidade e Auditabilidade

- Toda a sugestão deve ser **reproduzível** e **rastreável**:
  - Que ferramenta foi usada? (nome, versão, data)
  - Que inputs recebeu? (aplicação, eixos, dados brutos)
  - Que output gerou? (score, pontuação E/D/I, nível proposto)
  - Que critério de decisão foi aplicado? (threshold, regras, ponderação)

### I4 — Proteção de Ativos Críticos

- Qualquer ferramenta externa (SaaS, cloud, ou terceiros) é um **risco de supply chain**:
  - Dados sensíveis da aplicação (dados tratados, arquitetura, clientes) não devem ser enviados para sistemas desconhecidos.
  - Aprovação explícita requerida antes de usar qualquer ferramenta em L2/L3.

### I5 — Rastreabilidade de Decisão e Execução

- Toda a decisão de classificação deve responder:
  - **Quem decidiu?** (Developer, AppSec Engineer, Product Owner, etc.)
  - **Com base em quê?** (E/D/I manual, sugestão de ferramenta, feedback de Arquitetos, etc.)
  - **Que validações foram realizadas?** (checklist, revisão, testes)
  - **Que evidência suporta a decisão?** (documentação, relatórios, scans, aprovações)

---

## 🚨 Erros Plausíveis — Por Tipo de Assistência

### A. Scoring Automático de E/D/I

**Como funciona**: Ferramenta analisa descrição de projeto, endpoints, tipos de dados, e propõe scores para E, D, I.

**Erros plausíveis típicos**:

| Erro | Exemplos | Impacto | Mitigação |
|---|---|---|---|
| **Sobreponderação de um eixo** | "Tem muitos endpoints públicos → E=3 sempre", negligenciando que dados são públicos | Classificação enviesada, Controlos desproporcionais | Explicação narrativa obrigatória: "Por quê E=3?" |
| **Omissão de contexto** | Não detecta que uma dependência crítica é opcional ou que isolamento é possível | Subestimação de risco | Revisão manual de dependências + feedback de Arquitetos |
| **Regras inflexíveis** | "Aplicação com mais de 10 APIs → sempre L3", sem considerar que podem ser internas | Sobre-classificação | Critério "se ferramenta propõe L3, AppSec Engineer valida presença de exposição pública real" |
| **Falta de nuance temporal** | Classifica com base em estado actual, ignora crescimento previsto de dados | Risco de reclassificação precipitada | Incluir "previsão de 12 meses" na avaliação; revisar periodicamente |
| **Desalinhamento com modelo organizacional** | Ferramenta usa threshold genérico (ex: "dados PII=D2"), org usa "dados de cliente=D3" | Inconsistência com política | Policy explícita: "Todos os resultados de ferramenta são re-calibrados contra política organisacional" |

---

### B. Deteção Automática de Alterações (Event-Based Triggers)

**Como funciona**: Ferramenta analisa commits, PRs, configurações, e propõe reclassificação (ex: "Nova dependência crítica detectada").

**Erros plausíveis típicos**:

| Erro | Exemplos | Impacto | Mitigação |
|---|---|---|---|
| **Falso positivo** | Detecta `npm update lodash` como "alteração crítica" | Alarme excessivo, desconfiança em sistema | Whitelist + contexto: "Atualizações de patch são ignoradas; apenas minor/major geram alerta" |
| **Omissão de contexto** | Vê "integração com API externa" mas não sabe se é crítica ou opcional | Subdeteção | AppSec Engineer faz validação: "Este novo integração é crítica para o negócio?" |
| **Lag temporal** | Ferramenta detecta mudança 2 semanas depois | Atraso em revisão | Análise semanal ou por sprint, não ad-hoc |
| **Falta de priorização** | Trata "novo endpoint de telemetria" com mesma urgência que "novo acesso a dados de cliente" | Confusão de prioridades | Categorização: crítica (reclassifica já), importante (agenda revisão), informativa (log apenas) |

---

### C. Mapeamento Automático de Ameaças

**Como funciona**: Ferramenta gera STRIDE ou MITRE ATT&CK mapping baseado em tipo de aplicação.

**Erros plausíveis típicos**:

| Erro | Exemplos | Impacto | Mitigação |
|---|---|---|---|
| **Ameaças genéricas não-contextuais** | Mapeia "Denial of Service" para todas as apps, sem considerar SLA crítico | Ruído, wasted effort | Filtro: "Incluir apenas ameaças com probabilidade alta ou impacto crítico para este domínio" |
| **Omissão de ameaças contextuais** | Gera STRIDE genérico, ignora "roubo de IP por insider" (ameaça específica de R&D) | Risco residual não-identificado | Validação por Arquitetos + especialistas de domínio: "Faltam ameaças específicas?" |
| **Falta de priorização** | Lista 50 ameaças, sem indicar críticas vs. menores | Paralisia de análise | Classificação: crítica (cobertura obrigatória), major (cobertura recomendada), minor (opcional) |
| **Desalinhamento com nível de risco** | Mesmo mapeamento para L1 e L3 | Proporção perdida | Requerimento: "Ameaças críticas +60% para L3, +30% para L2, -50% para L1" |

---

## ✅ Checklist de Validação — Por Prática

### Checklist 1: US-01 (Classificação Inicial — Assistida)

**Quando**: Ferramenta propõe E/D/I ou nível L1/L2/L3.

**Checklist (DoD adicional)**:

- [ ] **Fonte de dados clara**: Ferramenta recebeu quais inputs? (descrição projeto, endpoints, tipos de dados)
- [ ] **Explicação narrativa**: Ferramenta justificou por quê E=X, D=Y, I=Z? (output com raciocínio anexado)
- [ ] **Validação de eixo**: Developer/Team Lead validou manualmente cada eixo contra realidade técnica
- [ ] **Revisão de contexto**: Arquitetos confirmam que E/D/I refletem exposição, dados, e impacto reais
- [ ] **Decisão assinada**: AppSec Engineer assinou a decisão final com registo explícito:
  ```
  Classificação: L2
  Origem: Sugestão de ferramenta (v1.2, data: 2025-01-15)
  Ajustes humanos: E mantido em 2 (confirmado por Arquitetos), 
                   D aumentado para 3 (dados de cliente identificados), 
                   I mantido em 1
  Aprovação: AppSec Engineer [nome], data
  ```
- [ ] **Benchmark vs. histórico**: Comparado com aplicações similares já classificadas?
- [ ] **TTL de re-validação**: Próxima revisão agendada (time-based per nivel + event-based triggers)

---

### Checklist 2: US-03 & US-07 (Revisão — Assistida por Deteção de Alteração)

**Quando**: Ferramenta detecta mudança e propõe reclassificação.

**Checklist (DoD adicional)**:

- [ ] **Trigger documentado**: O quê foi detectado? (nova dependência, novo endpoint, novo dado, etc.)
- [ ] **Ferramenta & método**: Quem detectou? (análise manual de commit, ferramenta X versão Y, etc.)
- [ ] **Contexto técnico**: AppSec Engineer/Arquitetos confirmam que alteração é relevante e não falso positivo
- [ ] **Impacto em E/D/I**: Qual eixo é afetado? (exemplo: "E aumenta por novo endpoint", "D aumenta por novo tipo de dado")
- [ ] **Reclassificação proposta**: E/D/I antigo → novo (com explicação de cada mudança)
- [ ] **Trilho de validação**: Se discordância (máquina propõe L2, AppSec quer L3):
  - Documentar: "Ferramenta propôs L2 por [razão X], AppSec override para L3 por [razão Y]"
  - Escalação: Product Owner informado se impacto de negócio
  - Decisão final registada com assinatura
- [ ] **GRC/Compliance audit trail**: Registo em ferramenta de conformidade com timestamp

---

### Checklist 3: US-06 (Mapeamento de Ameaças — Assistido)

**Quando**: Ferramenta gera STRIDE/MITRE ATT&CK mapping.

**Checklist (DoD adicional)**:

- [ ] **Ferramenta & versão**: Qual algoritmo? (ex: "Automated STRIDE Generator v2.1")
- [ ] **âmbito correto**: Mapping inclui ameaças apropriadas para nível L1/L2/L3?
- [ ] **Filtro de ruído**: Omitidas ameaças genéricas não-contextuais? (ex: filtrar "slow DDoS" se criticidade baixa)
- [ ] **Validação por especialistas**: Arquitetos/AppSec Engineer validou:
  - Ameaças criticas não foram omitidas?
  - Ameaças específicas de domínio foram incluídas?
  - Priorização (crítica vs. minor) está correcta?
- [ ] **Rastreamento**: Cada ameaça tem:
  - [ ] Descrição clara
  - [ ] Controlo aplicado (ou exceção com justificação)
  - [ ] Status: coberta / parcialmente coberta / não coberta (risco residual)
- [ ] **Escalação se risco crítico não coberto**: Dispara US-04 (risco residual) ou mitigação obrigatória

---

## 🔀 Trilho de Escalação — Discordância Humano ↔ Máquina

### Cenário 1: Developer propõe L1, Ferramenta propõe L2

```
┌─────────────────────────────────────────────────────┐
│ DISCORDÂNCIA DETECTADA                              │
│ Developer: "Apenas APIs internas, dados públicos"   │
│ Ferramenta: "E=2 (múltiplos endpoints) → L2"        │
└──────────────────┬──────────────────────────────────┘
                   ▼
         ┌─────────────────────┐
         │ AppSec Engineer     │
         │ Valida contexto:    │
         │ - Endpoints realmente│
         │   apenas internos?   │
         │ - Dados realmente    │
         │   públicos?          │
         └────────┬────────────┘
                  ▼
        ┌──────────────────────────────┐
        │ Decisão Final:               │
        │ L1 (concordou com Developer) │
        │ Motivo: "Ferramenta         │
        │  incorreu em falso positivo" │
        │ Registro: [assinado]         │
        └──────────────────────────────┘
```

### Cenário 2: AppSec propõe L3, Ferramenta propõe L1 (Subdeteção)

```
┌──────────────────────────────────────────────────────┐
│ DISCORDÂNCIA CRÍTICA DETECTADA                       │
│ AppSec: "Dados de cliente + APIs públicas → L3"      │
│ Ferramenta: "Apenas E=1, D=1 → L1"                   │
└───────────────────┬────────────────────────────────────┘
                    ▼
        ┌─────────────────────────────────────┐
        │ Investigação: Por quê ferramenta    │
        │ sub-classificou?                    │
        │ - Não detectou dados de cliente?    │
        │ - Não mapeou APIs públicas?         │
        │ Ação: Feedback para ferramenta      │
        │ (treino, ajuste de regras, etc.)    │
        └──────────┬──────────────────────────┘
                   ▼
        ┌──────────────────────────────┐
        │ Decisão Final:               │
        │ L3 (concordou com AppSec)    │
        │ Motivo: "Ferramenta errou;   │
        │  dados de cliente omissos"   │
        │ Escalação: Product Owner     │
        │  (impacto de negócio L3)     │
        │ Registro: [assinado]         │
        └──────────────────────────────┘
```

### Cenário 3: Discordância não resolvida no SLA

```
┌────────────────────────────────────────────┐
│ Sem consenso em 5 dias úteis (SLA)         │
├────────────────────────────────────────────┤
│ Developer: L1                              │
│ Ferramenta: L2                             │
│ AppSec Engineer: Indeciso                  │
└─────────────────┬──────────────────────────┘
                  ▼
        ┌────────────────────────────┐
        │ Escalonamento automático:  │
        │ Product Owner arbitral     │
        │ (aspectos de negócio)      │
        │ + CISO (aspectos técnicos) │
        └──────────┬─────────────────┘
                   ▼
        ┌────────────────────────┐
        │ Decisão Final Oficial  │
        │ Registro formal com    │
        │ assinatura(s)          │
        │ Motivo documentado     │
        └────────────────────────┘
```

---

## 📝 Exemplos — Boas e Más Práticas

### ❌ Má Prática 1: Aceitar Sugestão sem Validação

```
Ferramenta: "L2" (score: E=2, D=2, I=1)
Developer: "OK, vou com L2"
AppSec Engineer: (não revê)
Artefacto registado: classificacao-app.yaml com L2, sem explicação

PROBLEMA:
- Ninguém sabe por quê L2
- Impossível auditar decisão
- Ferramenta pode ter errado (ex: omitiu dados sensíveis)
- Reclassificação futura sem baseline
```

### ✅ Boa Prática 1: Validação com Rastreabilidade

```
Ferramenta: "L2" (E=2, D=2, I=1)
Output: {
  "eixos": {
    "exposicao": 2,
    "dados": 2,
    "impacto": 1
  },
  "raciocinio": "E=2: APIs internas (5 endpoints), 
                 D=2: Dados de utilizador, 
                 I=1: Downtime ~30min aceitável"
}

Developer + Arquitetos: Revisam E/D/I narrativa
- E=2: Confirmado? SIM (APIs internas, não públicas)
- D=2: Confirmado? SIM (dados de utilizador, não PII)
- I=1: Confirmado? NÃO — se cair, impacto é crítico → I=2

AppSec Engineer: Reclassifica E/D/I → L2 mantém-se (após ajuste I)

Artefacto registado:
  classificacao-app.yaml:
    nível: L2
    eixos_originais: {E: 2, D: 2, I: 1}
    eixos_finais: {E: 2, D: 2, I: 2}
    assistida_por_ferramenta: true
    ferramenta: "Automated Classifier v1.2"
    data_ferramenta: "2025-01-15"
    validadores: ["Developer-X", "Arquiteto-Y"]
    aprovador: "AppSec-Z"
    data_aprovacao: "2025-01-16"
    observações: "I ajustado de 1→2 por Arquitetos (impacto crítico)"

VANTAGENS:
✓ Totalmente rastreável
✓ Auditável ("quem decidiu o quê, quando, por quê")
✓ Benchmarkável contra outras apps
✓ Reclassificações futuras têm baseline claro
```

---

### ❌ Má Prática 2: Ferramenta Detecta Alteração, Ninguém Valida

```
Commit: "Add dependency on critical-auth v2.0"
Ferramenta: [Alerta automático] "Nova dependência crítica detectada!"
GRC/Compliance: Vê alerta, não faz nada (assume que já foi validado)
Developer: Não vê alerta (não subscrito)
AppSec Engineer: Não viu (não reviewou)

Resultado: Ninguém reviu, classificação não foi atualizada
RISCO: Controlo de segurança insuficiente, gap de conformidade
```

### ✅ Boa Prática 2: Deteção com Validação Explícita

```
Commit: "Add dependency on critical-auth v2.0"
Ferramenta: [Alerta] "Nova dependência crítica detectada!"
Email automático: AppSec Engineer + GRC/Compliance
Issue automática: "Reclassifique se necessário"

AppSec Engineer (3 dias úteis):
- Valida: "critical-auth é realmente crítica?"
- Resultado: SIM, acesso centralizado a dados de cliente
- Decisão: E (exposição) não muda; D (dados) permanece 2
- Nível: L2 → L2 (sem mudança, mas com ameaças críticas agora)
- Ação: Dispara US-06 (mapeamento de ameaças para nova dependência)

Artefacto registado:
  classificacao-revisao.md:
    data: 2025-01-20
    trigger: "Nova dependência crítica (critical-auth v2.0)"
    ferramenta_detetor: "Dependency Scanner v1.5"
    nível_anterior: L2
    nível_novo: L2
    decisão: "Mantém-se L2; novo mapeamento de ameaças requerido"
    validador: "AppSec-Z"
    próxima_revisão: "2025-02-20" (30 dias)

GRC/Compliance: Registra em audit trail
```

---

## 🔗 Integração com User Stories

### Para US-01 (Classificação Inicial)

Adicionar ao DoD:

```markdown
- [ ] **Se assistida por ferramenta:**
  - [ ] Output de ferramenta (scores, raciocínio) anexado
  - [ ] Justificação narrativa humana clara (por quê E=X, D=Y, I=Z)
  - [ ] Validação de cada eixo por especialistas (Developer, Arquitetos)
  - [ ] Aprovação final por AppSec Engineer com registo explícito
  - [ ] Ferramenta, versão, data documentados
```

### Para US-03 (Revisão Event-Based)

Adicionar ao DoD:

```markdown
- [ ] **Se assistida por ferramenta detetor:**
  - [ ] Ferramenta & método de deteção documentados
  - [ ] Trigger técnico validado (falso positivo excluído)
  - [ ] Contexto de negócio confirmado (alteração realmente relevante)
  - [ ] Impacto em E/D/I explicado
  - [ ] Se nível alterou: trilho de escalação documentado
```

### Para US-07 (Revisão Time-Based)

Adicionar ao DoD:

```markdown
- [ ] **Se assistida por ferrameta de análise:**
  - [ ] Ferramenta forneceu re-scoring de E/D/I?
  - [ ] Comparação: score anterior vs. score novo documentada
  - [ ] Se discordância (máquina vs. AppSec): trilho de resolução registado
```

### Para US-06 (Mapeamento de Ameaças)

Adicionar ao DoD:

```markdown
- [ ] **Se assistido por ferramenta de mapeamento:**
  - [ ] Ferramenta & versão documentados
  - [ ] Ameaças genéricas não-contextuais filtradas?
  - [ ] Ameaças específicas de domínio adicionadas (validação especialistas)?
  - [ ] Priorização (crítica vs. minor) correcta?
  - [ ] Ameaças críticas não cobertas dispararam US-04 (risco residual)?
```

---

## 📊 Matriz de Proporcionalidade — Esforço de Validação

| Prática | L1 | L2 | L3 |
|---|---|---|---|
| **Validação obrigatória de sugestão** | Recomendada | Obrigatória | Obrigatória + Gestão Executiva |
| **Benchmark vs. histórico** | Opcional | Recomendado | Obrigatório |
| **Trilho de escalação formalizado** | Ad-hoc | Documentado | Documentado + SLA |
| **TTL de re-validação assistida** | 12m | 6m | 3m |
| **Auditoria de decisões assistidas** | Anual | Semestral | Trimestral |

---

## 🎯 Resumo & Recomendações Operacionais

1. **Ferramentas são auxiliares, não autoridades**: Sugestões são valiosas, decisões são humanas.
2. **Rastreabilidade é não-negociável**: Todo o uso de automação deve deixar pista auditável.
3. **Validação proporcional ao risco**: L1 pode ser mais leve, L3 requer rigor máximo.
4. **Erros de ferramenta são esperados**: Ter checklist de erros plausíveis + mitigações.
5. **Escalação clara**: Quando máquina e humano discordam, processo formalizado leva a consenso.
6. **Feedback contínuo**: Se ferramenta errou sistematicamente, ajustar (treino, regras, etc.).
7. **Conformidade regulatória**: Auditorias devem conseguir rastrear "quem decidiu com base em quê".

---

## 🔗 Referências Internas

- agent.md — Invariantes Canonicos
- US-01 — Classificação Inicial
- US-03 — Revisão Event-Based
- US-06 — Mapeamento de Ameaças
- US-07 — Revisão Time-Based

---

# 🛠️ Aplicação da Classificação de Criticidade ao Longo do Ciclo de Vida

A correta aplicação da classificação de criticidade (L1–L3) ao longo de todo o ciclo de desenvolvimento é essencial para garantir que os controlos de segurança são sempre proporcionais ao risco real, efetivamente rastreáveis e revistos de acordo com os eventos e alterações relevantes.

Este capítulo detalha, de forma operacional e prescritiva, **quando e como implementar a classificação de criticidade na prática**, descrevendo as ações esperadas por cada papel, os artefactos produzidos, e apresentando exemplos de user stories reutilizáveis — sempre de acordo com o nível de risco da aplicação.

---

## 🧭 Abrangência e quando aplicar

| Fase / Evento                          | Ação esperada                                                   | Documento de apoio                                                                 |
|----------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 🚧 Início de projeto                   | Classificar aplicação segundo modelo E+D+I                      | Modelo de Classificação |
| 🔄 Nova release ou integração          | Rever classificação com base em alterações relevantes           | Ciclo de Vida do Risco |
| 🛠️ Mudança nos dados, exposição ou automação/assistência | Reclassificar eixos E/D/I conforme impacto; avaliar risco residual | Risco Residual |
| 🧪 Revisão de arquitetura              | Aplicar avaliação semiquantitativa e validar controlo aplicado  | Avaliação Quantitativa |
| 🚀 Go-live                             | Validar conformidade com matriz de controlos por risco          | Matriz de controlos por Risco |
| ⚠️ Ameaça emergente ou nova CVE        | Reavaliar criticidade e cobertura de ameaças                    | Mapeamento Ameaças por Risco |
| 🗓️ Decurso do tempo (cadência formal) | **Revisão periódica time-based** da classificação               | Ciclo de Vida do Risco |

---

## 👥 Quem executa cada ação

| Papel Formal (07-roles) | Responsabilidades em Cap. 01 |
|---|---|
| **Developer** | Propor classificação inicial; registar alterações E/D/I; atualizar documentação em commits |
| **Team Lead / Scrum Master** | Facilitar integração da classificação no backlog; remover bloqueios operacionais |
| **AppSec Engineer** | Validar modelo aplicado; ajustar nível (especialmente em L2/L3); mapear ameaças; parametrizar cadência; aprovar classificações |
| **Arquitetos de Software** | Rever implicações técnicas de risco, cenários de exposição, impacto em arquitetura |
| **Product Owner** | Notificado de alterações de nível (especialmente L1→L3); aprovar impacto de negócio de exceções |
| **GRC/Compliance** | Rastreabilidade normativa; definir TTL/expiração de exceções; consolidar KPIs; auditar decisões |
| **QA** | Validar cumprimento de requisitos por nível antes do go-live; documentar evidências |
| **DevOps/SRE** | Aplicar classificação a artefactos técnicos (pipeline/IaC/imagens) nos capítulos 07/08/09 |
| **Gestão Executiva / CISO** | Aprovar políticas de classificação e aceitação de risco; supervisionar exceções em L3 |
| **Auditores Internos** | Validar aplicação efetiva de classificações; auditar rastreabilidade; produzir achados |

---

## 🛠️ User stories reutilizáveis

### US-01 - Classificação inicial da aplicação

**Contexto.**  
A classificação inicial da aplicação é o ponto de entrada para a aplicação proporcional de controlos de segurança (L1–L3). Sem este passo, não é possível garantir rastreabilidade nem proporcionalidade.

:::userstory
**História.**  
Como **Developer / Team Lead**, quero **classificar a aplicação com base nos eixos Exposição, Dados e Impacto (E+D+I)**, para garantir a aplicação proporcional de controlos de segurança ao longo de todos os capítulos.

**Critérios de aceitação (BDD).**
- **Dado** uma aplicação nova ou em início de projeto  
  **Quando** aplico o modelo de classificação E+D+I  
  **Então** obtenho uma pontuação por eixo e um nível global **L1–L3 definido, validado por AppSec Engineer e documentado**

**Critérios de aceitação (DoD).**
- [ ] Modelo de classificação E+D+I aplicado à aplicação  
- [ ] Nível de criticidade (L1–L3) definido e **validado por AppSec Engineer**  
- [ ] Documento de classificação registado e versionado em repositório Git  
- [ ] Ferramentas de automação/assistência (incl. IA) identificadas e refletidas nos eixos E/D/I  
- [ ] Controlos mínimos extraídos da matriz de risco e associados à aplicação  
- [ ] **Em L2/L3: Aprovação formal por AppSec Engineer documentada**  
- [ ] **Product Owner notificado se classificação for L3**  
- [ ] **Se assistida por ferramenta:**
  - [ ] Output de ferramenta (scores E/D/I, raciocínio) anexado
  - [ ] Justificação narrativa humana clara (por quê E=X, D=Y, I=Z)
  - [ ] Validação de cada eixo por especialistas (Developer, Arquitetos)
  - [ ] Aprovação final por AppSec Engineer com registo explícito
  - [ ] Ferramenta, versão, data documentados
  - [ ] Referência: addon-11: Validação Assistida por Ferramentas

:::

**Artefactos & evidências.**
- Ficheiro: `classificacao-aplicacao.yaml` — Localização: Repo `security/`  
- Ficheiro: `matriz-controlos-aplicada.md` — Evidência: Anexo ao PR ou wiki

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Classificação simplificada, apenas eixos principais |
| L2 | Sim | Classificação completa com **validação formal por AppSec Engineer** |
| L3 | Sim | Classificação formal, **validada e aprovada por AppSec Engineer + GRC/Compliance** |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Início | Kick-off / Definição de projeto | **Developer + Team Lead + AppSec Engineer** | Antes da primeira release |
| Arquitetura | Revisão de design inicial | **Developer + Arquitetura + AppSec Engineer** | Antes da aprovação de arquitetura |

**Ligações úteis.**
- Modelo de Classificação  
- Matriz de Controlos por Risco  
- 07-roles.md

---

### US-02 - Aplicação da matriz de controlo

**Contexto.**  
A matriz de controlo define quais os requisitos de segurança aplicáveis em função do nível de risco. Sem mapeamento explícito, há risco de sobreproteção ou underprotection.

:::userstory
**História.**  
Como **Developer / Team Lead**, quero **aplicar a matriz de controlos e mapear cada requisito para REQ-XXX do Capítulo 02**, para garantir que apenas os requisitos necessários são exigidos e rastreáveis.

**Critérios de aceitação (BDD).**
- **Dado** uma aplicação já classificada (L1, L2 ou L3)  
  **Quando** consulto a matriz de controlos  
  **Então** extraio apenas os requisitos correspondentes ao nível atribuído **e mapeio cada um para REQ-XXX específico**

**Critérios de aceitação (DoD).**
- [ ] Matriz consultada para o nível da aplicação  
- [ ] Requisitos transformados em cartões/histórias de backlog  
- [ ] **Cada requisito mapeado explicitamente para REQ-XXX do Cap. 02** (ex: REQ-LOG-001, REQ-ARC-003)  
- [ ] Tabela de rastreamento: `controlo | L1/L2/L3 | REQ-XXX | responsável`  
- [ ] Exceções documentadas, aprovadas por AppSec Engineer com justificação técnica  
- [ ] **AppSec Engineer valida mapeamento antes de entrada em backlog**  

:::

**Artefactos & evidências.**
- Ficheiro: `matriz-controlos-aplicada.md` com rastreamento REQ-XXX  
- Localização: Backlog / Wiki / Repositório de documentação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Aplicar controlos mínimos |
| L2 | Sim | Controlos completos com rastreamento obrigatório |
| L3 | Sim | Controlos completos + reforçados + validação por AppSec |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Planeamento | Após classificação | **Developer + Team Lead + AppSec Engineer** | Antes de implementação |

**Ligações úteis.**
- Matriz de Controlos por Risco  
- Capítulo 02 - Requisitos de Segurança  
- 07-roles.md

---

### US-03 - Revisão por alteração relevante (event-based)

**Contexto.**  
A classificação deve ser revista quando existirem alterações significativas de arquitetura, dados ou exposição. Sem revisão, mudanças lentas podem gerar desalinhamento entre nível e controlos.

:::userstory
**História.**  
Como **AppSec Engineer**, quero **rever a classificação de criticidade sempre que houver alterações relevantes**, para garantir adequação contínua dos controlos ao contexto técnico real.

**Critérios de aceitação (BDD).**
- **Dado** que ocorreu uma alteração significativa (ex: nova API, novo dado sensível, mudança de exposição)  
  **Quando** reviso a classificação  
  **Então** documento se o nível foi mantido ou alterado, com justificação técnica clara

**Critérios de aceitação (DoD).**
- [ ] Trigger de revisão identificado e documentado  
- [ ] Documento de classificação atualizado ou revalidado  
- [ ] Justificação técnica registada (ex: "E aumentou de 1→2 por exposição a API pública")  
- [ ] **Se nível alterou: dispara revisão de matriz (US-02) e mapeamento de ameaças (US-06)**  
- [ ] **Product Owner notificado se houver impacto de negócio** (especialmente em escalação L1→L3)  
- [ ] GRC/Compliance registra alteração em auditable trail  
- [ ] **Se assistida por ferramenta detetor:**
  - [ ] Ferramenta & método de deteção documentados
  - [ ] Trigger técnico validado (falso positivo excluído)
  - [ ] Contexto de negócio confirmado (alteração realmente relevante)
  - [ ] Impacto em E/D/I explicado
  - [ ] Se nível alterou: trilho de escalação documentado
  - [ ] Referência: addon-11: Validação Assistida por Ferramentas

:::

**Artefactos & evidências.**
- Ficheiro: `classificacao-revisao.md` ou entrada em issue tracker  
- Conteúdo: `data | trigger | nível_anterior | nível_novo | justificação | responsável`  
- Evidência: commit rastreável com assinatura, issue comentada, ou registo em GRC

**Proporcionalidade por risco.**
| Nível | Obrigatório? |
|---|---|
| L1 | Sim (por alteração relevante) |
| L2 | Sim |
| L3 | Sim |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Contínuo | Mudança arquitetura, dados ou exposição | **AppSec Engineer + Developer + GRC/Compliance + Product Owner** | 3 dias úteis após trigger |

**Ligações úteis.**
- Ciclo de Vida do Risco  
- 07-roles.md

---

### **US-07 - Revisão Periódica Time-Based da Classificação (Cadência Obrigatória)**

**Contexto.**  
Para além dos triggers por alteração, a classificação deve ter **cadência periódica fixa**. Sem calendário, mudanças lentas (ex: crescimento de dados críticos) ficam não-detetadas.

:::userstory
**História.**  
Como **AppSec Engineer**, quero **rever a classificação com cadência fixa (L1 anual, L2 semestral, L3 trimestral)**, para garantir que o nível de criticidade e os controlos continuam adequados ao contexto actual.

**Critérios de aceitação (BDD).**
- **Dado** que existe uma classificação ativa com data de próxima revisão definida  
  **Quando** a data de revisão chega  
  **Então** executo reavaliação dos eixos E/D/I, documento decisão (manter/alterar) e **agenço próxima revisão**

**Critérios de aceitação (DoD).**
- [ ] Calendário de revisões definido por nível (L1=12m, L2=6m, L3=3m)  
- [ ] Ata ou issue de revisão criada, datada e documentada com evidência técnica  
- [ ] Justificação: "Alterado" (com novo nível e drivers) ou "Mantém-se" (com observações)  
- [ ] Próxima data de revisão agendada e alertas configurados (em ferramenta GRC se possível)  
- [ ] **Se nível alterado: dispara US-02 (matriz) e US-06 (ameaças)**  
- [ ] **Product Owner notificado se houver impacto de negócio** (especialmente L1→L3)  
- [ ] **GRC/Compliance registra em audit trail**  
- [ ] **Se assistida por ferramenta de análise:**
  - [ ] Ferramenta forneceu re-scoring de E/D/I?
  - [ ] Comparação: score anterior vs. score novo documentada
  - [ ] Se discordância (máquina vs. AppSec): trilho de resolução registado
  - [ ] Validação temporal: revisão de dados, dependências, impacto esperado para próximos 12m
  - [ ] Referência: addon-11: Validação Assistida por Ferramentas
:::

**Artefactos & evidências.**
- Ficheiro: `classificacao-revisoes.md` ou entrada em ferramenta GRC  
- Tabela: `data_revisao | nível_anterior | nível_novo | justificação | próxima_data | responsável`  
- Evidência: issue rastreável datada, commit versionado, ou registo auditable

**Proporcionalidade (cadência típica).**
| Nível | Frequência sugerida | Obrigatório? |
|---|---|---|
| L1 | 12 meses | Recomendado |
| L2 | 6 meses | Obrigatório |
| L3 | 3 meses (ou por sprint) | Obrigatório |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Operações + Governação | Calendário time-based + Eventos críticos | **AppSec Engineer + GRC/Compliance + Product Owner** | Conclusão em 5 dias úteis da data de revisão |

**Ligações úteis.**
- Ciclo de Vida do Risco  
- Critérios Aceitação Risco  
- 07-roles.md

---

### US-04 - Análise de risco residual

**Contexto.**  
Mesmo após aplicação da matriz, podem permanecer riscos residuais que devem ser documentados, quantificados e aprovados formalmente. Sem análise residual, exceções ficam sem justificação técnica clara.

:::userstory
**História.**  
Como **GRC/Compliance**, quero **registar o risco residual após aplicar os controlos definidos**, para fundamentar decisões de aceitação, mitigação ou transferência de risco.

**Critérios de aceitação (BDD).**
- **Dado** que alguns controlos não são aplicáveis ou foram excecionados  
  **Quando** documento as justificações técnicas e avalio risco residual  
  **Então** registo a análise de forma auditável com **aprovação de AppSec Engineer e Gestão**

**Critérios de aceitação (DoD).**
- [ ] Controlos não aplicados identificados explicitamente  
- [ ] Justificação técnica detalhada registada (ex: "Requisito X não aplicável porque Y")  
- [ ] **Risco residual avaliado contra limiares L1–L3** (ex: L2 máximo = risco médio)  
- [ ] **Aprovação formal por AppSec Engineer documentada**  
- [ ] **Em L3: aprovação adicional por Gestão Executiva/CISO**  
- [ ] Entrada em ferramenta GRC com audit trail  

:::

**Artefactos & evidências.**
- Ficheiro: `risco-residual.md` ou entrada em ferramenta GRC  
- Conteúdo: `id | controlo_não_aplicado | justificação | risco_residual | aprovadores | data`  
- Evidência: assinatura digital, email de aprovação, ou registo versionado

> **Referência:** Este US implementa [Cap 14-US-01: Processo formal de exceções]
> no contexto de análise de risco residual. A aprovação formal e o TTL das exceções devem seguir a política master definida em Cap 14.

**Proporcionalidade por risco.**
| L1 | L2 | L3 |
|----|----|----|
| Opcional (se crítico) | Obrigatório | Obrigatório |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Validação | Após mapeamento de matrix; pré-release | **GRC/Compliance + AppSec Engineer + Developer** | 5 dias úteis |

**Ligações úteis.**
- Risco Residual  
- Critérios Aceitação Risco  
- 07-roles.md

---

### **US-08 - Aceitação de Risco com TTL e Revalidação Obrigatória**

**Contexto.**  
Quando o nível de risco residual é aceitável mas com **Time-To-Live (TTL) limitado**, o risco pode expirar. Sem revalidação automática, excepções "dormem" indefinidamente.

:::userstory
**História.**  
Como **GRC/Compliance**, quero registar aceitações com **TTL explícito e alerta de re-aprovação**, para garantir que excepções não se tornam permanentes por esquecimento.

**Critérios de aceitação (BDD).**
- **Dado** que existe uma decisão de aceitar risco residual  
  **Quando** defino **TTL em função do nível** (L1=12m, L2=6m, L3=3m)  
  **Então** configuro alerta de **revalidação 15 dias antes da expiração**  
- E documento que **sem re-aprovação explícita, a excepção expira automaticamente**

**Critérios de aceitação (DoD).**
- [ ] Owner da excepção designado e contactível  
- [ ] **TTL definido por nível** (L1: 12 meses | L2: 6 meses | L3: 3 meses)  
- [ ] Critérios de encerramento claros (ex: "após implementação mitigação X" ou "até data Y")  
- [ ] **Alertas configurados 15 dias antes da expiração** (email ou issue automática)  
- [ ] Registo rastreável em ferramenta GRC ou repositório (com data e decisor)  
- [ ] **Re-aprovação explícita exigida para prorrogação** (mesmo critério de aprovação original)  
- [ ] **Em L3: aprovação adicional por Gestão Executiva/CISO antes de renovação**  
- [ ] **Se biz impact relevante: Product Owner notificado e de acordo**  

:::

**Artefactos & evidências.**
- Ficheiro: `aceitacoes-risco.md` ou entrada em ferramenta GRC/JIRA  
- Tabela: `excepção_id | L1/L2/L3 | data_aceitação | TTL | data_expiração | owner | critério_encerramento | status`  
- Evidência: aprovação datada, alerta de expiração, re-aprovação documentada ou registo de encerramento

**Proporcionalidade (TTL por nível).**
| Nível | TTL Recomendado | Revalidação | Obrigatório? |
|---|---|---|---|
| L1 | 12 meses | Anual | Recomendado |
| L2 | 6 meses | Semestral | Obrigatório |
| L3 | 3 meses | Trimestral | **Obrigatório + Gestão Executiva** |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Governação + Segurança | Decisão de aceitar risco; alerta 15d antes expiração | **GRC/Compliance (cria, registra) + AppSec Engineer (revalida, aprova) + Gestão Executiva/CISO (aprova L3) + Product Owner (notificado se impacto negócio)** | Criação: 2 dias úteis; Re-aprovação: 5 dias úteis antes da expiração |

**Ligações úteis.**
- Critérios Aceitação Risco  
- Análise de Risco Residual  
- 07-roles.md

---

### US-05 - Validação antes do go-live

**Contexto.**  
Antes de entrar em produção é necessário validar se todos os requisitos aplicáveis foram cumpridos. Esta etapa impede deployes com cobertura de segurança incompleta.

:::userstory
**História.**  
Como **QA**, quero **validar que os requisitos aplicáveis por nível de risco estão cumpridos antes da entrada em produção**, para garantir conformidade com a classificação atribuída.

**Critérios de aceitação (BDD).**
- **Dado** que a aplicação está pronta para go-live  
  **Quando** reviso a checklist de controlos aplicáveis (extraída de US-02)  
  **Então** confirmo que **evidências estão documentadas, testadas e aprovadas por AppSec Engineer**

**Critérios de aceitação (DoD).**
- [ ] Checklist de controlos revista completa (baseada em matriz aplicada)  
- [ ] Evidências documentadas (testes, relatórios, scans, revisões)  
- [ ] **Aprovação formal de AppSec Engineer registada**  
- [ ] **Em L3: aprovação adicional por Gestão/PMO ou CISO**  
- [ ] Nenhuma exceção não-aprovada pendente  
- [ ] Rastreamento: cada controlo ↔ evidência documentado  

:::

**Artefactos & evidências.**
- Ficheiro: `checklist-go-live.md` ou entrada em pipeline CI/CD  
- Conteúdo: `controlo | L1/L2/L3 | evidência | aprovação_AppSec | status_go_live`  
- Evidência: log de aprovação em pipeline, assinatura em documento, ou registo em GRC

**Proporcionalidade por risco.**
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Recomendado (obrigatório) | Obrigatório (formal + assinatura) |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Pré-Release | Aplicação pronta para go-live | **QA + AppSec Engineer + Gestão/PMO (L3)** | 2 dias úteis antes de deploy |

**Ligações úteis.**
- Matriz de Controlos por Risco  
- 07-roles.md

## 🚧 Cascata de Gates de Validação (US-05 em Contexto)

A validação antes do go-live é implementada através de uma **cascata de gates sequenciais**, cada um verificando dimensões específicas de segurança em capítulos distintos. A falha em qualquer gate bloqueia promoção a produção.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│  APLICAÇÃO PRONTA PARA RELEASE                                                  │
│  └─ Trigger: Pipeline de promoção a staging/produção                            │
│                                                                                 │
│                                       ▼                                         │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 1: Requisitos & Risco (Cap 01)                                      │  │
│  │ Responsável: QA + AppSec Engineer                                        │  │
│  │ Validação:                                                               │  │
│  │   ✓ Classificação de risco atribuída (L1/L2/L3)                          │  │
│  │   ✓ Matriz de controlos aplicáveis extraída                             │  │
│  │   ✓ Ameaças esperadas mapeadas (STRIDE, MITRE ATT&CK)                   │  │
│  │   ✓ Nenhuma exceção de risco residual não-aprovada pendente             │  │
│  │ Bloqueio se: Risco residual > threshold aprovado ou exceções pendentes   │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 2: Requisitos de Segurança (Cap 02)                                 │  │
│  │ Responsável: AppSec Engineer                                             │  │
│  │ Validação:                                                               │  │
│  │   ✓ Requisitos funcionalidade + segurança completos                      │  │
│  │   ✓ Gestão de exceções: todas as exceções têm aprovação + SLA            │  │
│  │   ✓ Rastreamento requisito ↔ teste ↔ evidência completo                 │  │
│  │ Bloqueio se: Requisitos incompletos ou exceções sem aprovação            │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 3: Dependências & SBOM (Cap 05)                                     │  │
│  │ Responsável: DevOps + AppSec Engineer                                    │  │
│  │ Validação:                                                               │  │
│  │   ✓ SBOM completo em CycloneDX/SPDX (todas as dependências listadas)     │  │
│  │   ✓ Scan de vulnerabilidades: nenhuma crítica não-mitigada em L2/L3      │  │
│  │   ✓ CVEs com risco > threshold têm mitigação/exceção documentada         │  │
│  │   ✓ Dependências verificadas em repositórios de reputação                │  │
│  │ Bloqueio se: CVE crítico não-mitigado ou SBOM incompleto                 │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 4: Artefactos CI/CD (Cap 07)                                        │  │
│  │ Responsável: DevOps + AppSec Engineer                                    │  │
│  │ Validação:                                                               │  │
│  │   ✓ Pipeline CI/CD: versionado, auditado, secrets em manager            │  │
│  │   ✓ Assinatura & proveniência de artefactos (in-toto, Cosign)            │  │
│  │   ✓ Testes de segurança integrados (SAST, dependency scanning, SBOM)     │  │
│  │   ✓ Logs de auditoria de cada deploy recolhidos e retidos                │  │
│  │ Bloqueio se: Pipeline não-auditado ou artefactos não-assinados           │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 5: Infraestrutura & Containers (Cap 08/09)                          │  │
│  │ Responsável: DevOps + Arquitetos                                         │  │
│  │ Validação:                                                               │  │
│  │   ✓ IaC versionado, aprovado, testado (Terraform, Helm, CloudFormation) │  │
│  │   ✓ Imagens container: base segura, SBOM, scanning, assinadas           │  │
│  │   ✓ Policies de runtime (OPA/Kyverno) ativas e bloqueantes em L2/L3     │  │
│  │   ✓ Network policies e RBAC configurados                                 │  │
│  │ Bloqueio se: Imagem não-assinada ou policies não-ativas                  │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 6: Deploy & Monitorização (Cap 11/12)                               │  │
│  │ Responsável: DevOps + AppSec Engineer + SRE                              │  │
│  │ Validação:                                                               │  │
│  │   ✓ Apenas artefactos assinados são promovidos                           │  │
│  │   ✓ Ambiente staging validado (testes + aprovações concluídas)           │  │
│  │   ✓ Monitorização + alertas ativados pré-deploy (logs, métricas, eventos)│  │
│  │   ✓ Playbook de incidentes documentado e testado                         │  │
│  │   ✓ Aprovação formal registada (assinatura, timestamp, audit trail)      │  │
│  │ Bloqueio se: Monitorização não-ativa ou aprovação não-documentada        │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ✅ DEPLOY EM PRODUÇÃO AUTORIZADO                                             │
│     └─ Timestamp de aprovação registado em audit trail central (Cap 14)       │
│                                                                                │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Características Críticas da Cascata:**
- **Sequencial:** Cada gate é pré-requisito para o próximo (falha em gate N bloqueia gate N+1)
- **Distribuído:** Cada gate é propriedade de capítulo específico, mas supervisionado por AppSec centralizado (Cap 14)
- **Auditável:** Todas as decisões e aprovações são registadas com timestamp e responsável
- **Proporcional:** L1 pode ter gates mais leves (audit mode), L2/L3 são bloqueantes (enforce mode)
- **Rastreável:** Gate 6 (Cap 11/12) alimenta matriz de rastreamento em Cap 14 para evidência de conformidade

---

### US-06 - Mapeamento de ameaças por nível de risco


**Contexto.**  
Cada nível de criticidade deve ser confrontado com ameaças conhecidas (STRIDE, MITRE ATT&CK) para validar que a cobertura de controlos é adequada. Sem mapeamento, seleção de controlos fica ad-hoc.

:::userstory
**História.**  
Como **AppSec Engineer**, quero **verificar se as ameaças esperadas para o nível de criticidade estão cobertas por controlos aplicados ou exceções rastreáveis**, para garantir que a seleção de controlos é fundamentada em ameaças reais.

**Critérios de aceitação (BDD).**
- **Dado** que a aplicação tem nível de criticidade definido (L1/L2/L3)  
  **Quando** consulto o mapeamento de ameaças apropriado (STRIDE, MITRE ATT&CK)  
  **Então** verifico que **todas as ameaças críticas têm cobertura por controlo ou exceção documentada**

**Critérios de aceitação (DoD).**
- [ ] Ameaças identificadas por nível (ex: STRIDE para L1, MITRE ATT&CK para L2/L3)  
- [ ] **Mapeamento ameaça ↔ controlo documentado** (ex: Spoofing → MFA, Tampering → TLS)  
- [ ] Cobertura validada por controlo aplicado ou exceção aprovada  
- [ ] **Arquitetos envolvidos para validação de contexto técnico**  
- [ ] Resultados registados e rastreáveis  
- [ ] **Se ameaça crítica não coberta: dispara US-04 (risco residual) ou mitigação obrigatória**  
- [ ] **Se assistido por ferramenta de mapeamento:**
  - [ ] Ferramenta & versão documentados
  - [ ] Ameaças genéricas não-contextuais filtradas?
  - [ ] Ameaças específicas de domínio adicionadas (validação especialistas)?
  - [ ] Priorização (crítica vs. minor) correcta?
  - [ ] Ameaças críticas não cobertas dispararam US-04 (risco residual)?
  - [ ] Validação por Arquitetos + especialistas de domínio concluída
  - [ ] Referência: addon-11: Validação Assistida por Ferramentas

:::

**Artefactos & evidências.**
- Ficheiro: `ameacas-mapeamento.md` com tabela: `ameaca | categoria | controlo_aplicado | cobertura_sim_nao | exceção`  
- Localização: Repo documentação de segurança  
- Evidência: rastreamento em Jira/backlog, validação por AppSec + Arquitetos

**Proporcionalidade por risco.**
| L1 | L2 | L3 |
|----|----|----|
| Opcional (STRIDE básico) | Recomendado (STRIDE completo) | Obrigatório (STRIDE + MITRE ATT&CK) |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Design | Após arquitetura definida | **AppSec Engineer + Arquitetos + Developer** | Antes de dev começar |
| Validação | Pré-release (L2/L3) | **AppSec Engineer** | 1 semana antes de release |

**Ligações úteis.**
- Mapeamento de Ameaças por Risco  
- Capítulo 03 - Threat Modeling  
- 07-roles.md

---

### **US-09 - Classificação de Artefactos Técnicos (Pipeline, IaC, Imagens)**

**Contexto.**  
A classificação da aplicação não é suficiente; **artefactos de entrega** (Dockerfile, scripts CI/CD, IaC, imagens) herdam a criticidade e exigem controlos específicos descritos nos capítulos 07 (CI/CD Seguro), 08 (IaC), 09 (Containers).

:::userstory
**História.**  
Como **DevOps/SRE**, quero classificar **artefactos técnicos da aplicação** (Dockerfile, pipeline, IaC, imagens) com a mesma criticidade, para garantir que controlos de segurança acompanham a integridade da entrega.

**Critérios de aceitação (BDD).**
- **Dado** que uma aplicação tem uma classificação L1/L2/L3  
  **Quando** crio/reviso artefactos de entrega (Dockerfile, script CI/CD, manifesto IaC, imagem)  
  **Então** aplico os **controlos de capítulos 07/08/09 equivalentes ao nível**  
- E documento **rastreabilidade: aplicação → artefacto → capítulo 07/08/09 → REQ-XXX**

**Critérios de aceitação (DoD).**
- [ ] Artefactos técnicos identificados (Dockerfile, pipeline/GitHub Actions/GitLab CI, Terraform/Helm, imagem registada)  
- [ ] **Classificação do artefacto registada = classificação da aplicação** (ex: L3 app → L3 Dockerfile, L3 pipeline)  
- [ ] **Controlos cap. 07 (CI/CD) aplicados se pipeline** (secrets manager, assinatura, scanning, audit log)  
- [ ] **Controlos cap. 08 (IaC) aplicados se infraestrutura-as-code** (versionamento, revisão rigorosa, scanning, tags)  
- [ ] **Controlos cap. 09 (Containers) aplicados se imagem Docker** (base image segura, scanning vulnerabilidades, runtime policy, registry autenticação)  
- [ ] **Tabela de rastreamento: artefacto | nível | capítulo | REQ-XXX | responsável | status**  
- [ ] **Arquitetos valida alinhamento entre controlos do artefacto e necessidades da aplicação**  
- [ ] **AppSec Engineer aprova antes do deploy**  

:::

**Artefactos & evidências.**
- Ficheiro: `artefactos-tecnicos.md` ou tabela em repositório  
- Tabela: `artefacto | nível | tipo (Dockerfile/pipeline/IaC) | capítulo | REQ-XXX | status | owner`  
- Evidência: commit com tags de classificação, issue rastreável, scan report, approval email

**Proporcionalidade (por tipo de artefacto).**
| Artefacto | Cap. Aplicável | L1 (Recomendado) | L2 (Obrigatório) | L3 (Reforçado) |
|---|---|---|---|---|
| Dockerfile | 09 | Base segura | Full hardening + scanning | Base segura auditada, scanning automático, registry private |
| Pipeline (GH/GL/Jenkins) | 07 | Secrets em variables | Secrets em KV, audit log, SAST | Secrets em KV, audit log, SAST+DAST, assinatura imagem, 2FA |
| IaC (Terraform/Helm) | 08 | Versionamento | Versionamento + review | Versionamento + review rigorosa + compliance scanning |
| Imagem registada | 09 | Versão explícita | Scan vulnerabilidades | Scan + runtime policy + image signing |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Construção + Entrega | Criação/atualização de artefacto | **DevOps/SRE (proprietário, implementa controlos) + Arquitetos (valida alinhamento) + AppSec Engineer (aprova)** | Approval antes de deploy: 2 dias úteis |

**Ligações úteis.**
- Cap. 07 - CI/CD Seguro  
- Cap. 08 - IaC e Infraestrutura  
- Cap. 09 - Containers e Imagens  
- 07-roles.md

---

### **US-10 - KPIs, Métricas e Reporting de Classificação e Conformidade**

**Contexto.**  
Sem indicadores e visibilidade executiva, não há governança efetiva nem feedback loop para melhoria contínua. É necessário consolidar métricas operacionais e de conformidade sobre o ciclo de classificação.

:::userstory
**História.**  
Como **GRC/Compliance**, quero consolidar **KPIs mensais/trimestrais** sobre a classificação, exceções e ciclos de revisão, para demonstrar maturidade de governação à **Gestão Executiva/CISO** e à **Auditoria**.

**Critérios de aceitação (BDD).**
- **Dado** que existem classificações, exceções, revisões e artefactos registados  
  **Quando** consolido os dados mensalmente  
  **Então** gero relatório com **KPIs por nível, tendências, alertas de conformidade e recomendações**  
- E distribuo a **Gestão Executiva/CISO + Auditores Internos**

**Critérios de aceitação (DoD).**
- [ ] **KPI 1: % de aplicações classificadas** (válidas com data de revisão/revalidação próxima)  
- [ ] **KPI 2: % de exceções ainda ativas** vs **% expiradas ou prorrogadas** (por nível)  
- [ ] **KPI 3: Lead time para classificação inicial** (dias desde criação até L1/L2/L3 atribuído)  
- [ ] **KPI 4: Lead time para revisão** (dias desde trigger até decisão final)  
- [ ] **KPI 5: Conformidade a cadência de revisão** (% de app L2/L3 revistos no prazo 6m/3m)  
- [ ] **KPI 6: % de controlos mapeados** (aplicações com todos os REQ-XXX do nível implementados ou com excepção TTL válida)  
- [ ] **KPI 7: Ameaças críticas não cobertas** (número e lista de aplicações com risco crítico residual)  
- [ ] **Série temporal (trend)**: Gráficos de KPI 1–7 dos últimos 6 meses  
- [ ] **Alertas automáticos**: Notificação se KPI 2 (exceções expiradas) > 5%, KPI 5 (conformidade) < 90%  
- [ ] **Fonte única de dados**: Ferramenta GRC, repositório, ou dashboard integrado (com rastreabilidade a aplicação original)  
- [ ] **Reporte trimestral** assinado por **GRC/Compliance**, distribuído a **Gestão Executiva/CISO + Auditores**  
- [ ] **Recomendações actionáveis**: Top 3 causas de atraso ou não-conformidade + plano de ação  

:::

**Artefactos & evidências.**
- Ficheiro: `kpi-classificacao-YYYY-MM.md` ou entrada em ferramenta BI/dashboard  
- Tabela: `data | KPI | valor | meta | % conformidade | tendência | alertas`  
- Evidência: reporte PDF/markdown datado, distribuição de email, apresentação a Gestão Executiva, registo de auditoria

**Proporcionalidade (reporte por nível de detalhe).**
| Audiência | Frequência | KPIs mínimos | Formato |
|---|---|---|---|
| **Operações/AppSec** | Semanal (opcional) | % classified, exceções próximas de expirar, atrasos revisão | Dashboard interno |
| **Product Owners** | Mensal | % classified (por negócio/squad), lead time, exceções de app |  Email com resumo ou Slack |
| **Gestão Executiva/CISO** | Trimestral | KPI 1,2,5,6,7; alertas críticos; recomendações | PDF formal com gráficos |
| **Auditores Internos** | Anual + ad-hoc | Série completa KPI 1-7; conformidade a regulamentos; draft policies; lista de exceções | PDF + acesso a repositório versionado |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Governação + Reporting | Fim de período (mensal/trimestral) | **GRC/Compliance (coleta dados, consolida, redige) + AppSec Engineer (valida métricas técnicas) + Gestão Executiva/CISO (aprova distribuição)** | Reporte: 10 dias úteis após fim do período; Distribuição: 1 dia após aprovação |

**Ligações úteis.**
- Critérios Aceitação Risco  
- Mapeamento de Ameaças  
- 07-roles.md  
- Auditoría & Rastreabilidade (Cap. 02)

---

### **US-11 - Políticas Organizacionais Formais (Classificação, Risco, Revisão Periódica, Rastreabilidade)**

**Contexto.**  
As user stories US-01 a US-10 definem o **como operacionalizar** a classificação. As políticas organizacionais definem o **por quê** (mandato), **quem aprova**, **qual o critério** e **como auditar**. Sem políticas, não há governança formal nem conformidade a regulamentos (NIS2, DORA,).

:::userstory
**História.**  
Como **Gestão Executiva/CISO**, quero que existam **4 políticas organizacionais formais aprovadas** (Classificação de Risco, Aceitação de Risco, Revisão Periódica, Rastreabilidade/Auditoria), para assegurar que **todas as equipas operam sob os mesmos critérios** e que o manual é **cumprido uniformemente e auditado**.

**Critérios de aceitação (BDD).**
- **Dado** que a organização necessita de **conformidade formal** a regulamentos (NIS2, DORA, ISO 27001)  
  **Quando** publico 4 políticas organizacionais assinadas por **Gestão Executiva**  
- E treinamento obrigatório é documentado com **attestation** de compreensão  
  **Então** **Auditores podem validar conformidade** e **todas as decisões de classificação/risco têm fundamento normativo**

**Critérios de aceitação (DoD).**
- [ ] **Política 1 - Classificação de Risco**: Modelo E+D+I, critérios L1/L2/L3, responsabilidades por nível, frequency de revisão (obrigatória em L2/L3)  
- [ ] **Política 2 - Aceitação de Risco**: Critérios de aceitabilidade, TTL por nível, aprovadores, exceções + revalidação obrigatória antes da expiração  
- [ ] **Política 3 - Revisão Periódica**: Cadência time-based (12m/6m/3m), owners, escalonamento de decisões, triggers para revisão de matriz e ameaças  
- [ ] **Política 4 - Rastreabilidade & Auditoria**: Registo centralizado de classificações, exceções, revisões; versionamento; pista de auditoria; retenção de dados; acesso restrito  
- [ ] **Cada política contém**: objetivo, âmbito, responsáveis, critérios decisão, processo aprovação, frequência revisão, ligação a capítulos do manual  
- [ ] **Assinatura formal** por **Gestão Executiva/CISO** e **GRC/Compliance** datada  
- [ ] **Publicação acessível** em Wiki interna, repositório de políticas, ou portal de compliance  
- [ ] **Treinamento obrigatório** para **todas as equipas** (Dev, AppSec, GRC, Gestão, Auditores) com **attestation de participação + quiz de compreensão**  
- [ ] **Revisão anual** por **GRC/Compliance + Auditores Internos** com registo de qualquer alteração  
- [ ] **Evidência de conformidade**: Checklist de cada aplicação validando aderência às 4 políticas (L1/L2/L3)  

:::

**Artefactos & evidências.**
- Ficheiro: `POLITICA-01-classificacao-risco.md`, `POLITICA-02-aceitacao-risco.md`, `POLITICA-03-revisao-periodica.md`, `POLITICA-04-rastreabilidade-auditoria.md`  
- Local: Wiki institucional, Repositório `docs/policies/` ou servidor de compliance  
- Evidência: PDF assinado, data/versão, distribuição de email, registo de treinamento (nome+data+assinatura), quiz scores, auditoria anual  

**Proporcionalidade (aplicação por nível).**
| Nível | Classificação | Aceitação | Revisão Periódica | Rastreabilidade |
|---|---|---|---|---|
| L1 | Recomendado (simplificado) | Recomendado | Recomendado (anual) | Recomendado |
| L2 | Obrigatório (completo) | Obrigatório + TTL | Obrigatório (semestral) | Obrigatório + audit trail |
| L3 | Obrigatório (formal com aprovações) | Obrigatório + TTL + re-aprovação Gestão | Obrigatório (trimestral) | Obrigatório + rastreamento granular |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Governação + Conformidade | Kick-off (criação políticas), anualmente (revisão) | **Gestão Executiva/CISO (assina, aprova) + GRC/Compliance (redige, distribui, treina) + AppSec Engineer (input técnico) + Auditores Internos (valida conformidade) + Todos os equipas (treino + attestation)** | Redação: 30 dias; Assinatura: 5 dias; Distribuição: 1 dia; Treinamento inicial: 10 dias; Revisão anual: 15 dias |

**Ligações úteis.**
- Intro Cap. 01 - Modelo E+D+I e Ciclos  
- Criterios Aceitação Risco (addon 03)  
- Ciclo de Vida do Risco (addon 02)  
- NIS2 / DORA / ISO 27001 (Cap. 002)  
- 07-roles.md

---

## 📑 Artefactos esperados (por fase)

| Fase         | Artefacto                          | Quem produz         | Onde fica                  | Evidência mínima                              |
|--------------|------------------------------------|---------------------|----------------------------|-----------------------------------------------|
| Início       | `classificacao-aplicacao.yaml`     | Developer / Team Lead     | Repo `security/`           | Commit + revisão AppSec Engineer |
| Planeamento  | `matriz-controlos.md`              | Developer / Team Lead     | Backlog / wiki             | REQ-XXX referenciados (Cap. 02); aprovado AppSec |
| Revisão      | `classificacao-revisao.md`         | AppSec Engineer      | Repo `docs/`               | Issue/ata datada; decisão justificada |
| Release      | `checklist-go-live.md`             | QA                  | Pipeline CI/CD             | Aprovação formal AppSec Engineer + Gestão (L3) |
| Operação     | `risco-residual.md`                | GRC/Compliance    | Ferramenta GRC / repo      | Owner + TTL + critérios encerramento; aprovação |
| Periódico    | `classificacao-revisao-anual.md` (L1), `semestral.md` (L2), `trimestral.md` (L3) | AppSec Engineer + GRC/Compliance | Repo docs / GRC | Data revisão, justificação manter/alterar, próxima data |
| Aceitação    | `aceitacoes-risco.md` com TTL      | GRC/Compliance    | Ferramenta GRC / repo      | TTL definido, owner, critério encerramento, alertas |
| Artefactos   | `artefactos-tecnicos.md`           | DevOps/SRE + Arquitetos | Repo `platform/docs` | Classificação por artefacto, rastreamento REQ, aprovação AppSec |
| Contínuo     | `kpi-classificacao-YYYY-MM.md`    | GRC/Compliance    | Dashboard / Repositório de reporting | KPI 1-7, série temporal, alertas, recomendações |
| Governação   | `politicas-organizacionais.md` (4 políticas) | GRC/Compliance + AppSec | Docs / Wiki / Política | Aprovação Gestão Executiva, treinamento + attestation, auditoria |

> **Formato canónico de evidência** (sugestão): `id`, `data`, `eixos` (E/D/I), `nível`, `decisão`, `owner`, `ligações` (issues/PRs), `aprovadores`, `expiração` (se aplicável).

---

## 📊 Matriz de proporcionalidade L1–L3

| Prática / Story                                 | L1 | L2 | L3 | Observações |
|-------------------------------------------------|----|----|----|-------------|
| US-01 - Classificação inicial                    | ✔  | ✔  | ✔  | Validação AppSec obrigatória em L2/L3 |
| US-02 - Aplicação da matriz (c/ REQ-XXX)        | ✔  | ✔  | ✔  | Rastreabilidade REQ para Cap. 02 |
| US-03 - Revisão por alteração relevante          | ✔  | ✔  | ✔  | Event-based, cascata a US-02/US-06 |
| **US-07-rev - Revisão periódica time-based**    | ✔ (Rec.) | ✔  | ✔  | Cadência: 12m / 6m / 3m (obrigatória em L2/L3) |
| US-04 - Risco residual                           | (opcional) | ✔ | ✔  | Aprovações formais em L3 |
| **US-08-rev - Aceitação com TTL**                | (Rec.) | ✔ | ✔  | TTL 12m/6m/3m; re-aprovação obrigatória em L2/L3 |
| US-05 - Validação go-live                        | (Rec.) | ✔ | ✔  | Aprovação AppSec + Gestão em L3 |
| US-06 - Mapeamento de ameaças                    | (opcional) | ✔ | ✔  | Validação Arquitetos; escala de risco crítico |
| US-09 - Classificação de artefactos técnicos    | ✔ (Rec.) | ✔ | ✔  | Aplica controlos Cap. 07/08/09; Arquitetos valida |
| **US-11 - Políticas Organizacionais Formais**   | (Rec.) | ✔ | ✔  | 4 políticas obrigatórias em L2/L3; treinamento + auditoria |
| **US-10 - KPIs e Reporting**                    | (Rec.) | ✔ | ✔  | Mensal (ops), trimestral (gestão), anual (auditores) |

---

## 📝 Recomendações operacionais

- Integrar a classificação de risco desde o **kick-off** do projeto.  
- Reavaliar a classificação **por alteração** e **por calendário** (time-based).  
- Manter a documentação **versionada e rastreável** em repositório controlado.  
- Mapear requisitos diretamente para **REQ-XXX (Cap. 02)** no backlog.  
- Exigir **TTL/expiração** em todas as aceitações de risco.  
- Validar proporcionalidade no go-live e documentar evidências.  
- Consolidar **KPIs** organizacionais para *compliance* e melhoria contínua.  
- Alinhar práticas com as **políticas organizacionais** de classificação, exceções e revisão periódica.

---

# 🏛️ Políticas Organizacionais - Gestão de Risco

A adoção eficaz do Capítulo 01 - Gestão de Risco - exige a existência de **políticas organizacionais formais** que **enquadrem, legitimem e sustentem a aplicação das práticas descritas neste capítulo**.

---

## 📌 Nota fundamental

> ⚠️ As práticas operacionais prescritas neste capítulo (classificação, revisão, aceitação, rastreabilidade) **devem ser legitimadas formalmente por políticas organizacionais aprovadas**.

Estas políticas:

- Tornam **visível e vinculativa** a prática da gestão de risco aplicacional dentro da organização;
- Permitem que as decisões de segurança deixem de depender de iniciativa individual;
- Servem de base normativa para **auditorias internas e externas**.

> 📎 A exigência de políticas formais de classificação e aceitação de risco é uma **expectativa explícita** em normas como **ISO/IEC 27005**, **ENISA Risk Management**, **NIST SSDF** e **CIS Controls v8**.

> 🧩 Este capítulo **implementa, na prática, o que as políticas definem** - a política aprova, o capítulo operacionaliza.

---

## 🧾 Políticas recomendadas

| Nome da Política                                   | Obrigatória? | Aplicação                             | Conteúdo mínimo esperado                                                                                      |
|----------------------------------------------------|--------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Política de Classificação de Risco Aplicacional    | ✅ Sim       | Todos os projetos e equipas de produto | Modelo de classificação obrigatório (exposição, dados, impacto); momentos de aplicação; registo e rastreio. |
| Política de Aceitação de Risco Residual            | ✅ Sim       | Segurança, gestão, donos de produto    | Critérios formais para aceitação; responsáveis; validade temporal; registo e rastreabilidade.               |
| Política de Revisão Periódica de Risco             | ✅ Sim       | Toda a organização                     | Frequência mínima (ex: 6 meses); triggers obrigatórios; evidência exigida.                                   |
| Política de Rastreabilidade de Decisões de Segurança | ⚠️ Opcional | Organizações sujeitas a auditoria      | Versionamento de classificações; ligação com arquitetura, requisitos e controlos.                           |

---

## 🧩 Correspondência com frameworks normativas

| Framework              | Requisitos cobertos pelas políticas acima                                       |
|------------------------|----------------------------------------------------------------------------------|
| **ISO/IEC 27005**      | Identificação (8.2), Avaliação (8.3), Aceitação (8.5)                            |
| **NIST SP 800-30**     | Etapas 1–4 (Caracterização, Ameaças, Vulnerabilidades, Impacto)                 |
| **NIST SSDF**          | RM.1 (Categorize SW), RM.2 (Assess Risk), RM.3 (Manage Risk)                    |
| **ENISA Risk Management** | Sec. 2.3, 3.1 - definição formal de políticas de avaliação e aceitação de risco |
| **CIS Controls v8**    | Control 2, 4 - políticas para inventário, avaliação e aceitação de risco         |
| **OWASP SAMM**         | Governance > Risk Management (níveis 1 e 2)                                      |


---

## 🧱 Estrutura sugerida de cada política

Cada política organizacional deve conter, no mínimo:

- **Objetivo e âmbito** da política;
- **Âmbito de aplicação**: quem, onde e quando se aplica;
- **Regras e critérios obrigatórios** (ex: quando aplicar, como classificar, quem aprova);
- **Papéis e responsabilidades** (segurança, produto, arquitetura, gestão);
- **Exigência de documentação e rastreabilidade**;
- **Periodicidade de revisão da política em si** (ex: anual).

---

## ✅ Recomendações finais

- Estas políticas devem ser **oficialmente aprovadas** pela gestão de segurança e da organização;
- Devem estar **publicadas e acessíveis** a todas as equipas;
- A sua existência é uma **pré-condição para garantir coerência, auditabilidade e maturidade real da segurança by design**;
- A sua aplicação deve estar alinhada com as práticas descritas neste capítulo.

> 📌 Templates para estas políticas poderão ser disponibilizados como ficheiros `60-*.md` complementares em futuras versões do manual.

---

# 🧭 Recomendações Avançadas - Gestão de Risco

Este anexo apresenta práticas **não obrigatórias**, mas altamente recomendadas para organizações que pretendam alcançar **níveis mais elevados de maturidade e auditabilidade** na gestão de risco aplicada ao ciclo de vida de software.

Estas recomendações **complementam as práticas obrigatórias do Capítulo 01**, podendo ser adotadas de forma progressiva consoante:

- O contexto regulatório aplicável;
- O apetite e tolerância ao risco da organização;
- O nível de maturidade pretendido (ex: ISO 27001, SOC 2, PCI-DSS);
- Os objetivos estratégicos de visibilidade e governança.

---

## 1. Integração com Ferramentas de GRC

- Integrar o modelo de classificação e aceitação de risco com ferramentas corporativas de GRC (Governance, Risk & Compliance), como:
  - **ServiceNow Risk**
  - **Archer GRC**
  - **Riskonnect**, entre outras.
- Esta integração permite:
  - Alinhar decisões técnicas com riscos organizacionais;
  - Suportar processos de auditoria internos e externos;
  - Garantir rastreabilidade centralizada das decisões.

---

## 2. Justificativas Estruturadas de Aceitação de Risco

- Adotar um **modelo formal de aceitação de risco informada**, com os seguintes campos mínimos:
  - Descrição e impacto do risco;
  - Motivo da aceitação;
  - Alternativas consideradas;
  - Compensações aplicadas (se existirem);
  - Responsável pela decisão e validade temporal;
- Deve ser versionado, rastreável e auditável.

---

## 3. SLA para Revisão da Classificação de Risco

- Estabelecer **prazos máximos para revisão formal da classificação**, como:
  - L3: reavaliação a cada 90 dias;
  - L2: a cada 180 dias;
  - L1: até 365 dias.
- Automatizar alertas e tarefas no backlog de segurança.

---

## 4. Suporte à Decisão com Visualização de Risco

- Usar ferramentas de visualização para:
  - Matrizes de calor (heatmaps) por aplicação ou equipa;
  - Dashboards com cruzamento risco vs controlo aplicado;
  - Alertas visuais de classificações expiradas.
- Facilita a **comunicação com gestão, auditoria e stakeholders não técnicos**.

---

## 5. Versionamento e Auditoria de Classificações

- Manter registo histórico de todas as classificações com:
  - Timestamp e autor;
  - Motivo da alteração;
  - Referência cruzada à release ou mudança técnica;
  - (Opcional) Hash digital para verificação de integridade.
- Essencial para conformidade com **ISO 27001, SOC 2, NIS2** e similares.

---

## 6. Alinhamento com Apetite ao Risco da Organização

- Definir **níveis de risco (L1/L2/L3) alinhados com o apetite formal** da organização.
- Permite:
  - Customização por tipo de aplicação (ex: SaaS, internos, regulados);
  - Apoio à priorização orçamental de controlos;
  - Coerência entre risco aceite e investimento em segurança.

---

## 7. Revisão Cruzada entre Equipas (Peer Review)

- Estabelecer um processo de **validação cruzada de classificações** por outras equipas (ex: entre produtos, AppSec, arquitetura).
- Benefícios:
  - Redução de viés individual;
  - Aumento da maturidade coletiva;
  - Promoção de consistência e boas práticas.

---

## 8. Formação Técnica Especializada

- Incluir nos planos formativos:
  - Avaliação de risco técnico aplicada ao SDLC;
  - Leitura e interpretação dos eixos de classificação;
  - Documentação e rastreabilidade para auditorias.
- Preferencialmente ligada aos **trilhos de formação por perfil** definidos no Cap. 13.

---

## 📌 Nota Final

Estas práticas não são obrigatórias para cumprimento mínimo do modelo SbD-ToE, mas são **altamente recomendadas** para organizações que pretendam:

- Aumentar a **eficiência e visibilidade** da gestão de risco;
- Obter ganhos de **maturidade, rastreabilidade e auditabilidade**;
- **Reduzir dependência de processos informais** em decisões críticas de segurança.

> ✅ A sua adoção pode ser gradual, alinhada com a capacidade da organização e com os requisitos regulatórios aplicáveis.

---

# 📈 Maturidade - Classificação da Criticidade Aplicacional

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 01** do manual SbD-ToE e os requisitos de frameworks reconhecidas: **OWASP SAMM**, **BSIMM**, **NIST SSDF**, **SLSA** e **OWASP DSOMM**.

A prática de classificação da criticidade aplicacional é **fundacional para o modelo SbD-ToE**. Ela define **quando e com que intensidade os controlos de segurança devem ser aplicados**, suportando uma abordagem proporcional, rastreável e auditável.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento **não mede a maturidade de uma organização**, mas sim o **grau de cobertura que as práticas deste capítulo oferecem relativamente às frameworks de referência**.

### Tipos de Avaliação Utilizados

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Framework prescritiva com 3 níveis por domínio   |
| OWASP DSOMM      | `n / m` (até 4)                     | Domínios com níveis formais                      |
| NIST SSDF        | Lista de controlos cobertos         | Modelo binário, sem níveis formais               |
| BSIMM            | Lista de práticas cobertas          | Modelo observacional, não prescritivo            |
| SLSA             | Nível máximo suportado (ex: 1 de 4) | Modelo acumulativo, não gradual por domínio      |

As avaliações aqui descritas foram realizadas com base numa leitura técnico-científica de cada fonte original.

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                         | Práticas ou Objetos Cobertos                                  | Avaliação de Maturidade             |
|------------------|----------------------------------------------|----------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Governance → Risk Management                 | Classificação de risco por eixos, integração no SDLC           | **2 / 3**                           |
| OWASP DSOMM      | Risk, Security Requirements, Compliance      | Derivação de requisitos, rastreabilidade, decisão proporcional | **2 / 3** (média dos domínios)      |
| NIST SSDF v1.1   | RM.1, RM.2                                   | Classificação e avaliação de risco                             | **✔️ RM.1, RM.2**                   |
| BSIMM13          | Strategy and Metrics                         | SR1.1, SR1.5: decisão por criticidade                          | Contributo parcial, SR2 fora do âmbito |
| SLSA v1.0        | Supply Chain Risk Awareness                  | Definição proporcional de requisitos à criticidade             | **Nível 1 / 4**                     |

---

## 🧱 OWASP SAMM - Governance → Risk Management

| Nível | Descrição SAMM                                                           | Cobertura pelo Cap. 01                  |
|-------|--------------------------------------------------------------------------|------------------------------------------|
| 1     | Realiza-se classificação básica dos riscos das aplicações                | ✅ Modelo de eixos aplicável             |
| 2     | Integração com processos organizacionais e rastreabilidade               | ✅ Com suporte a versão e auditoria      |
| 3     | Análise quantitativa e retroalimentação contínua                         | ❌ Fora do âmbito do capítulo            |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Governance, Risk Management, Requirements

| Domínio                  | Níveis cobertos | Justificação técnica                                                   |
|--------------------------|----------------|------------------------------------------------------------------------|
| Risk Management          | 2 / 3          | Modelo de classificação estruturado e aplicado sistematicamente       |
| Security Requirements    | 2 / 3          | Permite derivação proporcional baseada em risco                       |
| Compliance Mapping       | 2 / 3          | Rastreabilidade a frameworks de referência presente                    |
| Governance & Metrics     | 1 / 3          | Não define KPIs quantitativos nem reporting formal                     |

> A estrutura proposta é compatível com práticas DevSecOps guiadas por risco.

---

## 🧱 NIST SSDF - Risk Management (RM)

| Controlos NIST SSDF | Descrição                                             | Alinhamento com Cap. 01 |
|---------------------|--------------------------------------------------------|--------------------------|
| RM.1                | Classificar software por criticidade                   | ✅ Totalmente coberto    |
| RM.2                | Avaliar o risco de segurança associado ao software     | ✅ Coberto               |
| RM.3                | Gerir riscos identificados                             | ❌ Fora do âmbito        |

> O capítulo cobre os primeiros passos (classificação e avaliação), deixando a gestão para outros capítulos (ex: mitigação).

---

## 🧱 BSIMM - Strategy and Metrics

| Prática BSIMM       | Alinhamento com Cap. 01                                |
|---------------------|--------------------------------------------------------|
| SR1.1               | ✅ Classificação suporta decisões de segurança          |
| SR1.5               | ✅ Avaliação de criticidade incorporada                 |
| SR2.x               | ❌ Não são cobertas práticas de medição/benchmarking    |

> A abordagem SbD-ToE foca-se em práticas operacionais integradas no ciclo de vida, não em métricas organizacionais agregadas.

---

## 🧱 SLSA - Supply Chain Levels for Software Artifacts

| Nível | Requisitos principais                   | Cobertura pelo Cap. 01         |
|-------|------------------------------------------|--------------------------------|
| 1     | Consciência de risco                     | ✅ Classificação por eixos      |
| 2     | Proveniência do software                 | ❌ Fora do âmbito               |
| 3     | Build controlado                         | ❌ Coberto noutros capítulos    |
| 4     | Cadeia totalmente verificável            | ❌ Coberto noutros capítulos    |

**🔐 Nível máximo suportado por este capítulo: SLSA 1 / 4**

---

## ✅ Conclusão

- O Capítulo 01 atinge **nível 2/3 em SAMM e DSOMM**, e **alinha-se diretamente com RM.1 e RM.2 do SSDF**;
- A prática de classificação **é pré-condição para controlos proporcionais e justificados** nos restantes capítulos;
- Constitui um mecanismo de rastreabilidade entre risco, requisitos, validações e políticas;
- Não substitui frameworks formais de análise de risco regulada, mas é compatível com **ISO 27005, NIST 800-30**, entre outras.
