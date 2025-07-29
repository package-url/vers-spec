# SPDX-License-Identifier: MIT
# Copyright (c) the purl authors
# Visit https://github.com/package-url/vers-spec and https://packageurl.org for support

PYTHON_EXE?=python3
VENV_LOCATION=venv
ACTIVATE?=. ${VENV_LOCATION}/bin/activate;

virtualenv:
	@echo "-> Bootstrap the virtualenv with PYTHON_EXE=${PYTHON_EXE}"
	${PYTHON_EXE} -m venv ${VENV_LOCATION}

conf: virtualenv
	@echo "-> Install dependencies"
	@${ACTIVATE} pip install -r etc/scripts/requirements.txt

formatcode:
	@echo "-> Run Ruff format"
	@${ACTIVATE} ruff check --select I --fix
	@${ACTIVATE} ruff format
	@echo "-> Run Ruff linter"
	@${ACTIVATE} ruff check --fix

formatjson:
	@echo "-> Format JSON files"
	@${ACTIVATE} python etc/scripts/format_json.py schemas/
	@${ACTIVATE} python etc/scripts/format_json.py schemes/
	@${ACTIVATE} python etc/scripts/format_json.py tests/

format: formatcode formatjson
	@echo "-> Format all files"

checkjson:
	@echo "-> Validate JSON schemas"
	@${ACTIVATE} check-jsonschema --check-metaschema --verbose schemas/*.json
	@echo "-> Validate JSON data files against the schemas"
#	@${ACTIVATE} check-jsonschema --schemafile schemas/vers-test.schema.json --verbose tests/*/*-test.json

checkcode:
	@echo "-> Run Ruff linter validation (pycodestyle, bandit, isort, and more)"
	@${ACTIVATE} ruff --config etc/scripts/pyproject.toml check
	@echo "-> Run Ruff format validation"
	@${ACTIVATE} ruff --config etc/scripts/pyproject.toml format --check

check: checkjson checkcode
	@echo "-> Run all checks"

clean:
	@echo "-> Clean the Python env"
	rm -rf .venv/
	find . -type f -name '*.py[co]' -delete

gendocs:
	@${ACTIVATE} python etc/scripts/generate_index_and_docs.py


.PHONY: virtualenv conf formatcode formatjson format checkcode checkjson check clean  gendocs
