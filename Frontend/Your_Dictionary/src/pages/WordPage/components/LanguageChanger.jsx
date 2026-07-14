import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./WordPage.css";

export default function WordLanguageChanger() {
    const [isActive, setIsActive] = useState(false);

    return (
        <>
            <div className="word-language-container">
                <div className="lang-container">
                    <div 
                        className={isActive}
                        onClick={() => setIsActive(true)}
                    >
                        <a className="language-selection">English</a>
                    </div>
                    <div 
                        className={isActive}
                        onClick={() => setIsActive(true)}
                    >
                        <a className="language-selection">German</a>
                    </div>
                    <div 
                        className="lang-button"
                        className={isActive}
                        onClick={() => setIsActive(true)}    
                    >
                        <a className="language-selection">Ukrainian</a>
                    </div>
                </div>
            </div>
        </>
    );
}