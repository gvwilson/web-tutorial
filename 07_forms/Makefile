include ../common.mk

## split: explore data insertion with split operations
split:
	cp data/lab.db ./temp.db
	DATA=temp.db python explore_insert.py something random split

## combined: explore data insertion with combined operations
combined:
	cp data/lab.db ./temp.db
	DATA=temp.db python explore_insert.py something random combined

## serve: make fresh database and run server
serve:
	cp data/lab.db ./temp.db
	${RUN_TEMP} server.py run
