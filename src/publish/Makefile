# ---------------------------------------------------------------
# Makefile minimalista - build Docusaurus (web-only) com npm
# ---------------------------------------------------------------
SHELL := /bin/bash
.ONESHELL:

# Caminhos absolutos (baseados na localização deste Makefile)
MAKEFILE_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
REPO_ROOT    := $(abspath $(MAKEFILE_DIR)/../..)
SRC_DIR      := $(REPO_ROOT)/manuals_src
OUT_BASE     ?= $(abspath $(REPO_ROOT)/../_out)
WEB_DIR      := $(OUT_BASE)/web

# ---------------------------------------------------------------
# Alvos principais
# ---------------------------------------------------------------
.PHONY: help
help:
	@echo ""
	@echo "Targets disponíveis:"
	@echo "  make web        -> update-lock + clean + prepare + install + build"
	@echo "  make dev-setup  -> clean + prepare + install (setup inicial)"
	@echo "  make dev        -> start dev server em _out/web (use dev-setup primeiro)"
	@echo "  make sync       -> rsync incremental manuals_src/ -> _out/web/ (usar com dev ativo)"
	@echo "  make update-lock-> atualiza package-lock.json no repo"
	@echo "  make prepare    -> copia manuals_src/ -> _out/web/"
	@echo "  make install    -> npm install em _out/web/"
	@echo "  make build      -> npm run build (Docusaurus)"
	@echo "  make serve      -> npx docusaurus serve (pré-visualizar)"
	@echo "  make clean      -> remove _out/web/"
	@echo ""

# ---------------------------------------------------------------
# Pipeline completo
# ---------------------------------------------------------------
.PHONY: web
web: update-lock prepare install build

# ---------------------------------------------------------------
# Atualizar package-lock.json no repo (sem instalar node_modules)
# ---------------------------------------------------------------
.PHONY: update-lock
update-lock:
	@echo ">> Atualizando package-lock.json em $(SRC_DIR)"
	cd "$(SRC_DIR)"; \
	npm install --package-lock-only

# ---------------------------------------------------------------
# Copiar manuals_src -> build web
# ---------------------------------------------------------------
.PHONY: prepare
prepare:
	@echo ">> Copiando $(SRC_DIR) -> $(WEB_DIR)"
	@if [ ! -d "$(SRC_DIR)" ]; then \
	  echo "!! Origem não encontrada: $(SRC_DIR)"; exit 1; fi
	@mkdir -p "$(WEB_DIR)"
	@if command -v rsync >/dev/null 2>&1; then \
	  rsync -a --delete --exclude '.git' --exclude '.docusaurus' \
	    --exclude 'node_modules' --exclude 'build' --exclude '.DS_Store' \
	    "$(SRC_DIR)/" "$(WEB_DIR)/"; \
	else \
	  echo ">> rsync não encontrado, a usar cp -R"; \
	  rm -rf "$(WEB_DIR)"; mkdir -p "$(WEB_DIR)"; \
	  cp -R "$(SRC_DIR)/." "$(WEB_DIR)/"; \
	fi

# ---------------------------------------------------------------
# Instalar dependências npm
# ---------------------------------------------------------------
.PHONY: install
install:
	@echo ">> npm install em $(WEB_DIR)"
	cd "$(WEB_DIR)"; \
	if [ -f package-lock.json ]; then npm ci || npm install; \
	else npm install; fi

# ---------------------------------------------------------------
# Build Docusaurus
# ---------------------------------------------------------------
.PHONY: build
build:
	@echo ">> npm run build (Docusaurus) em $(WEB_DIR)"
	cd "$(WEB_DIR)"; \
	npm run build

# ---------------------------------------------------------------
# Servir localmente
# ---------------------------------------------------------------
.PHONY: serve
serve:
	@echo ">> Servindo build em http://localhost:3000"
	cd "$(WEB_DIR)"; \
	if [ -d build ]; then \
	  npx docusaurus serve --dir build --port 3000 --host 0.0.0.0; \
	else \
	  echo "!! build/ não existe; corre 'make web' primeiro"; \
	  exit 1; fi

# ---------------------------------------------------------------
# Limpeza
# ---------------------------------------------------------------
.PHONY: clean
clean:
	@echo ">> Removendo $(WEB_DIR)"
	rm -rf "$(WEB_DIR)"

.PHONY: clear
clear:
	@echo ">> Limpar caches Docusaurus"
	cd "$(WEB_DIR)"; \
	rm -rf .docusaurus node_modules/.cache build

# ---------------------------------------------------------------
# Setup inicial para desenvolvimento
# ---------------------------------------------------------------
.PHONY: dev-setup
dev-setup: clean prepare install
	@echo ">> Setup completo. Agora podes correr 'make dev'"

# ---------------------------------------------------------------
# Dev server (usa dev-setup primeiro se _out/web não existir)
# ---------------------------------------------------------------
.PHONY: dev
dev:
	@if [ ! -d "$(WEB_DIR)" ]; then \
	  echo "!! $(WEB_DIR) não existe. Corre 'make dev-setup' primeiro"; exit 1; fi
	@echo ">> npm run start (Docusaurus dev) em $(WEB_DIR)"
	cd "$(WEB_DIR)"; \
	npm run start

# ---------------------------------------------------------------
# Sync incremental - atualiza _out/web quando há alterações
# Nota: O dev server (make dev) deve estar a correr noutra janela
# ---------------------------------------------------------------
.PHONY: sync
sync:
	@echo ">> Sincronizando $(SRC_DIR) -> $(WEB_DIR)"
	@if [ ! -d "$(SRC_DIR)" ]; then \
	  echo "!! Origem não encontrada: $(SRC_DIR)"; exit 1; fi
	@if [ ! -d "$(WEB_DIR)" ]; then \
	  echo "!! $(WEB_DIR) não existe. Corre 'make dev' primeiro noutra janela"; exit 1; fi
	@if command -v rsync >/dev/null 2>&1; then \
	  rsync -av --exclude '.git' --exclude '.docusaurus' \
	    --exclude 'node_modules' --exclude 'build' --exclude '.DS_Store' \
	    "$(SRC_DIR)/" "$(WEB_DIR)/"; \
	  echo ">> Sincronização completa. O Docusaurus dev server deve recarregar automaticamente."; \
	else \
	  echo "!! rsync não encontrado"; exit 1; fi

