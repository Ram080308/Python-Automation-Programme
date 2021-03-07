from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Shipping_Confirm_Page:

    TermsAndCond_checkbox_xpath = "//input[@type='checkbox']"
    CheckoutShip_button_xpath = "//button[@name='processCarrier']"

    def __init__(self,driver):
        self.driver=driver

    def click_ship_conf(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.CheckoutShip_button_xpath)))
        self.driver.find_element_by_xpath(self.TermsAndCond_checkbox_xpath).click()
        self.driver.find_element_by_xpath(self.CheckoutShip_button_xpath).click()
