import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StarRatings from 'react-star-ratings';

const RatingsPage = () => {
  const [webStoreRatings, setWebStoreRatings] = useState([]);

  useEffect(() => {
    // Fetch data from the backend API endpoint
    axios.get('http://127.0.0.1:8000/store/webstore_ratings/')
      .then(response => {
        // Sort ratings based on averageRating in descending order
        const sortedRatings = response.data.sort((a, b) => b.averageRating - a.averageRating);
        setWebStoreRatings(sortedRatings);
      })
      .catch(error => {
        console.error('Error fetching web store ratings:', error);
      });
  }, []);

  return (
    <div className="container mt-3">
        <div className='card mx-auto' style={{ padding: '20px', maxWidth: '800px', width: '100%', boxShadow: '0px 0px 10px 2px rgba(0,0,0,0.1)', backgroundColor: '#f9f9f9' }}>
            <div className="card-body" style={{ backgroundColor: '#fff' }}>
                <h3 className="title text-center mt-2 pb-3" style={{ borderBottom: '2px solid #ccc', paddingBottom: '10px', fontSize: '24px' }}>Web Store Ratings</h3>
                <div className='py-1'></div>
                {webStoreRatings.map(rating => (
                <div className='row form-group py-1' key={rating.webstore}>
                    <div className="col-md-4 d-flex align-items-center justify-content-center" style={{ fontSize: '20px', fontWeight: 'bold' }}>{rating.webstore}</div>
                    <div className="col-md-4 d-flex align-items-center justify-content-center" style={{ fontSize: '18px' }}>Rating: {rating.averageRating}</div>
                    <div className="col-md-4 d-flex align-items-center justify-content-center">
                        <StarRatings
                            rating={rating.averageRating}
                            starRatedColor="gold"
                            numberOfStars={5}
                            name='rating'
                            starDimension="22px"
                            starSpacing="2px"
                        />
                    </div>
                </div>
                ))}
            </div>
        </div>
    </div>
  );
};

export default RatingsPage;
