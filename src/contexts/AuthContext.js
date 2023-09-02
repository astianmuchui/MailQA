import React, { createContext, useContext, useState } from 'react';

// Create the AuthContext
const AuthContext = createContext();

// Create a custom hook to use the AuthContext
export function useAuth() {
  return useContext(AuthContext);
}

// Create the AuthProvider component
export function AuthProvider({ children }) {
  // State to manage the authentication status
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Function to log in the user
  function login() {
    setIsLoggedIn(true);
    // You can also perform additional tasks like storing tokens, user data, etc.
  }

  // Function to log out the user
  function logout() {
    setIsLoggedIn(false);
    // You may also need to clear stored tokens and user data here.
  }

  // Value to be provided by the context
  const authContextValue = {
    isLoggedIn,
    login,
    logout,
  };

  return (
    <AuthContext.Provider value={authContextValue}>
      {children}
    </AuthContext.Provider>
  );
}
export default AuthContext;