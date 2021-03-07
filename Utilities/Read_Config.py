import configparser

parser = configparser.RawConfigParser()
parser.read("E:\Python_Automation_Programme\ConfigFile\config_file.ini")

class Read_Config_File:
    @staticmethod
    def get_url():
        url = parser.get("Web url", "url")
        return url

    @staticmethod
    def get_json_end_point_url():
        json_endpoint_url = parser.get("End Point urls" , "user_details")
        return json_endpoint_url

    @staticmethod
    def get_db_hostname():
        db_hostname = parser.get("Datebase details" , "host_name")
        return db_hostname

    @staticmethod
    def get_db_username():
        db_username = parser.get("Datebase details", "db_user_name")
        return db_username

    @staticmethod
    def get_db_password():
        db_pass = parser.get("Datebase details", "db_password")
        return db_pass

    @staticmethod
    def get_db_name():
        db_name = parser.get("Datebase details", "db_name")
        return db_name

    @staticmethod
    def get_back_office_url():
        bo_url = parser.get("Nop Admin details" , "bo_url")
        return bo_url




