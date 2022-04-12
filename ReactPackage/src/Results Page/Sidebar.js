import React from 'react'
import './Sidebar.css'



function Sidebar(){
    return(
        <div id="sidebar">
        <h1 className='Sideheader'>Filters </h1>
        <form>
            <div />
            <label>
                <input type="checkbox" name="oneperson" />
                One Person
            </label>
            <div />
            <label>
                <input type="checkbox" name="twoperson" />
                Two Person
            </label>
            <div />
            <label>
                <input type="checkbox" name="Threeperson" />
                Three Person
            </label>
            <div />
            <label>
                <input type="checkbox" name="beachfront" />
                Beachfront
            </label>
            <div />
            <label>
                <input type="checkbox" name="city" />
                City
            </label>
            <div />
            <label>
                <input type="range" min="$1" max="$100" class="slider" id="pricerange" />
                Price
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