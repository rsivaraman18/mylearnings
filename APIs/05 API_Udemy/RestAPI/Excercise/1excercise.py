# 1. Using List this program is done
# 2. ALL CRUD operations SUch as CREATE , RETRIEVE ,UPDATE ,DELETE
# 3. THis  stores data for temporry instance. because we are using List for storing data's.

from flask import Flask,jsonify,request
app = Flask (__name__ )

stores = [
            {
                'id':1001,
                'name':'Fruitstall',
                'items':[ "apple" ,"orange" ,"pineapple" ]                                               
            },
            {
                "id":1002,
                "name":"market",
                "items":["tomato","onion","drumn stick"]
            }
        ]


# **********************************************************************************************

@app.route( '/',methods=['GET'])
def welcome( ):
    return 'Welcome to store'

# **********************************************************************************************

# GET ALL STORES
@app.route( '/store',methods=['GET'])       
def get_stores( ):
    #return jsonify( {'Mystores':stores} )    # json accept Dictionary format
    return jsonify(stores )                    

# **********************************************************************************************

# GET Each store By name    http://127.0.0.1:5000/store/fruitstall
@app.route( '/store/<string:name>',methods=['GET'])
def get_mystore( name):
    for store in stores:
        if store['name'].lower( ) == name:
            return jsonify( store)
    return jsonify( {'msg':  'store with name not found ...'})

# **********************************************************************************************

# GET each store by ID  http://127.0.0.1:5000/store/1001
@app.route( '/store/<int:id>',methods=['GET'])
def get_mystore_id(id):
    for store in stores:
        if store['id'] == id:
            return jsonify(store)
    return jsonify( {'msg':'store with ID not found ' } )


# **********************************************************************************************

# Create a new store    POST http://127.0.0.1:5000/store
@app.route( '/store',methods=['POST'])
def create_store( ):
    data    = request.get_json( )
    sid     = data['id']
    sname   = data['name']
    sitem   = data['items']

    new_store = {
                    'id' : sid,
                    'name' : sname,
                    'items': sitem
                }
    stores.append( new_store)
    return jsonify( new_store)

"""
send this in post man to create a new
{
    "id":1002,
    "name":"vegetablestall",
    "items":["tomato","onion","drumn stick"]
}
"""


# **********************************************************************************************
# Update a store by ID       PUT   http://127.0.0.1:5000/store/1002
@app.route( '/store/<int:id>',methods=['PUT'])  
def update_by_id(id):
    data    = request.get_json( )
    Uid     = data['id']    
    Uname   = data['name']  
    Uitem   = data['items'] 
    
    for store in stores:
        if store['id'] == id:
            store['name'] = Uname           #string
            store['items'].append(Uitem)    #list
            return jsonify( "success")
    return jsonify( {'msg':'store not found'})


# **********************************************************************************************
# Update a store by Name      PUT   # http://127.0.0.1:5000/store/1002
@app.route( '/store/<string:name>',methods=['PUT'])  
def update_by_name(name):
    data    = request.get_json( )
    Uid     = data['id']    
    Uname   = data['name']  
    Uitem   = data['items'] 
    
    for store in stores:
        if store['name'].lower( ) == name:
            store['name'] = Uname           #string
            store['items'].append(Uitem)    #list
            return jsonify( "success")
    return jsonify( {'msg':'store not found'})

"""
Json format
{  
    "name":"medical xfgsdfgfdsg",
    "items":["cough syrup","dolo 650","Paracetamol"]
}
"""

# **********************************************************************************************
@app.route( '/store/<int:id>',methods=['DELETE'])   #DELETE  # http://127.0.0.1:5000/store/1002
def delete_by_id(id):
    for i in range(len(stores)):
        if stores[i]['id'] == id:
            del stores[i]
            return jsonify( "success deleted")
    return jsonify( {'msg':'store not found'})


# **********************************************************************************************




if __name__ == '__main__':
    app.run( debug=True)