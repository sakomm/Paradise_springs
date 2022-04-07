import React from 'react'
import './Sidebar.css'



function Sidebar(){
    return(
        <div id="sidebar">
        <h1>Filters </h1>
        <form>
            <div />
            <label>
                One Person
                <input type="checkbox" name="oneperson" />
            </label>
            <div />
            <label>
                Two Person
                <input type="checkbox" name="twoperson" />
            </label>
            <div />
            <label>
                Three Person
                <input type="checkbox" name="Threeperson" />
            </label>
            <div />
            <label>
                Beachfront
                <input type="checkbox" name="beachfront" />
            </label>
            <div />
            <label>
                City
                <input type="checkbox" name="city" />
            </label>
            <div />
            <label>
                Price
                <input type="range" min="$1" max="$100" class="slider" id="pricerange" />
            </label>
            <div />
            <label>
                <input type="submit" id="submit" />
            </label>
        </form>
        </div>
    );
}

export default Sidebar;