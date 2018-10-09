install:
	pip install -r requirements/base.txt
	pip install -r requirements/test.txt

test:
	python atlantic_demo/manage.py test atlantic_demo

start:
	python atlantic_demo/manage.py runserver