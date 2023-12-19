import Footer from "../components/global/Footer";
import Navigasi from "../components/global/Navigasi";
import email_icon from "../components/image/email.png";
import password_icon from "../components/image/password.png";
import "./Login.css";

import { useEffect, useState } from "react";
import { authWithEmailAndPassword } from "../backend-api/authAPI";

export default function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        const result = await authWithEmailAndPassword(email, password);
        if (result) {
            window.location.href = "/";
        }
    }

    return(
        <div >
            <div className="App"><Navigasi/></div>
            <div className="container">
                <div className="header">
                    <div className="text">Login</div>
                    <div className="underline"></div>
                </div>
                <div className="inputs">
                    <div className="input">
                        <img src={email_icon} alt=""/>
                        <input type={"text"} placeholder="Email" onChange={(e) => setEmail(e.target.value)}/>
                    </div>
                    <div className="input">
                        <img src={password_icon} alt=""/>
                        <input type={"password"} placeholder="Password" onChange={(e) => setPassword(e.target.value)}/>
                    </div>
                </div>
                <div className="small-login-signup">Sign Up</div>
                <div className="submit-container">
                    <button className="submit" onClick={handleLogin}>Login</button>
                </div>
            </div>

            <div className="App"><Footer/></div>
        </div>
    );
}

