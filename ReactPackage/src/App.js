import React from 'react'
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Searchbar from './components/Searchbar'
import Recommended from './components/Recommended'
import Navbar from './components/Navbar'
import Places from './components/Places'
import Footer from './components/Footer'
import ResultsPage from './Results Page/ResultsPage'

function App() {
  return (
    <div className="App">
      <Router>
      <Navbar />
      <Routes>
        <Route path ="/" exact></Route>
      </Routes>
    </Router>
     <Searchbar />
     <Places />
     <Footer />
     
     
    </div>
  );
}

export default App;
