import React, {useState, useEffect} from 'react'
import Rental from './Rental';
import './DisplayRentals.css';
import { Data1 } from '../MockData/Data1'
import { useSelector } from 'react-redux'
import { CircularProgress } from '@material-ui/core'
import * as api from '../api'


function DisplayRentals(){
    const[posts, setPosts] = useState([]);
    useEffect(() => {
        api.fetchPosts({
            params:{
                state:"",
                city:""
            }
        })
            .then(response => {
                setPosts(response.data);
                console.log(response.data)
            });
    }, []);
    
    
    return(
        !posts.length? <CircularProgress /> : (
        <div className="container">
           
               {posts.map((post) => (
                   <Rental key = {post._id} post={post} />
               ))}
            
        </div>
        )
    );
}

export default DisplayRentals;