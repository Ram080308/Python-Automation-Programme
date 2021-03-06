from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Womens_SummerDress_LP:
    SummerDressBanner_image_xpath = "(//img[@title='Printed Summer Dress'])[2]"
    AddtoCart_button_xpath = "(//span[text()='Add to cart'])[1]"
    ProceedToCheckout_button_xpath = "//a[@title='Proceed to checkout']"

    def __init__(self,driver):
        self.driver = driver

    def click_summerdress_image_banner(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.SummerDressBanner_image_xpath)))
        webelement = self.driver.find_element_by_xpath(self.SummerDressBanner_image_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(webelement).perform()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.AddtoCart_button_xpath)))
        self.driver.find_element_by_xpath(self.AddtoCart_button_xpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.ProceedToCheckout_button_xpath)))
        self.driver.find_element_by_xpath(self.ProceedToCheckout_button_xpath).click()




