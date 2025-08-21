import pymysql

def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",        
            password="",       
            database="bankdata"
        )
        return conn
    except Exception as e:
        print(e)

 
