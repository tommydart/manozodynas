.PHONY: prepare_env run test

prepare_env:
	rm -fr ~/.buildout
	python ez_setup.py --user
	python bootstrap.py
	bin/buildout
	mkdir var || touch var/db
	bin/django syncdb --noinput
	bin/django migrate manozodynas

run:
	bin/django migrate manozodynas
	bin/django runserver 77.241.198.205:8000
test:
	bin/django test
