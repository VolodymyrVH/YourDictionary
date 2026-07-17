import React from "react";
import AddCircle from "../../../assets/add-circle.svg";
import "./WordPage.css";

export default function CreateWordButton() {
    return (
        <button className="create-word-button">
            <img src={AddCircle} alt="Create word"/>
        </button>
    );
}