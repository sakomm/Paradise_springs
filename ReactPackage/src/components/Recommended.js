import React, {useState} from 'react'
import './Recommended.css'
import './Carousel.js'
import $ from 'jquery'
import Carousel from './Carousel.js';




class Recommended extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            data1: "fa-solid fa-angle-left",
            data2: "fa-solid fa-angle-right"
            
        }
        
    
    }

    
    
   render(){ 
    return(
        <div id="rec-stays">
            
            <h1>Recommended Stays</h1> 
            <Carousel />
      
           
                 
        </div>
    );
    }
}

$(function(){
    $('#post').on('resize', function(){
       
    });
});

export default Recommended;