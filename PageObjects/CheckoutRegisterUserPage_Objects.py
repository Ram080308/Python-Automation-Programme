from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout_RegisterUser_Page:

    Gender_radio_xpath = "(//input[@type='radio'])[1]"
    FirstName_textfield_xpath = "//input[@id='customer_firstname']"
    LastName_textfield_xpath = "//input[@id='customer_lastname']"
    Password_textfield_xpath = "//input[@id='passwd']"
    Days_dropdown_xpath = "//select[@id='days']"
    Month_dropdown_xpath = "//select[@id='months']"
    Years_dropdown_xpath = "//select[@id='years']"
    Company_textfield_xpath = "//input[@id='company']"
    Address_textfiled_xpath = "//input[@id='address1']"
    City_textfield_xpath = "//input[@id='city']"
    State_dropdown_xpath = "//select[@id='id_state']"
    Zipcode_textfield_xpath = "//input[@id='postcode']"
    Phone_textfield_xpath = "//input[@id='phone_mobile']"
    Alias_textfield_xpath = "//input[@id='alias']"
    Register_button_xpath = "//Span[text()='Register']"

    def __init__(self,driver):
        self.driver = driver

    def test_checkout_register_user(self,fn,ln,company,address,city,):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.Gender_radio_xpath)))
        self.driver.find_element_by_xpath(self.Gender_radio_xpath).click()
        self.driver.find_element_by_xpath(self.FirstName_textfield_xpath).send_keys(fn)
        self.driver.find_element_by_xpath(self.LastName_textfield_xpath).send_keys(ln)
        self.driver.find_element_by_xpath(self.Password_textfield_xpath).send_keys("Password")
        day = self.driver.find_element_by_xpath(self.Days_dropdown_xpath)
        month = self.driver.find_element_by_xpath(self.Month_dropdown_xpath)
        year = self.driver.find_element_by_xpath(self.Years_dropdown_xpath)
        sel_day = Select(day)
        sel_day.select_by_value('5')
        sel_mon = Select(month)
        sel_mon.select_by_value('4')
        sel_year = Select(year)
        sel_year.select_by_value('1986')
        self.driver.find_element_by_xpath(self.Company_textfield_xpath).send_keys(company)
        self.driver.find_element_by_xpath(self.Address_textfiled_xpath).send_keys(address)
        self.driver.find_element_by_xpath(self.City_textfield_xpath).send_keys(city)
        state = self.driver.find_element_by_xpath(self.State_dropdown_xpath)
        sel_state = Select(state)
        sel_state.select_by_visible_text('Florida')
        self.driver.find_element_by_xpath(self.Zipcode_textfield_xpath).send_keys('14110')
        self.driver.find_element_by_xpath(self.Phone_textfield_xpath).send_keys('1141452545')
        self.driver.find_element_by_xpath(self.Alias_textfield_xpath).send_keys('Mr')
        self.driver.find_element_by_xpath(self.Register_button_xpath).click()
