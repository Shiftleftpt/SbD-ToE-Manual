###############################################################################
# Makefile – Build Automático Multi-Livro SbD-ToE (Web + Print)
###############################################################################

copy ?= true

## ----------- ROOTS & TOOLS -----------
GIT_ROOT     ?= $(shell git rev-parse --show-toplevel)

PYTHON   ?= python3
VENV_DIR := $(GIT_ROOT)/.venv
PY       := $(VENV_DIR)/bin/python
PIP      := $(VENV_DIR)/bin/pip
REQ      := $(GIT_ROOT)/src/publish/requirements.txt

NPM      ?= npm
PANDOC   ?= pandoc
PANDOC_DATA_DIR ?= $(GIT_ROOT)


# === NOVO: controlo de formatos ===
FORMAT       ?= pdf           # valores: pdf | docx | both
PDF_ENGINE   ?= xelatex       # ou tectonic
DOCX_REF     ?=               # ex: $(GIT_ROOT)/src/publish/reference.docx

## ----------- SBD MANUAL (PRINT) -----------
SBD_SRC            := $(GIT_ROOT)/manuals_src
SBD_PRINT          := $(GIT_ROOT)/build/print/sbd-manual
SBD_BOOKYML_PRINT  := $(SBD_PRINT)/docs/sbd-toe/book.yml
SBD_PDF_OUT        := $(GIT_ROOT)/BOOK/pdf/sbd_manual

## ----------- SUPPLY CHAIN (PRINT) -----------
SUPPLY_SRC            := $(GIT_ROOT)/manuals_src
SUPPLY_PRINT          := $(GIT_ROOT)/build/print/supply_chain
SUPPLY_BOOKYML_PRINT  := $(SUPPLY_SRC)/docs/supply-chain/book.yml
SUPPLY_PDF_OUT        := $(GIT_ROOT)/BOOK/pdf/supply_chain

## ----------- WEB (Docusaurus único) -----------
WEB_SRC        := $(GIT_ROOT)/manuals_src
WEB_BUILD      := $(GIT_ROOT)/build/web
WEB_BOOKYML    := $(WEB_BUILD)/site-filters.yml
WEB_DOCUSAURUS := $(WEB_BUILD)

## ========================================================================== ##
##                               DEPENDÊNCIAS                                 ##
## ========================================================================== ##
$(VENV_DIR)/bin/activate: $(REQ)
	@echo "[venv] a preparar ambiente em $(VENV_DIR)"
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQ)
	@touch $(VENV_DIR)/bin/activate

deps: $(VENV_DIR)/bin/activate
.PHONY: deps

# === ALTERADO: checks condicionais por formato ===
check_tools:
	@command -v $(PANDOC) >/dev/null 2>&1 || { echo "[ERRO] pandoc não encontrado"; exit 1; }
ifneq ($(filter pdf both,$(FORMAT)),)
	@command -v $(PDF_ENGINE) >/dev/null 2>&1 || { echo "[ERRO] $(PDF_ENGINE) não encontrado"; exit 1; }
endif
	@echo "[ok] pandoc$(if $(filter pdf both,$(FORMAT)), + $(PDF_ENGINE),) disponíveis."
.PHONY: check_tools

check_node:
	@node -v && $(NPM) -v || { echo "[ERRO] node/npm não encontrados"; exit 1; }
.PHONY: check_node

## ========================================================================== ##
##                             PRINT – SBD MANUAL                              ##
## ========================================================================== ##
print_sbd_copy:
	mkdir -p $(SBD_PRINT)
	rsync -a --delete --exclude 'node_modules' --exclude '.git' $(SBD_SRC)/ $(SBD_PRINT)/
	@ls -l $(SBD_PRINT)/docs/ || true
.PHONY: print_sbd_copy

# pipeline completo (filtros -> concat -> saída(s))
print_sbd_main: deps check_tools
	cd $(GIT_ROOT)/src/publish && $(PY) main_filter.py --inputdir $(SBD_PRINT) --bookyml $(SBD_BOOKYML_PRINT)
	cd $(GIT_ROOT)/src/publish && $(PY) parse_book_yaml_eisvogel.py --book $(SBD_BOOKYML_PRINT) --outdir $(SBD_PDF_OUT)
ifneq ($(filter pdf both,$(FORMAT)),)
	cd $(SBD_PDF_OUT) && $(PANDOC) manual-sbd-toe.md --from markdown --template eisvogel \
		--data-dir="$(PANDOC_DATA_DIR)" \
		--lua-filter=$(GIT_ROOT)/src/publish/small_font_tables.lua \
		--pdf-engine=$(PDF_ENGINE) -o manual-sbd-toe.pdf
endif
ifneq ($(filter docx both,$(FORMAT)),)
	cd $(SBD_PDF_OUT) && $(PANDOC) manual-sbd-toe.md --from markdown+raw_tex \
		$(if $(DOCX_REF),--reference-doc=$(DOCX_REF),) \
		--resource-path=.:$(SBD_PRINT) \
		--toc --number-sections \
		-o manual-sbd-toe.docx
endif
.PHONY: print_sbd_main

# apenas filtros (útil para debug rápido)
print_sbd_filters_only: deps
	cd $(GIT_ROOT)/src/publish && $(PY) main_filter.py --inputdir $(SBD_PRINT) --bookyml $(SBD_BOOKYML_PRINT)
.PHONY: print_sbd_filters_only

ifeq ($(copy),true)
print_sbd: print_sbd_copy print_sbd_main
else
print_sbd: print_sbd_main
endif
.PHONY: print_sbd

clean_print_sbd:
	rm -rf $(SBD_PRINT) $(SBD_PDF_OUT)
.PHONY: clean_print_sbd

## ========================================================================== ##
##                          PRINT – SUPPLY CHAIN                               ##
## ========================================================================== ##
print_supply_copy:
	mkdir -p $(SUPPLY_PRINT)
	rsync -a --delete --exclude 'node_modules' --exclude '.git' $(SUPPLY_SRC)/ $(SUPPLY_PRINT)/
	@ls -l $(SUPPLY_PRINT)/docs/ || true
.PHONY: print_supply_copy

print_supply_main: deps check_tools
	cd $(GIT_ROOT)/src/publish && $(PY) main_filter.py --inputdir $(SUPPLY_PRINT) --bookyml $(SUPPLY_BOOKYML_PRINT)
	cd $(GIT_ROOT)/src/publish && $(PY) parse_book_yaml_eisvogel.py --book $(SUPPLY_BOOKYML_PRINT) --outdir $(SUPPLY_PDF_OUT)
ifneq ($(filter pdf both,$(FORMAT)),)
	cd $(SUPPLY_PDF_OUT) && $(PANDOC) manual-supply-chain.md --from markdown --template eisvogel \
		--data-dir="$(PANDOC_DATA_DIR)" \
		--lua-filter=$(GIT_ROOT)/src/publish/small_font_tables.lua \
		--pdf-engine=$(PDF_ENGINE) -o manual-supply-chain.pdf
endif
ifneq ($(filter docx both,$(FORMAT)),)
	cd $(SUPPLY_PDF_OUT) && $(PANDOC) manual-supply-chain.md --from markdown+raw_tex \
		$(if $(DOCX_REF),--reference-doc=$(DOCX_REF),) \
		--resource-path=.:$(SUPPLY_PRINT) \
		--toc --number-sections \
		-o manual-supply-chain.docx
endif
.PHONY: print_supply_main

print_supply_filters_only: deps
	cd $(GIT_ROOT)/src/publish && $(PY) main_filter.py --inputdir $(SUPPLY_PRINT) --bookyml $(SUPPLY_BOOKYML_PRINT)
.PHONY: print_supply_filters_only

ifeq ($(copy),true)
print_supply: print_supply_copy print_supply_main
else
print_supply: print_supply_main
endif
.PHONY: print_supply

clean_print_supply:
	rm -rf $(SUPPLY_PRINT) $(SUPPLY_PDF_OUT)
.PHONY: clean_print_supply

## ========================================================================== ##
##                                  WEB                                       ##
## ========================================================================== ##
web_copy:
	mkdir -p $(WEB_BUILD)
	rsync -a --delete --exclude 'node_modules' --exclude '.git' $(WEB_SRC)/ $(WEB_BUILD)/
	@ls -l $(WEB_BUILD)/docs/ || true
.PHONY: web_copy

# pipeline completo (filtros -> build docusaurus)
web_main: deps check_node
	cd $(GIT_ROOT)/src/publish && $(PY) main_filter.py --inputdir $(WEB_BUILD) --bookyml $(WEB_BOOKYML)
	cd $(WEB_BUILD) && $(NPM) install && $(NPM) run build
.PHONY: web_main

# dev server (não substitui web_main)
web_serve:
	cd $(WEB_BUILD) && $(NPM) run serve
.PHONY: web_serve

# desenvolvimento (hot reload) – caso o site tenha o script start
web_dev:
	cd $(WEB_BUILD) && $(NPM) run start
.PHONY: web_dev

# só filtros web (debug)
web_filters_only: deps
	cd $(GIT_ROOT)/src/publish && $(PY) main_filter.py --inputdir $(WEB_BUILD) --bookyml $(WEB_BOOKYML)
.PHONY: web_filters_only

ifeq ($(copy),true)
web: web_copy web_main
else
web: web_main
endif
.PHONY: web

clean_web:
	rm -rf $(WEB_BUILD)
.PHONY: clean_web

## ========================================================================== ##
##                               TARGETS GLOBAIS                               ##
## ========================================================================== ##
print_all: print_sbd print_supply
.PHONY: print_all

all: print_all web
.PHONY: all

clean_print: clean_print_sbd clean_print_supply
.PHONY: clean_print

clean: clean_print clean_web
.PHONY: clean

clean_venv:
	rm -rf $(VENV_DIR)
.PHONY: clean_venv

## ========================================================================== ##
##                                    HELP                                     ##
## ========================================================================== ##
help:
	@echo "VARIÁVEIS: FORMAT=(pdf|docx|both)  PDF_ENGINE=$(PDF_ENGINE)  DOCX_REF=$(DOCX_REF)"
	@echo "Targets principais:"
	@echo "  web (web_copy+web_main) | web_filters_only | web_serve | web_dev | clean_web"
	@echo "  print_sbd (copy+main)    | print_sbd_filters_only | clean_print_sbd"
	@echo "  print_supply (copy+main) | print_supply_filters_only | clean_print_supply"
	@echo "  print_all | all | clean_print | clean | deps | clean_venv | check_tools | check_node"
.PHONY: help
