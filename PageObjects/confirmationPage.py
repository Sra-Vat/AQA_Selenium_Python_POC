from selenium.webdriver.common.by import By


class ConfirmationPage():
    def __init__(self, driver):
        self.driver = driver
        self.message = (By.XPATH, "//h2[text()='Thank you for your order!']")

    def confirmationMessage(self):
        confirmation_message = self.driver.find_element(*self.message)
        return confirmation_message
