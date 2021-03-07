import requests
import pandas as pd
from Utilities.Read_Config import Read_Config_File

class Get_Data_From_SAP:

    @staticmethod
    def get_data_from_json_to_excel():
        json_url = Read_Config_File.get_json_end_point_url()
        response = requests.get(json_url)
        cust_data = response.json()
        length_cust_data = len(cust_data)
        all_first_names = []
        all_last_names = []
        all_emails = []
        all_address = []
        all_cities = []
        all_companies = []
        for values in range(length_cust_data):
            first_name = cust_data[values]['name']
            all_first_names.append(first_name)
            last_name = cust_data[values]['username']
            all_last_names.append(last_name)
            emails = cust_data[values]['email']
            all_emails.append(emails+'nopj')
            street_name = cust_data[values]['address']['street']
            suite_name = cust_data[values]['address']['suite']
            address = street_name + " , " + suite_name
            all_address.append(address)
            city = cust_data[values]['address']['city']
            all_cities.append(city)
            company = cust_data[values]['company']['name']
            all_companies.append(company)
        data_frame = pd.DataFrame([all_emails , all_first_names, all_first_names, all_address, all_cities, all_companies ]).transpose()
        data_frame.to_excel("E:\Python_Automation_Programme\TestData\DataFromSAP.xlsx", index=0,
                            header=['Email','First Name','Last Name','Address' ,'City' ,'Company'])





