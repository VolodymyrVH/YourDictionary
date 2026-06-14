import React from "react";
import AboutPage from "../AboutPage";

export default function ExplainPart () {
    return (
        <>
            <section className="explaining-components">
            <h1 className="main-text-explaining-com">
                Why do you need Your Dictionary?
            </h1>
            <p className="subtitle">
                Many users wonder why they should use Your Dictionary in everyday life.
            </p>
            <div className="blocks-container">
                <div className="block-container-of-usage">
                    <h2 className="block-name">Write your words!</h2>
                    <p className="inblock-explain">
                        Add new words and save important information about them.
                    </p>
                </div>
                <div className="block-container-of-usage">
                    <h2 className="block-name">Play and Learn!</h2>
                    <p className="inblock-explain">
                        Play games with your vocabulary and remember words faster.
                    </p>
                </div>
                <div className="block-container-of-usage">
                    <h2 className="block-name">Effective Learning!</h2>
                    <p className="inblock-explain">
                        Writing down new vocabulary makes language learning easier and more effective.
                    </p>
                </div>
            </div>
        </section>
        </>
    )
}