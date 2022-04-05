import React, {useState} from 'react'
import './Carousel.css'
import Rental from './Rental'
import Button from './Button'

function Carousel(){

const [index, setIndex] = useState(0);

const slideLeft = () => {
    setIndex(index - 1);
};

const slideRight = () => {
    setIndex(index + 1);
};
    return(
        <div id="end-of-page">
                     <div id="c-container">
                <div className="carousel">
                    <Button onClick = {slideLeft}/>   
                    <div id="postings-only">
                        <Rental />
                        <Rental />
                        <Rental />
                        <Rental />
                        <Rental />
                        <Rental />
                        <Rental />
                        <Rental />
                        <Rental />
                        <Rental />
                    </div>
                    <Button onClick = {slideRight}/>
                 </div> 
            </div> 
        </div>
    );
}

export default Carousel;