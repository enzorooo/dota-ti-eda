.PHONY: clean dev venv help
.DEFAULT_GOAL := help
-include .env

help: ## List Make Commands
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Setup dev environment
	poetry install
	poetry run pre-commit install
	@if [ -f ".env" ]; then\
		echo ".env already exists within ${PWD}"; else\
		cat .env.sample > .env && \
		echo "Created .env file om local";\
	fi

format: ## Run pre-commit to format files prior to committing
	poetry run pre-commit run --all-files

dagster: ## Run local dagster environment
	poetry run dagit
