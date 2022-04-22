import React from 'react'
import './Topbar.css'
import Navbar from '../components/Navbar';
import MainPicture2 from './MainPicture2';
import Searchbar from '../Results Page/Searchbar2';

function Topbar(){
    return(
        <div id="topbar">
            <Navbar />
            <MainPicture2 />
            <Searchbar />
        </div>
    );
}

export default Topbar;