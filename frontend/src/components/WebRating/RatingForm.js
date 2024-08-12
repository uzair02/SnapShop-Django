import React, { useState, useEffect } from 'react';
import { jwtDecode } from 'jwt-decode';
import axios from 'axios';
import StarRating from '../StarRating/StarRating';
import { useNavigate } from 'react-router-dom';

const RatingForm = () => {
   
    const token = localStorage.getItem("authTokens")
    let user_id = null;

    if (token){
      const decoded = jwtDecode(token) 
      user_id = decoded.user_id
    } 

  const navigate = useNavigate();
  const [resetStars, setResetStars] = useState(false);
  const [webStoreNames, setWebStoreNames] = useState([]);
  const [formData, setFormData] = useState({
    webstore: '',
    rating: 0,
    review: '',
    user: user_id,
  });

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/store/webstore_names/')
      .then(response => {
        console.log('Web store names:', response.data);
        setWebStoreNames(response.data);
      })
      .catch(error => {
        console.error('Error fetching web store names:', error);
      });
  }, []);

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleRate = rating => {
    setFormData({ ...formData, rating });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await axios.post('http://127.0.0.1:8000/store/submit_rating/', formData);
        // Handle successful submission
        console.log("Submission successful!!!");
        // Reset form fields
        setFormData({
        webstore: '',
        rating: 0,
        review: '',
        user: user_id,
        });
        console.log("0k!!!");
        // Reset stars
        setResetStars(true);
        navigate('/RatingsPage');
    } catch (error) {
      console.error('Error submitting rating:', error);
    }
  };

  return (
    <div className="container mt-4">
        <div className='col-md-9 card mx-auto d-flex flex-row px-0'>
            <div className="card-body d-flex flex-column justify-content-center">
                <h4 className="title text-center mt-4 pb-3">Rate Web Stores</h4>
                <form className='col-sm-10 col-12 mx-auto' onSubmit={handleSubmit}>
                <div className='form-group pb-2'>
                    <select class="form-select" aria-label="Default select example" name="webstore" value={formData.webstore} onChange={handleChange}>
                        <option value="" disabled>Select Web Store</option>
                        {webStoreNames.map(name => (
                            <option key={name} value={name}>{name}</option>
                        ))}
                    </select>
                </div>
                <div className='form-group py-2 px-2'>
                <label htmlFor="">Rating:</label>
                  {/* Use StarRating component for selecting rating */}
                  <StarRating starsSelected={formData.rating} totalStars={5} onRate={handleRate} resetStars={resetStars} />
                </div>
                <div className='form-group py-2'>
                    <span class="input-group-text">Write a Review</span>
                    <textarea class="form-control" aria-label="Write a Review" name="review" value={formData.review} onChange={handleChange} placeholder="Review (optional)"></textarea>
                </div>
                <div className='pt-1'>
                    <input type="submit" className="btn btn-secondary d-block w-100" value="Submit Ratings" />
                </div>
                </form>
            </div>
        </div>
    </div>
  );
};

export default RatingForm;
