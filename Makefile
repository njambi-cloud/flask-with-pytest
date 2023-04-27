all: sever tests

test:
	pytest

server:
	export FLASK_APP=index
	export FLASK_ENV=development
	flask run




