import WordGameHeader from "./components/WordGameHeader"
import WordLanguageChanger from "./components/LanguageChanger"
import WordSearchBar from "./components/SearchWordBar"

export default function WordPage() {
    return(
        <>
            <WordGameHeader />
            <WordLanguageChanger />
            <WordSearchBar />
        </>
    )
}