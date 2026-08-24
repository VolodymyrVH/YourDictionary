import React, { useEffect, useState } from "react";
import "./WordPage.css";
import axios from "axios";

export default function WordFormInfo({ onClose, wordId }) {
    const [userWord, setUserWord] = useState({
        word_string: "",
        language: null,
        article: null,
        part_of_speech: null,
        transcription: "",
        gender: null,
        definition: ""
    })

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

            setUserWord(response.data);
            console.log(response.data);

        } catch (error) {
            console.error("Error getting words", error);
            console.error("Response", error.response?.data);
        }
    };

    useEffect(() => {
        if(wordId){
            getWord();    
        }
    }, [wordId]);

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
                        <h1>{userWord.article_id} {userWord.word_string}</h1>
                        <div className="word-tags">
                            <span className="tag blue">{userWord.language}</span>
                            <span className="tag">{userWord.gender}</span>
                            <span className="tag green">{userWord.part_of_speech}</span>
                        </div>
                        <p className="transcription">{userWord.transcription}</p>
                    </div>
                    <div className="info-section">
                        <h3>Definition</h3>
                        <p>
                            {userWord.definition}.
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