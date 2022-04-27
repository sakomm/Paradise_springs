import React, {useState, useEffect} from 'react'
import Rental2 from './Rental2';
import './DisplayRentals2.css';
import { useSelector } from 'react-redux'
import { CircularProgress } from '@material-ui/core'
import * as api from '../api'



function DisplayRentals2(){

   
    const posts =useSelector((state)=>state.posts);
    const[posts1, setPosts] = useState([]);
    
    useEffect(() => {
        if(posts!=null)
            setPosts(posts);
        if(posts==null || posts.length==0){
            //console.log(JSON.parse(localStorage.getItem('posts')));
            setPosts(JSON.parse(localStorage.getItem('posts')));
            //console.log("one: "+ posts1)
        }
        
        
    
    },[posts]);
    
    
    //console.log("Posts2 :" + posts1);
    
    return(
        posts1==null? <CircularProgress /> : (
        <div className="container1">
           
               {posts1.map((post) => (
                   <Rental2 key = {post._id} post={post} />
               ))}
            
        </div>
        )
    );
}

export default DisplayRentals2;