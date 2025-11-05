---
id: intro
title: Testes de Segurança
description: Estratégias e práticas para validar continuamente a segurança de aplicações através de testes automatizados, manuais e ofensivos
tags: [testes, segurança, validação contínua, SAST, DAST, fuzzing, pentesting, DSOMM, SAMM, SSDF, SLSA]
sidebar_position: 0
---
import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: SFD1.2, SE1.1, T1.3, T2.4, SE3.5</Badge>
  <Badge color="info">SSDF: RV.1, RV.3, RV.6, PS.2</Badge>
  <Badge color="info">SLSA: Nível 2 / 4</Badge>
  <Badge color="info">DSOMM: 2 / 3 (Testing, Dev)</Badge>
  <a href="./achievable-maturity" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver análise de maturidade</a>
</div>

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua e mensurável.  

Os capítulos operacionais implementam o SbD-ToE em contextos técnicos específicos, incluindo:
- **Gestão de dependências e SBOM/SCA** (Cap. 05)  
- **Pipelines CI/CD e automação de controlo** (Cap. 07)  
- **Infraestrutura como Código (IaC)** (Cap. 08)  
- **Containers e imagens seguras** (Cap. 09)  
- **Testes de segurança e validação técnica** (Cap. 10)  
- **Deploy seguro, observabilidade e resposta** (Cap. 11 – 12)  

Estes capítulos traduzem as prescrições basilares em práticas de **execução verificável**, promovendo a **integração contínua da segurança** ao longo do ciclo de vida do software.
:::

# Testes de Segurança

Os testes de segurança são o **ponto de viragem entre teoria e prática**.  
Requisitos podem ser bem definidos e controlos bem desenhados, mas só com testes contínuos é possível provar que funcionam perante código real, integrações complexas e ameaças em evolução.  

Este capítulo diferencia-se por fornecer **evidência objetiva e auditável**: mostra se as medidas prescritas nos capítulos anteriores são eficazes e se resistem à pressão do uso em produção.  
Inclui desde ferramentas automatizadas (*linters*, SAST, DAST, fuzzing) até exercícios manuais/ofensivos (PenTesting), criando uma rede complementar de garantias.  

👉 Em síntese, os testes de segurança não são uma “fase” opcional - são o **ritmo de batimento cardíaco do ciclo de vida**, que confirma em cada commit, em cada build e em cada release que a aplicação continua segura.

---

Este capítulo cobre os seguintes eixos técnicos principais:  

- Estratégia formal de testes de segurança proporcional ao risco da aplicação.  
- Integração de scanners no CI/CD (SAST, SCA, IAST).  
- Execução de DAST autenticado em staging.  
- Testes de fuzzing em endpoints críticos.  
- Criação de regressões automatizadas para findings resolvidos.  
- Definição de *gates* de release e aceitação formal de risco.  
- Realização de PenTesting ofensivo orientado por risco.  
- Rastreabilidade dos testes em relação aos requisitos (Cap. 02).  

Cada técnica reforça as restantes. O valor surge na **orquestração coerente**: testes automatizados detetam cedo, regressões previnem reincidência, fuzzing expõe falhas ocultas, e Pentesting desafia a robustez de todo o ecossistema.

---

## 🧪 2. Prescrição prática

A aplicação prática deve ser entendida como um **ciclo contínuo**, não como lista isolada de ferramentas:  

- **O que fazer:**  
  Definir uma estratégia clara, automatizar o que for possível, testar em diferentes camadas (código, runtime, integrações), e completar com validação ofensiva em aplicações críticas.  

- **Como fazer:**  
  - **L1**: testes essenciais (SAST + checklist manual).  
  - **L2**: testes automatizados integrados (DAST, regressões, gates).  
  - **L3**: testes avançados (fuzzing sistemático, IAST, Pentesting pré-produção).  

- **Quando aplicar:**  
  - No início de cada projeto (estratégia formal).  
  - Em cada commit/PR (SAST).  
  - Em builds CI/CD (SCA, IAST).  
  - Em staging antes do go-live (DAST, fuzzing).  
  - Em cada release (checklist de critérios + aceitação de risco).  
  - Em ciclos de auditoria (PenTesting).  

- **Porquê:**  
  Porque a validação é a única forma de garantir que segurança não é promessa, mas realidade comprovada.  
  Os testes sustentam decisões de *go/no-go*, reduzem o tempo de exposição a vulnerabilidades e alinham a prática com normativos como **SSDF RV.1/RV.3**, **SAMM ST.1–3**, e **BSIMM T1.3/T2.4**.

---

## 👥 Papéis envolvidos

A responsabilidade pelos testes é **coletiva**, mas cada papel tem um contributo distinto:

- **Dev** → corrige findings e cria regressões automáticas.  
- **QA/Testes** → executa DAST, fuzzing e valida critérios de aceitação.  
- **AppSec** → define estratégia, afina regras e gere findings/exceções.  
- **DevOps** → integra scanners e gates no CI/CD.  
- **Gestão de Produto** → aprova risco residual e decide *go/no-go*.  
- **PenTester** → conduz validações ofensivas e reporta impacto real.  

👉 Estas responsabilidades não são teóricas: cada papel tem histórias de utilizador correspondentes no `aplicacao-lifecycle.md`, permitindo transformar esta matriz em prática repetível.

---

## 📚 Alinhamento com frameworks

- **OWASP SAMM** → ST.1, ST.2, ST.3.  
- **BSIMM** → T1.3, T2.4, SE3.5.  
- **SSDF** → RV.1, RV.3, RV.6, PS.2.  
- **SLSA** → Nível 2 / 4 (integração em pipelines).  
- **DSOMM** → Testing (maturidade DevSecOps).  

---

## 📜 Políticas Organizacionais Relevantes

| Política | Obrigatória? | Aplicação | Conteúdo mínimo |
|----------|--------------|-----------|-----------------|
| Política de Estratégia de Testes | Sim | AppSec | Documento versionado com mapeamento Cap. 2 ⇄ testes |
| Política de SAST em PR | Sim | Dev + DevOps | Execução automática em todos os PRs, thresholds L1–L3 |
| Política de DAST/Fuzzing | Recomendado | QA/Testes | DAST autenticado em staging, fuzzing em endpoints críticos |
| Política de Gates CI/CD | Sim | DevOps + AppSec | Thresholds definidos, logs versionados, exceções registadas |
| Política de Release Seguro | Sim | Gestão de Produto + AppSec | Checklist de release, critérios formais, aceitação de risco documentada |
| Política de PenTesting | Recomendado (L2), Obrigatório (L3) | AppSec + PenTesters | Escopo por risco, relatórios técnicos, retests planeados |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do manual**, onde estas políticas estão consolidadas transversalmente.

---

## 🏁 Conclusão

Testar é o que distingue boas intenções de segurança de evidência real.  
É o processo que confirma se requisitos foram implementados, se gates estão a funcionar e se a aplicação resiste a ataques credíveis.  
Mais do que uma fase, os testes são um **ritual contínuo de validação** - o que transforma o SbD-ToE num programa vivo, mensurável e auditável.

---
