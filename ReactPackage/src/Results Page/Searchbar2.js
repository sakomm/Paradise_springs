import React, { useState } from 'react'
import './Searchbar2.css'
import {Link} from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import {getPosts} from '../actions/posts'

import { usaCities } from '../components/usaCities';

var numberOfGuests =0;
function Searchbar2(){
    
    const posts =useSelector((state)=>state.posts);
    const dispatch = useDispatch();
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

    const onSubmit = () =>{
        var location = document.getElementsByClassName("place")[0].getElementsByTagName('input')[0].value;
        var index = location.indexOf(',');
        var city =undefined;
        if(index>-1){
         city = location.substring(0,index).trim();
        }
        
        var state = location.substring(index+1).trim();
        var checkin = document.getElementById("c1").value;
        var checkout = document.getElementById("c2").value;
        var guests = document.getElementById("hidden-but").value;
        if(guests=="0"){
            guests=undefined;
        }
        else{
            guests = guests+ " guests";
        }
        localStorage.setItem("state", state);
        localStorage.setItem("city", city);
        localStorage.setItem("guests", guests);
        
        console.log(checkout);
        dispatch(getPosts({
            params:{
                state: state,
                city: city,
                rental_amenities: guests,
                check_in: Date(checkin).toISOString,
                check_out: Date(checkout).toISOString,
                

            }
        }));
       
        
        
    }

    var Typeahead = require('react-typeahead').Typeahead;
   
    return(
        <div id = "search-div1" >
        <form method ="post" action= "createQuery.php">
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
                    'font-size': '1.5vh'
                }}} className='place'
                customClasses={{listItem:'locations2',
                listAnchor: 'locations1',
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
                    
                     <div className="search-icon">
                     <Link id="result-link" to="/ResultsPage" >
                        <button type="submit" name="Submit" id="search-button" onClick={onSubmit}>
                            <i  className="fas fa-search font"></i>
                        </button>
                        </Link>
                    </div>
                    
                    
            
            </div>
            </form>
            </div>

    );
}

export default Searchbar2;