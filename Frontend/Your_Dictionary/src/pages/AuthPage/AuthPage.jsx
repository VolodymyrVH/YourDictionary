import React from "react"

import RegitstrationForm from "./components/RegistrationForm"
import LoginForm from "./components/LoginForm"

export default function AuthPage() {
    return(
        <>
            <div className="background">
                <label class="switch">
                    <input type="checkbox" />
                    <span className="slider-switch-reg-to-log"></span>
                </label>
                <div className="reg-form">
                    <RegitstrationForm />
                </div>
                <div className="log-form">
                    <LoginForm />
                </div>
            </div>
        </>
    )
}