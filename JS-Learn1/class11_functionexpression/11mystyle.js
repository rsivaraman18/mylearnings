//  ( ) 
//Eg 1: 
const greeting = function( ) {      //in this function_name is not given instead comst variable given
    console.log("Hello") 
}

greeting( )
/* *******************************************************************   */
//Eg 2: 
const call = function( ) {      //in this function_name is not given instead comst variable given
    console.log("Say hello hello ") 
}

call( )

/* *******************************************************************   */
//Eg 3:onclick in different function
let count = 0;

function inccount( ){
    count = count+1
    document.getElementById("mylabel").innerHTML = count;
}

function deccount( ){
    count = count-1
    document.getElementById("mylabel").innerHTML = count;
}

/* *******************************************************************   */