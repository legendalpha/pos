import logo from './logo.svg';
import './App.css';
import React from 'react';
import ProductsPage from './ProductsPage'
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

function Products(){
  return(
    <div>
      <ProductsPage />
    </div>
  )
}
function AppWithRouting() {
  return (
    <BrowserRouter> 
      <Routes>
        <Route path="/" element={<App />} /> 
        <Route path="/products" element={<Products />} /> 
      </Routes>    
    </BrowserRouter>
  );
}

export default AppWithRouting;
