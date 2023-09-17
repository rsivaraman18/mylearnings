from flask import Flask ,jsonify


app = Flask(__name__)
print('I am ready siva')

friends =[
    {'name':'siva',
     'age':'123',
     'city':'chennai',
     'state':'Tamilnadu'
     },
    {'name':'lakshman',
     'age':'50',
     'city':'coimbatore',
     'state':'Tamilnadu'
    },
    {'name':'Rajesh',
     'age':'51',
     'city':'madurai',
     'state':'Tamilnadu'
    },
    {'name':'Vijay',
     'age':'52',
     'city':'theni',
     'state':'Tamilnadu'
    }
    ]

@app.route('/')
def index():
    return 'Welcome to the flask frame work'


@app.route('/showfriends',methods=['GET'])
def showall():
    return jsonify({'myfriends':friends})

@app.route('/showfriends/<int:friend_id>',methods=['GET'])
def showone(friend_id):
    return jsonify( {'Friends':friends[friend_id]} )

@app.route('/mystudent',methods=['GET'])
def all_student():
    import sqlite3
    con = sqlite3.connect('check.db')
    cur = con.cursor()
    query ="SELECT * FROM student"
    cur.execute(query)
    viewdata = cur.fetchall()
    con.close()
    return viewdata

@app.route('/studentshow/<id>',methods=['GET'])
def showmyfriend(id):
    import sqlite3
    con = sqlite3.connect('check.db')
    cur = con.cursor()
    query = "SELECT * FROM student"
    cur.execute(query)
    viewdata = cur.fetchall()
    con.close()
    return viewdata[id]


if __name__ == '__main__':
    app.run(debug=True)

