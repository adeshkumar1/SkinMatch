import './App.css';
import { Link } from 'react-router-dom';
import Webcam from 'react-webcam';
import React, { useRef, useCallback, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import Navigation from './Navigation';

function Camera() {
    const webcamRef = useRef(null);
    const [pictureCount, setPictureCount] = useState(0);
    const navigate = useNavigate();
    
    let captureGoalText = [
        "Please take a picture of your face in a front facing angle",
        "Please take a picture of the left side of your face",
        "Please take a picture of the right side of your face",
        "Please take a picture of your forehead",
    ];

    let imageBlobs = [];

    const sendToBackend = () => {

    }

    const captureImage = useCallback(() => {
        const currImage = webcamRef.current.getScreenshot();
        const blob = base64ToBlob(currImage, 'image/png');
        const formData = new FormData();
        formData.append("face-scans", blob, 'image.png');
        imageBlobs.push(formData);
        console.log("a");
        setPictureCount(prevCount => {
            const newCount = prevCount + 1;
            if (newCount >= 4) {
                navigate('/aboutus');
                fetch('http://localhost:8000/process_images', {
                    method: 'POST',
                    body: imageBlobs,
                })
                .then(response => response.json())
                .then(data => {
                    console.log("Image processed: ", data);
                })
            }
            return newCount;
        });

    }, [webcamRef]);

    return (
        <div>
            <Navigation />
            <div className='flex justify-center my-8'>
                <Webcam audio={false} ref={webcamRef} />
            </div>
            <div className='fbask-reg text-xl text-center mb-8'>
                {captureGoalText[pictureCount]}
            </div>
            <div className='flex justify-center'>
                <button className='p-4 fbask-reg text-3xl text-center border-2 border-black rounded-xl' onClick={captureImage}>Capture Image</button>
            </div>
        </div>
    );
}

export default Camera;
