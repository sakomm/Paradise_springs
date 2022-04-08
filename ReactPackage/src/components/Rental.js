import React from 'react'
import './Rental.css'




function Rental({description, price, photo}){
    return(
        <div id = "post">
            <a></a>
            <img class="rental-pic" src= {photo}></img>  
            <p id="property" >Entire residential home in Charlottesville</p>
            <p>Safety Rating:</p>
            <p id="price">${price}/night</p>
            
        </div>
    );
}

export default Rental;