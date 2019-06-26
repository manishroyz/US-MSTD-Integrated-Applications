import MySQLdb

db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "admin1234",
    database = "usmstd"
)

#print(db)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a table called 'experimental_data' in the 'usmstd' database
# cursor.execute("CREATE TABLE experimental_data (id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, "
#                "collect_date INT(11) UNSIGNED NOT NULL,"
#                 "tof_s1 DECIMAL(7,2) NOT NULL,"
#                 "tof_s2 DECIMAL(7,2) NOT NULL,"
#                 "tof_s3 DECIMAL(7,2) NOT NULL,"
#                 "tof_s4 DECIMAL(7,2) NOT NULL,"
#                 "temperature_s1 DECIMAL(7,2) NOT NULL,"
#                 "temperature_s2 DECIMAL(7,2) NOT NULL,"
#                 "temperature_s3 DECIMAL(7,2) NOT NULL,"
#                 "temperature_s4 DECIMAL(7,2) NOT NULL,"
#                 "tc1 DECIMAL(7,2) NOT NULL,"
#                 "tc2 DECIMAL(7,2) NOT NULL,"
#                 "tc3 DECIMAL(7,2) NOT NULL,"
#                 "tc4 DECIMAL(7,2) NOT NULL,"
#                 "tc5 DECIMAL(7,2) NOT NULL,"
#                 "tc6 DECIMAL(7,2) NOT NULL,")
               
               
## 'DESC table_name' is used to get all columns information
# cursor.execute("DESC experimental_data")
# ## it will print all the columns as 'tuples' in a list
# print(cursor.fetchall())


#### TABLE INSERTION
query = "INSERT INTO experimental_data (collect_date,tof_s1,tof_s2,tof_s3,tof_s4,temp_s1,temp_s2,temp_s3,temp_s4," \
        "tc1,tc2,tc3,tc4,tc5,tc6) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values = [(1560657245, 6100, 6600, 7100, 7600,	410, 510, 610, 710, 50, 450, 560, 590, 660, 760)]

## executing the query with valuess
cursor.executemany(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()