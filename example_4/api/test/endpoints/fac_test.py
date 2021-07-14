from flask.testing import FlaskClient
from flask_restx._http import HTTPStatus
from flask import Flask
import application # import create_app

import pytest
import json


@pytest.fixture()
def app(mocker) -> Flask:
    mocker.patch('application.services.calculator.Calculator.fac', return_value=1)
    return application.create_app("testing")


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    with app.test_client() as c:
        return c
        

def test__fac_endpoint__should_return_200__when_correct_parameters_are_send(client: FlaskClient):
    number_1 = 1

    response = client.get(
        f'/fac/{number_1}',
    )

    assert HTTPStatus.OK == response.status_code


def test__fac_endpoint__should_return_404__when_incorrect_parameters_are_send(client: FlaskClient):
    number_1 = 'a'

    response = client.get(
        f'/fac/{number_1}',
    )

    assert HTTPStatus.NOT_FOUND == response.status_code


def test__fac_endpoint__should_return_correct_result__when_3_is_send(client: FlaskClient, mocker):
    number_1 = 3
    result = {"id": 1, "operation": "fac", "number1": 3, "number2": None, "result": 6}
    mocker.patch('application.services.calculator.Calculator.fac', return_value=6)

    response = client.get(
        f'/fac/{number_1}',
    )

    assert HTTPStatus.OK == response.status_code
    assert result == json.loads(response.get_data())


def test__fac_endpoint__should_return_correct_result__when_4_is_send(client: FlaskClient, mocker):
    number_1 = 4
    result = {"id": 1, "operation": "fac", "number1": 4, "number2": None, "result": 24}
    mocker.patch('application.services.calculator.Calculator.fac', return_value=24)

    response = client.get(
        f'/fac/{number_1}',
    )

    assert HTTPStatus.OK == response.status_code
    assert result == json.loads(response.get_data())


def test__fac_endpoint__should_save_the_operation__when_valid_operation_is_send(client: FlaskClient, mocker):
    number_1 = 4
    result = {"id": 1, "operation": "fac", "number1": 4, "number2": None, "result": 24}
    mocker.patch('application.services.calculator.Calculator.fac', return_value=24)
    mocker.patch('application.database.DatabaseORM.save')

    response = client.get(
        f'/fac/{number_1}',
    )

    application.database.DatabaseORM.save.assert_called_once_with(result)
