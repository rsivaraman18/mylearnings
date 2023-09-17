// ( ) 

// function calling
birthday( )     //function call

function birthday( ) {
    console.log( "Hiii siva ")
    console.log( "Happy birthday")
    console.log( " end ")
    
}

/* ************************************************************ */



//using Variables from outside
let cname = "Swift"
let cprice = 2500

car( )          //function call
function car( ) {
    console.log( "My car name is",cname)
    console.log( "My car name is",cprice)
    console.log( " end ")

}
/* ************************************************************ */

// passing argument in a function & calling 1 function from other
function start( ){
    let bname = "R15"
    let bprice = "35000"
    displaybike(bname,bprice )

}

function displaybike( bname,bprice){
    console.log( "My Bike name is",bname)
    console.log( "My Bike name is",bprice)
    console.log( " end ")

}
start( )

/* 
same in Python 
def start( ):
    bname = "R15"
    bprice = "35000"
    displaybike(bname,bprice )


def displaybike( bname,bprice):
    print( "My Bike name is",bname)
    print( "My Bike name is",bprice)
    print( " end ")

start( )

*/

