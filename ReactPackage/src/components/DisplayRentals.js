import React from 'react'
import Rental from './Rental';
import './DisplayRentals.css';
import { Data1 } from '../MockData/Data1'

function DisplayRentals(){
    return(
        <div className="container">
           
               {Data1.map((post) => {
                   return <Rental {...post} />
               })}
            
        </div>
    );
}

export default DisplayRentals;