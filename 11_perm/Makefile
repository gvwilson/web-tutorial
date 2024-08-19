include ../common.mk

DB = ./temp.db

## json: test JSON
json:
	@cp data/lab.db ${DB}
	@sqlite3 ${DB} < add_roles_permissions.sql
	@DB=${DB} pytest test_json.py

## perm: test permissions
perm:
	@cp data/lab.db ${DB}
	@sqlite3 ${DB} < add_roles_permissions.sql
	@DB=${DB} pytest test_permissions.py
