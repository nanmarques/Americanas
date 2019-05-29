from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Results:


    def __init__(self, driver):
        self.driver = driver

    def findElement(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def findFirstProduct(self):
        xpath = (By.XPATH, "//*[@id='content-middle']/div[5]/div/div/div/div[1]"
                           "/div[1]/div/div[2]/a/section/div[2]/div[1]/h1")
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(xpath))

    def clickFirstPesult(self):
        self.findFirstProduct().click()