import "./App.css";
import Anirud from "./Static/Anirud.jpeg";
import Neil from "./Static/Neil.jpg";
import Adesh from "./Static/Adesh.jpeg";
import Theo from "./Static/Theodore.jpeg";

function Card() {
  return (
    <div className="grid grid-item-4 w-50 h-50" >
      <img src={Anirud} alt="Programmer Anirud"></img>
      <img src={Neil} alt="Programmer Neil"></img>
      <img src={Adesh} alt="Programmer Adesh"></img>
      <img src={Theo} alt="Programmer Theodore"></img>
    </div>
  );
}

export default Card;
