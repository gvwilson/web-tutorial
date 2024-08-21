include ../common.mk

ORIGINAL=data/lab.db
LOCAL=./lab.db
MIGRATIONS=./migrations

## forward: migrate database forward
forward:
	cp ${ORIGINAL} ${LOCAL}
	python migrate.py --forward --migrations ${MIGRATIONS} --db ${LOCAL} --verbose

## backward: revert database
backward:
	python migrate.py --backward --migrations ${MIGRATIONS} --db ${LOCAL} --verbose
