import React from "react";
import './ResultsPage.css'
import TopBar from './Topbar'
import SideBar from './Sidebar'
import Result from './Result'

function ResultsPage(){
    return(
        <div id="resultspage">
        <TopBar />
        <SideBar />
        <Result />
        </div>
    );
}

export default ResultsPage;