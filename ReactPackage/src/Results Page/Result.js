import React from 'react'
import './Result.css'
import Rental2 from './Rental2'

function Result(){
    return(
        <div id="result">
        <h2>Results</h2>
        <Rental2 description={"Waterfront beach property in Virginia Beach"} price={"35"} photo={require("../components/boat.jpg")}/>
        <Rental2 description={"Wooden Cabin in Charlottsville, Virginia"} price={"50"} photo={"https://www.trulogsiding.com/wp-content/uploads/2019/12/word-image-12-1024x684.png"}/>
        </div>
    );
}

export default Result;