help: Makefile
	@sed -n 's/^## //p' $<

## up
up:
	export START_MODE="start"
	docker-compose -f docker/development.yml up -d api db ui


## down
down:
	docker-compose -f docker/development.yml up


## stop
stop:
	docker-compose -f docker/development.yml stop


## test-end2end
test-end2end:
	docker-compose -f docker/development.yml stop ui
	export START_MODE="test-e2e"
	docker-compose -f docker/development.yml up -d ui chrome
	./run-test.sh end2end


## test-endpoints
test-endpoints:
	./run-test.sh endpoints


## test-repository
test-repository:
	./run-test.sh repository


## test-services
test-services:
	./run-test.sh services


## test-all
test-all:
	docker-compose -f docker/development.yml stop ui
	export START_MODE="test-e2e"
	docker-compose -f docker/development.yml up -d ui chrome
	./run-test.sh all
