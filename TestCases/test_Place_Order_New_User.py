from GetDataFromSAP.GetCustomersData_json import Get_Data_From_SAP
from PageObjects.CartSummaryPage_Objects import Cart_Summary_Page
from PageObjects.CheckoutAddressConfirmPage_Objects import Checkout_Address_Confirm_Page
from PageObjects.CheckoutAuthPage_Objects import Checkout_Auth_Page
from PageObjects.CheckoutRegisterUserPage_Objects import Checkout_RegisterUser_Page
from PageObjects.HomePage_Objects import Home_Page_Objects
from PageObjects.PaymentConfirmPage_Objects import Payment_Confirm_Page
from PageObjects.ShippingConfirmPage_Objects import Shipping_Confirm_Page
from PageObjects.WomenSummerDressesLP_Objects import Womens_SummerDress_LP
from Utilities.Read_Config import Read_Config_File
from Utilities.Database_Operations import DataBase_Operations



class Test_Place_Order_New_User:
    class_name = (__qualname__)
    test_case_id = '2'

    Get_Data_From_SAP.get_data_from_json_to_excel()

    url = Read_Config_File.get_url()
    db_hostname = Read_Config_File.get_db_hostname()
    db_username = Read_Config_File.get_db_username()
    db_password = Read_Config_File.get_db_password()
    db_name = Read_Config_File.get_db_name()

    def test_place_new_order(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)

        self.home_page = Home_Page_Objects(self.driver)
        self.home_page.click_summerdress_tab()

        self.womens_dress_lp = Womens_SummerDress_LP(self.driver)
        self.womens_dress_lp.click_summerdress_image_banner()

        self.cart_summary = Cart_Summary_Page(self.driver)
        self.cart_summary.click_continue_checkout_button()

        self.chkout_auth = Checkout_Auth_Page(self.driver)
        self.chkout_auth.enter_email("mytestqa7@gmail.com")

        self.chkout_register = Checkout_RegisterUser_Page(self.driver)
        self.chkout_register.test_checkout_register_user("Ram","Chigari","ITC","Vijaynagar","Bangalore")

        self.chk_address = Checkout_Address_Confirm_Page(self.driver)
        self.chk_address.click_proceed_to_chkout_address()

        self.ship_conf = Shipping_Confirm_Page(self.driver)
        self.ship_conf.click_ship_conf()

        self.payment_confirm = Payment_Confirm_Page(self.driver)
        self.payment_confirm.click_papercheck_payment_type()

        message = self.driver.find_element_by_xpath("//p[text()='Your order on My Store is complete.']").text
        if message == "Your order on My Store is complete.":
            db_query = "insert into test_results values ('" + self.test_case_id + "' , '" + self.class_name + "', NOW(), 'PASS')"
            DataBase_Operations.test_case_results(self.db_hostname, self.db_username, self.db_password, self.db_name,
                                                  db_query)
            print("Test Case updated successfully")

            self.driver.close()



