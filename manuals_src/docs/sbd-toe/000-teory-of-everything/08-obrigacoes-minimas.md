---
id: obrigacoes-minimas
title: Aplicabilidade mínima
description: O núcleo duro de práticas que todas as aplicações devem cumprir, independentemente do nível de risco
tags: [obrigacoes, baseline, minimo, must, nis2, dora, gdpr, pci, hipaa]
sidebar_position: 6
---



# Obrigações Mínimas Transversais

A segurança de software não pode depender da criticidade de cada aplicação para garantir a existência de um **piso mínimo comum**.  
Sem esse alicerce, a organização fragmenta-se: algumas equipas aplicam práticas robustas, outras não aplicam nenhuma, e o resultado é um ecossistema inconsistente, vulnerável e difícil de auditar.  
As **obrigações mínimas transversais** são, por isso, a base do SbD-ToE.  
Não pretendem substituir a proporcionalidade L1–L3, mas antes criar uma camada uniforme que garante que, seja qual for a aplicação, existe sempre um conjunto de controlos elementares implementados.

---

## O núcleo duro das obrigações

Independentemente do nível de risco, todas as aplicações devem implementar:

- Classificação da criticidade da aplicação antes do arranque (Cap. 01).  
- Definição e rastreabilidade de requisitos mínimos de segurança (Cap. 02).  
- Gestão explícita de dependências críticas, com inventário atualizado (Cap. 05).  
- Adoção de coding guidelines básicas e validação automática (Cap. 06).  
- Execução de pipelines CI/CD com verificações mínimas de segurança (Cap. 07).  
- Registo de logs essenciais e monitorização elementar (Cap. 12).  
- Formação inicial em segurança para toda a equipa envolvida (Cap. 13).  
- Documentação contratual de cláusulas mínimas de segurança em fornecedores (Cap. 14).  

Este conjunto garante que nenhuma aplicação fica fora de um sistema de governação coerente.  
São controlos elementares mas poderosos: estabelecem disciplina, criam rastreabilidade e reduzem riscos triviais que, acumulados, constituem uma das maiores fontes de vulnerabilidades exploráveis.

---

## Contexto técnico e científico

O racional técnico-científico para estas obrigações é robusto.  
Estudos de incidentes (ex.: relatórios Verizon DBIR, ENISA Threat Landscape, OWASP Top 10) demonstram que a maioria das falhas exploradas decorre de práticas básicas negligenciadas: bibliotecas não geridas, pipelines sem validações, ausência de logging ou formação insuficiente das equipas.  
Ao definir este núcleo duro, o SbD-ToE segue a evidência empírica: **controlos simples previnem a maioria dos ataques mais comuns**.

Modelos como OWASP SAMM mostram também que organizações maduras partilham uma característica em comum: **a uniformidade dos controlos mínimos**.  
A ausência dessa uniformidade leva a gaps, a duplicações e a custos acrescidos em auditorias.  
Por isso, mesmo antes de falar em maturidade avançada, importa garantir que o mínimo é consistente e transversal.

---

## Baseline vs. proporcionalidade

As obrigações mínimas não substituem o sistema de proporcionalidade L1–L3.  
O que muda entre níveis é a intensidade, profundidade e formalização das práticas.  
Mas existe sempre uma camada base que **não é negociável**:  
- Classificar risco antes de desenvolver.  
- Garantir que há requisitos mínimos aplicados.  
- Ter uma pipeline com verificações básicas.  
- Manter inventário de dependências.  
- Assegurar logging mínimo.  

Sem esta base, a aplicação de níveis superiores torna-se incoerente.  
Não é possível aplicar um Cap. 10 robusto (Testes de Segurança) se o Cap. 06 não tiver, pelo menos, guidelines básicas implementadas.  
O baseline é, portanto, condição necessária para que a proporcionalidade seja eficaz.

---

## Pragmatismo e aplicação universal

Um aspeto essencial é o pragmatismo.  
Em muitos casos, torna-se mais eficiente aplicar **determinadas práticas de forma universal**, mesmo em aplicações que em teoria não o exigiriam.  

Exemplos:  
- **SAST básico em todos os repositórios**: configurar uma ferramenta de análise estática com *default settings* pode eliminar vulnerabilidades triviais com custo marginal quase nulo.  
- **Scans automáticos de dependências em pipelines**: um job padrão aplicado a todos os projetos simplifica a política e reduz falsos negativos.  
- **Baselines de logging e monitorização**: ativar por defeito coletores de logs em todos os serviços facilita auditorias e acelera a deteção de incidentes.  
- **Templates contratuais mínimos**: aplicar cláusulas de segurança iguais a todos os fornecedores simplifica governança e reduz discussões jurídicas desnecessárias.  

Esta aplicação “por cima” simplifica políticas, evita debates caso a caso e reduz a carga cognitiva das equipas.  
O risco é impor ligeiro esforço adicional em aplicações de baixo risco, mas a prática mostra que esse esforço é marginal e, em geral, compensa amplamente.  

É por isso que o SbD-ToE advoga o princípio: **o perfeito é inimigo do bom**.  
Mais vale ter controlos aplicados de forma uniforme, ainda que não otimizados ao detalhe, do que deixar lacunas críticas à espera de soluções “ideais”.

---

## Ligação a referenciais e regulamentos

Estas obrigações mínimas estão alinhadas com as expectativas universais de normas e regulamentos:  

- **NIS2**: exige medidas técnicas e organizacionais adequadas a todos os operadores, incluindo gestão de risco, logging e monitorização.  
- **DORA**: impõe resiliência operacional digital, testes regulares e governação de fornecedores críticos, todos dependentes de práticas básicas já no baseline.  
- **GDPR**: consagra *privacy by design* e *by default*, aplicável mesmo em sistemas simples que tratem dados pessoais.  
- **PCI-DSS**: estabelece controlos elementares como logging, monitorização e gestão de dependências para qualquer sistema que trate dados de pagamento.  
- **HIPAA**: requer requisitos mínimos de segurança e confidencialidade em sistemas que tratem informação clínica.  
- **ISO/IEC 27001 e 27034**: prescrevem controlos técnicos e organizacionais mínimos para todas as aplicações, independentemente do risco.  

O SbD-ToE não reinventa estes referenciais; pelo contrário, organiza-os e transforma-os em prática concreta, objetiva e auditável.

---

## Conclusão

As **obrigações mínimas transversais** são a expressão prática de um princípio central: nenhuma aplicação fica fora do sistema.  
Elas criam consistência, reduzem falhas triviais, simplificam auditorias e asseguram que cada equipa, independentemente da sua maturidade, parte de uma base sólida.  
Com elas, a segurança deixa de ser exceção e passa a ser norma.  

Mais importante ainda, estas obrigações mostram como o SbD-ToE equilibra rigor técnico-científico e pragmatismo:  
- científico, porque se apoia em dados empíricos, normas internacionais e regulamentos;  
- pragmático, porque aceita que a aplicação transversal de certos controlos pode ser mais eficiente do que uma aplicação estritamente proporcional.  

É neste equilíbrio que reside a força do modelo: criar uma cultura de segurança que é ao mesmo tempo rigorosa, sustentável e aplicável em qualquer contexto organizacional.
