import React from "react";
import { Link } from "react-router-dom";
import "./WordPage.css";

export default function WordGameHeader() {
    return (
        <header className="header-wordpage">
            <div className="header-word-game">
                <Link to="/" className="logo">
                    <span className="logo-blue">Your Dictionary</span>
                </Link>
                <nav className="header-button-word-game-container">
                    <Link className="word-active-button">Words</Link>
                    <Link className="word-button">Games</Link>
                </nav>
            </div>
        </header>
    );
}