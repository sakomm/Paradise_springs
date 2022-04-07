import React from 'react'
import './ResultsPage.css'
import Topbar from './Topbar'
import Sidebar from './Sidebar'
import Result from './Result'
import Navbar from '../components/Navbar'


function ResultsPage(){
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