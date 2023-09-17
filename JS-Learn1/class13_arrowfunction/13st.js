//  ( ) 
// Arrow function removes the keyword in normal function

//Eg1 without any input parameter
const happy = ( ) => console.log(`Happy Birthday ` )

happy()

/**************************************************/
//Eg 2 :with input

const greet = (user) => console.log(`Hiii & Welcome to ${user}` )
greet("Siva" )

//************************************************************ */
//Eg 3 Normal function
const percent = function(x,y ) {     
    return ( x/y) * 100 
}
console.log( percent(100,50)  )
//************************************************************ */
//Eg 4 : Arrow function in single line
const mypercent = (x,y ) =>  ( x/y) * 100 

console.log( mypercent(100,50)  )
//************************************************************ */
//Eg 5 : Arrow function with curls used for multiline
mpercent = (x,y) => {
    return ( x/y) * 100 ;
  }

  console.log( mpercent(100,50)  )

//************************************************************ */
let grade = [100,10,40,60,20,30,50]

grade.sort(decorder)
function decorder(x,y){
    return y-x
}
console.log( grade  )

//************************************************************ */
