import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse("E:\Python_Automation_Programme\GetDataFromSAP\CustomerInfoFromSAP.xml")
root = tree.getroot()

all_emails = []
all_cmpany = []
all_firstnames = []
all_lastnames = []

for items in root.iter():
    if items.tag == "Email":
        email = items.text
        all_emails.append(email)
    elif items.tag == "CompanyName":
        companyname = items.text
        all_cmpany.append(companyname)
    elif items.tag == "FirstName":
        firstname = items.text
        all_firstnames.append(firstname)
    elif items.tag == "LastName":
        lastnames = items.text
        all_lastnames.append(lastnames)

data_frame = pd.DataFrame([all_emails , all_cmpany, all_firstnames, all_lastnames]).transpose()
data_frame.to_excel("E:\\Python_Automation_Programme\\TestData\\NOP_DataFromSAP.xlsx", index=0, header=['Email',
                    'Company Name', 'First Name', 'Last Name'])

