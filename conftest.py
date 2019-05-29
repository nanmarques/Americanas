import pytest
from values.strings import BASE_URL
from selenium import webdriver


def setup():
    driver = webdriver.Firefox(executable_path="geckodriver")
    driver.get(BASE_URL)
    return driver


@pytest.fixture(scope='function')
def test_driver():
    driver_set = setup()

    yield driver_set

    teardown(driver_set)


def teardown(driver):
    driver.quit()
