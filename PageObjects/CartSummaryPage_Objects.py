from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_Summary_Page:
    ContinueCheckout_button_xpath = "(//a[@title='Proceed to checkout'])[2]"

    def __init__(self,driver):
        self.driver = driver

    def click_continue_checkout_button(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.ContinueCheckout_button_xpath)))
        self.driver.find_element_by_xpath(self.ContinueCheckout_button_xpath).click()
