from flask.testing import FlaskClient
from flask_restx._http import HTTPStatus
from flask import Flask
import sqlalchemy
import application

import pytest


@pytest.fixture()
def app() -> Flask:
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


def test__reports_endpoint__should_return_404__when_incorrect_id_is_send(client: FlaskClient):
    id = 'a'

    response = client.get(
        f'/{id}',
    )

    assert HTTPStatus.NOT_FOUND == response.status_code


def test__reports_endpoint__should_query_in_bd__when_id_is_send(client: FlaskClient, mocker):
    mocker.patch(
        'application.database.DatabaseORM.query_by_id', return_value = {"id": 1, "operation": "fac", "number1": 3, "number2": None, "result": 6}
    )
    id = 1

    response = client.get(
        f'/{id}',
    )

    assert response.json == {"id": 1, "operation": "fac", "number1": 3, "number2": None, "result": 6}
