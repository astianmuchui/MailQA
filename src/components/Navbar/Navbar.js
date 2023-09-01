import React from 'react'

function Navbar() {
  return (
      <header>
        <p className="title">Mail Wise</p>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/signup">Signup</a></li>
            <li><a href="/login">Login</a></li>
          </ul>
        </nav>
      </header>
  )
}

export default Navbar
