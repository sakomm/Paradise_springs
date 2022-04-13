import React, { useState } from 'react'
import './Navbar.css'
import { Link } from 'react-router-dom'
import { MenuItems } from "./MenuItems"

function Navbar(){
    const [click, setClick]=useState(false);
    const handleClick = () => setClick(!click);
    return(
        <nav className='navbar'>
            <div className='navbar-container'>
                <Link to="/sakomm/Paradise_springs" className="logo">
                    Paradise Springs
                    <i className ="fa-solid fa-umbrella-beach"/>               
                </Link>
               
                
            </div>
        </nav>
    );
}

export default Navbar;