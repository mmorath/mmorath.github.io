# =============================================================================
# mmorath.github.io — Makefile
#
# Convenience wrapper around the MkDocs (Material) site published via GitHub
# Pages at https://mmorath.github.io/.
#
#   - edit:    Markdown in docs/ + mkdocs.yml on `main`
#   - preview: `make serve`  (live reload at http://127.0.0.1:8000)
#   - publish: `make deploy` (builds + force-pushes to the `gh-pages` branch)
#
# Run `make` (or `make help`) with no target to see a colourised list.
# =============================================================================

# ----- Config ----------------------------------------------------------------
MKDOCS    := mkdocs
SITE_DIR  := site
SERVE_ADDR := 127.0.0.1:8000

# ----- Colours (ANSI; honoured by the help target) ---------------------------
CYAN  := \033[36m
BOLD  := \033[1m
DIM   := \033[2m
RESET := \033[0m

.DEFAULT_GOAL := help

# =============================================================================
##@ General
# =============================================================================

help: ## Show this help
	@awk 'BEGIN { \
		FS = ":.*##"; \
		printf "\n$(BOLD)mmorath.github.io — site targets$(RESET)\n$(DIM)usage: make <target>$(RESET)\n"; \
	} \
	/^[a-zA-Z0-9_-]+:.*?##/ { printf "  $(CYAN)%-16s$(RESET) %s\n", $$1, $$2 } \
	/^##@/ { printf "\n$(BOLD)%s$(RESET)\n", substr($$0, 5) } \
	END { printf "\n" }' $(MAKEFILE_LIST)

# =============================================================================
##@ Setup
# =============================================================================

install: ## Install the docs toolchain (mkdocs-material + i18n) via pip
	@printf "$(CYAN)Installing mkdocs-material + mkdocs-static-i18n$(RESET)\n"
	@pip install --upgrade mkdocs-material mkdocs-static-i18n

# =============================================================================
##@ Site
# =============================================================================

serve: ## Live-preview the site with reload (http://127.0.0.1:8000)
	@$(MKDOCS) serve -a $(SERVE_ADDR)

build: ## Build the static site into ./site (clean)
	@$(MKDOCS) build --clean
	@printf "$(DIM)built → $(SITE_DIR)/$(RESET)\n"

deploy: ## Build + publish to the gh-pages branch (republishes the live site)
	@printf "$(BOLD)Publishing to GitHub Pages (gh-pages)…$(RESET)\n"
	@$(MKDOCS) gh-deploy --clean
	@printf "$(DIM)live → https://mmorath.github.io/$(RESET)\n"

clean: ## Remove the local build output (./site)
	@rm -rf $(SITE_DIR)
	@printf "$(DIM)removed $(SITE_DIR)/$(RESET)\n"

.PHONY: help install serve build deploy clean
