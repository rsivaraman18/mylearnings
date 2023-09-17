# paste this in a python interpreter to execute the code.
#this is using class method
# ( )

from flask import Flask
from flask_restful import Resource ,Api,request,reqparse

app = Flask(__name__ )
api = Api (app )

book_details ={  }

book_parser = reqparse.RequestParser ( )
book_parser.add_argument ('title',type=str,dest='dummytitle')
book_parser.add_argument ('author',type=str,required=True,)
book_parser.add_argument ('price',type=int,required=True)



class Book(Resource ):
    def get (self,bid ):
        if bid in book_details:       
            return book_details[bid]
    
        return { 'message' : 'Book with Id : ' +bid + '  not found'}
    
    def post(self,bid ):
        if bid in book_details:
            return {'msg':'Book with Id : ' +bid + '  already exists'}
        
        args =book_parser.parse_args ( )
        book_details[bid] = args
        
           

        return {'msg' : "Book with ID : " +bid + ' successfully added'}

api.add_resource( Book , '/books/<string:bid>')

if __name__ == "__main__":
    app.run ( debug=True)reterter