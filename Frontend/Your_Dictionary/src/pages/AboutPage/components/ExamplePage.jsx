import React from "react";
import { useState } from "react";
import "./AboutPage.css";

export default function ExampleTranslation () {
    const [word, setWord] = useState({
        word_name: "",
        article_bool: true,
        article: "der",
        language: "gr",
        part: "noun",
        explanation: ""
    });

    const [words, setWords] = useState([]);

    const addWord = (e) => {
        if (word.word_name.trim() === "") {
            return;
        }

        setWords([...words, word]);

        setWord({
            word_name: "",
            article_bool: true,
            article: "der",
            language: "gr",
            part: "noun",
            explanation: ""
        })
    }

    return(
        <>
            <div className="all-translation-contaiber">
                <div className="upper-explanation">
                    <h1>Try it yourself!</h1>
                </div>
                <div className="dictionary-container">
                    <div className="formular-container">
                        <form className="form-dictionary">
                            <div className="word-input">
                                <select
                                    disabled={word.language !== "gr" || word.part !== "noun"}
                                    value={word.article}
                                    onChange={(e) =>
                                        setWord({...word, article: e.target.value})
                                    }>
                                    <option value="der">der</option>
                                    <option value="die">die</option>
                                    <option value="das">das</option>
                                    <option value="die(pl)">die (pl)</option>
                                </select>
                                <input
                                    placeholder='For example "Car", "Auto"...'
                                    value={word.word_name}
                                    onChange={(e) => setWord({...word, word_name: e.target.value})}
                                    />
                                <select value={word.language}
                                onChange={(e) => {
                                    const selected = e.target.value;

                                    if (selected === "gr") {
                                        setWord({...word, language: selected, article_bool: true});
                                    } else {
                                        setWord({...word, language: selected, article_bool: false});
                                    }}}>
                                    <option value="en">English</option>
                                    <option value="gr">German</option>
                                    <option value="ua">Ukrainian</option>
                                </select>
                                <select value={word.part}
                                onChange={(e) => setWord({...word, part: e.target.value})}>
                                    <option value="noun">Noun</option>
                                    <option value="verb">Verb</option>
                                    <option value="adjective">Adjective</option>
                                </select>
                            </div>
                            <div className="explanation-word-input">
                                <textarea placeholder="Write explanation for that word..."
                                value={word.explanation}
                                onChange={(e) => setWord({...word, explanation: e.target.value})}/>
                            </div>
                            <button 
                            type="button"
                            onClick={addWord}>
                                Add word
                            </button>
                        </form>
                    </div>
                    <div className="field-word-container">
                        {words.map((item, index) => (
                            <div className="word-item" key={index}>
                                <div className="word-main">
                                    {item.article_bool && item.article + " "}
                                    {item.word_name}
                                </div>
                                <div className="word-hover-info">
                                    <span>
                                        {item.language === "gr" ? "🇩🇪" :
                                        item.language === "en" ? "🇬🇧" :
                                        item.language === "ua" ? "🇺🇦" :
                                        ""
                                        }</span>
                                    <span>{item.part}</span>
                                    <span>{item.explanation || "No explanation"}</span>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </>
    )
}