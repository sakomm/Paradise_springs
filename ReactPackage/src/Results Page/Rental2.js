import React from "react";
import './Rental2.css'
import Image from "../components/boat.jpg"

function Rental2({description, price, photo}){
    return(
        <div id = "Rental2">
            <a></a>
            <img class="rental-pic" src= {photo}></img>
            <div id = "textDiv" >
            <p id="property" className="postText">{description}</p>
            <p className="postText">Safety Rating: TBA</p>
            <p id="price" className="postText">${price}/night</p>
            </div>
            
        </div>
    );
}

export default Rental2;