from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource ,Api ,reqparse ,abort,marshal_with,fields
print ( "Hii siva I am ready" )

app = Flask (__name__)

app.config['BUNDLE_ERRORS'] = True          #shows multiple error at same time
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:siva@localhost/bookshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    #optional

api = Api(app)             #connecting flask with restful
db = SQLAlchemy(app)    #connecting flask with sqlalchemmy

# To create table in db:bookshop
class Mybook(db.Model):
    bid      = db.Column( db.String(20),  primary_key=True)
    title    = db.Column( db.String(255), nullable=False)
    author   = db.Column( db.String(255), nullable=False)
    price    = db.Column( db.Float() )
    quantity = db.Column( db.Integer() )

    def __init__(self,bid,title,author,price,quantity):
        self.bid        = bid
        self.title      = title
        self.author     = author
        self.price      = price
        self.quantity   = quantity

"""
# to create table run this command
with app.app_context():
    db.create_all()
"""

#**************************************************************************************
# To Add data's into database  we need add reqparse.
# We need this only for POST method
add_book_parser = reqparse.RequestParser()
add_book_parser.add_argument('author' , type=str ,  required =True)
add_book_parser.add_argument('title'  , type=str ,  required =True)
add_book_parser.add_argument('price'  , type=float, required =True)
add_book_parser.add_argument('quantity',type=int ,  required =True)


#**************************************************************************************
# To Update data's into database  we need add reqparse.
# We need this only for PUT method
update_book_parser = add_book_parser.copy( )
update_book_parser.remove_argument("title")     # we cannot update this field
update_book_parser.remove_argument("author")    # we cannot update this field

update_book_parser.replace_argument("price"   , type=float) # this can be update
update_book_parser.replace_argument("quantity", type=int)   # this can be update


#**************************************************************************************
# REname the paramter to display in browser
# WE CAN CHANGE parameter using lambda function
# we can set default value for empty or null values
# nested JON values
resource_fields =   {
                    'BooK ID '      : fields.String(attribute = "bid"),
                    'Book Title'    : fields.String(attribute ="title") ,
                    'Author'        : fields.String(attribute= lambda book:book.author.upper()),
                    'BookPrice'     : fields.Float(attribute="price" , default='Free'),
                    'Availabile'    : fields.Integer(attribute="quantity")
                    }
# 
'''nested packing
'BookPrice'     :{
                    'BookPrice'     : fields.Float(attribute="price" , default='Free'),
                    'Availabile'    : fields.Integer(attribute="quantity")
                }

}
'''

# call All books
class Books(Resource):
    @marshal_with(resource_fields)
    def get(self):
        data = Mybook.query.all()
        return data


class Firstauthor(Resource):
    @marshal_with(resource_fields , envelope= 'myauthor1')
    def get(self):
        bookdata = Mybook.query.filter_by(author = 'sivaraman').all( )
        return bookdata


class Secondauthor(Resource):
    @marshal_with(resource_fields , envelope= 'myauthor2')
    def get(self):
        bookdata = Mybook.query.filter_by(author = 'lakshan').all( )
        return bookdata


api.add_resource(Books,'/books/all')
api.add_resource(Firstauthor,'/books/sivaraman')
api.add_resource(Secondauthor,'/books/lakshan')


if __name__ == '__main__':
    app.run(debug=True)


