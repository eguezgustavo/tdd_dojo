from flask.testing import FlaskClient
from flask_restx._http import HTTPStatus
from flask import Flask
import application

import pytest


@pytest.fixture()
def app(mocker) -> Flask:
    mocker.patch('application.services.calculator.Calculator.fac', return_value=1)
    return application.create_app("testing")


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    with app.test_client() as c:
        return c
        

def test__reports_endpoint__should_return_200__when_correct_id_is_send(client: FlaskClient):
    id = 1

    response = client.get(
        f'/{id}',
    )

    assert HTTPStatus.OK == response.status_code

