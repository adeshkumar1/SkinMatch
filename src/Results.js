import './App.css';
import Navigation from './Navigation';
import ImageList from './ImageList';

import { useLocation } from 'react-router-dom';
import { useState } from 'react';

function Results() {
    
    const location = useLocation();
    const processingResults = location.state?.processingResults;
    let pathImages = processingResults['paths'];
    let summary = processingResults['summary'];

    const [imagePaths, setImagePaths] = useState(pathImages);

    console.log(pathImages);
    console.log(summary);

    return (
        <div>
            <Navigation />
            <div class="flex justify-center text-8xl mt-16 text-center fbask-reg">
                Results
            </div>
            <div>
                <ImageList imagePaths={imagePaths} />
            </div>
            <div className='text-center'>
                {summary}
            </div>
        </div>
    );
}

export default Results;
