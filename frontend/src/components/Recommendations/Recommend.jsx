import React, { useState, useEffect } from 'react';
import axios from 'axios';
import StarRatings from 'react-star-ratings';

const Recommendations = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/store/recommendations/');
        setProducts(response.data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, []);

  useEffect(() => {
    console.log(products);
  }, [products]);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="container ">
      <div className="counter">
          <h3 className="text-start my-4">Recommended Products</h3>
          <div className="row">
            <div className="col-12 mb-4">
              <div className="fw-bold my-0 py-2">
                <div className="row">
                  {products.length > 0 ? (
                    <>
                      {products.map(product => (
                        <div className="col-12 mb-2" key={product.id}>
                          <div className="border rounded p-2 d-flex justify-content-between align-items-center">
                            <div>
                              <p className="m-0px font-w-600">
                                <a href={product.link} className="wishlist-link" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none', fontFamily: 'inherit', color: 'inherit' }}>
                                  {product.title}
                                </a>
                              </p>
                              {product.price && (
                                <p className="m-0px font-w-500">
                                  Price: {product.price}
                                </p>
                              )}
                              {/* Display rating if not null */}
                              {product.rating !== null && (
                                <>
                                  <div className="rating-container" style={{ display: 'flex' }}>
                                    <p className="m-0px font-w-600 pr-2" style={{ order: -1 }}>Rating:</p>
                                    <StarRatings
                                      rating={product.rating}
                                      starRatedColor="gold"
                                      numberOfStars={5}
                                      name="rating"
                                      starDimension="22px"
                                      starSpacing="2px"
                                    />
                                  </div>
                                </>
                              )}
                            </div>
                          </div>
                        </div>
                      ))}
                    </>
                  ) : (
                    <p>No items in the wishlist</p>
                  )}
                </div>
              </div>
            </div>
          </div>
      </div>
    </div>
  );
};

export default Recommendations;
