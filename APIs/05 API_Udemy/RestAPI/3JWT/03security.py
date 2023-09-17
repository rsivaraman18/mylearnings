from werkzeug.security import safe_str_cmp
from user import User
# ( )

users = [
    User(1,"sivaraman",'siva' )
]

username_mapping = {u.username : u for u in users}
userid_mapping = {u.id : u for u in users}



def authenticate(myuser , mypwd ):
    user = username_mapping.get( myuser , None)   
    #if  user['password']== mypwd :
    if user and safe_str_cmp(user['password'] ,mypwd):
        return user

def identity (payload ):
    user_id = payload['identity']
    return userid_mapping.get (user_id,None )

"""
users = [
            {
            "id" : 1,
            "username" : 'sivaraman',
            "password" : 'siva'
            }
        ]

username_mapping = {
                'sivaraman':
                    {
                    "id" : 1,
                    "username" : 'sivaraman',
                    "password" : 'siva'
                    }
                }



userid_mapping = {
                1:
                    {
                    "id" : 1,
                    "username" : 'sivaraman',
                    "password" : 'siva'
                    }
                }

"""