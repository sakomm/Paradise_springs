import React, {useState} from 'react'
import './Carousel.css'
import Rental from './Rental'
import Button from './Button'
import DisplayRentals from './DisplayRentals';

class Carousel extends React.Component{
    constructor(props){
        super(props);
        this.state ={
            data1: "fa-solid fa-angle-right",
            data2: "fa-solid fa-angle-left"
        
        }
        this.slideLeft = this.slideLeft.bind(this);
        this.slideRight = this.slideRight.bind(this);
    }



slideRight = () =>{
        var slider = document.getElementById("postings-only");
        slider.scrollLeft = slider.scrollLeft + slider.offsetWidth;
}


slideLeft = () =>{
    var slider = document.getElementById("postings-only");
    slider.scrollLeft = slider.scrollLeft - slider.offsetWidth;
}



render(){
    return(
        <div>
            <div id="c-container">
                <div className="carousel">
                    <Button icon ={this.state.data2} slide = {this.slideLeft}/>   
                    <div id="postings-only">
                    <DisplayRentals />
                    </div>
                    <Button icon ={this.state.data1} slide = {this.slideRight}/>
                 </div> 
            </div> 
        </div>
    );
}
}
export default Carousel;