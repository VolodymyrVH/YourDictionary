import React from "react"
import { Link } from "react-router-dom";

import AuthPage from "../../AuthPage/AuthPage";
import "./AboutPage.css";

export default function Header() {
    return(
        <>
            <header className="header">
                <div className="header-log-reg">
                    <p className="header-name-p">Your Dictionary</p>
                    <nav className="header-button-container">
                        <Link className="login-button" to="/registration">Registration</Link>
                        <Link className="login-button" to="/login" state={{ isLogin: true}}>Login</Link>
                    </nav>
                </div>
            </header>
        </>
    )
}