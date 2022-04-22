import React, {useEffect } from 'react'
import './App.css';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import ResultsPage from './Results Page/ResultsPage'

import LandingPage from './LandingPage/LandingPage';

function App() {

  

  return (
    <BrowserRouter>
    <div className="App">
  
    
     <Link to="/sakomm/Paradise_springs"></Link>
    
    
    
     
    </div>

    <Routes>
      <Route exact path="/sakomm/Paradise_springs" element={<LandingPage />} />
      <Route path="/ResultsPage" element ={<ResultsPage />} />
    </Routes>
    </BrowserRouter>
  );
}

export default App;
