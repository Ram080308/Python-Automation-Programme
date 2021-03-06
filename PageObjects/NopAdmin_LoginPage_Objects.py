from selenium import webdriver


class NOP_Login_Page:

    Email_field_xpath = "//input[@id='Email']"
    Password_file_xpath = "//input[@id='Password']"
    Login_button_xpath = "//input[@value='Log in']"

    def __init__(self,driver):
        self.driver = driver

    def login_to_application(self, un, pw):
        self.driver.find_element_by_xpath(self.Email_field_xpath).clear()
        self.driver.find_element_by_xpath(self.Email_field_xpath).send_keys(un)
        self.driver.find_element_by_xpath(self.Password_file_xpath).clear()
        self.driver.find_element_by_xpath(self.Password_file_xpath).send_keys(pw)
        self.driver.find_element_by_xpath(self.Login_button_xpath).click()

