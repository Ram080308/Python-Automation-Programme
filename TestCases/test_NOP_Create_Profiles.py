from PageObjects.NOPAddNewCustomerPage_Objects import NOP_Add_New_Customer
from PageObjects.NOPAdmin_HomePage_Objects import NOP_Home_Page
from PageObjects.NOPCustomers_LP_Objects import NOP_Customer_LP
from PageObjects.NopAdmin_LoginPage_Objects import NOP_Login_Page
from Utilities import Get_Data_From_Excel
from Utilities.Read_Config import Read_Config_File
import os
from Utilities.Database_Operations import DataBase_Operations
from GetDataFromSAP import GetCustomersData_XML


class Test_NOP_Create_Profiles:
    class_name = (__qualname__)
    test_case_id = '5'

    bo_url = Read_Config_File.get_back_office_url()

    db_hostname = Read_Config_File.get_db_hostname()
    db_username = Read_Config_File.get_db_username()
    db_password = Read_Config_File.get_db_password()
    db_name = Read_Config_File.get_db_name()

    path = "E:\\Python_Automation_Programme\\TestData\\NopAdmin_Login.xlsx"
    sheetName = "Admin_Logins"
    email = Get_Data_From_Excel.data_from_excel(path, sheetName, 2, 1)
    password = Get_Data_From_Excel.data_from_excel(path, sheetName, 2, 2)

    GetCustomersData_XML
    data_path = "E:\\Python_Automation_Programme\\TestData\\NOP_DataFromSAP.xlsx"
    data_sheet_name = "Sheet1"


    def test_create_profiles(self,setup):
        self.driver = setup
        self.driver = setup
        self.driver.get(self.bo_url)
        self.driver.maximize_window()

        self.home_page = NOP_Login_Page(self.driver)
        self.home_page.login_to_application(self.email, self.password)

        self.home_page = NOP_Home_Page(self.driver)
        self.home_page.click_customers_link()

        self.cust_lp = NOP_Customer_LP(self.driver)
        self.cust_lp.click_add_new_button()

        row_count = Get_Data_From_Excel.get_row_count(self.data_path, self.data_sheet_name)
        for items in range(2, row_count + 1):
            data_email = Get_Data_From_Excel.data_from_excel(self.data_path, self.data_sheet_name, items, 1)
            data_com_name = Get_Data_From_Excel.data_from_excel(self.data_path, self.data_sheet_name, items, 2)
            data_fn = Get_Data_From_Excel.data_from_excel(self.data_path, self.data_sheet_name, items, 3)
            data_ln = Get_Data_From_Excel.data_from_excel(self.data_path, self.data_sheet_name, items, 4)

            self.new_cust = NOP_Add_New_Customer(self.driver)
            self.new_cust.create_profiles(data_email,data_fn,data_ln,data_com_name)

            query_insert_customers = "insert into nop_customers values ('"+data_email+"','"+data_fn+"','"+data_ln+"','"+data_com_name+"')"
            DataBase_Operations.insert_records_into_db(self.db_hostname,self.db_username,self.db_password,self.db_name
                                                       ,query_insert_customers)

        db_query = "insert into test_results values ('" + self.test_case_id + "' , '" + self.class_name + "', NOW(), 'PASS')"
        print(db_query)
        DataBase_Operations.test_case_results(self.db_hostname, self.db_username, self.db_password, self.db_name,
                                              db_query)
        print("Test Case updated successfully")

        self.driver.close()
        os.remove("E:\\Python_Automation_Programme\\TestData\\NOP_DataFromSAP.xlsx")



