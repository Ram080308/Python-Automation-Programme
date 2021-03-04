from PageObjects.HomePage_Objects import Home_Page_Objects
from Utilities.Read_Config import Read_Config_File
from GetDataFromSAP.GetCustomersData_json import Get_Data_From_SAP
from PageObjects.CreateAccountPage_Objects import Create_Account_Page_Objects
from Utilities import Get_Data_From_Excel
from PageObjects.RegisterUserPage_Objects import Register_User_Page_Objects
from Utilities.Database_Operations import DataBase_Operations
import os

class Test_CreateProfiles:

    class_name = (__qualname__)
    test_case_id = '1'

    Get_Data_From_SAP.get_data_from_json_to_excel()

    url = Read_Config_File.get_url()
    db_host_name = Read_Config_File.get_db_hostname()
    db_user_name = Read_Config_File.get_db_username()
    db_password = Read_Config_File.get_db_password()
    db_name = Read_Config_File.get_db_name()


    excel_file_path = "E:\Python_Automation_Programme\TestData\DataFromSAP.xlsx"

    sheet_name = "Sheet1"
    rows = Get_Data_From_Excel.get_row_count(excel_file_path, sheet_name)
    cols = Get_Data_From_Excel.get_col_count(excel_file_path, sheet_name)

    def test_create_discounts(self, setup):
            for row_nums in range(2, self.rows):
                print(row_nums)
                self.driver = setup
                self.driver.maximize_window()
                self.driver.get(self.url)
                self.home_page = Home_Page_Objects(self.driver)
                self.home_page.click_signin_link()

                email = Get_Data_From_Excel.data_from_excel(self.excel_file_path, self.sheet_name, row_nums, 1)
                print(email)
                first_name = Get_Data_From_Excel.data_from_excel(self.excel_file_path, self.sheet_name, row_nums, 2)
                last_name = Get_Data_From_Excel.data_from_excel(self.excel_file_path, self.sheet_name, row_nums, 3)
                address = Get_Data_From_Excel.data_from_excel(self.excel_file_path, self.sheet_name, row_nums, 4)
                city = Get_Data_From_Excel.data_from_excel(self.excel_file_path, self.sheet_name, row_nums, 5)
                company = Get_Data_From_Excel.data_from_excel(self.excel_file_path, self.sheet_name, row_nums, 5)

                self.create_account_page = Create_Account_Page_Objects(self.driver)
                self.create_account_page.test_enter_email(email)

                self.registration_page = Register_User_Page_Objects(self.driver)
                self.registration_page.test_register_user(first_name,last_name,company,address,city)
                self.home_page.click_signout_link()

            db_query = "insert into test_results values ('"+self.test_case_id+"' , '"+self.class_name+"', NOW(), 'PASS')"
            print(db_query)
            DataBase_Operations.test_case_results(self.db_host_name,self.db_user_name,self.db_password,self.db_name,
                                                  db_query)
            print("Test Case updated successfully")

            self.driver.close()
            os.remove("E:\Python_Automation_Programme\TestData\DataFromSAP.xlsx")




