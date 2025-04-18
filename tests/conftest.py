from xml.dom.xmlbuilder import Options

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def setup_and_teardown(request):
    #chrome_options=Options()
    #chrome_options.add_argument()
    #driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",options=chrome_options)
    driver=webdriver.Chrome()
    driver.get("https://www.beelivery.com/#")
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.close()