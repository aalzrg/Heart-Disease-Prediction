.PHONY: up down logs cli sh test

up:
\tdocker compose up -d --build

down:
\tdocker compose down -v

logs:
\tdocker compose logs -f --tail=100

cli:
\tdocker compose run --rm cli

sh:
\tdocker compose exec api sh

test:
\t# basic smoke tests
\tcurl -f http://localhost:8000/docs >/dev/null
\tpython scripts/test_api.py
