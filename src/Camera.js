import './App.css';
import { Link } from 'react-router-dom';
import Webcam from 'react-webcam';
import React, { useRef, useCallback } from 'react';

import Navigation from './Navigation';

function Camera() {
    const webcamRef = useRef(null);

<<<<<<< HEAD
    return (
        <div>
            <Navigation />

=======
    const sendToBackend = () => {

    }

    const captureImage = useCallback(() => {
        const currImage = webcamRef.current.getScreenshot();
        fetch('/apicall', {
            method: 'POST',
            body: JSON.stringify({ image:currImage })
        })
            .then(response => response.json())
            .then(data => console.log("Image processed: ", data))
    }, [webcamRef]);

    return (
        <div>
            <Navigation />
            <div className='flex justify-center my-8'>
                <Webcam audio={false} ref={webcamRef} />
            </div>
            <div className='flex justify-center'>
                <button className='p-4 fbask-reg text-3xl text-center border-2 border-black rounded-xl' onClick={captureImage}>Capture Image</button>
            </div>
>>>>>>> 25c235bd (Added camera to be added with Flask)
        </div>
    );
}

export default Camera;
