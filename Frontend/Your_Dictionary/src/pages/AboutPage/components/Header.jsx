import React from "react"
import "./AboutPage.css";

export default function Header() {
    return(
        <>
            <header className="header">
                <div className="header-log-reg">
                    <p className="header-name-p">Your Dictionary</p>
                    <nav className="header-button-container">
                        <a className="login-button" href="/">Registration</a>
                        <a className="login-button" href="/">Login</a>
                    </nav>
                </div>
            </header>
        </>
    )
}