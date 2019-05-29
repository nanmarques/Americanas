from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeScreen:

    user_sign_up = (By.CLASS_NAME, 'usr-signup')
    search_input = (By.ID, "h_search-input")
    user_icon = (By.ID, "h_usr-link")
    btn_search = (By.ID, "h_search-btn")


    def __init__(self, driver):
        self.driver = driver

    def findElement(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def is_search_input_present(self):
        return self.findElement(self.search_input).is_displayed()

    def is_user_icon_present(self):
        return self.findElement(self.user_icon).is_displayed()

    def click_user_icon(self):
        self.findElement(self.user_icon).click()

    def click_user_sign_up(self):
        self.findElement(self.user_sign_up).click()

    def click_btn_search(self):
        self.findElement(self.btn_search).click()

    def input_search(self, search):
        self.findElement(self.search_input).send_keys(search)

