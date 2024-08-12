// StarRating.js

import React, { useState, useEffect } from 'react';
import './StarRating.css'; // Import CSS file for styles

const StarRating = ({ starsSelected = 0, totalStars = 5, onRate = f => f, resetStars }) => {
  const [selectedStars, setSelectedStars] = useState(starsSelected);

  useEffect(() => {
    if (resetStars) {
      setSelectedStars(0);
    }
  }, [resetStars]);

  const handleRate = star => {
    setSelectedStars(star);
    onRate(star);
  };

  return (
    <div>
      {[...Array(totalStars)].map((n, i) => (
        <span key={i}
          className={i < selectedStars ? 'star checked' : 'star'}
          onClick={() => handleRate(i + 1)}>&#9733;</span> // Use a star unicode character
      ))}
    </div>
  );
};

export default StarRating;
