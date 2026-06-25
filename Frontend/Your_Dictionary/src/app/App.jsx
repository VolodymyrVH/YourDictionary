import { BrowserRouter, Routes, Route } from 'react-router-dom';

import AboutPage from "../pages/AboutPage/AboutPage"
import AuthPage from "../pages/AuthPage/AuthPage"

function App() {
    return(
        <>
            <BrowserRouter>
                <Routes>
                    <Route path='/' element={<AboutPage />} />
                    <Route path='/registration' element={<AuthPage />} />
                    <Route path='/login' element={<AuthPage />} />
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default App