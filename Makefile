.PHONY: install virtualenv clean test

install:
# O @ serve para não mostrar o comando no terminal, apenas mostrar o stdout
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	python -m venv .venv

test:
	@.venv/bin/pytest -vv -s 

watch:
	@@.venv/bin/ptw -- -vv -s tests/
#	utilizando entr
#	ls **/*.py | entr pytest

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -rf {} \;
	@find ./ -name '*~' -exec rm -rf {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
