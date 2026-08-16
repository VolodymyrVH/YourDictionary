import React, { useState }from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export default function LoginForm() {
    const navigate = useNavigate();

    const [userlog, setUserlog] = useState({
        email: "",
        password: ""
    })

    const [isSubmitted, setIsSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setIsSubmitted(true);

        if (userlog.email === "" || userlog.password === "") {
            return;
        }

        try {
            const response = await axios.post(
                "http://127.0.0.1:8000/auth/token",
                {
                    email: userlog.email,
                    password: userlog.password
                }
            );

            localStorage.setItem(
                "access_token",
                response.data.access_token
            );
            
            navigate("/wordpage");
        } catch (error) {
            console.error("error login", error);
        }
    }

    return(
        <div className="login-container">
            <h1>Login</h1>
            <form className="log-form" onSubmit={handleSubmit}>
                <label>E-Mail</label>
                <input 
                    type="email" 
                    className={isSubmitted && userlog.email === "" ? "empty" : ""}
                    value={userlog.email}
                    onChange={(e) => setUserlog({...userlog, email: e.target.value})}
                />
                <label>Password</label>
                <input 
                    type="password" 
                    className={isSubmitted && userlog.password === "" ? "empty" : ""}
                    value={userlog.password}
                    onChange={(e) => setUserlog({...userlog, password: e.target.value})}    
                />
                <button type="submit">Login</button>
            </form>
        </div>
    )
}