import React, {useState} from 'react'
import './Carousel.css'
import Rental from './Rental'
import Button from './Button'
import DisplayRentals from './DisplayRentals';

class Carousel extends React.Component{
state ={
    data1: "fa-solid fa-angle-right",
    data2: "fa-solid fa-angle-left"

}

slideRight = () =>{
    var slider = document.getElementById("#post");
    slider.scrollLeft = slider.scrollLeft + 500;
}

slideLeft = () =>{
    var slider = document.getElementById("#post");
    slider.scrollLeft = slider.scrollLeft + 500;
}

this.sildeLeft =this.slideLeft.bind(this);

render(){
    return(
        <div>
            <div id="c-container">
                <div className="carousel">
                    <Button icon ={this.state.data2} onClick = {this.slideLeft}/>   
                    <div id="postings-only">
                    <DisplayRentals />
                    </div>
                    <Button icon ={this.state.data1}/>
                 </div> 
            </div> 
        </div>
    );
}
}
export default Carousel;