# Runnable tasks.

include common.mk

all: commands

# CSS=-css chota.css
# CSS=-css neat.css
# CSS=-css picnic.css
# CSS=-css pico.css
# CSS=-css simple.css
# CSS=-css tacit.css
CSS=

## datasets: re-create snailz parameters and datasets
datasets:
	snailz params --outdir params
	snailz everything --paramsdir params --datadir data

## lint: check code and project
lint:
	@ruff check --exclude docs .
	@python bin/lint.py
	@html5validator --root docs --blacklist templates \
	--ignore \
	'Attribute "x-'

## render: convert to HTML
render:
	@python bin/render.py ${CSS}
	@touch docs/.nojekyll

## serve: serve generated HTML
serve:
	@python -m http.server -d docs
