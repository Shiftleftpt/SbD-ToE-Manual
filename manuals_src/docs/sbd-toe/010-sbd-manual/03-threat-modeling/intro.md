---
id: intro
title: 📘 Capítulo 3 - Threat Modeling
description: Identificação e mitigação estruturada de ameaças durante o ciclo de desenvolvimento
tags: [threat-modeling, stride, requisitos, mitigação, risco, arquitetura, SAMM, BSIMM, SSDF, SLSA, DSOMM]
---
import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: AA1.1, AA1.2, AA2.1</Badge>
  <Badge color="info">SSDF: PW.3, RV.1</Badge>
  <Badge color="info">SLSA: Nível 1 / 4</Badge>
  <Badge color="info">DSOMM: 2 / 3 (média)</Badge>
  <a href="./achievable-maturity" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver análise de maturidade</a>
</div>

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.  

Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo, cobrindo:
- **Classificação de risco e proporcionalidade** (Cap. 01)  
- **Definição estruturada de requisitos de segurança** (Cap. 02)  
- **Modelação de ameaças e priorização de controlos** (Cap. 03)  
- **Desenho e validação de arquitetura segura** (Cap. 04)  
- **Implementação disciplinada e revisão de código seguro** (Cap. 06)  

A ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE, tornando inviável a adoção coerente das práticas operacionais e de governação.
:::


# 📘 Capítulo 3 - Threat Modeling

## 1. 🧭 O que cobre tecnicamente

O Threat Modeling é uma técnica essencial para antecipar ataques e falhas de segurança antes que estas aconteçam.  
Permite identificar ameaças relevantes, validar controlos e garantir que os riscos são tratados de forma sistemática e proporcional ao impacto.

Este capítulo cobre:

- Integração de threat modeling no ciclo de desenvolvimento
- Métodos como STRIDE, LINDDUN e PASTA
- Criação e validação de modelos de ameaça (DFDs, trust boundaries)
- Mapeamento de ameaças para requisitos e controlo aplicado
- Integração com validação de arquitetura e revisão técnica
- Substituição do modelo manual por plataformas como o IriusRisk
- Reutilização segura de modelos em arquiteturas padronizadas

---

## 2. 🧪 Prescrição prática: o quê, quem, como, quando, porquê e para quê

### 🔐 Threat Modeling é a ponte entre risco, arquitetura e controlo aplicado

> *"Sem Threat Modeling, o controlo aplicado perde contexto e os requisitos não têm origem validada."*

### 📌 O que deve ser feito

- Realizar sessões de threat modeling com base no risco da aplicação
- Mapear ameaças usando modelos como STRIDE, LINDDUN ou PASTA
- Criar diagramas de fluxo de dados (DFDs) com trust boundaries
- Associar cada ameaça a um controlo e plano de mitigação
- Documentar decisões, ações futuras e justificar riscos aceites
- Assegurar que o modelo se baseia em artefactos arquiteturais definidos (ver Capítulo 4)
- Validar modelos de ameaça como parte da revisão de arquitetura formal
- Integrar threat modeling com ferramentas automatizadas quando disponível
- Garantir rastreabilidade entre ameaça identificada, requisito gerado e controlo aplicado

### ⚙️ Como deve ser feito

- Usar ferramentas como OWASP Threat Dragon, TMT, draw.io, ou IriusRisk
- Integrar em rituais ágeis, refinamento ou revisão de arquitetura
- Documentar e versionar os modelos
- Gerar cartões no backlog por mitigação necessária
- Considerar ameaças reais catalogadas (ex: OSC&R, CWE, OWASP Top 10)
- Alinhar requisitos derivados das ameaças com o Catálogo de Requisitos (Cap. 2)

### 📆 Quando aplicar

- No início de um projeto ou épico
- Antes de alterações significativas (ex: exposições, integrações)
- Sempre que a análise de risco (ver Cap. 1) classificar a aplicação como L2 ou superior

### 👥 Quem está envolvido

| Papel/Função             | Responsabilidades principais                                           |
|--------------------------|------------------------------------------------------------------------|
| DevSecOps / Arquitetura | Facilitar a sessão, manter documentação atualizada                   |
| Equipa de Desenvolvimento| Identificar fluxos, pontos de entrada, lógica de negócio              |
| Segurança / AppSec       | Ajudar a identificar ameaças relevantes e técnicas de ataque          |
| Product Owner / Negócio  | Validar cenários de impacto, prioridades de mitigação                 |

---

## 3. ⚠️ Caveats ou limitações da prescrição

- Sessões mal facilitadas podem ser vagas ou não acionáveis
- Documentação dispersa pode dificultar reutilização
- Nem todas as equipas dominam diagramas e análise de ameaças
- Ferramentas automatizadas ainda são limitadas em ambientes complexos

---

## 5. 💡 Exemplos de aplicação

- Ver [exemplo de aplicação de requisitos por nivel](exemplos-aplicacao-stride)
- Ver [exemplo de aplicação de privacidade](exemplo-privacidade-lindunn)
- Ver [exemplo uso de ferramentas, e.g., IriusRisk](/sbd-toe/sbd-manual/threat-modeling/addon/integracao-iriusrisk)

---

## 6. 🔍 O que pode ser feito mais (e porquê)

- Criar uma biblioteca interna de ameaças por tipo de aplicação
- Automatizar sugestões de ameaça com base em diagramas
- Incluir campos de ameaça e controlo nos cartões do backlog
- Formar facilitadores técnicos em threat modeling leve e iterativo

---

## 🧩 Ligações a outros capítulos

| Capítulo relacionado         | Relação técnica e de processo                                 |
|------------------------------|----------------------------------------------------------------|
| `01-gestao-risco`            | Determina quando o threat modeling é obrigatório (L2 ou L3)    |
| `02-requisitos-seguranca`   | Requisitos derivados do modelo de ameaça                      |
| `04-arquitetura-segura`     | Fonte primária de artefactos usados no threat modeling        |
| `06-desenvolvimento-seguro` | Integração de requisitos de segurança na implementação         |
| `07-cicd-seguro`            | Validação e rastreabilidade dos modelos via CI/CD             |
| `10-testes-seguranca`       | Cobertura de requisitos derivados de ameaças                  |

---

> 📌 Este capítulo é obrigatório para qualquer aplicação com criticidade **L2 ou L3**.  
> Ignorar o threat modeling anula a capacidade de rastrear riscos reais e mitigar ameaças com base na arquitetura e nos fluxos da aplicação.  
> É o capítulo que **liga risco, arquitetura e requisitos**, sendo condição fundamental para a maturidade do modelo SbD-ToE.
