import json
import pytest


from PageObjects.practicePage import PracticePage


def load_testdata():
    with open("demoqadata.json") as f:
        return json.load(f)["data"]


def get_base_url():
    with open("demoqadata.json") as f:
        return json.load(f)["baseUrl"]


@pytest.mark.parametrize("data", load_testdata())
def test_demoqa(browserInstance, data):
    driver = browserInstance
    base_url=get_base_url()
    driver.get(base_url)
    practicePage = PracticePage(driver)
    practicePage.enterNameAndMail(data["firstname"], data["lastname"], data["emailId"])
    practicePage.select_gender(data["gender"])
    practicePage.enterMobileNumber(data["phonenumber"])
    practicePage.uploadFile(data["filelocation"])
    practicePage.clickCheckBox(data["hobbies"])
    practicePage.selectStateandCity(data["state"], data["city"])
    practicePage.clickSubmitButton()

    index = load_testdata().index(data)
    practicePage.validateConfirmationMessage(index)
