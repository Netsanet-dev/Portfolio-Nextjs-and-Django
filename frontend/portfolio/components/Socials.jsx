import Link from "next/link";
import { FaTwitter, FaFacebook, FaGithub, FaLinkedin } from "react-icons/fa";

const social = [
  {
    icon: <FaGithub />,
    path: "",
  },
  {
    icon: <FaFacebook />,
    path: "",
  },
  {
    icon: <FaLinkedin />,
    path: "",
  },
  {
    icon: <FaTwitter />,
    path: "",
  },
];
const Social = ({ containerStyles, iconStyles }) => {
  return (
    <div className={containerStyles}>
      {social.map((item, index) => {
        return (
          <Link key={index} href={item.path} className={iconStyles}>
            {item.icon}
          </Link>
        );
      })}
    </div>
  );
};

export default Social;
