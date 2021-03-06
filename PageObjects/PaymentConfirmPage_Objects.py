from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Payment_Confirm_Page:

    PaymentMethodBankWire_link_xpath = "//a[@title='Pay by bank wire']"
    PaymentMethodPaperCheck_link_xpath = "//a[@title='Pay by check.']"
    OrderConfirmation_button_xpath = "//span[text()='I confirm my order']"

    def __init__(self,driver):
        self.driver = driver

    def click_bankwire_payment_type(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.PaymentMethodBankWire_link_xpath)))
        self.driver.find_element_by_xpath(self.PaymentMethodBankWire_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.OrderConfirmation_button_xpath)))
        self.driver.find_element_by_xpath(self.OrderConfirmation_button_xpath).click()


    def click_papercheck_payment_type(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.PaymentMethodPaperCheck_link_xpath)))
        self.driver.find_element_by_xpath(self.PaymentMethodPaperCheck_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.OrderConfirmation_button_xpath)))
        self.driver.find_element_by_xpath(self.OrderConfirmation_button_xpath).click()