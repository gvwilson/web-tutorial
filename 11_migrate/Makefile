include ../common.mk

ORIGINAL=data/lab.db
LOCAL=temp.db
MIGRATIONS=./migrations

## forward: migrate database forward
forward:
	cp ${ORIGINAL} ${LOCAL}
	${RUN_MIGRATE} --forward --migrations ${MIGRATIONS} --db ${LOCAL} --verbose --limit 01

## backward: revert database
backward:
	${RUN_MIGRATE} --backward --migrations ${MIGRATIONS} --db ${LOCAL} --verbose --limit 01
