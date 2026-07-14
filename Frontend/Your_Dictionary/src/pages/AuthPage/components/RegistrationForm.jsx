import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./AuthPage.css";

export default function RegitstrationForm() {
    const navigate = useNavigate();

    const [userreg, setUserreg] = useState({
        email: "",
        password: "",
        checkpassowrd: ""
    })

    const [isSubmitted, setIsSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setIsSubmitted(true);

        if (userreg.email === "" || userreg.password === "") {
            return;
        }

        if (userreg.password != userreg.checkpassowrd) {
            return;
        }

        try {
            const response = await axios.post(
                "http://127.0.0.1:8000/users",
                {
                    email: userreg.email,
                    password: userreg.password
                }
            );

            navigate("/wordpage");
        } catch (error) {
            console.error("Error registration");
        }
    }

    return (
    <div className="register-container">
        <h1>Registration</h1>
        <form className="register-form" onSubmit={handleSubmit}>
            <label>E-Mail</label>
            <input
                type="email"
                className={isSubmitted && userreg.email === "" ? "empty" : ""}
                value={userreg.email}
                onChange={(e) => setUserreg({ ...userreg, email: e.target.value })}
            />
            <label>Password</label>
            <input
                type="password"
                className={isSubmitted && userreg.password === "" ? "empty" : ""}
                value={userreg.password}
                onChange={(e) => setUserreg({ ...userreg, password: e.target.value })}
            />
            <label>Repeat Password</label>
            <input
                type="password"
                className={(isSubmitted && userreg.checkpassowrd === "") || (isSubmitted && userreg.checkpassowrd !== userreg.password) ? "empty" : ""}
                value={userreg.checkpassowrd}
                onChange={(e) => setUserreg({ ...userreg, checkpassowrd: e.target.value })}
            />
            <button type="submit">Register</button>
        </form>
    </div>
);
}