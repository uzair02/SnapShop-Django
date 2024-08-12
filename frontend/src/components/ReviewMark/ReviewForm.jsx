import React, { useState } from 'react';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';
import { useParams } from 'react-router-dom';
import StarRating from '../StarRating/StarRating';
import { useNavigate } from 'react-router-dom';

const ReviewForm = () => {
  // Accessing the productId parameter using useParams hook
  const { productId } = useParams();
  const token = localStorage.getItem("authTokens");

  let userId = null;
  
  if (token) {
    const decoded = jwtDecode(token);
    userId = decoded.user_id;
  }

  const navigate = useNavigate();
  const [resetStars, setResetStars] = useState(false);
  const [formData, setFormData] = useState({
    rating: 0,
    review: '',
    user: userId,
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };
  
  const handleRate = rating => {
    setFormData({ ...formData, rating });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await axios.post('http://127.0.0.1:8000/mark/submit_product_review/', {
        ...formData,
        product: productId, // Include productId in the request data
      });
      console.log('Review submitted successfully!');
      // You can redirect to another page or perform any other action after successful submission
      setFormData({
        rating: 0,
        review: '',
        user: userId,
        });

        setResetStars(true);
        navigate('/ProductPage');
    } catch (error) {
        // console.log(token);
        // console.log(userId);
        // console.log(productId)
      console.error('Error submitting review:', error);
      alert('Failed to submit review!');
    }
  };

  return (
    <div className="container mt-4">
        <div className='col-md-9 card mx-auto d-flex flex-row px-0'>
            <div className="card-body d-flex flex-column justify-content-center">
                <h4 className="title text-center mt-4 pb-3">Product Review:</h4>
                <form className='col-sm-10 col-12 mx-auto' onSubmit={handleSubmit}>
                <div className='form-group py-2 px-2'>
                    <label htmlFor="">Rating:</label>
                {/* Use StarRating component for selecting rating */}
                <StarRating starsSelected={formData.rating} totalStars={5} onRate={handleRate} resetStars={resetStars} />
                </div>
                <div className='form-group py-2'>
                    <span class="input-group-text">Review:</span>
                    <textarea class="form-control" aria-label="Write a Review" name="review" value={formData.review} onChange={handleChange} placeholder=""></textarea>
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

export default ReviewForm;






