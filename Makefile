install:
	poetry install

build:
	poetry build

publish:
	poetry publish

lint:
	flake8 gendiff.py
