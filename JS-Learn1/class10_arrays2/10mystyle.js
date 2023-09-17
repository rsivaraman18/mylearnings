// ( ) 

/* 
forEach syntax:     array.forEach(function_name)    
Filter syntax:      array.filter(function_name)     returns all value
Map syntaxx :       array.map(function_name)        returns only true value
reduce syntax:      array.reduce(function_name)
  */

/* **********************************************   */

//Eg1 :forEach( ) --guvi Mtd1
let box =['table','chair','fan','grinder','mixie'];
console.log( box) 

box.forEach(function (value1) {
    console.log(`Property in my room: ${value1}`);
}) ;

/* **********************************************   */

//Eg2 :forEach ( ) --General Mtd
let vehicles = ["car","bike","scooter","auto"];

function display(element){          //use 1 parameter to catch each instance
    console.log(element) 
}

vehicles.forEach(display) 
/* **********************************************   */
//Eg 3: dispaly in browser
let text = "";
const fruits = ["apple", "orange", "cherry"];
fruits.forEach(myFunction);

document.getElementById("demo").innerHTML =  text;
 
function myFunction(item, index) {
  text += index + ": " + item + "<br>"; 
}
/* **************************************************************************************   */


//2.Filter And Map method
/* 
forEach syntax:     array.forEach(function_name)
Filter syntax:      array.filter(function_name)
Map syntaxx :       array.map(function_name)
reduce syntax:      array.reduce(function_name)
  */

//Eg1 : Learn Map & filter
numbers = [1,2,3,0,5]

function square(item){
    return Math.pow(item,2) 
}

//Eg1 Map method
let mapsquare = numbers.map(square)
console.log('map method square is',mapsquare) 

//Eg1 Filter function
let filtersquare = numbers.filter(square)
console.log('Filter Method Square is',filtersquare) 

/* *****************************************************   */
//Eg2 : Learn Map & filter
size = [1,2,3,10,13,15,7]

function checksize(item){
    return item <= 10
}

//Eg2 Map method
let goodsize2 = size.map(checksize)
console.log('Goodsize of map is',goodsize2) 


// Eg2 filter function
goodsize1 = size.filter(checksize)
console.log('Goodsize of Filter',goodsize1) 

/* ***************************************************************************   */

//4.reduce function --reduces array to a single value
price = [5,10,15,20,25]
let total;
function checkout(total,val1){
    return total + val1
}

let final = price.reduce(checkout);
console.log('Reduce price',final) 
