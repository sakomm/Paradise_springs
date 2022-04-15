import React from "react";
import './Rental2.css'

function Rental2({description, price, photo}){
    return(
        <div id = "post">
            <a></a>
            <img class="rental-pic" src= {photo}></img>  
            <p id="property" >Property</p>
            <p>Safety Rating:</p>
            <p id="price">${price}/night</p>
            
        </div>
    );
}

export default Rental2;