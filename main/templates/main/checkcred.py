#{% csrf_token %}

class login():

	print("Hello!")
    
	def __init__(self):
        import mysql.connector as mysql
        from backend.db_connection import db_connection
        parent_db = db_connection()
        self.db_connection = mysql.connect(host=parent_db.HOST, database=parent_db.DATABASE, user=parent_db.USER, password=parent_db.PASSWORD)

def add_user_to_db(self,user):
        sql = "INSERT INTO login (username,password,email,AddedBy) VALUES (%s, %s, %s, %s)"
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




