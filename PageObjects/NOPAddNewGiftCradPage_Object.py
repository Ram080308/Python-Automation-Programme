from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class NOP_Add_New_GC:

    GCType_select_xpath = "//select[@id='GiftCardTypeId']"
    GCCuponCode_field_xpath = "//input[@id='GiftCardCouponCode']"
    GenerateGCCode_button_xpath = "//button[@id='generateCouponCode']"
    RecepientName_field_xpath = "//input[@id='RecipientName']"
    RecepientEmail_field_xpath = "//input[@id='RecipientEmail']"
    MessageBox_filed_xpath = "//textarea[@id='Message']"
    Save_Button_xpath = "//button[@name='save']"

    global_coupon_code = ""

    def __init__(self,driver):
        self.driver = driver

    def create_gift_cards(self,gc_type, name,email,message):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.Save_Button_xpath)))
        gctype = self.driver.find_element_by_xpath(self.GCType_select_xpath)
        type = Select(gctype)
        type.select_by_visible_text(gc_type)
        self.driver.find_element_by_xpath(self.GenerateGCCode_button_xpath).click()
        cupon_code = self.driver.find_element_by_xpath(self.GCCuponCode_field_xpath).get_attribute('value')
        self.driver.find_element_by_xpath(self.RecepientName_field_xpath).send_keys(name)
        self.driver.find_element_by_xpath(self.RecepientEmail_field_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.MessageBox_filed_xpath).send_keys(message)
        self.driver.find_element_by_xpath(self.Save_Button_xpath).click()

        NOP_Add_New_GC.global_coupon_code = cupon_code

