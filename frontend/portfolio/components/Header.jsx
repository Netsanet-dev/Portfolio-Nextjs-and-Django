import Link from "next/link";
import { Button } from "./ui/button";
import Nav from "./Nav";
import MobileNav from "./MobileNav";

const Header = () => {
  return (
    <header className="py-6 lg:py-8 text-white">
      <div className="container mx-auto flex justify-between items-center">
        {/* Logo*/}
        <Link href="/">
          <h1 className="text-4xl font-semibold">
            Netsanet<span className="text-accent">.</span>
          </h1>
        </Link>

        {/* Desktop Navigatoin and hide button Hire me*/}
        <div className="hidden lg:flex items-center gap-8">
          <Nav />
          <Link href="/contact">
            <Button>Hire Me</Button>
          </Link>
        </div>

        {/* Mobile Navigation*/}
        <div className="lg:hidden">
          <MobileNav />
        </div>
      </div>
    </header>
  );
};

export default Header;
