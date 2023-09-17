# paste this in a python interpreter to execute the code.
#this is using class method

from flask import Flask
from flask_restful import Resource ,Api,request

app = Flask(__name__ )
api = Api (app )

book_details ={  }

class Book(Resource ):
    def get (self,bid ):
        if bid in book_details:       
            return book_details[bid]
    
        return { 'message' : 'Book with Id : ' +bid + '  not found'}
    
    def post(self,bid ):
        if bid in book_details:
            return {'msg':'Book with Id : ' +bid + '  already exists'}
    
        book_info = { }
        data = request.form      
        
        for key in data:
            book_info[key] =data[key]
        
        book_details[bid] = book_info

        return {'msg' : "Book with ID : " +bid + ' successfully added'}

api.add_resource( Book , '/books/<string:bid>')

if __name__ == "__main__":
    app.run ( debug=True)