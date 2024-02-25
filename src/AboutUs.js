import './App.css';
// import skincareWomanImage from './skincare_woman.jpeg';

import Navigation from "./Navigation";
import Card from "./Card";

function AboutUs() {
  return (
    <div>
      <div>
        <Navigation />
        <div class="flex justify-center text-8xl mt-16 text-center fbask-reg">
          About&nbsp;<span class="fbask-ital">us</span>
        </div>
      </div>

      <div>
        <Card />
      </div>
    </div>
  );
}

export default AboutUs;
