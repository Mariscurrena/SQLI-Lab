import pymysql

#Connection variable and authentication
connection = pymysql.connect(user='root', 
                             passwd='admin1234',
                             host='localhost',
                             db='Prueb1')

#Cursor variable to be able to perform sql queries
cur = connection.cursor()

#Execute a querir
cur.execute("SELECT * FROM firsttable;")

#Print all querie's values
for idk, name, passd in cur.fetchall():
    print(idk," | ",name," | ",passd)

#Finish the connection
connection.close()