from selenium.webdriver.common.by import By


class LogoutPage():
    def __init__(self,driver):
        self.driver=driver
        self.menuButton=(By.XPATH, "//button[text()='Open Menu']")
        self.logoutLink=(By.LINK_TEXT, "Logout")

    def logoutAccount(self):
        self.driver.find_element(*self.menuButton).click()
        self.driver.find_element(*self.logoutLink).click()
