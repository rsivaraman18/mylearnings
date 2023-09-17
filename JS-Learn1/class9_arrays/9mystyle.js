// ( ) 
let fruits = ["mangoes", "oranges","apples","kiwi","watermelon"]
console.log('Fruit Array',fruits) 
//
//2 index Array
console.log('Fruit 1 is ',fruits[0]) 

//3 sort of array in ascending
fruits = fruits.sort( ) 
console.log('Sort Fruit in Ascending ',fruits) 


//3 sort of array in descending
fruits = fruits.sort( ).reverse( ) 
console.log('Sort Fruit in Descending',fruits) 

//4 using Loop extract elements in array
//mtd1 
for  (i of fruits ){
    console.log(i) 
} 



//5 Spread operator -unpacks element
console.log(...fruits ) 

let numbers = [1,2,3,4,5,6,7,8,9];
let maximum = Math.max(...numbers ) 
console.log("maximum Value is ",maximum)




//To change values in array
//mtd1 _ Using index
fruits[0]='sathukodi'
console.log(...fruits ) 

//mtd2 - push
fruits.push( "kamala")       // add an element at end
console.log(...fruits ) 

let scigroup =["physics","chemistry","biology"];
let comgroup = ["accounts","Economics","commerce"]
scigroup.push(comgroup )
console.log("items in scigroup is",...scigroup ) 

//mtd3 - pop                //remove last element               
fruits.pop( ) 
console.log(...fruits ) 

//mtd 4 -unshift
fruits.unshift( "banana")   //add element at begining
console.log(...fruits ) 

//mtd 5 -shift
fruits.shift( ) 
console.log(...fruits )     //removes element at begining

/* ******************************************************************* */

//To find length
console.log(fruits.length ) 
/* ******************************************************************* */

//2D arrays 
let vegetables = ["tomato","onion","carrot"]
let meats =["fish","egg","chicken"]
let sweets =["kajukattli","Laddu","Gulab jamun"]

let basket = [vegetables,meats,sweets] //2D array
for(item of basket ){
    console.log(item ) 
} 
console.log(basket[2][0] )


/* **************** REST PARAMETER *****************************/
//Rest parameter    -Takes n number of parameter

function addition(...mynumbers ){           //any number of parameter can be passed
    let total=0;
    for (item of mynumbers ){
        total =total + item
    }
    return total
}


result = addition(5,6,7 )    //any number of parameter can be passed
console.log(result)                


/* **************** REST PARAMETER ENDS here *****************************/
 


