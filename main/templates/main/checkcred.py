#{% csrf_token %}

class login():

	print("Hello!")
    
	def __init__(self):
		import mysql.connector as mysql
		self.db_connection = mysql.connect(host="slayersec.mysql.pythonanywhere-services.com", database="testslayersecdatabase", user="slayersec", password="13146@Data")

def add_user_to_db(self,user):
        sql = "SELECT * FROM login_table WHERE username = '$uname'  and password= '$psw'";
        values = (user.username,user.password,user.email,user.email)
        user_cursor = self.db_connection.cursor()
        try:
            user_cursor.execute(sql, values)
            self.db_connection.commit()
            user_cursor.close()
            return True
        except:
            user_cursor.close()
            return False




