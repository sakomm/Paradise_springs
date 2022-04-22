import React, {useState} from 'react'
import './TypesOfStays.css'
import axios from 'axios';
import {useDispatch} from 'react-redux'
import { getResults } from '../actions/posts';
import {Link} from 'react-router-dom'
import { useSelector} from 'react-redux'
import * as api from '../api'
import {getPosts} from '../actions/posts'



function TypesOfStays(){
    
    const dispatch = useDispatch();
    const handleClick = () =>{
       dispatch(getPosts({
        params:{
            state: ["Florida", "California", "Hawaii"],
            city: ""
        }
    }));
       
       
    }
    const handleClick1 = () =>{
        dispatch(getPosts({
            params:{
                state: "",
                city: ["Nashville", "Atlanta", "Chicago"]
            }
        }));

            
    }

    const handleClick2 = () =>{
        dispatch(getPosts({
            params:{
                state: ["Colorado", "Montana", "Wyoming"],
                city: ""
            }
        }));
            
    }
    const handleClick3 = () =>{
        dispatch(getPosts({
            params:{
                state: ["Hawaii", "", ""],
                city: ""
            }
        }));
            
    }
    const handleClick4 = () =>{
        dispatch(getPosts({
            params:{
                state: ["West Virginia", "Louisiana", "North Carolina"],
                city: ""
            }
        }));
            
      
    }
    return(
        <div id="types">
              <h1>Choose Your Type of Stay</h1> 
              <div id ="outer-div">
                  <div id="circle1"></div>
                  <div className = "inner-div">
                  <Link id="result-link1" to="/ResultsPage"><a id="beach" onClick={handleClick} data-value="beach"><div className="stay"><img src= { require("./beach-stay.jpg") } /><p className="place-label">Beach</p></div></a></Link>
                  <Link id="result-link1" to="/ResultsPage"><a id="city" onClick={handleClick1} data-value="city"><div className="stay"><img src ={ require("./city.jpg") }  /><p className="place-label">City</p></div></a></Link>
                  <Link id="result-link1" to="/ResultsPage"> <a id="mountain" onClick={handleClick2} data-value="mountain"><div className="stay"><img src={ require("./mountain.jpg") } /><p className="place-label">Mountain</p></div></a></Link>
                  <Link id="result-link1" to="/ResultsPage"> <a id="water" onClick={handleClick3} data-value="water"><div className="stay"><img src= { require("./boat.jpg") } /><p className="place-label">On the Water</p></div></a></Link>
                  <Link id="result-link1" to="/ResultsPage"> <a id="country" onClick={handleClick4} data-value="country"><div className="stay"><img src= { require("./country.jpg") } /><p className="place-label">Country</p></div></a></Link>
                   </div> 
                   <div id="circle1"></div>
              </div>
        </div>
    );
}

export default TypesOfStays;