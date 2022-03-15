import React from 'react'
import './App.css';
import Searchbar from './components/Searchbar'
import Recommended from './components/Recommended'

function App() {
  return (
    <div className="App">
     <Searchbar />
     <Recommended />
    </div>
  );
}

export default App;
