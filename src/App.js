import './assets/css/style.css';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Navbar from './components/Navbar/Navbar';
import Landing from './components/Main/Landing';
import Login from './login/login';
import Signup from './signup/signup';
import Prompt from './components/prompt/Prompt';
import { AuthProvider } from './contexts/AuthContext';

function App() {
  return (
    <AuthProvider>
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
      <Landing />
    </AuthProvider>
  );
}

export default App;
