from flask.testing import FlaskClient
from flask_restx._http import HTTPStatus
from flask import Flask
import application # import create_app

import pytest
import json


@pytest.fixture()
def app(mocker) -> Flask:
    mocker.patch('application.services.calculator.Calculator.sum', return_value=1)
    return application.create_app("testing")


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


def test__sum_endpoint__should_return_correct_result__when_1_and_2_are_send(client: FlaskClient, mocker):
    number_1 = 1
    number_2 = 2
    result = {"id": 1, "operation": "sum", "number1": 1, "number2": 2, "result": 3}
    mocker.patch('application.services.calculator.Calculator.sum', return_value=3)

    response = client.get(
        f'/sum/{number_1}/{number_2}',
    )

    assert HTTPStatus.OK == response.status_code
    assert result == json.loads(response.get_data())


def test__sum_endpoint__should_return_correct_result__when_5_and_7_are_send(client: FlaskClient, mocker):
    number_1 = 5
    number_2 = 7
    result = {"id": 1, "operation": "sum", "number1": 5, "number2": 7, "result": 12}
    mocker.patch('application.services.calculator.Calculator.sum', return_value=12)

    response = client.get(
        f'/sum/{number_1}/{number_2}',
    )

    assert HTTPStatus.OK == response.status_code
    assert result == json.loads(response.get_data())
