# Runnable tasks.

include common.mk

all: commands

## datasets: re-create snailz parameters and datasets
datasets:
	snailz params --outdir params
	snailz everything --paramsdir params --datadir data

## lint: check code and project
lint:
	@ruff check .
	@python bin/lint.py

## build: convert to HTML
build:
	@python bin/render.py
