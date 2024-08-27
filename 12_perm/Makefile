include ../common.mk

DB=./temp.db

## json: test JSON
json:
	@cp data/lab.db ${DB}
	${RUN_MIGRATE} --forward --migrations migrations --db ${DB}
	@DB=${DB} pytest test_json.py

## perm: test permissions
perm:
	@cp data/lab.db ${DB}
	${RUN_MIGRATE} --forward --migrations migrations --db ${DB}
	@DB=${DB} pytest test_permissions.py
