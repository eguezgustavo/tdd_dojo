.PHONY: install
install:
	docker build -t tdd_dojo .

.PHONY: uninstall
uninstall:
	docker rmi tdd_dojo

.PHONY: shell
shell:
	docker run --rm -it -v $(PWD):/app -v ~/.ssh:/root/.ssh tdd_dojo zsh
