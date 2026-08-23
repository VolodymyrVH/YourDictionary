import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./WordPage.css";

export default function WordLanguageChanger({ selectedLanguage, onLanguageChange }) {
    const languages = [
        {name: "English", code:"eng"}, 
        {name: "German", code: "ger"},
        {name: "Ukrainian", code: "ukr"}
    ];

    return (
        <div className="word-language-container">
            <div className="lang-container">
                {languages.map((language) => (
                    <button
                        key={language.code}
                        className={`lang-button ${selectedLanguage === language.code ? "active" : ""}`}
                        onClick={() => onLanguageChange(language.code)}>
                        {language.name}
                    </button>
                ))}
            </div>
        </div>
    );
}