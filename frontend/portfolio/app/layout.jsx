import { JetBrains_Mono } from "next/font/google";
import "./globals.css";
// import { Weight } from "lucide-react";
import PageTransisiton from "@/components/pageTransisiton";
import StartTransition from "@/components/StartTransition";
//Components
import Header from "@/components/Header";

const jetBrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  weight: ["100", "200", "300", "400", "500", "600", "700", "800"],
  variable: "--font-jetBrainsMono",
});

export const metadata = {
  title: "Portfolio",
  description: "Netsanet Solomon",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={jetBrainsMono.variable}>
        <Header />
        <StartTransition />
        <PageTransisiton>{children}</PageTransisiton>
      </body>
    </html>
  );
}
