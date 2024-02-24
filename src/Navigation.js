import './App.css';
import { Link } from 'react-router-dom';
import React, { useState, useEffect } from 'react';

function Navigation() {
<<<<<<< HEAD
    
    return (
        <div className='fbask-reg text-3xl border-b-black border-b-2'>
            <div className='flex justify-between'>
                <Link to="/">
                    <div>
                        <button className='flex fbask-reg p-4 mx-32'>
                            Skin <div className='fbask-ital'>Match</div>
                        </button>
                    </div>
                </Link>
                <Link to="/aboutus">
                    <button className='p-4 mx-32'>
                        About Us
                    </button>
                </Link>
                <Link to="/camera">
                    <button className='p-4 mx-32'>
                        Camera
                    </button>
                </Link>
            </div>
        </div>
    );
=======
  return (
    <div className='fbask-reg text-2xl border-b-black border-b-2'>
        <div className='flex justify-between'>
            <Link to="/">
                <div>
                    <button className='flex fbask-reg p-4 mx-4'>
                        Skin <div className='fbask-ital'>Match</div>
                    </button>
                </div>
            </Link>
            <Link to="/aboutus">
                <button className='p-4 mx-4'>
                    About Us
                </button>
            </Link>
            <Link to="/camera">
                <button className='p-4 mx-4'>
                    Camera
                </button>
            </Link>
        </div>
    </div>
  );
>>>>>>> 25c235bd (Added camera to be added with Flask)
}

export default Navigation;
