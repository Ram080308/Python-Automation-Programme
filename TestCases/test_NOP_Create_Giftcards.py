from PageObjects.NOPAddNewGiftCradPage_Object import NOP_Add_New_GC
from PageObjects.NOPAdmin_HomePage_Objects import NOP_Home_Page
from PageObjects.NOPGiftCardLandingPage_Objects import Nop_Giftcard_LP
from PageObjects.NopAdmin_LoginPage_Objects import NOP_Login_Page
from Utilities.Read_Config import Read_Config_File
from Utilities import Get_Data_From_Excel
from Utilities.Database_Operations import DataBase_Operations

class Test_Create_Gift_Cards:
    class_name = (__qualname__)
    test_case_id = '6'

    bo_url = Read_Config_File.get_back_office_url()
    db_hostname = Read_Config_File.get_db_hostname()
    db_username = Read_Config_File.get_db_username()
    db_password = Read_Config_File.get_db_password()
    db_name = Read_Config_File.get_db_name()

    path = "E:\\Python_Automation_Programme\\TestData\\NopAdmin_Login.xlsx"
    sheetName = "Admin_Logins"
    email = Get_Data_From_Excel.data_from_excel(path, sheetName, 2, 1)
    password = Get_Data_From_Excel.data_from_excel(path, sheetName, 2, 2)

    gc_data_table = DataBase_Operations.items_from_db
    print(gc_data_table)

    def test_create_giftcards(self,setup):
        self.driver = setup
        self.driver = setup
        self.driver.get(self.bo_url)
        self.driver.maximize_window()

        self.login_page = NOP_Login_Page(self.driver)
        self.login_page.login_to_application(self.email, self.password)

        self.home_page = NOP_Home_Page(self.driver)
        self.home_page.click_gift_cards_link()

        self.giftcard_lp = Nop_Giftcard_LP(self.driver)
        self.giftcard_lp.click_AddNewGC_button()

        sql_query = "select * from gift_cards"
        DataBase_Operations.retrive_all_data_from_table(self.db_hostname,self.db_username,self.db_password,self.db_name,
                                                        sql_query)
        self.new_gc = NOP_Add_New_GC(self.driver)
        for items in self.gc_data_table:
            gc_type = items[0]
            gc_rec_name = items[1]
            gc_rec_email = items[2]
            gc_message = items[3]
            self.new_gc.create_gift_cards(gc_type,gc_rec_name,gc_rec_email,gc_message)

        self.driver.close()












