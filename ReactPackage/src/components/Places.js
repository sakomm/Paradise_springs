import React from 'react'
import './Places.css'
import Recommended from './Recommended.js'
import TypesOfStays from './TypesOfStays.js'


function Places(){
    return(
        <div id="places">
               <Recommended />
               <TypesOfStays /> 
        </div>
    );
}

export default Places;