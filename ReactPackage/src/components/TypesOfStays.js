import React, {useState} from 'react'
import './TypesOfStays.css'
import axios from 'axios';
import {useDispatch} from 'react-redux'
import { getResults } from '../actions/posts';
import {Link} from 'react-router-dom'
import { useSelector } from 'react-redux'
import * as api from '../api'

var filter;
function TypesOfStays(){
    const [filters, setFilters] = useState({location: [], checkin: '', checkout: '', guests: ''});
    
    const handleClick = () =>{
        filter = "beach";
        setFilters({...filters, location:['Florida', 'Hawaii', 'California']})
        var listings = api.fetchResults(filters)
            .then(response => console.log(response.data));
       
    }
    const handleClick1 = () =>{
        filter = "city";
    }
    const handleClick2 = () =>{
        filter = "mountain";
    }
    const handleClick3 = () =>{
        filter = "water";
    }
    const handleClick4 = () =>{
        filter = "country";
      
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