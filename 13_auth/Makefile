include ../common.mk

DB_BASE=data/lab.db
DB_TEMP=./temp.db
PLAIN_FWD=migrations/02_fwd_add_plaintext_passwords.sql
MIGRATIONS=migrations

## generate: create passwords and add to database
generate:
	DATA=${DB_BASE} python generate_accounts.py --seed 42179843 --template add_plaintext_passwords.sql > ${PLAIN_FWD}

## migrate: apply migrations
migrate:
	cp ${DB_BASE} ${DB_TEMP}
	python migrate.py --forward --migrations ${MIGRATIONS} --db ${DB_TEMP} --verbose --limit 02

## serve: run server
serve:
	make migrate
	${RUN_TEMP} server.py run
