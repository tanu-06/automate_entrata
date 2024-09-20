import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup(request):
    """
    Opens the URL and return the driver
    """
    driver = webdriver.Chrome()
    driver.get("https://www.entrata.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//a[@id='cookie-decline']").click()
    yield driver
    driver.close()
