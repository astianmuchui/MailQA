import './assets/css/style.css';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import Landing from './components/Main/Landing';
import Login from './login/login';
import Signup from './signup/signup';
function App() {
  return (
    <div>
      <Navbar /> 
      <BrowserRouter>
        <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} /> 
            <Route path="/*" element={<Landing />} />
          </Routes>
      </BrowserRouter>
      <Landing />
    </div>
  );
}

export default App;
