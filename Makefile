## setup: installs package locally
setup:
	@pip install .

## deploy: deploys to PyPi
deploy:
	@rm -rf dist
	 rm -f MANIFEST
	 python setup.py sdist
	 twine upload dist/*

## tag: tags current state
tag:
ifndef VERSION
	$(error Provide VERSION as env var)
endif
	@git tag -a "${VERSION}" -m "${VERSION}"
	 git push origin --tags

## help: displays this message
help:
	@echo "thumbor-request-modifier"
	@echo
	@echo "Usage:"
	@echo
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'
	@echo
