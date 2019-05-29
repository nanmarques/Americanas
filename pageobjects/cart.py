from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:

    btn_logo = (By.ID, "brd-link")

    def __init__(self, driver):
        self.driver = driver

    def findElement(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def clickLogo(self):
        self.findElement(self.btn_logo).click()

    def isProductDisplayed(self, product):
        xpath = (By.XPATH, "//a[contains(@title, '"+product+"')]")
        assert self.findElement(xpath).is_displayed()
        print("Product "+product+" is being displayed in cart")