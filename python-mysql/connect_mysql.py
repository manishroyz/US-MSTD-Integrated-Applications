import MySQLdb

db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "admin1234"
)

print(db)
