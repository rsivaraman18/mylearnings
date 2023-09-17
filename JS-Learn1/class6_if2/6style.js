// ( ) 

//checkbox
document.getElementById( "sbut").onclick = function( ) {
    const box=document.getElementById("python").checked;
    if (box ) {
        console.log(" You know python!. " ) ;
        document.getElementById("para1").innerHTML=" You know python!. "
    }
    else{
        console.log(" please Prepare Python language " ) ;
        document.getElementById("para1").innerHTML="  please Prepare Python language "

    }

}
/************************************************************************************ */

//radio button
document.getElementById( "cbut").onclick = function( ) {
    const c1 =document.getElementById("python1").checked;
    const c2 =document.getElementById("flask1").checked;
    const c3 =document.getElementById("Js1").checked;
    if (c1 ) {
        console.log(" You know python!. " )
        document.getElementById("para2").innerHTML=" You know python!. "

    }
    else if  (c2 ) {
        console.log(" You Know Flask" ) ;
        document.getElementById("para2").innerHTML=" you Know Flask Framework. "

    } 
    else if (c3 ) {
        console.log(" You Know Js " ) ;
        document.getElementById("para2").innerHTML=" you Know Java Script. "

    } 
    else {
        console.log(" Nothing were selected " ) ;
    }

}

/************************************************************************************ */

//grade system using IfElse
document.getElementById( "gbut").onclick = function( ) {
    grade = document.getElementById( "grade").value
    grade = grade.toUpperCase( ) 
    console.log(grade )
    if (grade == "A" ) {
        console.log(" Excellent Performance " );
        document.getElementById("para3").innerHTML=" Excellent Performance "
    }
    else if (grade == "B" ) {
        console.log(" Very Good " );
        document.getElementById("para3").innerHTML=" Very Good " 
    }
    else if (grade == "C" ) {
        console.log("  Good " );
        document.getElementById("para3").innerHTML="  Good " 
    }
    else if (grade == "D" ) {
        console.log("  Not bad Or fair" );
        document.getElementById("para3").innerHTML="  Not bad Or fair " 

    }
    else{
        console.log("  U failed " );
        document.getElementById("para3").innerHTML="  U Failed " 
    }


}

/************************************************************************************ */

//grade system using IfElse
document.getElementById( "g1but").onclick = function( ) {
    grade1 = document.getElementById( "g1").value
    grade1 = grade1.toUpperCase( ) 
    console.log(grade1)

    switch(grade1){
        case "A":
            console.log(" Excellent Performance " );
            document.getElementById("para4").innerHTML=" Excellent Performance "
            break
        
        case "B":
            console.log(" Very Good "  );
            document.getElementById("para4").innerHTML=" Very Good " 
            break
        
        case "C":
            console.log("  Good "  );
            document.getElementById("para4").innerHTML="  Good " 
            break
            
        case "D":
            console.log("  Not bad Or fair" );
            document.getElementById("para4").innerHTML="  Not bad Or fair " 
            break
        default:
            console.log("  U were failed" );
            document.getElementById("para4").innerHTML="  U Failed " 

        

    }
}









//2 condition check in ifElse
//  && AND
//  || OR
//  ! NOT 
let temp = 15;
if (temp > 0 && temp <30 ){
    console.log(" The Weather is Good" );
}
else{
    console.log(" The Weather i sbad" );
}
/*  ********************Ternary Function *********************************/

//ternary Operator - shortcut for If/else -statement
//if else 
let adult = checkage( 21);

function checkage( age){
    if ( age >= 18){
        console.log("eligible to vote" )
    }
    else{
        console.log("Not eligible to vote" )
    }
}


//ternary operator -1
checkgender('male');

function checkgender(gen){
    return gen=='male' ? console.log("this person is Male" ) : console.log("This is not male" )
}


//ternary operator -2
checkwin(true)
function checkwin(win){
    win ? console.log("you win" ) :console.log("you lost") 
}

/* ternary ends here */
