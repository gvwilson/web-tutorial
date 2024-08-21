include ../common.mk

ORIGINAL=data/lab.db
LOCAL=temp.db
MIGRATIONS=./migrations

## forward: migrate database forward
forward:
	cp ${ORIGINAL} ${LOCAL}
	python migrate.py --forward --migrations ${MIGRATIONS} --db ${LOCAL} --verbose --limit 01

## backward: revert database
backward:
	python migrate.py --backward --migrations ${MIGRATIONS} --db ${LOCAL} --verbose --limit 01
