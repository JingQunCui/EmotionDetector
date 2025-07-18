import { Routes, Route } from 'react-router-dom'
import Login from './Login'
import Register from './Register'
import Detector from './Detector'

function App() {
  return (
    <Routes>
      <Route path="/detector" element={<Detector />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="*" element={<Login />} />
    </Routes>
  )
}

export default App