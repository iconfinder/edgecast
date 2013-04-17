all:

test:
	@nosetests
	@pep8 edgecast django_edgecast tests setup.py

pep8:
	@pep8 edgecast django_edgecast tests setup.py

publish:
	@python setup.py sdist upload

install:
	@python setup.py install
