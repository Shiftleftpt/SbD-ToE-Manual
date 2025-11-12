# Guia de Configuração do Repositório GitHub

Este documento fornece instruções passo-a-passo para configurar as definições de segurança no GitHub que não podem ser configuradas através de ficheiros no repositório.

## 📋 Índice

1. [Proteção de Branches](#protecao-branches)
2. [Segurança e Análise](#seguranca-analise)
3. [GitHub Actions](#github-actions)
4. [Verificação Pós-Configuração](#verificacao)

---

## 🛡️ Proteção de Branches {#protecao-branches}

### Branch `master`

Navegar para: **Settings → Branches → Add branch protection rule**

**Branch name pattern**: `master`

#### Configurações obrigatórias:

**Protect matching branches**:
- ✅ **Require a pull request before merging**
  - ✅ Require approvals: `0` (enquanto 1 mantenedor) ou `1` (quando 2+ contribuidores)
  - ✅ Dismiss stale pull request approvals when new commits are pushed
  - ✅ Require review from Code Owners
  - ✅ Require approval of the most recent reviewable push

- ✅ **Require status checks to pass before merging**
  - ✅ Require branches to be up to date before merging
  - **Status checks requeridos** (adicionar quando disponíveis):
    - `analyze (javascript)` - CodeQL security scanning
    - `Build & validate` ou similar - Build do Docusaurus
    - (Futuro) `lint-links`, `anchors-validate`

- ✅ **Require conversation resolution before merging**

- ✅ **Require signed commits**

- ✅ **Require linear history**

- ✅ **Do not allow bypassing the above settings**
  - Exceção: Permitir que administradores façam bypass (para emergências)

- ✅ **Allow force pushes**: ❌ **DESATIVADO**

- ✅ **Allow deletions**: ❌ **DESATIVADO**

**Rules applied to everyone including administrators**:
- ✅ Ativar (exceto se precisar de bypass em emergências)

---

### Branch `gh-pages`

**Branch name pattern**: `gh-pages`

#### Configurações:
- ✅ **Lock branch** - Apenas GitHub Actions pode fazer push
- ✅ **Do not allow bypassing the above settings**
- ✅ **Allow force pushes**: ❌ **DESATIVADO** (exceto para `github-actions` bot)
- ✅ **Allow deletions**: ❌ **DESATIVADO**

**Specify who can force push**:
- ✅ Adicionar: `github-actions[bot]` ou similar (para deploys)

---

## 🔒 Segurança e Análise {#seguranca-analise}

Navegar para: **Settings → Security & analysis**

### Configurações obrigatórias:

**Dependency graph**:
- ✅ **Enabled** (geralmente ativado por padrão em repos públicos)

**Dependabot**:
- ✅ **Dependabot alerts**: Enabled
- ✅ **Dependabot security updates**: Enabled
- 📝 Nota: A configuração `.github/dependabot.yml` já está no repositório

**Code scanning**:
- ✅ **CodeQL analysis**: Configurado via workflow
  - Verificar que o workflow `.github/workflows/codeql-analysis.yml` está ativo
  - Monitorizar resultados em: **Security → Code scanning**

**Secret scanning**:
- ✅ **Secret scanning**: Enabled (disponível em repos públicos)
- ✅ **Push protection**: Enabled
  - Bloqueia commits que contenham secrets conhecidos

**Private vulnerability reporting**:
- ✅ **Enabled** - Permite reportar vulnerabilidades privadamente
- 📝 Nota: Complementa o processo definido em `SECURITY.md`

---

## ⚙️ GitHub Actions {#github-actions}

Navegar para: **Settings → Actions → General**

### Configurações recomendadas:

**Actions permissions**:
- ✅ **Allow all actions and reusable workflows** OU
- ✅ **Allow select actions and reusable workflows**
  - Se selecionar esta opção, adicionar:
    - `actions/*` (GitHub official actions)
    - `github/*` (GitHub official actions)
    - Outras actions específicas usadas no projeto

**Workflow permissions**:
- ✅ **Read repository contents and packages permissions** (default)
  - Workflows individuais podem elevar permissões conforme necessário
  - Segue o princípio de menor privilégio

**Fork pull request workflows**:
- ✅ **Require approval for first-time contributors who are new to GitHub**
- ✅ **Require approval for all outside collaborators**

---

## ✅ Verificação Pós-Configuração {#verificacao}

Após configurar todas as definições, verificar:

### 1. Proteção de Branches
```bash
# Tentar push direto para master (deve falhar)
git push origin master
# Erro esperado: "protected branch"
```

### 2. Status Checks
- [ ] Abrir um PR de teste
- [ ] Verificar que os checks do CodeQL são executados
- [ ] Verificar que o build do Docusaurus é executado
- [ ] Confirmar que não é possível merge sem checks verdes

### 3. Dependabot
- [ ] Navegar para: **Security → Dependabot**
- [ ] Verificar que não há alertas críticos
- [ ] Verificar que Dependabot está configurado para as ecosistemas corretos

### 4. CodeQL
- [ ] Navegar para: **Security → Code scanning**
- [ ] Verificar que o primeiro scan foi executado
- [ ] Confirmar que não há alertas (ou revisar alertas existentes)

### 5. Secret Scanning
- [ ] Navegar para: **Security → Secret scanning**
- [ ] Confirmar que está ativo
- [ ] Verificar que push protection está ativo

### 6. CODEOWNERS
- [ ] Abrir um PR alterando um ficheiro crítico (ex: `SECURITY.md`)
- [ ] Verificar que `@Shiftleftpt` é automaticamente solicitado para review

---

## 🔄 Manutenção

### Revisão Trimestral
- [ ] Revisar e atualizar lista de status checks obrigatórios
- [ ] Verificar que branch protection rules estão corretas
- [ ] Avaliar se é necessário adicionar novos owners em CODEOWNERS
- [ ] Confirmar que todas as funcionalidades de segurança estão ativas

### Quando a Equipa Crescer
- [ ] Aumentar `Require approvals` de `0` para `1`
- [ ] Ativar `Require review from Code Owners`
- [ ] Ativar `Require approval from someone other than the last pusher`
- [ ] Considerar adicionar **Merge queue** para escalar reviews
- [ ] Atualizar `.github/CODEOWNERS` com novos membros da equipa

---

## 📞 Suporte

**Documentação GitHub**:
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
- [About code scanning](https://docs.github.com/en/code-security/code-scanning)
- [About Dependabot](https://docs.github.com/en/code-security/dependabot)
- [About secret scanning](https://docs.github.com/en/code-security/secret-scanning)

**Questões**:
- Email: security@shiftleft.pt
- Issues: https://github.com/Shiftleftpt/SbD-ToE-Manual/issues

---

*Última atualização: 2025-11-12*
*Versão: 1.0*
