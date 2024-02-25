<<<<<<< HEAD
import "./App.css";

import { useEffect } from "react";
import Navigation from "./Navigation";
// import ImageList from './ImageList';

import { useLocation } from "react-router-dom";
import { useState } from "react";
import ProductCard from "./ProductCard";

function Results() {
  const location = useLocation();
  const processingResults = location.state?.processingResults;
  let pathImages = processingResults["paths"];
  let summary = processingResults["summary"];
  let products = processingResults["products"];
  console.log(products);

  useEffect(() => {
    // Perform a GET request to fetch the processed results
    fetch("http://localhost:8000/process_images", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the data received from the server
        console.log("Results:", data);
        // You can update your component state or take other actions based on the data
      })
      .catch((error) => {
        console.error("Error fetching results:", error);
      });
  }, []);

  return (
    <div>
      <Navigation />
      <div class="flex justify-center text-5xl my-12 text-center fbask-reg">
        Your skin match
      </div>
      {/* <div>
                <ImageList imagePaths={imagePaths} />
            </div> */}
      <div className="text-center fbask-reg text-2xl mx-64 mb-8">{summary}</div>
      <div className="text-center fbask-ital text-2xl mx-64 mb-16">
        Here are some products that you can use...
      </div>
      <div className="mx-64 fbask-reg">
        <ProductCard products={products} index={0} />
        <ProductCard products={products} index={1} />
        <ProductCard products={products} index={2} />
        <ProductCard products={products} index={3} />
        <ProductCard products={products} index={4} />
        <ProductCard products={products} index={5} />
        <ProductCard products={products} index={6} />
        <ProductCard products={products} index={7} />
      </div>
    </div>
  );
=======
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
>>>>>>> 2d40a058 (results changes)
}

export default Results;
