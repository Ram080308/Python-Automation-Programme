from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class NOP_Add_New_Customer:

    Email_field_xpath = "//input[@id='Email']"
    FirstName_field_xpath = "//input[@id='FirstName']"
    LastName_field_xpath = "//input[@id='LastName']"
    Company_filed_xpath = "//input[@id='Company']"
    Save_button_xpath = "//button[@name='save']"
    Add_button_xpath = "//a[@class='btn bg-blue']"

    def __init__(self,driver):
        self.driver = driver

    def create_profiles(self, email, fn,ln,cn):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.Save_button_xpath)))
        self.driver.find_element_by_xpath(self.Email_field_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.FirstName_field_xpath).send_keys(fn)
        self.driver.find_element_by_xpath(self.LastName_field_xpath).send_keys(ln)
        self.driver.find_element_by_xpath(self.Company_filed_xpath).send_keys(cn)
        self.driver.find_element_by_xpath(self.Save_button_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.Add_button_xpath)))
        self.driver.find_element_by_xpath(self.Add_button_xpath).click()

