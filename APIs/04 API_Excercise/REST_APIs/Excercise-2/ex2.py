#  ( )
print ("Hii siva" )
from flask import Flask,jsonify,request

# DB creation from Python
import mysql.connector
mydb = mysql.connector.connect(host="localhost" , user="root" , password="siva" )
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS furniturestore")
print("Database successfully created ... ")

# DB connection with Python
con = mysql.connector.connect(host ="localhost",user ="root",password="siva",database ="furniturestore")
print(" Connection Successfully ... ")

# Create Table in DB
cur = con.cursor()
query = "CREATE TABLE IF NOT EXISTS furniture (Id INT AUTO_INCREMENT PRIMARY KEY , Name VARCHAR(50) NOT NULL ,Price INT ,Material VARCHAR(50) , Length VARCHAR(10) ,breadth VARCHAR(10))"
cur.execute(query)
print("table created successfully")

# Working With flask
app = Flask(__name__)

@app.route('/' )
def Welcome( ):
    return "Hii siva Welcome to REST API EXCERCISE 2"

@app.route('/furniture',methods =['GET'] )
def get_allfurniture():
    cur = con.cursor( )
    query1 = " SELECT * FROM furniture "
    cur.execute( query1)
    resdata = cur.fetchall( )
    #return jsonify(resdata )
    return (resdata )


@app.route('/furniture/<int:id>',methods =['GET'] )
def get_furniture(id ):
    cur = con.cursor( )
    query2 = " SELECT * FROM furniture WHERE id= %s"
    qdata2 = (id,)
    cur.execute(query2 , qdata2)
    resdata = cur.fetchone( )
    return jsonify(resdata )

@app.route('/furniture',methods =['POST'] )
def create_furniture():
    data = request.form
    cur = con.cursor( )
    query3 = "INSERT INTO furniture (name,price,material,length,breadth) VALUES  (%s,%s,%s,%s,%s)"
    qdata3  = ( data['name'] ,data['price'] , data['material'] , data['length'], data['breadth'] )
    
    cur.execute(query3,qdata3)
    con.commit( )    
    return "msg:Successfully added"

@app.route('/furniture/<int:id>',methods =['PUT'] )
def update_furniture(id):
    data = request.form
    cur = con.cursor( )
    query4 = "UPDATE furniture SET name=%s, price =%s, material=%s, length =%s, breadth=%s Where id=%s"     
    qdata4  = ( data['name'] ,data['price'] , data['material'] , data['length'], data['breadth'] ,id )
    
    cur.execute(query4,qdata4)
    con.commit( )    
    return "msg:Successfully Updated"


@app.route('/furniture/<int:id>',methods =['DELETE'] )
def delete_furniture(id):
    cur = con.cursor( )
    query5 = "DELETE FROM furniture WHERE id=%s"
    qdata5 = ( id,)
    cur.execute(query5,qdata5)
    con.commit( ) 
    return " deleted successfully" 


if __name__  == "__main__":
    app.run( debug=True)

"""
check with POSTMAN App
1 GET    http://127.0.0.1:5000/furniture
2 GET    http://127.0.0.1:5000/furniture/1001
3 POST   http://127.0.0.1:5000/furniture
4 PUT    http://127.0.0.1:5000/furniture/1002
5 DELETE http://127.0.0.1:5000/furniture/1002
"""