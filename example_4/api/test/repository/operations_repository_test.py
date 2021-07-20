
import pytest
from flask import Flask
import pytest

import application
from application.repository.operations_repository import OperationsRepository

result =  { "id": 1, "operation": "sum", "number1": 1, "number2": 1, "result": 2 }

docker_compose_dir = "../docker/development.yml"


@pytest.fixture()
def app() -> Flask:  
    return application.create_app("testing")


def test__OperationsRepository__saves_on_database__when_element_is_given(app):
    response = { "operation": "sub", "number1": 50, "number2": 1, "result": 49 }

    repository = OperationsRepository()
    saved_element = repository.save(response)
    id = saved_element.id
    operation = repository.query_by_id(id)

    assert operation == {"id": id, "operation": "sub", "number1": 50, "number2": 1, "result": 49 }
