import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Nani@1234",
        database = "management"
    )
    return connection
print("Successfully connection established")
