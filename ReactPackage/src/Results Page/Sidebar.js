import { FormHelperText } from '@material-ui/core'
import React from 'react'
import './Sidebar.css'

// https://stackoverflow.com/questions/24369197/how-to-add-static-text-inside-an-input-form

function Sidebar() {
    // Code for Platform selector inspired by https://web.dev/building-a-multi-select-component/ article by Adam Argyle 
    return (

        <div id="sidebar">
            <h1 id="sidebar-title">Search Filters</h1>
            <form>
                <label for="nbeds"> Number of Bedrooms: </label>
                <input aria-label='nbeds' id="sidebar-input" type="number" min="1" max="10" placeholder="Number of Beds" />
                <label for="price"> Price Max: </label>
                <input aria-lable='price' id="sidebar-input" type="number" name="price" min="0" max="5000" step="100" placeholder='Price Range' />
                <label for="saftey"> Safety Min: </label>
                <input aria-label='saftey' id="sidebar-input" type="number" name="Saftey" min="0" max="100" step="5" placeholder='Saftey Filter' />
                <label for="ratings"> Rating Min: </label>
                <input aria-lable='rating' id="sidebar-input" type="number" name="rating" min="0" max="5" step="1" placeholder='Rating' />

                <fieldset>
                    <legend>Platform Selector</legend>
                    <div>
                        <input type="checkbox" id="airbnb" name="platforms" value="airbnb" />
                        <label for="airbnb">AirBnB</label>
                    </div>
                    <div>
                        <input type="checkbox" id="hotels" name="platforms" value="hotels" />
                        <label for="hotels">Hotels.com</label>
                    </div>
                    <div>
                        <input type="checkbox" id="vrbo" name="platforms" value="vrbo" />
                        <label for="vrbo">VRBO</label>
                    </div>
                    <div>
                        <input type="checkbox" id="booking" name="platforms" value="booking" />
                        <label for="booking">Booking.com</label>
                    </div>
                </fieldset>

            </form>
        </div>

    
    );
}


export default Sidebar;