import React from 'react'
import './Result.css'
import Rental2 from './Rental2'

function Result(){
    return(
        <div id="result">
        <h2>Results</h2>
        <Rental2 description={"Bruh Boat"} price={"35"} photo={require("../components/boat.jpg")}/>
        </div>
    );
}

export default Result;