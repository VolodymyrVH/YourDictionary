import React from "react";

export default function LoginForm() {
    return(
        <>
            <h1>Login</h1>
            <form>
                <label>E-Mail</label><br />
                <input type="email" /><br />
                <label>Password</label><br />
                <input type="passwrod" /><br />
                <input type="submit"/>
            </form>
        </>
    )
}