# Common Make variables and targets

DB_BASE=../data/lab.db
DB_TEMP=./temp.db
MIGRATIONS=../migrations

RUN_CSV=DATA=../data/staff.csv flask --app
RUN_LAB=DATA=${DB_BASE} flask --app
RUN_MIGRATE=python migrate.py --migrations ${MIGRATIONS}
RUN_TEMP=DATA=${DB_TEMP} flask --app

## ---: ---

## commands: show available commands (*)
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} \
	| sed -e 's/## //g' \
	| column -t -s ':'

## clean: clean up
clean:
	@find . -type f -name '*~' -exec rm {} \;
	@find . -type d -name __pycache__ | xargs rm -r
	@find . -type d -name .pytest_cache | xargs rm -r
	@find . -type d -name .ruff_cache | xargs rm -r
