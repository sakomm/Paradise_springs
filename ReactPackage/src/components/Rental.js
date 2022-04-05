import React from 'react'
import './Rental.css'

var description;
var address;
var price;
var photo;


function Rental(){
    return(
        <div id = "post">
            <img class="rental-pic" src= { require("./beach.jpg") }></img>           
            
        </div>
    );
}

export default Rental;