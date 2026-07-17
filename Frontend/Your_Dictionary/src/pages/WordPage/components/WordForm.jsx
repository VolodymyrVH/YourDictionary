import React from "react";
import "./WordPage.css";


export default function WordFormCreate() {
    return (
        <div className="word-modal-overlay">
            <div className="created-word-container">
                <div className="create-word-header">
                    <h2>Create Word</h2>
                    <button className="close-button">✕</button>
                </div>
                <div className="create-word-form-container">
                    <div className="word-string-container">
                        <select className="language-selection">
                            <option>GER</option>
                            <option>ENG</option>
                            <option>UKR</option>
                        </select>
                        <select className="article-selection">
                            <option>der</option>
                            <option>die</option>
                            <option>das</option>
                            <option>die (Pl.)</option>
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