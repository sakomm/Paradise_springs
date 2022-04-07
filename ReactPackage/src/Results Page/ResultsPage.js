import React from 'react'
import './ResultsPage.css'
import Topbar from './Topbar'
import Sidebar from './Sidebar'
import Result from './Result'


function ResultsPage(){
    return(
        <div id="resultpage">
        <Topbar />
        <div id = "section-one">
        <Sidebar />
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
        </form>
        <Result />
        </div>
        </div>
    );
}

export default ResultsPage;