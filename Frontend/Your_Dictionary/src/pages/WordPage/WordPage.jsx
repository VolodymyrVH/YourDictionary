import WordGameHeader from "./components/WordGameHeader"
import WordLanguageChanger from "./components/LanguageChanger"
import WordSearchBar from "./components/SearchWordBar"
import CreateWordButton from "./components/CreateWordButton"
import WordFormCreate from "./components/WordForm"

export default function WordPage() {
    return(
        <>
            <WordGameHeader />
            <WordLanguageChanger />
            <WordSearchBar />
            <WordFormCreate />
            <CreateWordButton />
        </>
    )
}