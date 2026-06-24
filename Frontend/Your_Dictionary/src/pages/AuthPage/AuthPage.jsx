import React, { useState } from "react";
import { useLocation } from "react-router-dom";

import RegistrationForm from "./components/RegistrationForm";
import LoginForm from "./components/LoginForm";

import "./components/AuthPage.css";

export default function AuthPage() {
    const location = useLocation();

    const [isLogin, setIsLogin] = useState(
        location.state?.isLogin ?? false
    );

    return (
        <div className="background">
            <div className="auth-card">
                <div className="auth-tabs">
                    <button
                        className={!isLogin ? "tab active" : "tab"}
                        onClick={() => setIsLogin(false)}
                    >
                        Registration
                    </button>
                    <button
                        className={isLogin ? "tab active" : "tab"}
                        onClick={() => setIsLogin(true)}
                    >
                        Login
                    </button>
                    <div
                        className={`tab-slider ${isLogin ? "right" : "left"}`}
                    />
                </div>
                <div className="auth-content">
                    {isLogin ? (<LoginForm />) : (<RegistrationForm />)}
                </div>
            </div>
        </div>
    );
}