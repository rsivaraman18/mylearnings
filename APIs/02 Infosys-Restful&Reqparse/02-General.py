print(" Book store Normal mtd PART-2 ")
from flask import Flask,request

#import flask_restful    #I dont know the use

app = Flask (__name__ )

book_details ={  }

@app.route('/')
def index ( ):
    return "welcome to flask Rest Api"


@app.route('/books/<string:bid>' ,methods=['GET'])
def collect(bid):    
    if bid in book_details:       
        return book_details[bid]
    
    return { 'message' : 'Book with Id : ' +bid + '  not found'}


@app.route('/books/<string:bid>' ,methods=['POST'])
def create( bid):
    if bid in book_details:
        return {'msg':'Book with Id : ' +bid + '  already exists'}
    
    book_info = { }
    data = request.form         # data send as formdata in postman
    #data = request.get_json()  # incase data sended in json format
    for key in data:
        book_info[key] =data[key]
    
    book_details[bid] = book_info

    return {'msg' : "Book with ID : " +bid + ' successfully added'}

if __name__ == "__main__":
    app.run ( debug=True)

'''
Use this in postman
http://127.0.0.1:5000/books/B101
'''