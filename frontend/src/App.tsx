import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/dashboard">Dashboard</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/" element={
            <div className="App-header">
              <h1>Welcome to NeurAI Explorer</h1>
              <Link to="/dashboard" className="dashboard-link">
                Go to Dashboard
              </Link>
            </div>
          } />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
