from flask.testing import FlaskClient
from flask_restx._http import HTTPStatus
from flask import Flask
import application

import pytest


@pytest.fixture()
def app() -> Flask:
    return application.create_app("testing")


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    with app.test_client() as c:
        return c
        

def test__sub_endpoint__should_return_200__when_correct_parameters_are_send(client: FlaskClient):
    number_1 = 1
    number_2 = 1

    response = client.get(
        f'/sub/{number_1}/{number_2}',
    )

    assert HTTPStatus.OK == response.status_code
