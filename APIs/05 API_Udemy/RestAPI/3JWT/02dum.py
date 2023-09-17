#  ( )
from werkzeug.security import safe
users = [
            {
            "id" : 1,
            "username" : 'sivaraman',
            "password" : 'siva'
            }
        ]

username_mapping = { "sivaraman" : {
    "id" : 1 ,
    "username" : "sivaraman" ,
    "password" : "siva"
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

def authenticate(myuser , mypwd ):
    user = username_mapping.get( myuser , None)   
    if  user['password']== mypwd :
        return user
    
def identity (payload ):
    user_id = payload['identity']
    return userid_mapping.get (user_id,None )


