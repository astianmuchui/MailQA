import './assets/css/style.css';

import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import Landing from './components/Main/Landing';
import Login from './login/login';
import Signup from './signup/signup';
import Prompt from './components/prompt/Prompt';
import { useEffect } from 'react';
import { gapi } from 'gapi-script';

function App() {
  useEffect(() => {
    function start() {
      gapi.client.init({
        clientId:'965274681666-p08jm4et6g955b9fmm0jeirg410qcug4.apps.googleusercontent.com',
        scope: '',
      });
    }

    gapi.load('client:auth2', start);
  }, []);
  return (
    <>
      <Navbar /> 
      <BrowserRouter>
        <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} /> 
            <Route path="/prompt" element={<Prompt />} /> 
            <Route path="/*" element={<Landing />} />
          </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
