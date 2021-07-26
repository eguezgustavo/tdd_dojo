from  application.services.calculator import Calculator
from application.repository.operations_repository import OperationsRepository
from flask.testing import FlaskClient
from flask import Flask
import application # import create_app
import pytest

@pytest.fixture()
def app(mocker) -> Flask:
    mocker.patch(
        'application.repository.operations_repository.OperationsRepository.save', 
        lambda _, x: x['result']
    )
    return application.create_app("testing")


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    with app.test_client() as c:
        return c


@pytest.fixture
def repository(client: FlaskClient):
    return OperationsRepository()
        

def test__sum_method__returns_nine__when_inputs_are_six_and_three(repository):
    number_1 = 6
    number_2 = 3

    calculator_test = Calculator(repository)
    result = calculator_test.sum(number_1, number_2)

    assert result == 9


def test__sum_method__returns_seven__when_inputs_are_four_and_three(repository):
    number_1 = 4
    number_2 = 3
    repository = OperationsRepository()

    calculator_test = Calculator(repository)
    result = calculator_test.sum(number_1, number_2)

    assert result == 7


def test__sub_method__returns_two__when_inputs_are_six_and_four(repository):
    number_1 = 6
    number_2 = 4
    repository = OperationsRepository()

    calculator_test = Calculator(repository)
    result = calculator_test.sub(number_1, number_2)

    assert result == 2


def test__sub_method__returns_seven__when_inputs_are_nine_and_two(repository):
    number_1 = 9
    number_2 = 2
    repository = OperationsRepository()

    calculator_test = Calculator(repository)
    result = calculator_test.sub(number_1, number_2)

    assert result == 7


def test__fac_method__returns_six__when_input_is_three(repository):
    number = 3

    calculator_test = Calculator(repository)
    result = calculator_test.fac(number, None)

    assert result == 6


def test__fac_method__returns_362880__when_input_is_nine(repository):
    number = 9

    calculator_test = Calculator(repository)
    result = calculator_test.fac(number, None)

    assert result == 362880
