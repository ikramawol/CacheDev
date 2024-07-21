import { CheckCircle2 } from "lucide-react";
import sent from "../assets/sent.jpg";
import { checklistItems } from "../constants";

const Workflow = () => {
  return (
    <div className="mt-20">
      <div className="flex justify-center">
      <span className="text-black rounded-full h-10 text-3xl font-semi-bold font-large px-3 py-2 uppercase background: linear-gradient(to right, blue, purple); color: white;">
  ABOUT US
</span>
</div>

      <h2 className="text-6xl sm:text-5xl lg:text-6xl text-center mt-6 tracking-wide px-30 py-10">
      Empowering insights with real-time {" "}
        <span className="bg-gradient-to-r from-blue-500 to-purple-800 text-transparent bg-clip-text">
        AI-driven sentiment analysis 
        </span>
      </h2>
      <div className="flex flex-wrap justify-center">
        <div className="p-2 w-full lg:w-1/2">
          <img src={sent} alt="Coding" />
        </div>
        <div className="pt-12 w-full lg:w-1/2">
          {checklistItems.map((item, index) => (
            <div key={index} className="flex mb-12">
              <div className="text-blue-400 mx-6 bg-neutral-900 h-10 w-10 p-2 justify-center items-center rounded-full">
                <CheckCircle2 />
              </div>
              <div>
                <h5 className="mt-1 mb-2 text-xl">{item.title}</h5>
                <p className="text-md text-neutral-500">{item.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Workflow;
