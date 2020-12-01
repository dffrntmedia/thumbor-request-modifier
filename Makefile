.PHONY: deploy
## deploy: deploys to PyPi
deploy:
	@rm -rf dist
	 rm MANIFEST
	 python setup.py sdist
	 twine upload dist/*

.PHONY: help
## help: prints help message
help:
	@echo "thumbor-request-modifier-http-loader"
	@echo
	@echo "Usage:"
	@echo
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'
	@echo
