include ../common.mk

SERVER=DATA=data/staff.csv fastapi dev

## run_hello: run "hello, world" server
run_hello:
	${SERVER} server_hello.py

## run_func: run server that builds app in function
run_func:
	${SERVER} server_func.py

## run_routes: run server that has multiple routes
run_routes:
	${SERVER} server_routes.py

## run_err: run server that handles errors
run_err:
	${SERVER} server_err.py
