import './App.css';

import { useEffect } from 'react';
import Navigation from './Navigation';

function Results() {

    useEffect(() => {
        // Perform a GET request to fetch the processed results
        fetch('http://localhost:8000/process_images', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            // Handle the data received from the server
            console.log('Results:', data);
            // You can update your component state or take other actions based on the data
        })
        .catch(error => {
            console.error('Error fetching results:', error);
        });
    }, []);

    return (
        <div>
            <Navigation />
            <div class="flex justify-center text-8xl mt-16 text-center fbask-reg">
                Results
            </div>
            
        </div>
    );
    }

export default Results;
