import React, {useState, useEffect} from 'react'
import './Rental2.css'
import { useDispatch, useSelector } from 'react-redux'
import {getRating} from '../actions/posts'
import axios from "axios";
import * as api from '../api'

function Rental2({post}){
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
        <div id = "rental2">
             <a id ="house-url1" href = {post.room_link}>
            <div id="imgDiv" >
            <img className="rentalPostPic" src= {post.rental_image}></img>
            </div>
            <div id = "textDiv" >
            <div id="top-half">
            <p id="property" className="postText1">{post.rental_name}</p>
            <p className="postText">Safety Rating: {rated} </p>
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