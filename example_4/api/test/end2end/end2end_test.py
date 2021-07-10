import pytest
from seleniumwire import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import pytest


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("localhost", 5000)

def test__app__can_sum_two_numbers_using_web_interface(httpserver):
    body = '{ "id": 1, "operation": "sum", "number1": 1, "number2": 1, "result": 2 }'
    endpoint = "/sum/1/1"
    httpserver.expect_request(endpoint).respond_with_data(body)
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--disable-web-security")
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


    chrome_driver.get('http://localhost:4200/')
    endpoint_select = Select(chrome_driver.find_element_by_id("endpoint"))
    endpoint_select.select_by_value('1')
    operation_select = Select(chrome_driver.find_element_by_id("operation"))
    operation_select.select_by_value('sum')
    input_number_1 = chrome_driver.find_element_by_id("number_1")
    input_number_1.send_keys('1')
    input_number_2 = chrome_driver.find_element_by_id("number_2")
    input_number_2.send_keys('1')
    chrome_driver.find_element_by_id("send").click()
    sleep(5)
    output_str = chrome_driver.find_element_by_id("response").text
    sleep(5)

    assert output_str == '{ "id": 1, "operation": "sum", "number1": 1, "number2": 1, "result": 2 }'
    
    sleep(2)
    chrome_driver.close()
