import { BrowserRouter, Routes, Route } from 'react-router-dom';

import AboutPage from "../pages/AboutPage/AboutPage"
import AuthPage from "../pages/AuthPage/AuthPage"
import WordPage from '../pages/WordPage/WordPage';

function App() {
    return(
        <>
            <BrowserRouter>
                <Routes>
                    <Route path='/' element={<AboutPage />} />
                    <Route path='/registration' element={<AuthPage />} />
                    <Route path='/login' element={<AuthPage />} />
                    <Route path='/wordpage' element={<WordPage />} />
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default App