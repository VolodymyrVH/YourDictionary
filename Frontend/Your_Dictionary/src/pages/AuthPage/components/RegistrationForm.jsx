import React, { useState } from "react";
import axios from "axios";
import "./AuthPage.css";

export default function RegitstrationForm() {
    const [userreg, setUserreg] = useState({
        email: "",
        password: "",
        checkpassowrd: ""
    })

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (userreg.password != userreg.checkpassowrd) {
            console.log("wrong second password");
            return;
        }

        const response = await axios.post(
            "http://127.0.0.1:8000/users/",
            {
                email: userreg.email,
                password: userreg.password
            }
        );

        console.log(response.data);
    }

    return (
    <div className="register-container">
        <h1>Registration</h1>
        <form className="register-form" onSubmit={handleSubmit}>
            <label>E-Mail</label>
            <input
                type="email"
                value={userreg.email}
                onChange={(e) => setUserreg({ ...userreg, email: e.target.value })}
            />
            <label>Password</label>
            <input
                type="password"
                value={userreg.password}
                onChange={(e) => setUserreg({ ...userreg, password: e.target.value })}
            />
            <label>Repeat Password</label>
            <input
                type="password"
                value={userreg.checkpassowrd}
                onChange={(e) => setUserreg({ ...userreg, checkpassowrd: e.target.value })}
            />
            <button type="submit">Register</button>
        </form>
    </div>
);
}