#  ( )
# print  ( )
print ( " Hii Ready with RESTful class ")
from flask import Flask
from flask_restful import Resource,Api

app =Flask( __name__)
api = Api(app )



class Welcome(Resource):
    def get(self):
        return "Welcome To the RESTful APIs class"
    
api.add_resource(Welcome,"/" )

Items = [ ]

class Items(Resource):
    def get( self,name):
        return {'student' :name}
    
    def post( self,name):
        return {'student' :name}



api.add_resource(Items,"/item/<string:name>" )

if __name__ == "__main__":
    app.run( debug=True)



