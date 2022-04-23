import React, {useState, useEffect} from 'react'
import './Rental.css'
import { useDispatch, useSelector } from 'react-redux'
import * as api from '../api'




function Rental({ post}){
    const posts =useSelector((state)=>state.posts);
    const[rating, setRating] = useState([]);
    var rated = "N/A"
    useEffect(() => {
        //console.log(post.key)
        
            api.fetchPosts({
            params:{
                key:post.key
               
            }
        }).then(response => {
            setRating(response.data);
                
            });
        
    },[]);

    if(rating[0]!==undefined){
        rated=rating[0].safety_rating;            
        //console.log("Rating: "+rating[0].safety_rating)
    }
   
    return(
        <div id = "post">
            
            <a id ="house-url" href = {post.room_link}>
            <img id="rental-pic" src= {post.rental_image}></img>
         <div id="text-cont">
            <p id="property" >{post.rental_name}</p>
            <p>Safety Rating: {rated}</p>
            <p id="price">{post.rental_price}</p>
            </div>  
            </a>
        </div>
    );
}

export default Rental;