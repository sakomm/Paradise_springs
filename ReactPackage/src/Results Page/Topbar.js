import React from 'react'
import './Topbar.css'
import Navbar from '../components/Navbar';
import MainPicture from '../components/MainPicture';
import Searchbar from '../components/Searchbar';

function Topbar(){
    return(
        <div id="topbar">
            <Navbar />
            <MainPicture />
            <Searchbar />
        </div>
    );
}

export default Topbar;