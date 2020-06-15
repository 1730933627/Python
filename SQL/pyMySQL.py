import pymysql
 
db = pymysql.connect("localhost","yanin","wh20010210","TESTDB" )
 
cursor = db.cursor()
 
cursor.execute("SELECT VERSION()")
 
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
db.close()
