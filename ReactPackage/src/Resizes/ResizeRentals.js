import React, { useEffect } from 'react'

function myComponent(){
   useEffect(()=>{
       function handleResize(elementIdString){
        document.getElementById(elementIdString).innerwidth = document.getElementById('#c-container').innerwidth /
       }
       window.addEventListener('resize', handleResize()); 
   });
}