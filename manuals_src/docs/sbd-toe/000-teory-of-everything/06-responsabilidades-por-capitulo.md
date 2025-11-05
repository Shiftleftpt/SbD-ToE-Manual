---
id: responsabilidades-por-capitulo
title: Práticas por Role
description: Descrição discursiva das responsabilidades de cada papel organizacional em todos os capítulos do SbD-ToE, com ligação regulatória explícita
tags: [responsabilidades, roles, capitulos, governance, nis2, dora, gdpr, aiact]
sidebar_position: 3
---



# Responsabilidades por Capítulo

A segurança só é efetiva quando cada papel compreende com clareza o seu contributo em cada área de conhecimento.  
O SbD-ToE não distribui responsabilidades de forma arbitrária; propõe uma matriz viva, onde cada função encontra o seu espaço, e onde o esforço coletivo se transforma em resiliência digital.  
O que aqui se descreve não é “mais trabalho”: são atividades que já hoje existem, mas que o manual **tipifica, organiza e torna visíveis**, conferindo-lhes transparência e rastreabilidade.  

---

## 👨‍💻 Developers

O papel do Developer é transversal a quase todo o manual, porque é no ato de escrever código que se materializam grande parte das práticas de segurança.  
A responsabilidade é dupla: garantir que o software cumpre os requisitos funcionais esperados e, em simultâneo, que o faz de forma robusta, rastreável e conforme às guidelines de segurança.  

No **Cap. 01 - Classificação da Criticidade**, o Developer contribui com informação técnica sobre integrações, dependências e impacto operacional, dados essenciais para avaliar o risco.  
No **Cap. 02 - Requisitos de Segurança**, implementa os requisitos mínimos derivados dessa classificação, integrando-os no *definition of done*.  
Participa nas sessões de **Threat Modeling (Cap. 03)**, onde traduz diagramas e cenários em controlos práticos.  
No **Cap. 04 - Arquitetura Segura**, assegura que a implementação respeita os padrões definidos pelos arquitetos.  
No **Cap. 05 - Dependências e SBOM**, declara bibliotecas utilizadas e suporta a criação de inventários auditáveis.  
O **Cap. 06 - Desenvolvimento Seguro** é central: aqui o Developer segue guidelines, utiliza linters e corrige findings de SAST, prevenindo vulnerabilidades triviais.  
Nos capítulos seguintes - **CI/CD (07)**, **IaC (08)**, **Containers (09)**, **Testes de Segurança (10)**, **Deploy (11)** e **Operações (12)** - colabora com DevOps e QA, garantindo que o código é base sólida para pipelines, infraestruturas e runtime.  
Finalmente, em **Formação (13)** e **Governança (14)**, participa em programas de capacitação e cumpre requisitos contratuais associados ao desenvolvimento.  

**Enquadramento regulatório:**  
O trabalho do Developer concretiza obrigações de **NIS2** (práticas seguras de desenvolvimento e gestão de vulnerabilidades), de **DORA** (resiliência digital em sistemas financeiros) e de princípios de *security by design* previstos no **GDPR** e no **AI Act**.

---

## 🧪 Quality Assurance (QA)

O QA garante que qualidade e segurança são inseparáveis.  
Já não basta validar que o software “funciona”: é necessário comprovar que funciona de forma resiliente e protegida contra ameaças.  

No **Cap. 01–02**, QA valida que os requisitos de segurança estão descritos de forma testável e que os critérios de aceitação os incluem.  
No **Cap. 03**, traduz cenários de threat modeling em testes objetivos.  
No **Cap. 06**, conduz testes estáticos e dinâmicos em colaboração com AppSec.  
Nos capítulos de **CI/CD (07)** e **Testes de Segurança (10)**, assegura que pipelines e regressões incorporam verificações de segurança.  
No **Cap. 12**, valida alertas e métricas de runtime, confirmando que eventos críticos são detetados.  

**Enquadramento regulatório:**  
QA materializa exigências de **NIS2** (verificação de medidas técnicas) e **DORA** (testes regulares de resiliência digital).

---

## 📋 Product Owner (PO)

O Product Owner é quem equilibra negócio e segurança, garantindo que esta não é vista como custo, mas como valor intrínseco ao produto.  

No **Cap. 01**, valida classificações de risco em função dos objetivos estratégicos.  
No **Cap. 02**, prioriza requisitos de segurança no backlog, equilibrando *features* com controlos.  
No **Cap. 05**, aprova correções críticas de dependências.  
No **Cap. 07**, define gates de release que bloqueiam versões inseguras.  
No **Cap. 11**, autoriza apenas releases com critérios de segurança cumpridos.  
Nos capítulos finais (**13–14**), assegura que formação e cláusulas contratuais refletem práticas seguras.  

**Enquadramento regulatório:**  
Apoia DORA (integração da resiliência digital no ciclo de vida) e NIS2 (incorporação da gestão de risco no negócio).

---

## 🧭 Scrum Master / Team Lead

O Scrum Master ou Team Lead é o guardião da disciplina ágil.  
A sua função é assegurar que a segurança não é relegada para “quando houver tempo”, mas integrada no planeamento e execução diária.  

No **Cap. 01–02**, facilita discussões sobre criticidade e requisitos.  
No **Cap. 03**, modera sessões de threat modeling, garantindo participação de toda a equipa.  
No **Cap. 06–07**, assegura que práticas seguras entram no sprint planning.  
No **Cap. 13**, promove capacitação e formação, apoiando cultura de segurança.  

**Enquadramento regulatório:**  
Cumpre NIS2 e DORA ao operacionalizar governação executiva sobre práticas de segurança.

---

## ⚙️ DevOps / SRE

DevOps e SRE são os artesãos da automação e da infraestrutura.  
O seu papel é garantir que segurança está embutida nos pipelines e no runtime, não aplicada como adereço posterior.  

No **Cap. 05**, automatizam SBOM e gestão de vulnerabilidades.  
No **Cap. 07**, desenham pipelines com scanners, gates e assinaturas de release.  
No **Cap. 08**, aplicam enforcement em IaC com *policy-as-code*.  
No **Cap. 09**, asseguram baseline seguro para containers.  
No **Cap. 11–12**, configuram ambientes de produção com monitorização contínua e resposta a alertas.  

**Enquadramento regulatório:**  
Essenciais para **DORA** (resiliência operacional digital) e **NIS2** (implementação de medidas técnicas adequadas).

---

## 🔐 AppSec Engineers

O papel de AppSec é ser ponte entre normas e execução técnica.  
É quem transforma obrigações abstratas em controlos concretos.  

No **Cap. 01–02**, define critérios de classificação e requisitos técnicos.  
No **Cap. 03–04**, facilita threat modeling e revisão arquitetural.  
No **Cap. 05–06**, seleciona ferramentas de SCA e coding standards.  
No **Cap. 07–10**, desenha controlos críticos de pipelines, IaC, containers e testes.  
No **Cap. 12–14**, estabelece métricas de monitorização e apoia cláusulas contratuais de segurança.  

**Enquadramento regulatório:**  
Assegura rastreabilidade exigida por **NIS2** e governação de fornecedores imposta por **DORA**.

---

## 🏅 Security Champions

Security Champions são catalisadores locais.  
Não substituem AppSec, mas tornam a segurança próxima do quotidiano da equipa.  

Atuam em todos os capítulos como facilitadores: ajudam Developers e QA, garantem que checklists são seguidos e que histórias de segurança não são ignoradas.  

**Enquadramento regulatório:**  
Apoiam a criação de cultura de segurança exigida tanto em **NIS2** como em **DORA**.

---

## 🏛️ Gestão Executiva

A gestão executiva é quem dá direção e garante condições de aplicação.  
Sem patrocínio ao mais alto nível, segurança perde prioridade e recursos.  

No **Cap. 01–02**, aprova modelos de classificação e requisitos mínimos.  
Nos **Cap. 05–09**, apoia investimento em ferramentas e processos.  
No **Cap. 11–12**, decide sobre riscos elevados em produção.  
No **Cap. 14**, garante governação e contratos coerentes.  

**Enquadramento regulatório:**  
NIS2 e DORA atribuem responsabilidade explícita ao órgão de gestão pela segurança digital.

---

## 📑 GRC / Compliance

O GRC assegura que práticas internas estão alinhadas com normas e regulamentos externos.  

Coordena auditorias, mantém documentação de risco residual e gere exceções.  
Acompanha todos os capítulos, ligando requisitos técnicos a obrigações legais (NIS2, DORA, GDPR, AI Act).  

**Enquadramento regulatório:**  
Fornece prova documental exigida em NIS2 (auditorias, reporting) e DORA (resiliência e governação de terceiros).

---

## 🏗️ Arquitetos de Software

Os arquitetos desenham soluções que resistem ao tempo e às ameaças.  

No **Cap. 03–04**, definem padrões arquiteturais e revêm integrações críticas.  
No **Cap. 07–08**, asseguram consistência arquitetural em pipelines e IaC.  
No **Cap. 11–12**, apoiam desenho resiliente de ambientes de produção.  

**Enquadramento regulatório:**  
Dão corpo a *security by design* previsto em **GDPR** e **AI Act**, e às medidas técnicas de **NIS2**.

---

## 🔧 Operações (Ops)

Ops mantêm a integridade em runtime.  
São responsáveis por patches, monitorização e resposta a incidentes.  

No **Cap. 09**, mantêm baseline de containers.  
No **Cap. 11**, asseguram resiliência em deploys.  
No **Cap. 12**, coordenam resposta a incidentes com métricas e alertas.  

**Enquadramento regulatório:**  
Linha da frente em **NIS2** (notificação em 24h) e **DORA** (continuidade operacional).

---

## 🤝 Fornecedores / Terceiros

Fornecedores são parte da cadeia de responsabilidade.  

No **Cap. 05**, fornecem SBOM atualizado.  
Nos **Cap. 08–09**, asseguram segurança em módulos IaC e imagens.  
No **Cap. 14**, cumprem cláusulas contratuais de segurança.  

**Enquadramento regulatório:**  
Gestão da cadeia de fornecimento é exigência explícita em **NIS2** e **DORA**.

---

## 📋 Auditores Internos e Externos

Auditores validam a aplicação efetiva das práticas.  
Verificam classificações de risco (Cap. 01), rastreabilidade (Cap. 02 e 25) e evidência de aplicação em todos os capítulos.  

**Enquadramento regulatório:**  
São instrumentos formais para comprovar cumprimento perante autoridades (NIS2, DORA).

---

## 🗒 Nota sobre carga de trabalho e transparência

É natural que a introdução do SbD-ToE suscite receios de aumento da carga de trabalho.  
É importante sublinhar: **não se trata de adicionar tarefas novas**, mas de **dar nomes, forma e rastreabilidade** a atividades que já existem hoje, ainda que executadas de forma menos explícita ou mais ad-hoc.  

- O Developer já corrige vulnerabilidades - o SbD-ToE apenas tipifica essa atividade.  
- O QA já valida critérios - o SbD-ToE apenas assegura que a segurança é um desses critérios.  
- O PO já define prioridades - o SbD-ToE apenas garante que requisitos de segurança são incluídos.  
- O DevOps já mantém pipelines - o SbD-ToE apenas explicita controlos de segurança.  

Assim, o manual não **aumenta trabalho**, mas **aumenta transparência e visibilidade** sobre o que já é feito.  

Outro ponto importante: nem todas as organizações terão todos os papéis aqui descritos.  
Em muitas, um único profissional acumula várias funções, ou certas responsabilidades são partilhadas por equipas.  
O SbD-ToE não impõe estrutura rígida; apenas explicita que as atividades **têm de existir** - sejam desempenhadas por um ou vários papéis.  

O valor está precisamente aqui: transformar práticas isoladas em processos claros, visíveis e auditáveis, **sem criar esforço adicional desnecessário**.
