import pymysql.cursors
import json
from DBConnector import DBConnector

# Connect to the database

dbconnector = DBConnector('localhost','root','','kolpbdc_site')

print("Getting from DB...")
books = dbconnector.books()

print(books);
dbconnector.saveBook("10", "My book");


