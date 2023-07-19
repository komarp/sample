prettify:
	pautoflake ./src
	isort ./src
	black ./src

build:
	docker build -t ram_connector .
