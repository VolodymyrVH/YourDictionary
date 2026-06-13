import React from "react";
import "./AboutPage.css";

export default function AboutSite() {
    return(
        <>
            <div className="header_container">
                <div className="header_main_container">
                    <h1 className="header_main_name">
                        Your Dictionary
                    </h1>
                </div>
                <div className="header_p_container">
                    <p className="header_p_text">
                        A platform for creating your own dictionary and learning words
                    </p>
                </div>
            </div>
        </>
    )
}