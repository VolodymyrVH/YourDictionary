import Header from "./components/Header"
import AboutSite from "./components/AboutSitePage"
import FooterPart from "./components/Footer"
import ExplainPart from "./components/ExplainPart"
import ExampleTranslation from "./components/ExamplePage"

export default function AboutPage() {
    return(
        <>
            <Header />
            <AboutSite />
            <ExplainPart />
            <ExampleTranslation />
            <FooterPart />
        </>
    )
}