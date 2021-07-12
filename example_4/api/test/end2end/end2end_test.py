from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest


url = 'http://localhost:4200/'


class BasePage(object):
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.driver.get(url)

    def set_select_by_id(self, id, value) -> None:
        operation_select = Select(self.driver.find_element_by_id(id))
        operation_select.select_by_value(value)

    def enter_text_by_id(self, id, value) -> None:
        input_number_1 = self.driver.find_element_by_id(id)
        input_number_1.send_keys(value)

    def click_on_buttom_by_id(self, id) -> None:
        self.driver.find_element_by_id(id).click()

    def get_text_of_element_by_id(self, element) -> str:
        response = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(((By.ID, element)))
        )
        return response.text


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("localhost", 5000)


@pytest.fixture(scope="session")
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--disable-web-security")
    _chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield _chrome_driver
    _chrome_driver.quit()


def test__app__can_sum_two_numbers_using__web_interface(httpserver, chrome_driver):
    body = '{ "id": 1, "operation": "sum", "number1": 1, "number2": 1, "result": 2 }'
    endpoint = "/sum/1/1"
    httpserver.expect_request(endpoint).respond_with_data(body)

    page = BasePage(chrome_driver, url)
    page.set_select_by_id('endpoint', '1')
    page.set_select_by_id('operation', 'sum')
    page.enter_text_by_id('number_1', '1')
    page.enter_text_by_id('number_2', '1')
    page.click_on_buttom_by_id('send')
    output_str = page.get_text_of_element_by_id('response')

    assert output_str == '{ "id": 1, "operation": "sum", "number1": 1, "number2": 1, "result": 2 }'


def test__app__can_subctract_two_numbers__using_web_interface(httpserver, chrome_driver):
    body = '{ "id": 1, "operation": "sub", "number1": 2, "number2": 1, "result": 1 }'
    endpoint = "/sub/2/1"
    httpserver.expect_request(endpoint).respond_with_data(body)

    page = BasePage(chrome_driver, url)
    page.set_select_by_id('endpoint', '1')
    page.set_select_by_id('operation', 'sub')
    page.enter_text_by_id('number_1', '2')
    page.enter_text_by_id('number_2', '1')
    page.click_on_buttom_by_id('send')
    output_str = page.get_text_of_element_by_id('response')

    assert output_str == '{ "id": 1, "operation": "sub", "number1": 2, "number2": 1, "result": 1 }'


def test__app__can_return_the_factorial__using_web_interface(httpserver, chrome_driver):
    body = '{ "id": 1, "operation": "fac", "number1": 3, "number2": null, "result": 6 }'
    endpoint = "/fac/3"
    httpserver.expect_request(endpoint).respond_with_data(body)

    page = BasePage(chrome_driver, url)
    page.set_select_by_id('endpoint', '1')
    page.set_select_by_id('operation', 'fac')
    page.enter_text_by_id('number_1', '3')
    page.click_on_buttom_by_id('send')
    output_str = page.get_text_of_element_by_id('response')

    assert output_str == '{ "id": 1, "operation": "fac", "number1": 3, "number2": null, "result": 6 }'


def test__app__can_return_stored_operation__using_web_interface(httpserver, chrome_driver):
    body = '{ "id": 1, "operation": "sub", "number1": 2, "number2": 1, "result": 1 }'
    endpoint = "/1"
    httpserver.expect_request(endpoint).respond_with_data(body)

    page = BasePage(chrome_driver, url)
    page.set_select_by_id('endpoint', '2')
    page.enter_text_by_id('id', '1')
    page.click_on_buttom_by_id('send')
    output_str = page.get_text_of_element_by_id('response')

    assert output_str == '{ "id": 1, "operation": "sub", "number1": 2, "number2": 1, "result": 1 }'
