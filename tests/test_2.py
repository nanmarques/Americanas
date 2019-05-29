from pageobjects.homepage import HomeScreen
from pageobjects.results import Results
from pageobjects.product import Product
from pageobjects.insurance import Insurance
from pageobjects.cart import Cart


def test_2(test_driver):
    products = {
        'Iphone X 64gb Cinza-espacial',
        'Smartphone Samsung Galaxy A9 Preto'
    }
    for product in products:
        homepage = HomeScreen(test_driver)
        homepage.input_search(product)
        homepage.click_btn_search()
        results = Results(test_driver)
        results.clickFirstPesult()
        productPage = Product(test_driver)
        productPage.clickBuy()
        insurancePage = Insurance(test_driver)
        insurancePage.clickContinue()
        cartPage = Cart(test_driver)
        cartPage.isProductDisplayed(product)
        cartPage.clickLogo()

