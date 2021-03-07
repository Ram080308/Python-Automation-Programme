from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Checkout_Address_Confirm_Page:
    ProceedToChkout_button_xpath = "//span[text()='Proceed to checkout']"

    def __init__(self,driver):
        self.driver = driver

    def click_proceed_to_chkout_address(self):
        wait = WebDriverWait(self.driver,30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.ProceedToChkout_button_xpath)))
        self.driver.find_element_by_xpath(self.ProceedToChkout_button_xpath).click()


