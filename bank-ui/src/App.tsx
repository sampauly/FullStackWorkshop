import { Route, Routes } from 'react-router-dom'
import HeaderComponent from './components/HeaderComponent'
import HomePage from './pages/HomePage'
import AboutPage from './pages/AboutPage'
import ServicesPage from './pages/ServicesPage'
import './App.css'

function App() {
  return (
    <>
      <HeaderComponent />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/services" element={<ServicesPage />} />
      </Routes>
    </>
  )
}

export default App