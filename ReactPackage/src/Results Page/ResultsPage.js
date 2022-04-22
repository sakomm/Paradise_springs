import './ResultsPage.css'
import Topbar from './Topbar'
import Sidebar from './Sidebar'
import Result from './Result'
import Navbar from '../components/Navbar'
import { useSelector } from 'react-redux'
import React, {useState, useEffect} from 'react'


function ResultsPage(){
    const posts =useSelector((state)=>state.posts);
    console.log(posts);
    
    if(posts.length>0){
        
        localStorage.setItem('posts', JSON.stringify(posts));
        //console.log(JSON.parse(localStorage.getItem('posts')));
    
    }

    return(

        <div id="resultpage">
        <Topbar />
        <div id = "section-one">
        <Sidebar />
        <Result />
        </div>
        </div>
    );
}

export default ResultsPage;