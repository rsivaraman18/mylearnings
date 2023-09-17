//( ) 
let username= "sivaraman"
let myname = "       siva      "
let demoname="siv-ram-an"


console.log( username.length);              //find the length of string
console.log( username.charAt(2 ));          //letter at gfiven index
console.log( username.match('raman'))       // search the index at which the word match in a sting
console.log( username.repeat(3 ))           // repeats a particular string
console.log( username.replace("raman","lakshan" ) ) 

//Index Function
console.log('Index Function')
console.log( username.indexOf("r" ));       //Index value of particular letter
console.log( username.indexOf("z" ));       //not found -1
console.log( username.lastIndexOf('a' ) )   //index value of a string 


//search function
console.log('Search Function')
console.log( username.search( 'm'))     //returns index of a string, not found return -1
console.log( username.search( 'z'))    //returns index of a string, not found return -1


console.log( username.toUpperCase( ) );     // convert to uppercase
console.log( myname.trim( )  )              // Removes unwanted space before and after string
console.log( myname.repeat(3 ))   

console.log( demoname.split("-" ) ) 

//slicing of string
let fullname="Python programmer";
let firstname;
let lastname;
firstname = fullname.slice(0,6) 
lastname =fullname.slice(7) 
console.log("Fullname is", fullname ) 
console.log("Firstname is", firstname ) 
console.log("Lastname is", lastname ) 

//Using slicing And Index Together
let newname = "Singam Puli"
let fname= newname.slice(0,newname.indexOf(" ") ) 
let lname = newname.slice(newname.indexOf(" ") +1) 
console.log("newname  is", newname) 
console.log("fname  is", fname) 
console.log("lanme  is", lname) 



//Type conversion
let age =11;
console.log(typeof age) 

//string to number
let x=Number('3.123')
console.log(x,typeof x) 

let a=Number('3pizza')
console.log(a,typeof a)     //this is not number



//number to string
let y=String(321) 
console.log(y,typeof y) 

//str to boolean  -- only empty false 
let z=Boolean(" ") 
console.log(z,typeof z) 
