import React from 'react'
import './Rental.css'




function Rental({description, price, photo}){
    return(
        <div id = "post">
            <img class="rental-pic" src= {photo}></img>  
            <p>Entire residential home in Charlottesville</p>
            <p id="price">{price}</p>
        </div>
    );
}

export default Rental;