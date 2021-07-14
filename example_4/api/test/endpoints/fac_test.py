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

