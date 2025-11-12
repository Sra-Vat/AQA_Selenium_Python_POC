from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PracticePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(driver,10)
        self.firstName = (By.ID, "firstName")
        self.lastName = (By.ID, "lastName")
        self.mail = (By.ID, "userEmail")
        self.phoneNumber = (By.ID, "userNumber")
        self.file = (By.XPATH, "//input[@type='file']")
        self.checkboxSelection = (By.XPATH, "//div[@id='hobbiesWrapper']/div[2]/div/label")
        self.dropdownSelection = (By.XPATH, "//div[text()='{state_name}']")
        self.submitButton = (By.ID, "submit")
        self.message = (By.ID, "example-modal-sizes-title-lg")

    def enterNameAndMail(self, firstname, lastname, email):
        self.driver.find_element(*self.firstName).send_keys(firstname)
        self.driver.find_element(*self.lastName).send_keys(lastname)
        self.driver.find_element(*self.mail).send_keys(email)

    def select_gender(self,gender):
        # gender_label=self.driver.find_element(*self.gender)
        gender_label = self.driver.find_elements(By.XPATH, "//div[@id='genterWrapper']/div[2]/div/label")
        for genderselection in gender_label:
            if genderselection.text == gender:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", genderselection)
                genderselection.click()

        # self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_label)
        # gender_label.click()

    def enterMobileNumber(self, phonenumber):
        self.driver.find_element(*self.phoneNumber).send_keys(phonenumber)

    def uploadFile(self, location):
        file_upload = self.driver.find_element(*self.file)
        file_upload.send_keys(location)

    def clickCheckBox(self,hobbies_list):
        hobbies_checkbox = self.driver.find_elements(*self.checkboxSelection)
        for hobby_element in hobbies_checkbox:
            if hobby_element.text in hobbies_list:
                hobby_element.click()

    def selectStateandCity(self,state_name,city_name):
        state_dropdown = self.driver.find_element(By.ID, "state")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
        state_dropdown.click()
        state_option=self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//div[text()='{state_name}']")))
        state_option.click()
        city_dropdown=self.driver.find_element(By.ID,"city")
        city_dropdown.click()
        city_option=self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,f"//div[text()='{city_name}']")))
        city_option.click()

    def clickSubmitButton(self):
        self.driver.find_element(*self.submitButton).click()

    def validateConfirmationMessage(self,index):
        confirmation_message = self.driver.find_element(*self.message)
        print(confirmation_message.text)
        assert "Thanks" in confirmation_message.text
        self.driver.save_screenshot(f"screenshots/demoqascreenshot{index + 1}.png")