import React from 'react'
import './Topbar.css'
import Navbar from '../components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'


function Topbar(){
    return(
        <div id="topbar">
            <Navbar />
            <div className = "search center" >
                
                <input className='place center-text' type='text' value="Where would you like to go?"></input>
                <input type="date" className="in-dates center-text" value="check-in"></input>
                <input type="date" className="out-dates center-text" value="check-out"></input>
                <select className="guests center-text" value="guests">
                    <option value="0"></option>
               </select>
               <div className="search-icon">
                   <i  class="fas fa-search"></i>
               </div>
               
       
       </div>
        </div>
    );
}

export default Topbar;