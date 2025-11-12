import json

import pytest

from PageObjects.cartPage import CartPage
from PageObjects.confirmationPage import ConfirmationPage
from PageObjects.loginPage import LoginPage
from PageObjects.logoutPage import LogoutPage
from PageObjects.productsPage import ProductsPage
from PageObjects.checkoutPage import CheckoutPage


def load_testdata():
    with open("saucedemodata.json") as f:
        return json.load(f)["data"]


def get_base_url():
    with open("saucedemodata.json") as f:
        return json.load(f)["baseUrl"]


@pytest.mark.parametrize("data", load_testdata())
def test_saucedemo(browserInstance, data):
    driver = browserInstance
    base_url = get_base_url()
    driver.get(base_url)
    loginPage = LoginPage(driver)
    productsPage = ProductsPage(driver)
    cartPage = CartPage(driver)
    checkoutPage = CheckoutPage(driver)
    confirmationPage = ConfirmationPage(driver)
    logoutPage = LogoutPage(driver)
    loginPage.enterUsernameAndPassword(data["username"], data["password"])
    loginPage.clickLoginButton()
    addtocartproducts_length = productsPage.addToCartProducts()
    productsPage.clickOnCartIcon()
    items_length = cartPage.cartItems()
    assert items_length == addtocartproducts_length
    cartPage.clickCheckoutButton()
    checkoutPage.checkoutInformation(data["firstname"], data["lastname"], data["postalcode"])
    checkoutPage.shippingItems()
    confirmation_message = confirmationPage.confirmationMessage()
    assert "Thank you" in confirmation_message.text
    logoutPage.logoutAccount()
