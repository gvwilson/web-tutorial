include ../common.mk

DB_BASE=data/lab.db
DB_TEMP=./temp.db
MIGRATIONS=migrations

## migrate_sessions: apply migrations up to and including this lesson (including sessions table)
migrate_sessions:
	@if [ ! -f ${DB_TEMP} ]; then \
		cp ${DB_BASE} ${DB_TEMP}; \
		${RUN_MIGRATE} --forward --migrations ${MIGRATIONS} --db ${DB_TEMP} --verbose --limit 04; \
	fi

## sessions: run secure server with persistent sessions
sessions:
	make migrate_sessions
	SECRET=$$(cat secret.txt) DATA=temp.db flask --app server_sessions.py run

