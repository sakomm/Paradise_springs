import { FormHelperText } from '@material-ui/core'
import React from 'react'
import './Sidebar.css'
import { useDispatch, useSelector } from 'react-redux'
import {getPosts} from '../actions/posts'
import {Link} from 'react-router-dom'

// https://stackoverflow.com/questions/24369197/how-to-add-static-text-inside-an-input-form

function Sidebar() {
    
    // Code for Platform selector inspired by https://web.dev/building-a-multi-select-component/ article by Adam Argyle 
    const dispatch = useDispatch();
    const onSubmit = () =>{
        var beds =document.getElementById("beds").value;
        if(beds){
            beds =beds + " beds"
        }
        var price =document.getElementById("price-box").value;
        if(price){
            price ="$"+price+" per night"
        }
        var wifi;
        if(document.getElementById("wifi").checked){
            wifi = "Wifi"
        }

        var kitchen;
        if(document.getElementById("kitchen").checked){
            kitchen="Kitchen"
        }

        var airbnb;
        if(document.getElementById("airbnb").checked){
            airbnb="AirBnB"
        }

        var hotels;
        if(document.getElementById("hotels").checked){
            hotels="AirBnB"
        }

        
        
        
        dispatch(getPosts({
            params:{
                state: localStorage.getItem("state"),
                city: localStorage.getItem("city"),
                rental_amenities: localStorage.getItem("guests"),
                beds: beds,
                price: price,
                wifi:wifi,
                kitchen:kitchen,

            }
        }));

    }
   
    return (


        <div id="sidebar">
            <div id="side-cont">
            <h1 id="sidebar-title">Search Filters</h1>
            <form>
            <label for="price"> Price: </label>
                <input id ="price-box" aria-lable='price' className="sidebar-input" type="number" name="price" min="0" max="5000" step="100" placeholder='$' />
                <label for="nbeds"> Number of Beds: </label>
                <input id="beds" aria-label='nbeds' className="sidebar-input" type="number" min="1" max="10" placeholder="Number of Beds" />
                
                
                <fieldset>
                    <legend>Amenities</legend>
                    <div>
                    <input className="in amen" id ="wifi" aria-label='saftey'  type="checkbox" /><label for="saftey"> Wifi </label>
                    </div>
                    <div>
                    <input className="in amen" id ="kitchen" aria-label='saftey'  type="checkbox" /><label for="ratings"> Kitchen </label>
                    </div>
                    
                </fieldset>
                
               
                
                
                
                



                <fieldset>
                    <legend>Platform Selector</legend>
                    <div>
                        <input className="in" type="checkbox" id="airbnb" name="platforms" value="airbnb" />
                        <label for="airbnb"> AirBnB</label>
                    </div>
                    <div>
                        <input className="in" type="checkbox" id="hotels" name="platforms" value="hotels" />
                        <label for="hotels"> Hotels.com</label>
                    </div>
                    <div>
                        <input className="in" type="checkbox" id="vrbo" name="platforms" value="vrbo" />
                        <label for="vrbo"> VRBO</label>
                    </div>
                    <div>
                        <input className="in" type="checkbox" id="booking" name="platforms" value="booking" />
                        <label for="booking"> Booking.com</label>
                    </div>
                </fieldset>

            </form>

            
            <Link id="result-link" to="/ResultsPage" ><button id="update" onClick={onSubmit}>Update</button></Link>
        
            </div>
        </div>

    
    );
}


export default Sidebar;