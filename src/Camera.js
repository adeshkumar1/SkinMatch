import './App.css';
import { Link } from 'react-router-dom';
import Webcam from 'react-webcam';
import React, { useRef, useCallback } from 'react';

import Navigation from './Navigation';

function Camera() {
    const webcamRef = useRef(null);

    return (
        <div>
            <Navigation />

        </div>
    );
}

export default Camera;
