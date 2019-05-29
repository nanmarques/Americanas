from pageobjects.homepage import HomeScreen
from pageobjects.sign_up import SignUp
from values.generate_cpf import cpf_funcional
import values.strings


def test_1(test_driver):
    # Este teste simula a criação de uma conta, porém, devido ao captcha solicitado pela
    # Americanas, não é possível completar

    cpf = cpf_funcional()
    homepage = HomeScreen(test_driver)
    homepage.is_search_input_present()
    homepage.is_user_icon_present()
    homepage.click_user_icon()
    homepage.click_user_sign_up()
    signup = SignUp(test_driver)
    signup.input_email(values.strings.person_data['EMAIL'])
    signup.input_password(values.strings.person_data['PASSWORD'])
    signup.input_cpf(cpf)
    signup.input_name(values.strings.person_data['NAME'])
    signup.input_birthday(values.strings.person_data['BIRTHDAY'])
    signup.click_gender_M()
    signup.input_phone_input(values.strings.person_data['PHONE'])
    signup.click_submit()

