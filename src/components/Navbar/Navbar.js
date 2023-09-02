import React, { useContext,useState,useEffect } from 'react';
import logo from '../../assets/img/logo.png';
import { gapi } from 'gapi-script';
function Navbar() {
  // Assume your authentication context provides a `isLoggedIn` property
  const isLoggedIn = localStorage.getItem('accessToken');
  const accessToken = isLoggedIn;
  const [userinfo,setUserinfo]=useState();

  useEffect(()=>{
    //FETCH API
       // Make a request to the Google API to fetch user information
        fetch('https://www.googleapis.com/oauth2/v1/userinfo?alt=json', {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        })
          .then((response) => response.json())
          .then((data) => {
            // `data` contains user information, including the username
            console.log('User information:', data);
            setUserinfo(data);
            // You can access the username as data.email or data.name, depending on the response format
          })
          .catch((error) => {
            console.error('Error fetching user information:', error);
          });
    //FETCH API
  },[])
   
  return (
    <header>
      <p className="title">
        <img src={logo} alt="Mail QA" height="85%" />
      </p>

      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          {isLoggedIn ? null : <li><a href="/signup">Signup</a></li>} 
          {isLoggedIn ? null : <li><a href="/login">Login</a></li>}
          <li><a href="/prompt">Prompt</a></li>
          <li><a href="/prompt">{userinfo ? userinfo.name ? 'Online' : 'Offline' : 'Loading..'}</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Navbar;
