from selenium.webdriver.common.by import By


class ProductsPage():
    def __init__(self, driver):
        self.driver = driver
        self.allproducts = (By.XPATH, "//button[text()='Add to cart']")
        self.cart = (By.CLASS_NAME, "shopping_cart_link")

    def addToCartProducts(self):
        products = self.driver.find_elements(*self.allproducts)
        for product in products:
            product.click()
        return len(products)

    def clickOnCartIcon(self):
        self.driver.find_element(*self.cart).click()
