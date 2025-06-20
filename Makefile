.PHONY: install virtualenv clean test lint fmt build publish-test

install:
# O @ serve para não mostrar o comando no terminal, apenas mostrar o stdout
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	python -m venv .venv

lint:
	@.venv/bin/pflake8 dundie tests integration

test:
	@.venv/bin/pytest -s --forked

fmt:
	@.venv/bin/black dundie tests integration

watch:
	@@.venv/bin/ptw -- -vv -s --forked
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

build:
	@python setup.py sdist bdist_wheel


publish-test:
	@twine upload --repository testpypi dist/*
