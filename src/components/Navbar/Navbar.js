import React, { useContext } from 'react';
import logo from '../../assets/img/logo.png';
import AuthContext from '../../contexts/AuthContext'; // Import your authentication context

function Navbar() {
  // Assume your authentication context provides a `isLoggedIn` property
  const { isLoggedIn } = useContext(AuthContext);

  return (
    <header>
      <p className="title">
        <img src={logo} alt="Mail QA" height="85%" />
        <p>Hello {isLoggedIn ? 'Yes' : 'No' }</p>
      </p>

      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          {isLoggedIn ? null : <li><a href="/signup">Signup</a></li>} 
          {isLoggedIn ? null : <li><a href="/login">Login</a></li>}
          <li><a href="/prompt">Prompt</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Navbar;
