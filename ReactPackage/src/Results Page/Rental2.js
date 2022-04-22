import React from "react";
import './Rental2.css'

function Rental2({post}){
    return(
        <div id = "rental2">
             <a id ="house-url1" href = {post.room_link}>
            <div id="imgDiv" >
            <img className="rentalPostPic" src= {post.rental_image}></img>
            </div>
            <div id = "textDiv" >
            <div id="top-half">
            <p id="property" className="postText1">{post.rental_name}</p>
            <p className="postText">Safety Rating: TBA</p>
            </div>
            <div id="bot-rent">
                <div id="rating">
                    <p id="rate1">{post.rental_rating}</p>
                </div>
                <div id="pricing">
                    <p id="price1" className="postText">{post.rental_price}</p>
                </div>
            </div>

            </div>
            </a>
        </div>
    );
}

export default Rental2;