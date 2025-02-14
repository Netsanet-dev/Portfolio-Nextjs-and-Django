import { Button } from "@/components/ui/button";
import { FiDownload } from "react-icons/fi";
import Social from "@/components/Socials";
import Photo from "@/components/Photo";
import Stats from "@/components/Stats";

const Home = () => {
  return (
    <section className="h-full">
      <div className="container mx-auto h-full">
        <div className="flex flex-col lg:flex-row items-center justify-between lg:pt-0 lg:pb-15">
          <div className="text-center lg:text-left order-2 lg:order-none">
            <span className="text-xl">Software Developer</span>
            <h1 className="h1 mb-6 mt-4">
              Hello I'm <br />{" "}
              <span className="text-accent">Netsanet Solomon</span>
            </h1>
            <p>
              I excel at crafting elegant digital experiances and I am
              proficient in various programming languages and technlologies.
            </p>
            <div className="flex flex-col lg:flex-row items-center gap-8">
              <Button
                variant="outline"
                size="lg"
                className="uppercase flex items-center gap-2"
              >
                <span>Download CV </span>
                <FiDownload className="text-lg" />
              </Button>
              <div className="mb-8 lg:mb-0">
                <Social
                  containerStyles="flex gap-6"
                  iconStyles="w-9 h-9 border border-accent rounded-full flex justify-center items-center text-accent text-base hover:bg-accent hover:text-primary hover:transition-all duration-500"
                />
              </div>
            </div>
          </div>
          <div className="order-1 lg:order-none mb-8 lg:mb-0">
            <Photo />
          </div>
        </div>
      </div>
      <Stats />
    </section>
  );
};

export default Home;
