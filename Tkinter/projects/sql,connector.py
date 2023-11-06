import mysql.connector
try:
                conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="test")
                my_cursor = conn.cursor()
             
                conn.commit()
                my_cursor.close()
                conn.close()
                print("Connection Sucessful")
      
                


except mysql.connector.Error as error:
                    print("Error:", error)

