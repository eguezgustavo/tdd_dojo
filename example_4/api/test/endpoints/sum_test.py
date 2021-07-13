from flask.testing import FlaskClient
from flask_restx._http import HTTPStatus
from flask import Flask
from application import create_app

import pytest
import json


@pytest.fixture(scope='session')
def app() -> Flask:
    return create_app("testing")


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    with app.test_client() as c:
        return c
        

def test__sum_endpoint__should_return_200__when_correct_parameters_are_send(client: FlaskClient):
    number_1 = 1
    number_2 = 1

    response = client.get(
        f'/sum/{number_1}/{number_2}',
    )

    assert HTTPStatus.OK == response.status_code


def test__sum_endpoint__should_return_404__when_incorrect_parameters_are_send(client: FlaskClient):
    number_1 = 'a'
    number_2 = 'b'

    response = client.get(
        f'/sum/{number_1}/{number_2}',
    )

    assert HTTPStatus.NOT_FOUND == response.status_code


def test__sum_endpoint__should_return_result_json__when_1_and_2_are_send(client: FlaskClient):
    number_1 = 1
    number_2 = 2
    result = {"id": 1, "operation": "sum", "number1": 1, "number2": 2, "result": 3}

    response = client.get(
        f'/sum/{number_1}/{number_2}',
    )

    assert HTTPStatus.OK == response.status_code
    assert result == json.loads(response.get_data())
