import mysql.connector as connector

class DataBase_Operations:

    items_from_db = ()

    @staticmethod
    def test_case_results(hostname, db_un, db_password, db_name, db_query):
        db_connection = connector.connect(host=hostname,username=db_un,passwd=db_password)
        db_cursor = db_connection.cursor()
        db_cursor.execute("use "+db_name)
        db_cursor.execute(db_query)
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def insert_records_into_db(hostname, db_un, db_password, db_name, db_query):
        db_connection = connector.connect(host=hostname, username=db_un, passwd=db_password)
        db_cursor = db_connection.cursor()
        db_cursor.execute("use " + db_name)
        db_cursor.execute(db_query)
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def retrive_all_data_from_table(hostname, db_un, db_password, db_name, db_query):
        db_connection = connector.connect(host=hostname, username=db_un, passwd=db_password)
        db_cursor = db_connection.cursor()
        db_cursor.execute("use " + db_name)
        db_cursor.execute(db_query)
        all_data = db_cursor.fetchall()
        print(all_data)
        DataBase_Operations.items_from_db = all_data
        db_connection.commit()
        db_connection.close()


