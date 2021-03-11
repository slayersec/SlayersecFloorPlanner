#{% csrf_token %}
import mysql.connector as mysql
print("Hello!")
db_connection = mysql.connect(host="slayersec.mysql.pythonanywhere-services.com", database="testslayersecdatabase", user="slayersec", password="13146@Data")
sql = "SELECT * FROM login_table WHERE username = '$uname'  and password= '$psw'";

values = (uname,pwd)
user_cursor = db_connection.cursor()
try:
    user_cursor.execute(sql, values)
    db_connection.commit()
    user_cursor.close()
    return True
except:
    user_cursor.close()
    return False




