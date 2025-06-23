import mysql.connector 

def stream_users():
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    
    for row in cursor:
        yield row

    cursor.close()
    connection.close()
