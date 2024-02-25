import './App.css';
import Webcam from 'react-webcam';
import React, { useRef, useCallback, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navigation from './Navigation';

const { v4: uuidv4 } = require('uuid');

function Camera() {
    const webcamRef = useRef(null);
    const [pictureCount, setPictureCount] = useState(0);
    const navigate = useNavigate();

    let captureGoalText = [
        "Please take a picture of your face in a front facing angle",
        "Please take a picture of the left side of your face",
        "Please take a picture of the right side of your face",
        "Please takae a picture of your forehead",
    ]

    const base64ToBlob = (base64, type) => {
        const byteString = atob(base64.split(',')[1]);
        const ab = new ArrayBuffer(byteString.length);
        const ia = new Uint8Array(ab);
        for (let i = 0; i < byteString.length; i++) {
            ia[i] = byteString.charCodeAt(i);
        }
        return new Blob([ab], { type });
    };


    let imagePaths = [];
    const captureImage = useCallback(async () => {
        const currImage = webcamRef.current.getScreenshot();
        const blob = base64ToBlob(currImage, 'image/png');
        const formData = new FormData();
        const filename = uuidv4() + ".png";
        formData.append("face-scans", blob, 'image.png')


        fetch('http://localhost:8000/process_images', {
            method: 'POST',
            headers: {
                'Content-Disposition': `attachment; filename="${filename}"`
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log("Image processed: ", data);
            imagePaths.push(filename);
            setPictureCount(prevCount => {
                const newCount = prevCount + 1;

                if (newCount >= 4) {
                    console.log()
                    navigate('/aboutus');
                }

                return newCount;
            });
        });

    }, [webcamRef, navigate]);

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
