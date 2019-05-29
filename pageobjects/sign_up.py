from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUp:

    email_input = (By.ID, 'email-input')
    password_input = (By.ID, "password-input")
    cpf_input = (By.ID, "cpf-input")
    gender_M = (By.XPATH, "//*[@id='gender']/div[1]/label")
    phone_input = (By.ID, "phone-input")
    name_input = (By.ID, "name-input")
    birthday_input = (By.ID, "birthday-input")
    submit_button = (By.XPATH, "//*[@id='root']/div/div[2]/form/button")

    def __init__(self, driver):
        self.driver = driver

    def findElement(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def input_email(self, email):
        self.findElement(self.email_input).send_keys(email)

    def input_name(self, name):
        self.findElement(self.name_input).send_keys(name)

    def input_password(self, password):
        self.findElement(self.password_input).send_keys(password)

    def input_cpf(self, cpf):
        self.findElement(self.cpf_input).send_keys(cpf)

    def click_gender_M(self):
        self.findElement(self.gender_M).click()

    def input_phone_input(self,  phone):
        self.findElement(self.phone_input).send_keys(phone)

    def input_birthday(self, birthday):
        self.findElement(self.birthday_input).send_keys(birthday)

    def click_submit(self):
        self.findElement(self.submit_button).click()