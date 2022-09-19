.PHONY: install
install:
	docker build -t tdd_dojo .

.PHONY: uninstall
uninstall:
	docker rmi tdd_dojo

.PHONY: shell
shell:
	docker run --rm -it -v ~/.ssh:/root/.ssh -v $(PWD):/app tdd_dojo zsh
