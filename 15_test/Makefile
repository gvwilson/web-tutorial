include ../common.mk

DB_BASE=data/lab.db
DB_TEMP=./temp.db

## migrate: apply all migrations
migrate:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --migrations migrations --db ${DB_TEMP} --limit 03

## serve: run server
serve:
	make migrate
	SECRET=$$(cat secret.txt) DATA=temp.db flask --app server.py run
