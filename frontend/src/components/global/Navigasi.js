import "./Navigasi.css"
import myKeranjang from '../../components/image/keranjang.png';

import { logoutUser } from "../../backend-api/authAPI";

export default function Navigasi() {
    // check localStorage for token
    const token = localStorage.getItem('token');

    const handleLogout = async () => {
        const result = await logoutUser(token);
        if (result) {
            window.location.href = "/";
        }
    }

    return(
        <nav className="App-nav">
            <ul>
                <li><a href="http://localhost:3000/">Home</a></li>
                <li><a href="http://localhost:3000/profile">Profile</a></li>
                {
                    token !== null ? (
                        <>
                            // <li><button href="http://localhost:3000/logout" onClick={handleLogout}>Logout</button></li>
                            <li><a href="http://localhost:3000/cart"><img src={myKeranjang} alt="" /></a></li>
                        </>
                    ) : (
                        <li><a href="http://localhost:3000/login">Login</a></li>
                    )
                }
                {/* <li><a href="http://localhost:3000/login">Login</a></li>
                <li><a href="http://localhost:3000/signin">Sign In</a></li>
                <li><a href="http://localhost:3000/cart"><img src={myKeranjang} alt="" /></a></li> */}
            </ul>
        </nav>
    );
}