import React from 'react';

function ImageList({ imagePaths }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      {imagePaths.map((imageName, index) => (
          <img
          key={index}
          src={`face_images/${imageName}`} // Adjust the path accordingly
          alt={`face_images/${imageName}`}
          className="w-full h-auto rounded-md"
          />
      ))}
    </div>
  );
}

export default ImageList;