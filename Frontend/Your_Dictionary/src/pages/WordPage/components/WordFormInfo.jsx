import React, { useState } from "react";
import "./WordPage.css";
import axios from "axios";

export default function WordFormInfo({ onClose, wordId }) {
    const getWord = async () => {
        try {
            const token = localStorage.getItem("access_token");

            const response = await axios.get(
                `http://127.0.0.1:8000/words/id/${wordId}`,
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );
            //write here showing word

        } catch (error) {
            console.error("Error getting words", error);
            console.error("Response", error.response?.data);
        }
    };

    return (
        <div className="word-modal-overlay">
            <div className="info-word-container">
                <div className="create-word-header">
                    <h2>Word Information</h2>
                    <button 
                        onClick={onClose}
                        className="close-button">
                            ✕
                    </button>
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