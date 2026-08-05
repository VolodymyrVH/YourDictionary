import WordGameHeader from "./components/WordGameHeader"
import WordLanguageChanger from "./components/LanguageChanger"
import WordSearchBar from "./components/SearchWordBar"
import CreateWordButton from "./components/CreateWordButton"
import WordFormCreate from "./components/WordForm"
import WordFormInfo from "./components/WordFormInfo"
import WordsField from "./components/WordsField"

export default function WordPage() {
    return(
        <>
            <WordGameHeader />
            <WordLanguageChanger />
            <WordSearchBar />
            <WordsField />
            <CreateWordButton />
        </>
    )
}