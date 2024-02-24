import './App.css';
// import skincareWomanImage from './skincare_woman.jpeg';
import { Link } from 'react-router-dom';

import Navigation from './Navigation';

function HeaderSection() {
  return (
    <div>
      <Navigation />
      <div className='mx-16 h-screen py-32'>
        <div class="flex justify-center text-8xl mt-16 text-center fbask-reg">
          Skincare&nbsp;routine&nbsp;made&nbsp;for&nbsp;<span class="fbask-ital">you</span>
        </div>
        <div className='fbask-ital mb-32 text-xl text-center '>
          Learn more below...
        </div>
      </div>

      {/* <div className='text-center'>
        <img src={skincareWomanImage} alt='skincare woman' className='mx-auto w-full max-w-xl'></img>
      </div> */}

      <div className='flex align-auto justify-between'>
        <div className='fbask-reg text-3xl py-4'>
          Figure out your skin issues
        </div>
        <Link to="/camera">
          <button className='p-4 mx-32 border-2 border-black rounded-xl'>
            Camera
          </button>
        </Link>
      </div>
    </div>
  );
}

export default HeaderSection;
