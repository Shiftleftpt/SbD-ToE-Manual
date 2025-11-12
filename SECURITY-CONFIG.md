# Configuração de Segurança para Projeto Público

Este documento descreve as medidas de segurança implementadas no repositório **Security by Design - Theory of Everything (SbD-ToE)** para garantir a segurança e integridade do projeto público.

> 📘 **Para configurar as definições do GitHub**, consulte o guia passo-a-passo: [GITHUB-CONFIG.md](GITHUB-CONFIG.md)

## 📋 Índice

1. [Scanning Automatizado de Vulnerabilidades](#scanning-automatizado)
2. [Proteção de Branches](#protecao-branches)
3. [Gestão de Dependências](#gestao-dependencias)
4. [Revisão de Código](#revisao-codigo)
5. [Workflows e CI/CD](#workflows-cicd)
6. [Política de Divulgação](#politica-divulgacao)
7. [Checklist de Verificação](#checklist)

---

## 🔍 Scanning Automatizado de Vulnerabilidades {#scanning-automatizado}

### CodeQL Analysis

O repositório utiliza **GitHub CodeQL** para análise estática de segurança:

- **Workflow**: `.github/workflows/codeql-analysis.yml`
- **Frequência**: 
  - Execução em todos os pushes para `master`
  - Execução em todos os pull requests
  - Scan semanal agendado (segunda-feira às 03:00 UTC)
- **Linguagens analisadas**: JavaScript/TypeScript (Docusaurus)
- **Query suite**: `security-and-quality` (análise abrangente)
- **Resultados**: Publicados no GitHub Security tab

#### Ações recomendadas:
1. Monitorizar regularmente o Security tab no GitHub
2. Resolver alertas críticos e de alta severidade imediatamente
3. Avaliar e corrigir alertas de média e baixa severidade periodicamente

### Dependabot

O **Dependabot** está configurado para monitorização automática de vulnerabilidades em dependências:

- **Configuração**: `.github/dependabot.yml`
- **Ecosistemas monitorizados**:
  - GitHub Actions (workflows)
  - npm (projeto Docusaurus)
- **Frequência**: Verificação semanal (segunda-feira às 09:00)
- **PRs automáticos**: Criados para atualizações de segurança e dependências

#### Ações recomendadas:
1. Revisar e aprovar PRs do Dependabot prioritariamente
2. Testar atualizações de segurança antes do merge
3. Manter dependências atualizadas regularmente

---

## 🛡️ Proteção de Branches {#protecao-branches}

### Branch `master`

Configurações obrigatórias (definidas em `CONTRIB.md`):

- ✅ **Pull Request obrigatório** - Nenhum push direto permitido
- ✅ **Status checks obrigatórios**:
  - Build do Docusaurus
  - CodeQL security scanning
  - (Futuro) Lint de links e validação de âncoras
- ✅ **Branch atualizada** - Requer atualização antes do merge
- ✅ **Histórico linear** - Apenas "Squash and Merge"
- ✅ **Commits assinados** - Verificação de autenticidade
- ✅ **Proteção contra eliminação**

### Branch `gh-pages`

- **Push automático** - Apenas via GitHub Actions
- **Proteção contra eliminação**

#### Aprovações de PR:

Política escalável definida em `CONTRIB.md`:
- **Fase atual** (1 mantenedor): 0 aprovações obrigatórias, mas checks automatizados são mandatórios
- **Fase futura** (2+ contribuidores):
  - Mínimo 1 aprovação de pessoa diferente do autor
  - Code Owners review obrigatória
  - Aprovação de pessoa diferente do último pusher
  - Dismissal de aprovações obsoletas
  - Resolução de conversas obrigatória

---

## 📦 Gestão de Dependências {#gestao-dependencias}

### Princípios

1. **Manter dependências atualizadas**: Reduz superfície de ataque
2. **Atualizações agrupadas**: Reduz ruído de PRs (definido em dependabot.yml)
3. **Testes antes do merge**: Validar funcionalidade após atualizações
4. **Overrides declarados**: Versões específicas definidas em `package.json`

### Grupos de Dependências (Dependabot)

- **Docusaurus**: Atualiza todos os pacotes `@docusaurus/*` juntos
- **React**: Atualiza `react` e `react-dom` juntos
- **Dev Dependencies**: Agrupa atualizações menores/patches de deps de desenvolvimento

### Ignorar Atualizações

Dependências ignoradas para manter estabilidade:
- **Node.js**: Mudanças major ignoradas (requer validação manual)

---

## 👥 Revisão de Código {#revisao-codigo}

### CODEOWNERS

O ficheiro `.github/CODEOWNERS` define proprietários de código:

- **Owner principal**: `@pedrofarinhaatshiftleftpt`
- **Ficheiros críticos**: Segurança, workflows, configuração
- **Expansível**: Preparado para adicionar revisores específicos por área

### Processo de Revisão

1. **PR templates**: Disponíveis para diferentes tipos de contribuição
2. **Auto-labeling**: PRs automaticamente etiquetados baseado no template
3. **Issue tracking**: Cada PR deve referenciar um issue
4. **Squash merge**: Mantém histórico limpo

---

## ⚙️ Workflows e CI/CD {#workflows-cicd}

### Princípio de Menor Privilégio

Todos os workflows seguem o princípio de menor privilégio nas permissões:

#### `deploy-pages.yml`
- **Job build**: `contents: read` apenas
- **Job deploy**: `pages: write`, `id-token: write`, `contents: read`
- **Trigger**: Tags de release (`v*.*.*`) ou manual

#### `preview-pages.yml`
- **Permissões**: `contents: read`, `pages: write`, `id-token: write`
- **Trigger**: Pull requests para `master`
- **Concurrency**: Cancela previews anteriores do mesmo PR

#### `release.yml`
- **Permissões**: `contents: write` (criar releases)
- **Trigger**: Tags de release (`v*.*.*`)

#### `pr-auto-label.yml`
- **Permissões**: `contents: read`, `pull-requests: write`
- **Trigger**: `pull_request_target` (seguro - não faz checkout de código do PR)
- **Funcionalidade**: Auto-etiquetagem baseada em templates

#### `codeql-analysis.yml`
- **Permissões**: `security-events: write`, `actions: read`, `contents: read`
- **Trigger**: Push para master, PRs, schedule semanal
- **Build mode**: `none` (JavaScript não requer compilação)

### Segurança em Workflows

✅ **Boas práticas implementadas**:
- Permissões explícitas e mínimas em cada job
- Uso de `pull_request_target` de forma segura (sem checkout de código do PR)
- Versões fixas de actions (ex: `@v4`, `@v3`)
- Concurrency groups para evitar conflitos
- Timeouts definidos

⚠️ **Pontos de atenção**:
- Manter actions atualizadas (Dependabot ajuda)
- Não expor secrets em logs
- Validar inputs de usuários em scripts

---

## 📢 Política de Divulgação {#politica-divulgacao}

Definida em `SECURITY.md`:

### Reportar Vulnerabilidades

- **Email**: security@shiftleft.pt
- **Não abrir issue público**
- **Resposta**: Máximo 72 horas

### Prazos

| Etapa | Prazo Máximo |
|-------|--------------|
| Triagem inicial | 3 dias úteis |
| Mitigação/plano | 14 dias |
| Divulgação pública | 30 dias ou após correção |

### Escopo

- Código de build e workflows
- Scripts auxiliares
- Conteúdos Markdown e pipelines de geração

---

## ✅ Checklist de Verificação {#checklist}

Use esta checklist para verificar periodicamente a configuração de segurança:

### Configuração do Repositório

- [ ] Branch `master` está protegida conforme `CONTRIB.md`
- [ ] Branch `gh-pages` está protegida contra push direto e eliminação
- [ ] CODEOWNERS está configurado e ativo
- [ ] Secrets do GitHub Actions estão configurados corretamente (se aplicável)
- [ ] Dependabot está ativo e configurado

### Scanning e Monitorização

- [ ] CodeQL está a executar semanalmente
- [ ] Últimos resultados de CodeQL foram revistos
- [ ] Alertas de segurança críticos/altos estão resolvidos
- [ ] PRs do Dependabot estão a ser processados regularmente
- [ ] Não há vulnerabilidades conhecidas em dependências

### Workflows

- [ ] Todas as GitHub Actions estão em versões recentes
- [ ] Permissões de workflows seguem princípio de menor privilégio
- [ ] Secrets não são expostos em logs
- [ ] Builds e testes passam consistentemente

### Documentação

- [ ] `SECURITY.md` está atualizado
- [ ] `CONTRIB.md` reflete o processo atual
- [ ] Este documento (`SECURITY-CONFIG.md`) está atualizado
- [ ] README menciona práticas de segurança

### Processo

- [ ] PRs são revisados antes do merge
- [ ] Commits são assinados (quando possível)
- [ ] Issues de segurança são triados rapidamente
- [ ] Equipa conhece o processo de divulgação

---

## 🔄 Manutenção Contínua

### Mensal
- Revisar e resolver alertas do CodeQL
- Processar PRs do Dependabot
- Verificar logs de workflows para anomalias

### Trimestral
- Revisar e atualizar esta documentação
- Avaliar novas funcionalidades de segurança do GitHub
- Rever permissões de workflows e CODEOWNERS

### Anual
- Audit completo de segurança
- Revisar política de divulgação
- Atualizar proteções de branch conforme crescimento da equipa

---

## 📚 Recursos Adicionais

- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
- [Coordinated Vulnerability Disclosure – ENISA](https://www.enisa.europa.eu/)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [SLSA Framework](https://slsa.dev/)

---

## 📞 Contacto

Para questões sobre segurança do repositório:
- **Email**: security@shiftleft.pt
- **Repository**: https://github.com/Shiftleftpt/SbD-ToE-Manual

---

*Última atualização: 2025-11-12*
