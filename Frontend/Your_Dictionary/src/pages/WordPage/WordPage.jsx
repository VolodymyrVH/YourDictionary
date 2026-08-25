import WordGameHeader from "./components/WordGameHeader"
import WordLanguageChanger from "./components/LanguageChanger"
import WordSearchBar from "./components/SearchWordBar"
import CreateWordButton from "./components/CreateWordButton"
import WordFormCreate from "./components/WordForm"
import WordFormInfo from "./components/WordFormInfo"
import WordsField from "./components/WordsField"
import { useState } from "react"

export default function WordPage() {
    const [refreshTrigger, setRefreshTrigger] = useState(0);
    const [selectedLanguage, setSelectedLanguage] = useState("eng");

    const handleWordAdded = () => {
        setRefreshTrigger(prev => prev + 1);
    };

    const handleWordDeleted = () => {
        setRefreshTrigger(prev => prev + 1);
    };

    return(
        <>
            <WordGameHeader />
            <WordLanguageChanger 
                selectedLanguage={selectedLanguage} 
                onLanguageChange={setSelectedLanguage}
            />
            <WordSearchBar />
            <WordsField
                languageCode={selectedLanguage}
                refreshTrigger={refreshTrigger}
                onWordDeleted={handleWordDeleted}
            />
            <CreateWordButton onWordAdded={handleWordAdded} />
        </>
    )
}