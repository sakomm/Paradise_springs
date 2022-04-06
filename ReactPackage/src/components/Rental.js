import React from 'react'
import './Rental.css'




function Rental({description, price, photo}){
    return(
        <div id = "post">
            <img class="rental-pic" src= {photo}></img>   
          
        </div>
    );
}

export default Rental;