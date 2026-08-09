import React, { use, useState } from "react";
import "./WordPage.css";
import axios from "axios";


export default function WordFormCreate({ onClose }) {
    const [showComponent, setShowComponent] = useState(true);

    const [selectedLanguageCode, setSelectedLanguageCode] = useState("ger");
    const [selectedArticle, setSelectedArticle] = useState(null);

    const [userWord, setUserWord] = useState({
        word_string: "",
        language_id: 1,
        article_id: null,
        part_of_speech_id: null,
        transcription: "",
        gender_id: null,
        definition: ""
    })

    const [isSubmitted, setIsSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setIsSubmitted(true);

        try {
            const response = await axios.post(
                "http://127.0.0.1:8000/words/word",
                {
                    word_string: userWord.word_string,
                    language_id: userWord.language_id,
                    article_id: userWord.article_id,
                    part_of_speech_id: userWord.part_of_speech_id,
                    transcription: userWord.transcription,
                    gender_id: userWord.gender_id,
                    definition: userWord.definition
                }
            );
        } catch (error) {
            console.error("Errod adding word");
        }
    }

    return (
        <div className="word-modal-overlay">
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
                                        language_id: response.data.id
                                    }));
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
                            value={selectedArticle}
                            onChange={async (e) => {
                                const article = e.target.value;

                                if (e.target.value === null){
                                    
                                } else {
                                    setSelectedArticle(article);

                                    try {
                                        const response = await axios.get(

                                        );
                                    } catch {}
                                }

   
                            }}
                            >
                            <option value={null}>-</option>
                            <option value="der">der</option>
                            <option value="die">die</option>
                            <option value="das">das</option>
                            <option value="die (Pl.)">die (Pl.)</option>
                        </select>
                        <input className="string-input" placeholder="Word"/>
                    </div>
                    <div className="second-layer-create-word">
                        <select className="selection-part-of-speech">
                            <option>Noun</option>
                            <option>Pronoun</option>
                            <option>Verb</option>
                            <option>Adjective</option>
                            <option>Adverb</option>
                            <option>Preposition</option>
                            <option>Conjunction</option>
                            <option>Interjection</option>
                        </select>
                        <input className="transcription-input" placeholder="Transcription"/>
                    </div>
                    <textarea className="definition-text-input" placeholder="Definition..." rows="5"/>
                    <button className="submit-word-button">Add Word</button>
                </div>
            </div>
        </div>
    );
}