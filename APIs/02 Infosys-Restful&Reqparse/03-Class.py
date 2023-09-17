# paste this in a python interpreter to execute the code.
#this is using class method
# ( )

from flask import Flask
from flask_restful import Resource ,Api,request,reqparse

app = Flask(__name__ )
app.config['BUNDLE_ERRORS'] = True
api = Api (app )

book_details ={  }

add_book_parser = reqparse.RequestParser ()

add_book_parser.add_argument ('title',type=str,required=True)
add_book_parser.add_argument ('author',type=str,required=True)
add_book_parser.add_argument ('price',type=int)
add_book_parser.add_argument ('lang',type=str,choices=('english','tamil','telgu' ))


update_book_parser = add_book_parser.copy( )

update_book_parser.remove_argument ("author")   #this cannot be updated
update_book_parser.remove_argument ("title")    #this cannot be updated

update_book_parser.replace_argument ('price',type=int)  #This can be updated
update_book_parser.replace_argument  ('lang',type=str)  #This can be updated


class Book(Resource ):
    def get (self,bid ):
        if bid in book_details:       
            return book_details[bid]
    
        return { 'message' : 'Book with Id : ' +bid + '  not found'}
    
    def post(self,bid ):
        if bid in book_details:
            return {'msg':'Book with Id : ' +bid + '  already exists'}
        
        args = add_book_parser.parse_args ( )
        book_details[bid] = args

        return {'msg' : "Book with ID : " +bid + ' successfully added'}
    
    def put(self,bid ):
        if bid not in book_details:
            return {'msg':'Book with Id : ' +bid + '  does not exists'}
        
        args = update_book_parser.parse_args ( )

        for key,value in args.items( ):
            if value:
                book_details[bid][key] = value
        return {'msg' : "Book with ID : " +bid + ' successfully updated '}

        


api.add_resource( Book , '/books/<string:bid>')

if __name__ == "__main__":
    app.run ( debug=True)