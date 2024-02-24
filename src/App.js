import './App.css';
import skincareWomanImage from './skincare_woman.jpeg';

function HeaderSection() {
  return (
    <div className='m-16'>
      <div className='border-2 border-black mx-64 mb-16'>
        <div className="text-5xl mt-16 text-center fbask-reg">
          Skincare ahhh site.
        </div>
        <div className='fbask-ital mb-32 text-3xl text-center '>
          By: Anirud Lappathi and others
        </div>
      </div>

      <div className='text-center'>
        <img src={skincareWomanImage} alt='skincare woman' className='mx-auto w-full max-w-xl'></img>
      </div>

      <div className='flex'>
        <div className='fbask-reg text-3xl'>
          Figure out your skin issues
        </div>
        <button className=''>
          ahhh
        </button>
      </div>
    </div>
  );
}

export default HeaderSection;
