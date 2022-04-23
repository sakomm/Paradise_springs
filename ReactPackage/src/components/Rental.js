import React from 'react'
import './Rental.css'





function Rental({ post}){

   
    return(
        <div id = "post">
            
            <a id ="house-url" href = {post.room_link}>
            <img id="rental-pic" src= {post.rental_image}></img>
         <div id="text-cont">
            <p id="property" >{post.rental_name}</p>
            <p>Safety Rating:</p>
            <p id="price">{post.rental_price}</p>
            </div>  
            </a>
        </div>
    );
}

export default Rental;