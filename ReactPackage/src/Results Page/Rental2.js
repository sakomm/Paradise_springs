import React from "react";
import './Rental2.css'
import Image from "../components/boat.jpg"

function Rental2({description, price, photo}){
    return(
        <div id = "Rental2">
            <a></a>
            <img class="rental-pic" src= {Image}></img>  
            <p id="property" >{description}</p>
            <p>Safety Rating: TBA</p>
            <p id="price">${price}/night</p>
            
        </div>
    );
}

export default Rental2;