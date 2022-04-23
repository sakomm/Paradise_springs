import React, {useState, useEffect} from 'react'
import Rental2 from './Rental2';
import './DisplayRentals2.css';
import { useSelector } from 'react-redux'
import { CircularProgress } from '@material-ui/core'
import * as api from '../api'



function DisplayRentals2(){

   
    var posts =useSelector((state)=>state.posts);
    const[post, setPosts] = useState([]);
   
   
    if(posts.length==0){
        setPosts(JSON.parse(localStorage.getItem('posts')));
    }
    
    
    
    
    console.log(posts);
    
    return(
        !posts.length? <CircularProgress /> : (
        <div className="container1">
           
               {posts.map((post) => (
                   <Rental2 key = {post._id} post={post} />
               ))}
            
        </div>
        )
    );
}

export default DisplayRentals2;