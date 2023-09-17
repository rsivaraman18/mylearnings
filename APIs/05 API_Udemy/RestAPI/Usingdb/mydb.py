 # ()
import sqlite3
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()

# create a table 
Create_table_query = "CREATE TABLE myusers (Id INT , Username TEXT , Password TEXT)"

