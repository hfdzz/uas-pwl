import Footer from "../components/global/Footer";
import Navigasi from "../components/global/Navigasi";
import user_icon from "../components/image/person.png";
import email_icon from "../components/image/email.png";
import password_icon from "../components/image/password.png";
import "./Login.css";

export default function Signin() {
    return(
        <div >
            <div className="App"><Navigasi/></div>
            <div className="container">
                <div className="header">
                    <div className="text">Sign In</div>
                    <div className="underline"></div>
                </div>
                <div className="inputs">
                    <div className="input">
                        <img src={user_icon} alt=""/>
                        <input type={"text"} placeholder="Name"/>
                    </div>
                    <div className="input">
                        <img src={email_icon} alt=""/>
                        <input type={"email"} placeholder="Email"/>
                    </div>
                    <div className="input">
                        <img src={password_icon} alt=""/>
                        <input type={"password"} placeholder="Password"/>
                    </div>
                </div>
                <div className="submit-container">
                    <div className="submit">Sign Up</div>
                </div>
            </div>

            <div className="App"><Footer/></div>
        </div>
    );
}