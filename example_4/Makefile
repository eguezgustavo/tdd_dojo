help: Makefile
	@sed -n 's/^## //p' $<

## up
up:
	export API_URL="http://localhost:5000"; \
	docker-compose -f local_environment/development.yml up -d api db ui


## down
down:
	docker-compose -f local_environment/development.yml up


## stop
stop:
	docker-compose -f local_environment/development.yml stop


## test-end2end
test-end2end:
	docker-compose -f local_environment/development.yml stop ui
	export API_URL="http://172.18.0.2:5000"; \
	docker-compose -f local_environment/development.yml up -d ui chrome
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
	docker-compose -f local_environment/development.yml stop ui
	export API_URL="http://172.18.0.2:5000"; \
	docker-compose -f local_environment/development.yml up -d ui chrome
	./run-test.sh all


## init-db
init-db:
	docker exec -ti local_environment_api_1 bash -c "flask db init"
	docker exec -ti local_environment_api_1 bash -c "flask db migrate"
	docker exec -ti local_environment_api_1 bash -c "flask db upgrade"