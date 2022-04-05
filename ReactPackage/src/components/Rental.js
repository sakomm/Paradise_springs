import React from 'react'
import './Rental.css'




function Rental({description, price, photo}){
    return(
        <div id = "post">
            <img class="rental-pic" src= {photo}></img>   
            <h3>{price}</h3>        
            <p>{description}</p>
        </div>
    );
}

export default Rental;