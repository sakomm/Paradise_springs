import React from 'react'
import './Result.css'
import Rental2 from './Rental2'
import DisplayRentals2 from './DisplayRentals2';

function Result(){
    return(
        <div id="result">
        <h2>Results</h2>
        <DisplayRentals2 />
        </div>
    );
}

export default Result;