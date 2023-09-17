# print ( )
# ( )
# This is using Class Method
# 1  GET ALl
# 2  GET one
# 3  POST one


from flask import Flask,request,jsonify
from flask_restful import Resource , Api

app = Flask (__name__ )
api = Api(app )

bakery_stall = [
            {
                'id':1001,
                'name':'cake',
                'price':500,
                'type':[ "Black Forest" ,"White Forest" ,"pineapple" ]                                               
            },
            {
                "id":1002,
                "name":"icecream",
                'price':250,
                "type":["Vanilla","Choculate","Mango"]
            }
        ]
# *******************************************************************************
# to call all items
class Mybakery(Resource):
    def get(self):
        #return {'msg':'hii '+name}
        return bakery_stall 
    
    def post(self):
        data = request.get_json( )
        sid     = data['id']
        sname   = data['name']
        sprice  = data['price']
        stype   = data['type']
        
        new_item = {
                    'id' : sid,
                    'name' : sname,
                    'price': sprice,
                    'type' : stype
                }
        bakery_stall.append( new_item)
        return  new_item,201

api.add_resource(Mybakery,"/items" )

# *******************************************************************************
# Calling each item with its name
class Bakery(Resource):

    def get(self,name):
        for item in bakery_stall:
            if item['name'].lower ( ) == name:
                return item
        return {"msg" : "Sorry, bakery does not have " +name  },404

        '''
        Alter Method using filter function
        def get(self,name):
            item = next(filter( lambda x:x['name'] == name , bakery_stall),None )
            return {'item' : item},200 if item else 200
        '''
    
    def delete(self,name): 
        global  bakery_stall
        bakery_stall = list(filter(lambda item: item['name'] != name, bakery_stall))
        return "successfully deleted"
        

api.add_resource(Bakery,"/items/<string:name>" )

 
# *******************************************************************************
if __name__ == '__main__':
    app.run( debug=True)


