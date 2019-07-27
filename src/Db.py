import mysql.connector
user = "root"
password = "pass"
host = "mysql"
port = 3306
database = "mendako"

def connect():
    return mysql.connector.connect(
        user = user,
        password = password,
        host = host,
        port=3306, database = database
        )