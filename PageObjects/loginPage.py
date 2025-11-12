from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.loginbutton = (By.XPATH, "//input[@type='submit']")

    def enterUsernameAndPassword(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(*self.loginbutton).click()

