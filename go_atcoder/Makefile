download:
	bash cmd/download.sh
.PHONY: download

test:
	oj t -d $(dir $(abspath $(lastword $(MAKEFILE_LIST))))/tests -c 'go run $$(pwd)/main.go'
.PHONY: test

submit:
	acc submit main.go
.PHONY: submit