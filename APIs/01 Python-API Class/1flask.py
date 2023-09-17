from flask import Flask,render_template,jsonify,request

import pymysql
con =pymysql.connect(host = 'localhost',
                             user = 'root', 
                             password='siva',
                             database = 'fruitshop',
                            )
print("connection suuccess" )


app = Flask( __name__)

@app.route('/' )
def hello( ):
    return "Hii siva ,Welcome to new class"

@app.route('/kadai' ,methods=['GET'])
def get( ):
    cur =con.cursor( )
    query1 = "SELECT * FROM products"
    cur.execute(query1 )
    get_data = cur.fetchall( )
    get_data = jsonify (get_data )
    return get_data


@app.route('/kadaipost' ,methods=['POST'])
def add( ):
    cur = con.cursor( )
    new  = request.get_json( )
    fname = new ['name']
    funit  = new['unit']
    fprice = new['price']
    query2 = "INSERT INTO products (prod_name,prod_unit,Prod_price) VALUES (%s,%s,%s) "
    qudata2 = ( fname,funit,fprice)
    cur.execute(query2 , qudata2)
    con.commit( )   
    id ="This Is POST Method "
    return {"id":id,"message":"success"},201

    

    '''
    To check use POSTMAN app and send request
    use this link :  http://127.0.0.1:5000/kadaipost
    {
    "name": "puliampalam",
    "unit": "kg",
    "price": 15
    }   
    '''
    

    
@app.route('/kadaiupdate' ,methods=['PUT'])
def update( ):
    cur = con.cursor( )
    new  = request.get_json( )
    fid = new['id']
    fname = new ['name']
    funit  = new['unit']
    fprice = new['price']
    #query3 = "INSERT INTO products (prod_id,prod_name,prod_unit,Prod_price) VALUES (%s,%s,%s,%s) "
    query3 = "UPDATE products SET prod_name = %s, prod_unit = %s ,Prod_price=%s WHERE prod_id= %s"
    qudata3 = ( fname,funit,fprice,fid)
    cur.execute(query3 , qudata3)
    con.commit( )

    return {'info':'PUT method', 'message':"successfully Updated.."}

    """
    Check this in POST MAN APP 
    use this link : http://127.0.0.1:5000/kadaiupdate
    {
    "id":1,
    "name" : "strawberry",
    "price" : 150,
    "unit" : "box"
    }
    """
@app.route('/kadaitest' ,methods=['PUT'])
def kadaitest( ):
    url_link = " http://127.0.0.1:5000/kadai"
    mydata = {
                "fid": "1",
                "fname": "kuttralam"
                }
    req_data = requests.put(url_link , data = mydata)
    return "success"





if __name__ == "__main__":
    app.run(debug =True )
