import React from 'react'
import './Recommended.css'
import Rental from './Rental'

function Recommended(){
    return(
        <div>
            <h1>Recommended Stays</h1> 
            <Rental />
            <Rental />
            <Rental />
            <Rental />           
        </div>
    );
}

export default Recommended;