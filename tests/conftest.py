from xml.dom.xmlbuilder import Options

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup_and_teardown(request):
    #chrome_options=Options()
    #chrome_options.add_argument()
    #driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",options=chrome_options)

    service = Service(executable_path="C:\Proveway\pythonProject3\driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=service)
    driver.get("https://www.beelivery.com/#")
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.close()