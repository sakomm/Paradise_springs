import React from 'react'
import './App.css';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Searchbar from './components/Searchbar'
import Recommended from './components/Recommended'
import Navbar from './components/Navbar'
import Places from './components/Places'
import Footer from './components/Footer'
import ResultsPage from './Results Page/ResultsPage'
import MainPicture from './components/MainPicture';
import LandingPage from './LandingPage/LandingPage';

function App() {
  return (
    <BrowserRouter>
    <div className="App">
  
    
     <Link to="/sakomm/Paradise_springs"></Link>
     <Link to="/ResultsPage"></Link>
    
    
     
    </div>

    <Routes>
      <Route exact path="/sakomm/Paradise_springs" element={<LandingPage />} />
      <Route path="/ResultsPage" element ={<ResultsPage />} />
    </Routes>
    </BrowserRouter>
  );
}

export default App;
