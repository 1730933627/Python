import MySQLdb

db = MySQLdb.connect(
    host = "localhost",
    user = "yanlin",
    passwd = "wh20010210",
    db = "mysql"
)
cur = db.cursor()

db.close()
