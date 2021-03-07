from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Home_Page_Objects:
    SignIn_link_xpath = "//a[@class='login']"
    Signout_link_xpath = "//a[@class='logout']"
    Dresses_tab_xpath = "(//a[@title='Dresses'])[2]"
    SummerDresses_tab_xpath = "(//a[@title='Summer Dresses'])[2]"


    def __init__(self,driver):
        self.driver = driver

    def click_signin_link(self):
        self.driver.find_element_by_xpath(self.SignIn_link_xpath).click()

    def click_signout_link(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.Signout_link_xpath)))
        self.driver.find_element_by_xpath(self.Signout_link_xpath).click()

    def click_summerdress_tab(self):
        dress_tab = self.driver.find_element_by_xpath(self.Dresses_tab_xpath)
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 30)
        actions.move_to_element(dress_tab).perform()
        wait.until(EC.element_to_be_clickable((By.XPATH, self.SummerDresses_tab_xpath)))
        self.driver.find_element_by_xpath(self.SummerDresses_tab_xpath).click()
