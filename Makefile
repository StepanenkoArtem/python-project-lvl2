install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r testPyPI -u artem.stepanenko -p Fb_706428

lint:
	flake8 gendiff.py

bump:
	poetry version patch
