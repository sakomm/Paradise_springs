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
                <Link to="/" className="logo">
                    Paradise Springs
                    <i className ="fa-solid fa-umbrella-beach"/>               
                </Link>
                <div className= 'burger-menu' onClick= {handleClick}>
                    <i className= {click ? 'fas fa-times' : 'fas fa-bars'}/>
                </div>
                    <ul className={click ? 'nav-menu mobile' : 'nav-menu' }>
                        {MenuItems.map((item, index)=>{
                                return(
                                    <li key = {index}>
                                        <a className={item.cName} href ={item.url}>
                                        {item.title}
                                    </a></li>

                                )
                         })}
                    </ul>
                
            </div>
        </nav>
    );
}

export default Navbar;