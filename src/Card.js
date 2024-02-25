import "./App.css";
import Anirud from "./Static/Anirud.jpeg";
import Neil from "./Static/Neil.jpg";
import Adesh from "./Static/Adesh.jpeg";
import Theo from "./Static/Theodore.jpeg";
import LinkedIn from "./Static/linkedin.svg";

function Card() {
  return (
    <div className="w-3/4 mx-auto grid grid-cols-4 gap-16 mt-16">
      <div className="text-center">
        <img
          className="rounded-full aspect-w-1 aspect-h-1 transform hover:scale-110 transition-transform"
          src={Anirud}
          alt="Programmer Anirud"
        ></img>

        <h1 className="fbask-reg text-2xl mt-4">
          Hey! Im Anirud, a Computer Science + Crop Science student at UIUC!
        </h1>
        <div className="">
          <a
            href="https://www.linkedin.com/in/anirudl/"
            target="_blank"
            className="flex justify-between" rel="noreferrer"
          >
            <img
              src={LinkedIn}
              className="mx-auto mt-2 aspect-w-1 aspect-h-1 transform hover:scale-110 transition-transform"
              alt=""
            ></img>
          </a>
        </div>
      </div>
      <div className="text-center">
        <img
          className="rounded-full aspect-w-1 aspect-h-1 transform hover:scale-110 transition-transform"
          src={Neil}
          alt="Programmer Neil"
        ></img>

        <h1 className="fbask-reg text-2xl mt-4">
          Wassup! Im Neil, a Computer Science student passionate in AI/ML at
          UIUC!
        </h1>
        <div className="">
          <a
            href="https://www.linkedin.com/in/neil-ganguly/"
            target="_blank"
            className="flex justify-between" rel="noreferrer"
          >
            <img
              src={LinkedIn}
              className="mx-auto mt-2 aspect-w-1 aspect-h-1 transform hover:scale-110"
              alt=""
            ></img>
          </a>
        </div>
      </div>
      <div className="text-center">
        <img
          className="rounded-full aspect-w-1 aspect-h-1 transform hover:scale-110 transition-transform"
          src={Adesh}
          alt="Programmer Adesh"
        ></img>

        <h1 className="fbask-reg text-2xl mt-4">
          Greetings! Im Adesh, a passionate Computer Science student here at
          UIUC!
        </h1>
        <div className="">
          <a
            href="https://www.linkedin.com/in/adesh-kumar2/"
            target="_blank"
            className="flex justify-between" rel="noreferrer"
          >
            <img
              src={LinkedIn}
              className="mx-auto mt-2 aspect-w-1 aspect-h-1 transform hover:scale-110 transition-transform"
              alt=""
            ></img>
          </a>
        </div>
      </div>
      <div className="text-center">
        <img
          className="rounded-full aspect-w-1 aspect-h-1 transform hover:scale-110 transition-transform"
          src={Theo}
          alt="Programmer Theodore"
        ></img>

        <h1 className="fbask-reg text-2xl mt-4">
          Salutations! Im Theodore, and I'm interested in Comp E at UIUC!
        </h1>
        <div className="">
          <a
            href="https://www.linkedin.com/in/theodore-ng/"
            target="_blank"
            className="flex justify-between" rel="noreferrer"
          >
            <img
              src={LinkedIn}
              className="mx-auto mt-2 aspect-w-1 aspect-h-1 transform hover:scale-110 transition-transform"
              alt=""
            ></img>
          </a>
        </div>
      </div>
    </div>
  );
}

export default Card;
