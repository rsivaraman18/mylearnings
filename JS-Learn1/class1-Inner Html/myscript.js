// ( ) 
//alert( 'siva') 

//square
document.getElementById('sqbutton').onclick = function( ) {
    let a = document.getElementById('sqside') .value;
    let area= a*a ;
    let perimeter = 4*a;
    document.getElementById('sqarea' ) .innerHTML ='Area of square is  ' + area;
    document.getElementById('sqperi' ) .innerHTML ='Perimeter of square is  ' + perimeter;

};

//rectangle
document.getElementById('rbutton').onclick = function( ) {
    let l = document.getElementById('rlength') .value;
    let b = document.getElementById('rbreadth') .value;
    l=Number( l)
    b=Number(b )
    let area= l*b ;
    let perimeter =2*(l+b);
    document.getElementById('rarea' ) .innerHTML ='Area of Rectangle is  ' + area;
    document.getElementById('rperi' ) .innerHTML ='Perimeter of Rectangle is  ' + perimeter;

};

//Circle
document.getElementById('cbutton').onclick = function( ) {
    let r = document.getElementById('cradius') .value;
    
    let area= (22/7 )  *r*r ;
    area =Math.round(area)
    let perimeter = 2*(22/7)*r;
    perimeter = Math.round(perimeter)
    document.getElementById('carea') .innerHTML ='Area of square is  ' + area;
    document.getElementById('cperi') .innerHTML ='Perimeter of square is  ' + perimeter;

};


//right triangle
document.getElementById('rtbutton').onclick = function( ) {
    let b = document.getElementById('rtbreadth') .value;
    let h = document.getElementById('rtheight') .value;
    b=Number( b)
    h=Number(h )
    let area=(0.5 ) *b*h ;
    
    document.getElementById('rtarea' ) .innerHTML ='Area of Rectangle is  ' + area;
    
};

//Equilateral Triangle
document.getElementById('eqbutton').onclick = function( ) {
    let a = document.getElementById('eqside') .value;
    let area=(1.732/4) *a*a ;
    let perimeter = 3*a;
    document.getElementById('eqarea') .innerHTML ='Area of square is  ' + area;
    document.getElementById('eqperi') .innerHTML ='Perimeter of square is  ' + perimeter;

};

//scalar triangle
document.getElementById('stbutton').onclick = function( ) {
    let a = document.getElementById('side1') .value;
    let b = document.getElementById('side2') .value;
    let c = document.getElementById('side3') .value;
    a=Number(a)
    b=Number(b)
    c=Number(c)
    
    let s;
    s=(0.5 )*(a+b+c) ;
    
    

    
    //let area=Math.sqrt(s*( s*a) * ( s*b) * ( s*c) )
    let area =(s*( s*a) * ( s*b) * ( s*c) );
    area =Math.sqrt(area);
    
    document.getElementById('starea' ) .innerHTML = 'Area of Rectangle is  ' + area;
    document.getElementById('stperi') .innerHTML  = 'Perimeter of square is  ' + s;
    
};

//area=Math.SQRT(s*( s*a) * ( s*b) * ( s*c) )

// celsius to Fahrenheit 
document.getElementById('celbutton').onclick = function( ) {
    let a = document.getElementById('cel') .value;
    let confa=( a *(9/5 ) )+32 ;
    document.getElementById('farval' ) .innerHTML ='Faherhenheit value is  ' + confa + 'Fahrenheit';
};

//Fahrenheit to   celsius 
document.getElementById('fabutton').onclick = function( ) {
    let a = document.getElementById('fa') .value;
    let concel=((a-32 ) *(5/9 ) ) ;
    document.getElementById('celval' ) .innerHTML ='Faherhenheit value is  ' + concel +' celsius';
};

//count
let count=0;

document.getElementById("decreasebtn").onclick = function( ){
    count -=1;
    document.getElementById("countlabel" ).innerHTML =count;
};

document.getElementById("resetbtn").onclick = function( ){
    count =0;
    document.getElementById("countlabel" ).innerHTML =count;
};

document.getElementById("increasebtn").onclick = function( ){
    count +=1;
    document.getElementById("countlabel" ).innerHTML =count;
};


//Random Dice roller
let d1;
let d2;
let d3;

document.getElementById("rollbutton").onclick=function( ){
    d1 = Math.ceil(Math.random( ) * 6 );
    d2 = Math.ceil(Math.random( ) * 10 );
    d3 = Math.ceil(Math.random( ) * 20 );

    document.getElementById( "dice1").innerHTML = "Dice1 (1 to 6):    "  +d1;
    document.getElementById( "dice2").innerHTML = "Dice1 (1 to 10):   " +d2;
    document.getElementById( "dice3").innerHTML = "Dice1 (1 to 20):   "  +d3;
}