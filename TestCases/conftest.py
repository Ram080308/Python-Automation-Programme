import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="E:\Python_Automation_Programme\BrowserDrivers\chromedriver.exe")
    return driver

