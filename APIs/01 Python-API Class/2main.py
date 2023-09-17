# ( )
# print( )
import requests
import webbrowser
import requests
from pprint import pprint

def eg1 ( ):
    print ("This is Infosys POST request multiple paramters but falls error for me " )
    link = "https://pastebin.com/7fML3Hkt"
    load = {'username':'singam','email':'singam@gmail.com'}
    api_key = " b0eFgRoaAps3mcNlkG2WufEfEC8_Qa0Y "
    parameters ={
                    'api_dev_key':api_key,
                    'api_option':'paste',
                    'api_paste_code':load,
                    'api_paste_format':'python'
                }
    mydata = requests.post(link ,data=load)
    
    print( mydata.status_code) 

def eg2( ):
    print( "Hii to HEAD method ")
    data =requests.head('http://127.0.0.1:5000/kadai' )
    #print( data.status_code)           #200
    pprint( data.text)                  #'' 
    pprint( data.content)               #b''
    pprint( data.headers) 



def eg3( ):
    print( "Hii to PUT method ")
    url_link = "https://pastebin.com/7fML3Hkt"
    mydata = {
                "id": "2",
                "place": "kuttralam"
                }
    req_data = requests.put(url_link , data = mydata)
    print( req_data.status_code)
    print( req_data.text)
    type(req_data )

def eg4( ):
    url_link = " https://pastebin.com/7fML3Hkt"
    req_option = requests.options( url_link)   
    type(req_option )
    print(req_option.text)





eg4 ( )