//  ( )
//MTd 1 
let count = 0;

function inc( ){
    count = count+1
    document.getElementById("mylabel").innerHTML = count;
}

function dec( ){
    count = count-1
    document.getElementById("mylabel").innerHTML = count;
}

/* ************************************************************************/
//Mtd 2:

let acount=0;

document.getElementById("decreasebtn").onclick = function( ){
    acount -=1;
    document.getElementById("countlabel" ).innerHTML =acount;
};

document.getElementById("resetbtn").onclick = function( ){
    acount =0;
    document.getElementById("countlabel" ).innerHTML =acount;
};

document.getElementById("increasebtn").onclick = function( ){
    acount +=1;
    document.getElementById("countlabel" ).innerHTML =acount;
};

/* ************************************************************************/
//Mtd 3: