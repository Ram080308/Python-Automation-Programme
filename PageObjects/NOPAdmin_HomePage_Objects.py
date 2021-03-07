from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NOP_Home_Page:

    Customers_link_xpath = "//span[text()='Customers']"
    CustomersInside_link_xpath = "(//span[text()='Customers'])[2]"
    Sales_link_xpath = "//span[text()='Sales']"
    SalesGiftCards_link_xpath = "//span[text()='Gift cards']"

    def __init__(self,driver):
        self.driver = driver

    def click_customers_link(self):
        wait = WebDriverWait(self.driver, 30)
        self.driver.find_element_by_xpath(self.Customers_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.CustomersInside_link_xpath)))
        self.driver.find_element_by_xpath(self.CustomersInside_link_xpath).click()

    def click_gift_cards_link(self):
        wait = WebDriverWait(self.driver, 30)
        self.driver.find_element_by_xpath(self.Sales_link_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.SalesGiftCards_link_xpath)))
        self.driver.find_element_by_xpath(self.SalesGiftCards_link_xpath).click()



