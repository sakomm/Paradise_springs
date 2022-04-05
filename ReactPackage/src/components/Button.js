import React from 'react'
import './Button.css'



class Button extends React.Component{
 
    render(){
    return(
        <div id="circle">
            <button id="circleButton">
               <i id="border" class={ this.props.icon } />
            </button>
        </div>
    );
    }
}


export default Button;