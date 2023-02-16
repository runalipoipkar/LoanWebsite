import React from 'react'
import { FaFacebookSquare , FaInstagram, FaYoutube} from "react-icons/fa";
import "./NavBar.css";

function NavBar() {
  return (
    <div className='NavBar'>
        <nav className="main-nav">
            {/* 1st logo */}
            <div className='logo'>
                <h2>
                    <span>L</span>oan
                    <span>B</span>azar
                </h2>
            </div>
            {/* 2nd Menu part */}
            <div className='menu-link'>
                <ul> 
                    <li><a href='#'>Home</a></li>
                    <li><a href='#'>About</a></li>
                    <li><a href='#'>Services</a></li>
                    <li><a href='#'>Contact</a></li>
                </ul>
            </div>
            {/* 3rd part social-media */}
            <div className='social-media'>
                <ul className='social-media-desktop'>
                    <li>
                        <a href='#'><FaFacebookSquare  className='facebook'/></a>
                    </li>
                    <li>
                        <a href='#'><FaInstagram  className='insta'/></a>
                    </li>
                    <li>
                        <a href='#'><FaYoutube  className='youtube'/></a>
                    </li>
                </ul>
                {/* hamburget menu start */}
                
            </div>
        </nav>
        {/* hero section */}
    </div>
  )
}

export default NavBar;