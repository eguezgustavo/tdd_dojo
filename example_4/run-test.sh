#!/bin/bash
END2END_TEST="python3 -m pytest -svv test/end2end"
ENDPOINTS_TEST="python3 -m pytest -v test/endpoints"
SERVICES_TEST="python3 -m pytest -v test/services"
REPOSITORY_TEST="python3 -m pytest -v test/repository"
ALL_TEST="python3 -m pytest -v"
API_CONTAINER_NAME="docker_api_1"
API_CONTAINER_URI="localhost:5000"
UI_CONTAINER_URI="localhost:4200"

execute_end2end(){
    docker exec -ti $API_CONTAINER_NAME bash -c "$END2END_TEST"
}

execute_endpoints(){
    docker exec -ti $API_CONTAINER_NAME bash -c "$ENDPOINTS_TEST"
}

execute_services(){
    docker exec -ti $API_CONTAINER_NAME bash -c "$SERVICES_TEST"
}

execute_repository(){
    docker exec -ti $API_CONTAINER_NAME bash -c "$REPOSITORY_TEST"
}

execute_all(){
    docker exec -ti $API_CONTAINER_NAME bash -c "$ALL_TEST"
}

wait_api(){
    until curl -ksf "${API_CONTAINER_URI}" > /dev/null; do
        echo "Waiting for API to start..."
        sleep 5
    done
}

wait_all(){
    wait_api
    until curl -ksf "${UI_CONTAINER_URI}" > /dev/null; do
        echo "Waiting for UI to start..."
        sleep 5
    done
}

case $1 in
    end2end)
        wait_all
        execute_end2end
        ;;

    endpoints)
        wait_api
        execute_endpoints
        ;;

    services)
        wait_api
        execute_services
        ;;

    repository)
        wait_all
        execute_repository
        ;;

    all)
        wait_all
        execute_all
        ;;
esac

