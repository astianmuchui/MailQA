import React from 'react';
import { GoogleLogin } from 'react-google-login';

function Login() {
  const responseGoogle = (response) => {
    console.log(response); // You can handle the response here

    // Check if the response contains an access token
    if (response.accessToken) {
      // Store the access token in localStorage
      localStorage.setItem('accessToken', response.accessToken);

      // You can also store other user information if needed
      localStorage.setItem('userProfile', JSON.stringify(response.profileObj));

      // Typically, you'd send the response to your server for authentication and user creation.
    }
  };

  const accessToken = localStorage.getItem('accessToken');
  if(accessToken){
    window.location.href='/prompt';
  }

  return (
    <main>
      <div className="form-container shadowed">
        <h2 className="txt-gradient">Welcome on board</h2>

        <div className="google-btn">
          <GoogleLogin
            clientId="965274681666-p08jm4et6g955b9fmm0jeirg410qcug4.apps.googleusercontent.com"
            buttonText="Sign In with Google" 
            onSuccess={responseGoogle}
            onFailure={responseGoogle}
            cookiePolicy={'single_host_origin'}
          />
        </div>
      </div>
    </main>
  );
}

export default Login;
