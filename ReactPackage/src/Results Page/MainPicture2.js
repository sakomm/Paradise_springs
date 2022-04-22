import React from 'react'



function MainPicture2(){

    const handleClick2 = () => {
        document.getElementsByClassName('show')[0].className = "popup";
    }
    return(
        <div id="back-one" onClick={handleClick2}>
               
        </div>
    );
}

export default MainPicture2;