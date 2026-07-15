import React from "react";
import "./WordPage.css";
import SearchGlass from "../../../assets/magnifying-glass.svg";

export default function WordSearchBar() {
    return (
        <div className="word-searchbar-container">
            <div className="searchbar-wrapper">
                <img src={SearchGlass} alt="Search" className="search-icon"/>
                <input type="text" className="searchbar" placeholder="Search words..."/>
            </div>
        </div>
    );
}