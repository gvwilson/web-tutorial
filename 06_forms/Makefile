include ../common.mk

## serve: make fresh database and run server
serve:
	cp data/lab.db ./temp.db
	DB=temp.db fastapi dev server.py
