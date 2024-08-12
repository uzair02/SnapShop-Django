import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import Chatbot from './components/ChatBot/Chatbot'; // Import the Chatbot component
import Navbar from './components/Navbar/Navbar';
import AboutUs from './components/AboutUs/AboutUs';
import Footer from './components/Footer/Footer';
import EditProfile from './components/EditProfile/EditProfile';
import RatingForm from './components/WebRating/RatingForm'; 
import ReviewForm from './components/ReviewMark/ReviewForm'; 
import Recommend from './components/Recommendations/Recommend'; 
import Login from './Pages/Login';
import HomePage from './Pages/HomePage';
import Register from './Pages/Register';
import ContactUs from './Pages/ContactUs';
import ProductPage from './Pages/ProductPage';
import RatingsPage from './Pages/RatingsPage';
import ProfilePage from './Pages/ProfilePage';
import PrivateRoute from './utils/PrivateRoute';

function App() {
  return (
    <div>
      <Router> 
        <AuthProvider>
          <Navbar />
          <Chatbot />
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/login" element={<Login />} />
            <Route path="/AboutUs" element={<AboutUs />} />
            <Route path="/Register" element={<Register />} />
            <Route
              path="/ContactUs"
              element={
                <PrivateRoute>
                  <ContactUs />
                </PrivateRoute>
              }
            />
            <Route
              path="/RatingForm"
              element={
                <PrivateRoute>
                  <RatingForm />
                </PrivateRoute>
              }
            />
            <Route
              path="/ReviewForm/:productId"
              element={
                <PrivateRoute>
                  <ReviewForm />
                </PrivateRoute>
              }
            />
            <Route
              path="/ProfilePage"
              element={
                <PrivateRoute>
                  <ProfilePage />
                </PrivateRoute>
              }
            />
            <Route
              path="/EditProfile"
              element={
                <PrivateRoute>
                  <EditProfile />
                </PrivateRoute>
              }
            />
            <Route
              path="/Recommend"
              element={
                <PrivateRoute>
                  <Recommend />
                </PrivateRoute>
              }
            />
            <Route path="/ProductPage" element={<ProductPage />} />
            <Route path="/RatingsPage" element={<RatingsPage />} />
          </Routes>
          <Footer />
        </AuthProvider>
      </Router>
    </div>
  );
}

export default App;
