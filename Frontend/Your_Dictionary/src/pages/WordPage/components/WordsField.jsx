import React, { useState, useEffect } from "react";
import "./WordPage.css";
import axios from "axios";
import WordFormInfo from "./WordFormInfo";

export default function WordsField({ refreshTrigger, languageCode }) {
    const [userWords, setUserWords] = useState([]);

    const [showWordComponent, setShowWordComponent] = useState(false);

    const [selectedWordId, setSelectedWordId] = useState(null);

    const getWords = async () => {
        try {
            const token = localStorage.getItem("access_token");

            const response = await axios.get(
                "http://127.0.0.1:8000/words/filtered_words",
                {
                    params: {
                        language_code: languageCode
                    },
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            setUserWords(response.data);

        } catch (error) {
            console.error("Error getting words", error);
            console.error("Response", error.response?.data);
        }
    };

    useEffect(() => {
        getWords();
    }, [languageCode, refreshTrigger]);

    return(
        <>
            <div className="wordfield-container">
                {userWords.map((word) => (
                    <div 
                        className="word-container"
                        key={word.id}
                        onClick={() => {
                            setSelectedWordId(word.id)
                            setShowWordComponent(true);
                        }}
                    >
                        <p>{word.word_string}</p>
                    </div>
                ))}
                {showWordComponent && (
                    <WordFormInfo
                        wordId={selectedWordId}
                        onClose={() => setShowWordComponent(false)}
                    />
                )}

                <div className="category-container">
                    <p>Category</p>
                    <div className="word-container-list">
                        <div className="word-container">
                            <p>Word</p>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}