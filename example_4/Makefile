help: Makefile
	@sed -n 's/^## //p' $<

## up
up:
	docker-compose -f docker/development.yml up -d


## down
down:
	docker-compose -f docker/development.yml up


## stop
stop:
	docker-compose -f docker/development.yml stop


## test-end2end
test-end2end:
	make up ; ./run-test.sh end2end ; make stop


## test-endpoints
test-endpoints:
	make up ; ./run-test.sh endpoints ; make stop


## test-repository
test-repository:
	make up ; ./run-test.sh repository ; make stop


## test-services
test-services:
	make up ; ./run-test.sh services ; make stop


## test-all
test-all:
	make up ; ./run-test.sh all ; make stop
