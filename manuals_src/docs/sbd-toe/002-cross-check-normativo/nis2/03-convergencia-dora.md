---
id: convergencia-dora
title: Nota – Convergência DORA & NIS2
description: Orientação para organizações potencialmente enquadradas simultaneamente por DORA e NIS2
sidebar_position: 4
tags: [dora, nis2, convergencia, lex-specialis, governação]
---

# Nota: Organizações abrangidas por DORA e NIS2

## Âmbito

Esta nota destina-se a organizações do setor financeiro (bancos, seguradoras, infraestruturas de mercado, intermediários) que surgem listadas em transposições NIS2 mas são reguladas primariamente por DORA (Regulamento UE 2022/2554). Resume princípios de **lex specialis**, evita duplicação e orienta a integração no SbD-ToE.

## Princípio Lex Specialis

DORA é lex specialis para gestão de risco TIC, testes de resiliência e reporte de incidentes em entidades financeiras reguladas. Onde há sobreposição temática:

| Tema | NIS2 Artigos | DORA Artigos | Qual prevalece |
|------|--------------|--------------|----------------|
| Governação TIC | 20 | 5 | DORA (mais específico financeiro) |
| Gestão de risco técnico | 21 | 5 | DORA |
| Testes/Resiliência | 21 (genérico) | 19–20 (TLPT, continuidade) | DORA |
| Reporte de incidentes | 23 (24h/72h/1M) | 18 (tipologias RTS/ITS) | DORA (formato / circuito supervisor) |
| Cadeia de fornecimento | 21 | 26–28 | DORA para terceiras TIC críticas financeiras; NIS2 pode complementar requisitos gerais |
| Partilha de ameaças | (implícito ENISA) | 16 | DORA |

## O que continua relevante da NIS2

Mesmo sob DORA, aspetos NIS2 podem manter valor:
- Linguagem comum para interação com entidades essenciais/importantes não financeiras (ex.: saúde, energia) que dependem de serviços bancários.
- Expectativas de **all-hazards approach** ajudam a justificar amplitude dos controlos (já presentes no SbD-ToE).
- Requisitos nacionais sobre **pontos de contacto** ou **registos de dependências críticas** podem exigir harmonização documental.

## Riscos de Duplicação (Evitar)

| Duplicação potencial | Porque evitar | Forma única recomendada |
|----------------------|---------------|--------------------------|
| Dois fluxos de reporte (incidentes) | Risco de inconsistência de prazos/dados | Adotar fluxo DORA; mapear campos NIS2 como subset |
| Dois catálogos de controlos | Overhead, divergência textual | Usar catálogo SbD-ToE + marcar origem (DORA/NIS2/ISO) |
| Duas classificações de criticidade | Confusão em matrizes de risco | Manter L1–L3 SbD-ToE; documentar que atende classes DORA & NIS2 |
| Logs com retenções diferentes | Custos e ambiguidade | Aplicar requisito mais exigente (DORA ≥3 anos) e declarar como cobrindo NIS2 |

## Estratégia de Implementação Única (SbD-ToE)

1. **Política mestra de Resiliência Digital** – Integra governação, testes, reporte e fornecedores (referencia DORA Art. 5, 18–20, 26–28; nota que substitui NIS2 Art. 20–23).
2. **Matriz de origem regulatória** – Para cada requisito técnico ([Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)), nova coluna `Fonte` com enum: `DORA`, `NIS2`, `Ambas`, `Outras`.
3. **Esquema de incidente** – Base = DORA RTS/ITS; marcar campos adicionais NIS2 (ex.: impacto em serviços essenciais) como opcionais.
4. **Processo de exceções** – Escalonamento L3 sempre com supervisão board (cobre governance DORA & NIS2 simultaneamente).
5. **Inventário de fornecedores** – Unificar: SBOM (componentes), contractors ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)), fornecedores TIC críticos (marcar se exigidos por DORA ou por clientes NIS2).
6. **Formação** – Módulo anual board (DORA governance) + módulo ciber all-hazards (NIS2) integrados; uma trilha, duas etiquetas.

## Checklist de Convergência (SIM = pronto)

- [ ] Catálogo de requisitos SbD-ToE tem coluna `Fonte` preenchida.
- [ ] Política mestra inclui secção "Lex Specialis: DORA substitui NIS2 Art. 20–23".
- [ ] Esquema de incidentes baseado em RTS/ITS DORA, com campos NIS2 opcionais.
- [ ] Retenção de logs definida ≥3 anos (justificada como cobrindo ambas).
- [ ] Inventário de fornecedores indica criticidade + origem regulatória.
- [ ] Formação anual da gestão registada (conteúdos DORA + NIS2 integrados).
- [ ] Processo formal de exceções com aprovação board para L3.
- [ ] Não existem playbooks paralelos divergentes (apenas anotações de diferenças).

## Perguntas Frequentes

**Q1. Preciso reportar incidente duas vezes?**  
Não. Segue circuito DORA. Se autoridade nacional exigir visão agregada NIS2, reutiliza export do formato DORA.

**Q2. E se fornecedor não financeiro invoca NIS2?**  
Mapeia exigência do fornecedor a controlo já satisfeito por DORA; envia SoA com origem regulatória.

**Q3. Logs de 1 ano bastam para NIS2?**  
Para convergência, manter 3+ anos (DORA) reduz discussões. Documentar racional.

**Q4. TLPT vs. testes NIS2?**  
Executar TLPT (se aplicável) satisfaz e supera a exigência genérica NIS2 de avaliação de eficácia.

## Referências

- Regulamento (UE) 2022/2554 (DORA)
- Diretiva (UE) 2022/2555 (NIS2) Anexos I/II
- ENISA – Orientações técnicas NIS2 (2024/2025)
- SbD-ToE Manual ([Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))

## Nota Final

SbD-ToE já abstrai controlos técnicos. A convergência DORA/NIS2 concretiza-se ao **anotar origem regulatória** e usar sempre a forma **mais exigente** como baseline – evitando redundância e mantendo elegância operacional.
