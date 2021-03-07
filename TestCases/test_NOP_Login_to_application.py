from PageObjects.NopAdmin_LoginPage_Objects import NOP_Login_Page
from Utilities.Read_Config import Read_Config_File
from Utilities.Database_Operations import DataBase_Operations
from selenium import webdriver
from Utilities import Get_Data_From_Excel
#driver = webdriver.Chrome()


class Test_Login_to_NOP_Admin:
    class_name = (__qualname__)
    test_case_id = '4'

    bo_url = Read_Config_File.get_back_office_url()

    db_hostname = Read_Config_File.get_db_hostname()
    db_username = Read_Config_File.get_db_username()
    db_password = Read_Config_File.get_db_password()
    db_name = Read_Config_File.get_db_name()

    path = "E:\\Python_Automation_Programme\\TestData\\NopAdmin_Login.xlsx"
    sheetName = "Admin_Logins"

    email = Get_Data_From_Excel.data_from_excel(path, sheetName, 2,1)
    password = Get_Data_From_Excel.data_from_excel(path,sheetName, 2,2)

    def test_login_nop_admin(self,setup):
        self.driver = setup
        self.driver.get(self.bo_url)
        self.driver.maximize_window()

        self.home_page = NOP_Login_Page(self.driver)
        self.home_page.login_to_application(self.email,self.password)

        if (self.driver.find_element_by_xpath("//a[text()='Logout']").is_displayed()):
            sql_query = "insert into test_results values ('"+self.test_case_id+"' , '"+self.class_name+"', " \
                                                          "NOW(), 'PASS')"
            DataBase_Operations.test_case_results(self.db_hostname,self.db_username,self.db_password,self.db_name,
                                                  sql_query)
            print("Record Inserted!")

        else:
            sql_query = "insert into test_results values ('" + self.test_case_id + "' , '" + self.class_name + "', " \
                                                          "NOW(), 'FAIL')"
            DataBase_Operations.test_case_results(self.db_hostname, self.db_username, self.db_password,self.db_name,
                                                  sql_query)
        self.driver.close()





