import React from "react";
import "./WordPage.css";

export default function WordFormInfo() {
    return (
        <div className="word-modal-overlay">
            <div className="info-word-container">
                <div className="create-word-header">
                    <h2>Word Information</h2>
                    <button className="close-button">✕</button>
                </div>
                <div className="info-word-form-container">
                    <div className="word-info-header">
                        <h1>der Computer</h1>
                        <div className="word-tags">
                            <span className="tag blue">German</span>
                            <span className="tag">Masculine</span>
                            <span className="tag green">Noun</span>
                        </div>
                        <p className="transcription">/kɔmˈpjuːtɐ/</p>
                    </div>
                    <div className="info-section">
                        <h3>Definition</h3>
                        <p>
                            An electronic device that processes and stores
                            information.
                        </p>
                    </div>
                    <div className="info-section">
                        <h3>Categories</h3>
                        <div className="chips">
                            <span className="chip">Technology</span>
                            <span className="chip">Electronics</span>
                            <button className="add-chip-button">+</button>
                        </div>
                    </div>
                    <div className="info-section">
                        <h3>Translations</h3>
                        <div className="chips">
                            <span className="chip">Комп'ютер</span>
                            <span className="chip">Computer</span>
                            <button className="add-chip-button">+</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}