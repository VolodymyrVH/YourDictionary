import React, { useState } from "react";
import AddCircle from "../../../assets/add-circle.svg";
import "./WordPage.css";

import WordFormCreate from "./WordForm";

export default function CreateWordButton() {
    const [showComponent, setShowComponent] = useState(false);

    return (
        <>
            <button
                onClick={() => setShowComponent(true)}
                className="create-word-button">
                <img src={AddCircle} alt="Create word" />
            </button>
            {showComponent && (<WordFormCreate onClose={() => setShowComponent(false)}/>)}
        </>
    );
}