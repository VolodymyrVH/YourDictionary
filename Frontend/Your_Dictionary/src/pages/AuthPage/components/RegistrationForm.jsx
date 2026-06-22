import React, { useState } from "react";
import axios from "axios"

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

    return(
        <>
            <h1>Registration</h1>
            <form onSubmit={handleSubmit}>
                <label>E-Mail</label><br />
                <input 
                    type="email" 
                    value={userreg.email}
                    onChange={(e) => setUserreg({...userreg, email: e.target.value})}
                /><br />
                <label>Password</label><br />
                <input 
                    type="password" 
                    value={userreg.password}
                    onChange={(e) => setUserreg({...userreg, password: e.target.value})}
                /><br />
                <label>Repeat Password</label><br />
                <input 
                    type="password" 
                    value={userreg.checkpassowrd}
                    onChange={(e) => setUserreg({...userreg, checkpassowrd: e.target.value})}    
                /><br />
                <input type="submit"/>
            </form>
        </>
    )
}