import React from 'react'



function MainPicture(){

    const handleClick2 = () => {
        document.getElementsByClassName('show')[0].className = "popup";
    }
    return(
        <div id="back" onClick={handleClick2}>
               
        </div>
    );
}

export default MainPicture;