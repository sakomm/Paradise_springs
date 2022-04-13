import React from 'react'
import './TypeaheadList.css';

class TypeaheadList extends React.Component{

render(){
    
    return(
        <div id="drop-down">
           
           <ul>
                {this.props.options.map((option) => {
                   return <li onClick= {this.props.onOptionSelection} className="location-options"> {option}</li>
                })}
                
           </ul>
        </div>
    );
}
}

export default TypeaheadList;