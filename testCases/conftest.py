import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path='C:/Drivers/ChromeDriver 102.0.5005.61/chromedriver')
    return driver
