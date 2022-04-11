import React, { useState } from 'react'
import './Searchbar.css'

import { usaCities } from './usaCities';

var numberOfGuests =0;
function Searchbar(){
    
    const guestInc = () =>{
        numberOfGuests++;
        document.getElementById('guest-text').innerHTML = numberOfGuests;
        document.getElementById('hidden-but').value =numberOfGuests;
    }
    const guestDec = () =>{
        if(numberOfGuests>0)
            numberOfGuests--;
        document.getElementById('guest-text').innerHTML = numberOfGuests;
        document.getElementById('hidden-but').value =numberOfGuests;
    }

    //const [click, setClick]=useState(false);
    const handleClick = () => {
        document.getElementsByClassName('popup')[0].className = "show";
    }

    const handleClick2 = () => {
        document.getElementsByClassName('show')[0].className = "popup";
    }

    const handleEntailmentRequest= (e)=> {
        e.preventDefault();
    }
    var Typeahead = require('react-typeahead').Typeahead;
   
    return(
        <div id = "search-div" >
        <form onSubmit={""}>
            <div className = "search center" >
               
                <Typeahead placeholder ={'Where do you want to go?'} inputProps={{className: "place", style: {
                    'border-style': 'none',
                    'height': '100%',
                    'width': '100%',
                    'border-radius': '8px 0px 0px 8px',
                    'outline': 'none',
                    'text-align': 'center',
                    'display': 'block',
                    'margin':'0',
                    'border-right-style': 'solid',
                    'border-box': 'box-sizing',
                    'background-color' :'transparent',
                }}} className='place'
                customClasses={{listItem:'locations',
                listAnchor: 'locations',
                results: 'type-results'}} options = {usaCities} maxVisible = {10} />
                     
                     <input type="date" className="in-dates center-text" placeholder="check-in" onClick={handleClick2}></input>
                     <input type="date" className="out-dates center-text" placeholder="check-out" onClick={handleClick2}></input>
                     <div id ="guests" onClick={handleClick} >
                        <span className="popup" >
                            <button id="hidden-but" value={numberOfGuests}></button >
                            <p id="guest-font">Guests</p>
                            <div id="button-cont">
                               <div id="but-one"> <div className="g-button" onClick ={guestDec}>-</div></div>
                               <p id="guest-text">0</p>
                               <div id="but-two"><div className="g-button" onClick={guestInc}>+</div></div>
                            </div>
                        </span>
                     </div>
                     <div className="search-icon" onClick={handleClick2}>
                        <button id="search-button">
                            <i  class="fas fa-search"></i>
                        </button>
                    </div>
                    
            
            </div>
            </form>
            </div>

    );
}

export default Searchbar;