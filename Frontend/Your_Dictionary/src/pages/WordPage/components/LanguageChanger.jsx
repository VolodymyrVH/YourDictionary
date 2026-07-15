import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./WordPage.css";

export default function WordLanguageChanger() {
    const [activeLanguage, setActiveLanguage] = useState("English");

    const languages = ["English", "German", "Ukrainian"];

    return (
        <div className="word-language-container">
            <div className="lang-container">
                {languages.map((language) => (
                    <button
                        key={language}
                        className={`lang-button ${activeLanguage === language ? "active" : ""}`}
                        onClick={() => setActiveLanguage(language)}>
                        {language}
                    </button>
                ))}
            </div>
        </div>
    );
}