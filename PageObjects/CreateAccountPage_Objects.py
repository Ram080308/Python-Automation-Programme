from selenium import webdriver

class Create_Account_Page_Objects:
    EmailAddress_Textbox_xpath = "//input[@id='email_create']"
    CreateAccount_butoon_xpath = "//i[@class='icon-user left']"

    def __init__(self,driver):
        self.driver = driver

    def test_enter_email(self,email):
        self.driver.find_element_by_xpath(self.EmailAddress_Textbox_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.CreateAccount_butoon_xpath).click()
