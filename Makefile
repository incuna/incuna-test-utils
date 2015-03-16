SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo "    make release    | Release to pypi."

release:
	python setup.py register sdist bdist_wheel upload

test:
	@py.test --cov-report term-missing --cov incuna_test_utils tests
	@flake8 .

install:
	pip install -r test_requirements.txt
	pip install -r test_local_requirements.txt
