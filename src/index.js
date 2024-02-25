import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

import './index.css';
import HeaderSection from './Frontpage';
import Camera from './Camera';
import AboutUs from './AboutUs';
import Results from './Results';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode className="overflow-none">
    <Router>
      <Routes>
        <Route path="/" element={<HeaderSection />} />
        <Route path="/camera" element={<Camera />} />
        <Route path="/aboutus" element={<AboutUs />} />
        <Route path="/results" element={<Results />} />
      </Routes>
    </Router>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
