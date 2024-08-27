include ../common.mk

DB_BASE=data/lab.db
DB_TEMP=./temp.db

## serve: run server
serve:
	cp ${DB_BASE} ${DB_TEMP}
	${RUN_MIGRATE} --forward --migrations migrations --db ${DB_TEMP} --limit 03
	TXLATE=site_translation.json SECRET=$$(cat secret.txt) DATA=temp.db flask --app server.py run
