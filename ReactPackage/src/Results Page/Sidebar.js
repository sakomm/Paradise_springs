import { FormHelperText } from '@material-ui/core'
import React from 'react'
import './Sidebar.css'

// https://stackoverflow.com/questions/24369197/how-to-add-static-text-inside-an-input-form
function Sidebar(){
    // make a nice sidebar for the results page in the return statement have inputs for the number of people, city, and price range have the labels inside the inputs field


        return(

            
            <div id="sidebar">
                <h1 id="sidebar-title">Search Filters</h1>
                    <form>
                        <div id="people-inputs">
                            {/* <label for="input-people">Number of People:</label> */}
                            { /* center the label and input */ }
                            <input id="input-people" type="number" min="1" max="10" placeholder="Number of People"  />
                        </div>
                        <div id="city-inputs">
                            <label id="sidebar-label">City</label>
                            <input id="sidebar-input" type="text" name="city" />
                        </div>
                        <div id="price-inputs">
                            <label id="sidebar-label">Price Range</label>
                            <input id="sidebar-input" type="number" name="price" min="0" max="5000" step="100" defaultValue="0" />
                        </div>
                        <div id="rating-inputs">
                            <label id="sidebar-label">Rating</label>
                            <input id="sidebar-input" type="number" name="rating" min="0" max="5" step="1" defaultValue="0" />
                        </div>
                        <div id="checkin-inputs">
                            <label id="sidebar-label">checkin</label>
                            <input id="sidebar-input" type="date" name="rating" min="0" max="5" step="1" defaultValue="0" />
                        </div>
                        <div id="chekout-inputs">
                            <label id="sidebar-label">chekout</label>
                            <input id="sidebar-input" type="date" name="rating" min="0" max="5" step="1" defaultValue="0" />
                        </div>
                    </form>
            </div>
        );
    }
    

export default Sidebar;