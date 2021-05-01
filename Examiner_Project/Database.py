import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "kubanek",
    database = "mydata"
    )


mycursor = db.cursor()

