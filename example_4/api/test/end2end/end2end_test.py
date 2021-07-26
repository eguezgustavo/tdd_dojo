from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
import pytest
import json
from time import sleep

url = 'http://172.18.0.4:4200/'


class MainPage:
    class ACTIONS:
        OPERATION = '1'
        HISTORY = '2'
    
    class OPERATIONS:
        SUM = 'sum'
        SUB = 'sub'
        FAC = 'fac'

    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.driver.get(url)

    def __set_select_by_id(self, id, value) -> None:
        operation_select = Select(self.driver.find_element_by_id(id))
        operation_select.select_by_value(value)
    
    def __enter_text_by_id(self, id, value) -> None:
        input_number_1 = self.driver.find_element_by_id(id)
        input_number_1.send_keys(value)
    
    def __click_on_buttom_by_id(self, id) -> None:
        self.driver.find_element_by_id(id).click()
    
    def __get_text_of_element_by_id(self, element) -> str:
        sleep(5)
        response = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(((By.ID, element)))
        )
        return json.loads(response.text)

    def set_action(self, action_type: str):
        self.__set_select_by_id('action', action_type)

    def set_operation(self, operation_type: str):
        self.__set_select_by_id('operation', operation_type)

    def set_number_1(self, number: int):
        self.__enter_text_by_id('number_1', number)
    
    def set_number_2(self, number: int):
        self.__enter_text_by_id('number_2', number)
    
    def set_id(self, number: int):
        self.__enter_text_by_id('id', number)

    def send_request(self):
        self.__click_on_buttom_by_id('send')

    def get_response(self):
        return self.__get_text_of_element_by_id('response')


@pytest.fixture(scope="session")
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--disable-web-security")
    _chrome_driver = webdriver.Remote(
            command_executor='http://172.18.0.5:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options
            )
    yield _chrome_driver
    _chrome_driver.quit()


def test__app__can_sum_two_numbers_using__web_interface(chrome_driver):

    page = MainPage(chrome_driver, url)
    page.set_action(MainPage.ACTIONS.OPERATION)
    page.set_operation(MainPage.OPERATIONS.SUM)
    page.set_number_1(1)
    page.set_number_2(1)
    page.send_request()
    output_str = page.get_response()

    assert output_str["result"] == 2


def test__app__can_subctract_two_numbers__using_web_interface(chrome_driver):

    page = MainPage(chrome_driver, url)
    page.set_action(MainPage.ACTIONS.OPERATION)
    page.set_operation(MainPage.OPERATIONS.SUB)
    page.set_number_1(2)
    page.set_number_2(1)
    page.send_request()
    output_str = page.get_response()

    assert output_str["result"] == 1


def test__app__can_return_the_factorial__using_web_interface(chrome_driver):

    page = MainPage(chrome_driver, url)
    page.set_action(MainPage.ACTIONS.OPERATION)
    page.set_operation(MainPage.OPERATIONS.FAC)
    page.set_number_1(3)
    page.send_request()
    output_str = page.get_response()

    assert output_str["result"] == 6


def test__app__can_return_stored_operation__using_web_interface(chrome_driver):
    
    page = MainPage(chrome_driver, url)
    page.set_action(MainPage.ACTIONS.HISTORY)
    page.set_id(1)
    page.send_request()
    output_str = page.get_response()

    print(output_str)

    assert output_str["id"] == 1
