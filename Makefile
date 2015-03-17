SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo "    make release    | Release to pypi."
	@echo "    make test       | Run the tests."
	@echo "    make install    | Install development dependencies."

release:
	python setup.py register sdist bdist_wheel upload

test:
	@py.test --cov-report term-missing --cov incuna_test_utils tests
	@flake8 .

install:
	pip install -r requirements.txt
