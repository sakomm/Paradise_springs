import React from "react";
import './Rental2.css'
import Image from "../components/boat.jpg"

function Rental2({description, price, photo}){
    return(
        <div id = "Rental2">
            <a></a>
            <div id="imgDiv" >
            <img className="rentalPostPic" src= {photo}></img>
            </div>
            <div id = "textDiv" >
            <p id="property" className="postText">{description}</p>
            <p className="postText">Safety Rating: TBA</p>
            <p id="price" className="postText">${price}/night</p>
            </div>
            
        </div>
    );
}

export default Rental2;