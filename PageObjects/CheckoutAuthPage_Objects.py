from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Checkout_Auth_Page:
    Email_Field_xpath = "//input[@id='email_create']"
    CreateAccount_button_xath = "//button[@id='SubmitCreate']"

    def __init__(self,driver):
        self.driver = driver

    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.CreateAccount_button_xath)))
        self.driver.find_element_by_xpath(self.Email_Field_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.CreateAccount_button_xath).click()


