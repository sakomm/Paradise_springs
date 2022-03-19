import React from 'react'
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Searchbar from './components/Searchbar'
import Recommended from './components/Recommended'
import Navbar from './components/Navbar'

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
     <Recommended />
    </div>
  );
}

export default App;
