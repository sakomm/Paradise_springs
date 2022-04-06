import React from 'react'
import './TypesOfStays.css'


function TypesOfStays(){
    return(
        <div id="types">
              <h1>Choose Your Type of Stay</h1> 
              <div id ="outer-div">
                  <div id="circle1"></div>
                  <div className = "inner-div">
                      <div className="stay"><img src= { require("./beach-stay.jpg") } /><p className="place-label">Beach</p></div>
                      <div className="stay"><img src ={ require("./city.jpg") }  /><p className="place-label">City</p></div>
                      <div className="stay"><img src={ require("./mountain.jpg") } /><p className="place-label">Mountain</p></div>
                      <div className="stay"><img src= { require("./boat.jpg") } /><p className="place-label">On the Water</p></div>
                      <div className="stay"><img src= { require("./country.jpg") } /><p className="place-label">Country</p></div>
                   </div> 
                   <div id="circle1"></div>
              </div>
        </div>
    );
}

export default TypesOfStays;