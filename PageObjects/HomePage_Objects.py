from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home_Page_Objects:
    SignIn_link_xpath = "//a[@class='login']"
    Signout_link_xpath = "//a[@class='logout']"

    def __init__(self,driver):
        self.driver = driver

    def click_signin_link(self):
        self.driver.find_element_by_xpath(self.SignIn_link_xpath).click()

    def click_signout_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.Signout_link_xpath)))
        self.driver.find_element_by_xpath(self.Signout_link_xpath).click()