from selenium.webdriver.common.by import By


class CartPage():
    def __init__(self,driver):
        self.driver=driver
        self.checkoutButton=(By.ID, "checkout")
        self.items=(By.XPATH,"//div[@class='cart_item']")

    def cartItems(self):
        elements=self.driver.find_elements(*self.items)
        return len(elements)

    def clickCheckoutButton(self):
        self.driver.find_element(*self.checkoutButton).click()