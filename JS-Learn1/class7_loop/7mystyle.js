// ( ) 

//while statement - Infinite loop
let a=1;
while(a==10){
    console.log( " Hii SIVA ") 
    break
} 

//for loop
let i;
for (i=1 ; i<=5; i++ ){
    console.log( i) 
} 
console.log("bye bye")

//nested loop
let x;
for (x=1; x<=5; x++ ){
    for (y=1; y<=5; y++ ){
        console.log("*")
        document.getElementById("mybox").innerHTML += y;
    }
    console.log("1")
    //document.getElementById("mybox").innerHTML +="<br>";
} 

