from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product:

    btn_buy = (By.ID, "btn-buy")

    def __init__(self, driver):
        self.driver = driver

    def findElement(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def clickBuy(self):
        self.findElement(self.btn_buy).click()