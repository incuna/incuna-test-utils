SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo "    make release    | Release to pypi."

release:
	python setup.py register sdist bdist_wheel upload

test:
	@py.test -Wmodule incuna_test_utils tests
	@flake8 .

install:
	pip install -r requirements.txt
