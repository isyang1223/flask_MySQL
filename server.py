from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'testdb')
# an example of running a query
data = mysql.query_db("SELECT * FROM users")

for x in range(0,len(data)):
    print "First Name: {}".format(data[x]["first_name"])
    print "Last Name: {}".format(data[x]["last_name"])
app.run(debug=True)