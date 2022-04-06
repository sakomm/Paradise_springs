import React from 'react'
import './TypesOfStays.css'


function TypesOfStays(){
    return(
        <div id="types">
              <h1>Choose Your Type of Stay</h1> 
              <div id ="outer-div">
                  <div id="circle1"></div>
                  <div className = "inner-div">
                      <div className="stay"><img src= { require("./beach-stay.jpg") } /></div>
                      <div className="stay"><img src ={ require("./city.jpg") }  /></div>
                      <div className="stay"><img src={ require("./beach-stay.jpg") } /></div>
                      <div className="stay"><img src= { require("./boat.jpg") } /></div>
                      <div className="stay"><img src= { require("./country.jpg") } /></div>
                   </div> 
                   <div id="circle1"></div>
              </div>
        </div>
    );
}

export default TypesOfStays;