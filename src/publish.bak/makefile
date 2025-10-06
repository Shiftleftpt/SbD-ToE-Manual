
###############################################################################
# Makefile – Build Automático Multi-Livro SbD-ToE (Web + Print)
#
# Este Makefile automatiza o processo de build, filtragem, concatenação e
# publicação dos manuais Security by Design – Theory of Everything (SbD-ToE)
# e derivados, tanto para versão Web (Docusaurus) como Print (PDF/Eisvogel).
#
# Principais funcionalidades:
# - Build isolado para cada manual ("livro") e output (print/web)
# - Sincronização incremental das fontes (controlada por variável `copy`)
# - Filtros de transformação configuráveis via YAML (ex: main_filter.py)
# - Targets clean para remoção de artefactos por livro/output
# - Pronto para pipelines CI/CD (GitHub Actions, GitLab CI, etc)
#
# Uso típico:
#   make print_sbd            # Build PDF do manual principal (com copy)
#   make print_sbd copy=false # Build PDF sem copy (incremental/debug)
#   make web_supply           # Build web do manual Supply Chain
#   make all                  # Build de todos os manuais e outputs
#   make clean                # Limpa todos os artefactos gerados
#
# Adapta e expande para novos livros/output duplicando os blocos relevantes.
# Mantém paths e configs alinhadas com o repositório.
###############################################################################

copy ?= true

# Paths globais (ajusta conforme estrutura real)
GIT_ROOT     ?= $(shell git rev-parse --show-toplevel)

## ----------- SBD MANUAL -----------

SBD_SRC           := $(GIT_ROOT)/manuals_src/sbd_manual
SBD_PRINT         := $(GIT_ROOT)/build/print/sbd_manual
SBD_WEB           := $(GIT_ROOT)/build/web/sbd_manual
SBD_BOOKYML_PRINT := $(SBD_SRC)/book_print.yml
SBD_BOOKYML_WEB   := $(SBD_SRC)/book_web.yml
SBD_PDF_OUT       := $(GIT_ROOT)/BOOK/pdf/sbd_manual

print_sbd_copy:
	mkdir -p $(SBD_PRINT)
	rsync -a --delete --exclude 'node_modules' --exclude '.git' $(SBD_SRC)/ $(SBD_PRINT)/
	@ls -l $(SBD_PRINT)/docs/

print_sbd_main:
	python3 src/publish/main_filter.py --inputdir $(SBD_PRINT) --bookyml $(SBD_BOOKYML_PRINT)
	cd $(GIT_ROOT)/src/publish && python3 parse_book_yaml_eisvogel.py --book $(SBD_BOOKYML_PRINT) --outdir $(SBD_PDF_OUT)
	cd $(SBD_PDF_OUT) && pandoc manual-sbd-toe.md --from markdown --template eisvogel --lua-filter=$(GIT_ROOT)/src/publish/small_font_tables.lua --pdf-engine=xelatex -o manual-sbd-toe.pdf

ifeq ($(copy),true)
print_sbd: print_sbd_copy print_sbd_main
else
print_sbd: print_sbd_main
endif

clean_print_sbd:
	rm -rf $(SBD_PRINT) $(SBD_PDF_OUT)

web_sbd_copy:
	mkdir -p $(SBD_WEB)
	rsync -a --delete --exclude 'node_modules' --exclude '.git' $(SBD_SRC)/ $(SBD_WEB)/
	@ls -l $(SBD_WEB)/docs/

web_sbd_main:
	python3 src/publish/main_filter.py --inputdir $(SBD_WEB) --bookyml $(SBD_BOOKYML_WEB)
	cd $(SBD_WEB) && npm install && npm run build

ifeq ($(copy),true)
web_sbd: web_sbd_copy web_sbd_main
else
web_sbd: web_sbd_main
endif

clean_web_sbd:
	rm -rf $(SBD_WEB)

## ----------- SUPPLY CHAIN -----------

SUPPLY_SRC           := $(GIT_ROOT)/manuals_src/supply_chain
SUPPLY_PRINT         := $(GIT_ROOT)/build/print/supply_chain
SUPPLY_WEB           := $(GIT_ROOT)/build/web/supply_chain
SUPPLY_BOOKYML_PRINT := $(SUPPLY_SRC)/book_print.yml
SUPPLY_BOOKYML_WEB   := $(SUPPLY_SRC)/book_web.yml
SUPPLY_PDF_OUT       := $(GIT_ROOT)/BOOK/pdf/supply_chain

print_supply_copy:
	mkdir -p $(SUPPLY_PRINT)
	rsync -a --delete --exclude 'node_modules' --exclude '.git' $(SUPPLY_SRC)/ $(SUPPLY_PRINT)/
	@ls -l $(SUPPLY_PRINT)/docs/

print_supply_main:
	python3 src/publish/main_filter.py --inputdir $(SUPPLY_PRINT) --bookyml $(SUPPLY_BOOKYML_PRINT)
	cd $(GIT_ROOT)/src/publish && python3 parse_book_yaml_eisvogel.py --book $(SUPPLY_BOOKYML_PRINT) --outdir $(SUPPLY_PDF_OUT)
	cd $(SUPPLY_PDF_OUT) && pandoc manual-supply-chain.md --from markdown --template eisvogel --lua-filter=$(GIT_ROOT)/src/publish/small_font_tables.lua --pdf-engine=xelatex -o manual-supply-chain.pdf

ifeq ($(copy),true)
print_supply: print_supply_copy print_supply_main
else
print_supply: print_supply_main
endif

clean_print_supply:
	rm -rf $(SUPPLY_PRINT) $(SUPPLY_PDF_OUT)

web_supply_copy:
	mkdir -p $(SUPPLY_WEB)
	rsync -a --delete --exclude 'node_modules' --exclude '.git' $(SUPPLY_SRC)/ $(SUPPLY_WEB)/
	@ls -l $(SUPPLY_WEB)/docs/

web_supply_main:
	python3 src/publish/main_filter.py --inputdir $(SUPPLY_WEB) --bookyml $(SUPPLY_BOOKYML_WEB)
	cd $(SUPPLY_WEB) && npm install && npm run build

ifeq ($(copy),true)
web_supply: web_supply_copy web_supply_main
else
web_supply: web_supply_main
endif

clean_web_supply:
	rm -rf $(SUPPLY_WEB)

## ----------- TARGETS GLOBAIS -----------

print_all: print_sbd print_supply
web_all: web_sbd web_supply

clean_print: clean_print_sbd clean_print_supply
clean_web: clean_web_sbd clean_web_supply

all: print_all web_all
clean: clean_print clean_web

.PHONY: print_sbd print_supply web_sbd web_supply \
		clean_print_sbd clean_print_supply clean_web_sbd clean_web_supply \
		print_all web_all clean_print clean_web all clean
# EOF