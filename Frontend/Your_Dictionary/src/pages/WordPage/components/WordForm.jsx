import React, { useState } from "react";
import "./WordPage.css";
import axios from "axios";

export default function WordFormCreate({ onClose, onWordAdded }) {
    //const [showComponent, setShowComponent] = useState(true);
    const [messageComponent, setMessageComponent] = useState("");
    const [messageType, setMessageType] = useState("");

    const [selectedLanguageCode, setSelectedLanguageCode] = useState("ger");
    const [selectedArticle, setSelectedArticle] = useState("");
    const [selectedPart, setSelectedPart] = useState("Noun");
    
    const articleToGender = {
        "der": "Masculine",
        "die": "Feminine",
        "das": "Neuter",
        "die (Pl.)": "Plural",
    };

    const [userWord, setUserWord] = useState({
        word_string: "",
        language_id: 2,
        article_id: null,
        part_of_speech_id: 1,
        transcription: "",
        gender_id: null,
        definition: ""
    });

    //const [isSubmitted, setIsSubmitted] = useState(false);
    const resetForm = () => {
        setSelectedLanguageCode("ger");
        setSelectedArticle("");
        setSelectedPart("Noun");

        setUserWord({
            word_string: "",
            language_id: 2,
            article_id: null,
            part_of_speech_id: 1,
            transcription: "",
            gender_id: null,
            definition: ""
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const token = localStorage.getItem("access_token");

            const response = await axios.post(
                "http://127.0.0.1:8000/words/word",
                userWord,
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );

            console.log("Word added:", response.data);

            setMessageComponent("The word added succesfuly!");
            setMessageType("success");
            resetForm();
            onWordAdded();

            setTimeout(() => {
                setMessageComponent("");
                setMessageType("");
            }, 10000);

        } catch (error) {
            setMessageComponent("Some fields are empty or incorrect!");
            setMessageType("error");
            console.error("Errod adding word", error);
            console.error("Response", error.response?.data);
        }
    }

    return (
        <div className="word-modal-overlay">
            {messageComponent && (
                <div className={`message-word ${messageType}`}>
                    <p className="messege-word-text">
                        {messageComponent}
                    </p>
                </div>
            )}
            <div className="created-word-container">
                <div className="create-word-header">
                    <h2>Create Word</h2>
                    <button 
                        onClick={onClose}
                        className="close-button">
                        ✕
                    </button>
                </div>
                <div className="create-word-form-container">
                    <div className="word-string-container">
                        <select
                            className="language-selection"
                            value={selectedLanguageCode}
                            onChange={async (e) => {
                                const code = e.target.value;

                                setSelectedLanguageCode(code);

                                try {
                                    const response = await axios.get(
                                        `http://127.0.0.1:8000/languages/by-code/${code}`
                                    );

                                    setUserWord((prev) => ({
                                        ...prev,
                                        language_id: response.data.id,
                                        article_id: null,
                                        gender_id: null,
                                    }));
                                    setSelectedArticle("");

                                } catch (error) {
                                    console.error("Error getting language:", error);
                                }
                            }}
                        >
                            <option value="ger">GER</option>
                            <option value="eng">ENG</option>
                            <option value="ukr">UKR</option>
                        </select>
                        <select 
                            className="article-selection"
                            disabled={selectedLanguageCode !== "ger" || selectedPart !== "Noun"}
                            value={selectedArticle}
                            onChange={async (e) => {
                                const article = e.target.value;
                                
                                if (article === "") {
                                    setSelectedArticle("");

                                    setUserWord((prev) => ({
                                        ...prev,
                                        article_id: null,
                                        gender_id: null,
                                    }));

                                    return;
                                }
                                    
                                setSelectedArticle(article);

                                try {
                                    const responseArticle = await axios.get(
                                        `http://127.0.0.1:8000/articles/by-name/${article}`
                                    );

                                    const gender = articleToGender[article];

                                    const responseGender = await axios.get(
                                        `http://127.0.0.1:8000/genders/by-name/${gender}`
                                    );

                                    setUserWord((prev) => ({
                                        ...prev,
                                        article_id: responseArticle.data.id,
                                        gender_id: responseGender.data.id
                                    }))
                                } catch (error) {
                                    console.error("Error getting article/gender: ", error);
                                }
                            }}
                        >
                            <option value="">-</option>
                            <option value="der">der</option>
                            <option value="die">die</option>
                            <option value="das">das</option>
                            <option value="die (Pl.)">die (Pl.)</option>
                        </select>
                        <input 
                        className="string-input" 
                        placeholder="Word"
                        value={userWord.word_string}
                        onChange={(e) => {
                            setUserWord((prev) => ({
                                ...prev,
                                word_string: e.target.value
                            }));
                        }} 
                        />
                    </div>
                    <div className="second-layer-create-word">
                        <select 
                        className="selection-part-of-speech"
                        value={selectedPart}
                        onChange={async (e) => {
                            const part = e.target.value;

                            setSelectedPart(part)

                            try {
                                const response = await axios.get(
                                    `http://127.0.0.1:8000/parts-of-speech/by-name/${part}`
                                );

                                setUserWord((prev) => ({
                                    ...prev,
                                    part_of_speech_id: response.data.id,
                                }));

                            } catch (error) {
                                console.error("Error getting part of speach: ", error);
                            }
                        }}
                        >
                            <option value="Noun">Noun</option>
                            <option value="Pronoun">Pronoun</option>
                            <option value="Verb">Verb</option>
                            <option value="Adjective">Adjective</option>
                            <option value="Adverb">Adverb</option>
                            <option value="Preposition">Preposition</option>
                            <option value="Conjunction">Conjunction</option>
                            <option value="Interjection">Interjection</option>
                        </select>
                        <input 
                        className="transcription-input" 
                        placeholder="Transcription"
                        value={userWord.transcription}
                        onChange={(e) => {
                            setUserWord((prev) => ({
                                ...prev,
                                transcription: e.target.value
                            }));
                        }}
                        />
                    </div>
                    <textarea 
                    className="definition-text-input" 
                    placeholder="Definition..." 
                    rows="5"
                    value={userWord.definition}
                    onChange={(e) => {
                        setUserWord((prev) => ({
                            ...prev,
                            definition: e.target.value
                        }));
                    }}
                    />
                    <button 
                    type="button"
                    className="submit-word-button"
                    onClick={handleSubmit}
                    >
                        Add Word
                    </button>
                </div>
            </div>
        </div>
    );
}