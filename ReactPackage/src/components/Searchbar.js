import React from 'react'
import './Searchbar.css'

function Searchbar(){
    var guestVal=0;
    const numOfGuest = ()=>{
        guestVal++;

    }
    return(
        <div id = "back">
        
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

export default Searchbar;