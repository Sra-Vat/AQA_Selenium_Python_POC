from selenium.webdriver.common.by import By


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.firstName = (By.NAME, "firstName")
        self.lastName = (By.ID, "last-name")
        self.postalcode=(By.ID, "postal-code")
        self.continueButton=(By.ID, "continue")

    def checkoutInformation(self,firstname,lastname,postalcode):
        self.driver.find_element(*self.firstName).send_keys(firstname)
        self.driver.find_element(*self.lastName).send_keys(lastname)
        self.driver.find_element(*self.postalcode).send_keys(postalcode)
        self.driver.find_element(*self.continueButton).click()

    def shippingItems(self):
        self.driver.find_element(By.ID, "finish").click()
