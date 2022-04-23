import { FormHelperText } from '@material-ui/core'
import React from 'react'
import './Sidebar.css'

// https://stackoverflow.com/questions/24369197/how-to-add-static-text-inside-an-input-form

function Sidebar(){
        return(

            <div id="sidebar">
                <h1 id="sidebar-title">Search Filters</h1>
                    <form>
                        <div id="bed-inputs">
                            <input id="input-bed" type="number" min="1" max="10" placeholder="Number of Beds" />
                        </div>
                        <div id="price-inputs">
                            <input id="sidebar-input" type="number" name="price" min="0" max="5000" step="100" placeholder='Price Range'/>
                        </div>
                        <div id="saftey-inputs">
                            <input id="sidebar-input" type="number" name="Saftey" min="0" max="100" step="5" placeholder='Saftey Filter'/>
                        </div>
                        <div id="rating-inputs">
                            <input id="sidebar-input" type="number" name="rating" min="0" max="5" step="1" placeholder='Rating' />
                        </div>
                        <div id = "platform-selector">
                            <select id="platform-select" multiple> 
                                <option value="AirBnB">AirBnB</option>
                                <option value="Booking">Booking.com</option>
                                <option value="VRBO">VRBO</option>
                                <option value="Hotels">Hotels.com</option>
                            </select>    
                        </div>
                        <div id = "submit-button">
                            <button id="submit-button" type="submit">Submit</button>
                        </div>
                    </form>
            </div>
        );
    }
    

export default Sidebar;