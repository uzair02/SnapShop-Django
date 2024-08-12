import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';
import axios from 'axios';
import './ProfilePageCSS/ProfilePage.css';
import StarRatings from 'react-star-ratings';

const ProfilePage = () => {
    const token = localStorage.getItem("authTokens");
    let userId = null;

    if (token) {
        const decoded = jwtDecode(token);
        userId = decoded.user_id;
    }

    const [userInfo, setUserInfo] = useState(null);
    const [wishlist, setWishlist] = useState([]);
    const [reviews, setReviews] = useState([]);

    const fetchWishlist = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/mark/get_wishlist_items/', {
                params: { userId },
            });

            const productIds = response.data.map(item => item.product);
            const url = `http://127.0.0.1:8000/store/webstores/?productIds=${productIds.join(',')}`;

            const productDetailsResponse = await axios.get(url);

            if (productDetailsResponse.data) {
                const detailedProducts = productDetailsResponse.data;
                // console.log(detailedProducts)
                const wishlistWithDetails = response.data.map(item => {
                    const productDetail = detailedProducts.find(product => product.id === item.product);
                    return {
                        ...item,
                        product: productDetail.title,
                        link: productDetail.link,
                        productId: productDetail.id
                    };
                });

                setWishlist(wishlistWithDetails);
            } else {
                console.error('Unexpected response from product details endpoint');
            }

        } catch (error) {
            console.error('Error fetching wishlist:', error);
        }
    };


    const fetchReviews = async () => {
      try {
          const response = await axios.get('http://127.0.0.1:8000/mark/get_user_reviews/', {
              params: { userId },
          });

          const productIds = response.data.map(review => review.product);

          const url = `http://127.0.0.1:8000/store/webstores/?productIds=${productIds.join(',')}`;

          const productDetailsResponse = await axios.get(url);

          const detailedProducts = productDetailsResponse.data;
          console.log(detailedProducts)
          const reviewsWithNames = response.data.map(review => {
            const productDetail = detailedProducts.find(product => product.id === review.product);
            return{
              ...review,
              product: productDetail.title,
              reviewId: productDetail.id,
              price: productDetail.price
            };
          });
          setReviews(reviewsWithNames);
      } catch (error) {
          console.error('Error fetching reviews:', error);
      }
  };


    useEffect(() => {
        const fetchUserInfo = async () => {
            try {
                // console.log("in user clock id = ", userId);
                const response = await axios.get('http://127.0.0.1:8000/api/get_profile/', {
                    params: { userId }
                });
                setUserInfo(response.data);
            } catch (error) {
                console.error('Error fetching user info:', error);
            }
        };

        fetchWishlist();
        fetchReviews();
        fetchUserInfo();
    }, []);

    const handleToggleWishlist = async (productId) => {
        try {
            const confirmation = window.confirm('Are you sure you want to remove this item from wishlist?');
            if (confirmation) {
                await axios.delete(`http://127.0.0.1:8000/mark/remove_from_wishlist/${productId}/`);
                // After removing item, reload wishlist
                fetchWishlist();
            }
        } catch (error) {
            console.error('Error toggling wishlist:', error);
            alert('Failed to toggle wishlist!');
        }
    };


    const handleDeleteReview = async (reviewId) => {
      try {
          const confirmation = window.confirm('Are you sure you want to delete this review?');
          if (confirmation) {
          await axios.delete(`http://127.0.0.1:8000/mark/delete_review/${reviewId}`);
          // After successful deletion, you may want to update the reviews state to reflect the changes
          // For example, refetch the reviews data after deletion
          fetchReviews(); // Assuming fetchReviews() fetches the updated review data
          }
      } catch (error) {
          console.error('Error deleting review:', error);
          alert('Failed to delete review!');
      }
  };



    return (
        <>
            <section className="section about-section gray-bg" id="about">
                <div className="container">
                    <div className="row align-items-center flex-row-reverse">
                        <div className="col-lg-6">
                        <div className="about-text go-to">
                          <h3 className="dark-color">About Me</h3>
                          <div className="row about-list">
                          {userInfo ? (
                            <>
                            <div className="col-md-6">
                              <div className="media">
                                <label>Full Name</label>
                                <p>{userInfo.full_name}</p>
                              </div>
                              <div className="media">
                                <label>Email</label>
                                <p>{userInfo.email}</p>
                              </div>
                            </div>
                            <div className="col-md-6">
                              <div className="media">
                                <label>Username</label>
                                <p>{userInfo.username}</p>
                              </div>
                              <div className="media">
                                <label>Bio</label>
                                <p>{userInfo.bio}</p>
                              </div>
                            </div>
                            <div className="py-2"></div>
                            <Link to="/EditProfile" className="btn btn-secondary">Edit Profile</Link>

                            {/* <Link to="/edit-profile" className="btn btn-primary">Edit Profile</Link> */}
                            </>
                              ) : (
                                <p>Loading user information...</p>
                              )}
                          </div>

                          {/* End of Profile information */}

                        </div>
                        </div>
                        <div className="col-lg-6">
                          <div className="about-avatar">
                            <img src="https://bootdey.com/img/Content/avatar/avatar7.png" title="" alt="" />
                          </div>
                        </div>
                    </div>
                    <div className="counter">
                        <h3 className="text-start mb-4">Wishlist</h3>
                        <div className="row">
                            <div className="col-12 mb-4">
                                <div className="fw-bold my-0 py-2">
                                    <div className="row">
                                          {wishlist.length > 0 ? (
                                              <>
                                                  {wishlist.map(item => (
                                                      <div className="col-12 mb-2" key={item.productId}>
                                                          <div className="border p-2 d-flex justify-content-between align-items-center">
                                                              <p className="m-0px font-w-600">
                                                                  <a href={item.link} className="wishlist-link" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none', fontFamily: 'inherit', color: 'inherit' }}>
                                                                      {item.product}
                                                                  </a>
                                                              </p>
                                                              <button
                                                                  className="btn btn-outline-secondary rounded-circle"
                                                                  style={{ border: 'none', width: '40px', height: '40px' }}
                                                                  onClick={() => handleToggleWishlist(item.productId)}
                                                              >
                                                                  <i className="fas fa-heart heart-icon"></i>
                                                              </button>
                                                          </div>
                                                      </div>
                                                  ))}
                                              </>
                                          ) : (
                                            <>
                                            <div class="counter">
                                              <div class="row">
                                                  <div class="col-12">
                                                      <div class="count-data text-center">
                                                          <h6 class="count h2" style={{ fontSize: 25}}>No Wishlist Yet</h6>
                                                      </div>
                                                  </div>
                                              </div>
                                          </div>
                                          </>
                                          )}

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="py-4"></div>

                    <div className="counter">
                        <h3 className="text-start mb-4">Reviews</h3>
                        <div className="row">
                            <div className="col-12 mb-4">
                                <div className="fw-bold my-0 py-2">
                                    <div className="row">
                                    {reviews.length > 0 ? (
                                          <>
                                              {reviews.map(review => (
                                                  <div className="col-12 mb-2" key={review.id}>
                                                      <div className="border p-2">
                                                        <div className="d-flex justify-content-between align-items-center">
                                                            <p className="m-0px font-w-600">
                                                                <a href={review.link} className="wishlist-link" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none', fontFamily: 'inherit', color: 'inherit' }}>
                                                                    Title: {review.product}
                                                                </a>
                                                            </p>
                                                            <button
                                                                className="btn btn-outline-secondary rounded-circle"
                                                                style={{ border: 'none', width: '40px', height: '40px' }}
                                                                onClick={() => handleDeleteReview(review.reviewId)}
                                                            >
                                                                <i className="fas fa-trash text-red heart-icon"></i>
                                                            </button>
                                                        </div>
                                                        {review.price && (
                                                                <p className="m-0px font-w-600">Price: {review.price}</p>
                                                            )}
                                                          <div className="d-flex align-items-center py-1">
                                                              <p className="m-0px font-w-600 mr-2">Rating:</p>
                                                              {/* Incorporate the StarRatings component here */}
                                                              <StarRatings
                                                                  rating={review.rating}
                                                                  starRatedColor="gold"
                                                                  numberOfStars={5}
                                                                  name='rating'
                                                                  starDimension="22px"
                                                                  starSpacing="2px"
                                                              />
                                                          </div>
                                                          <p className="m-0px font-w-600">Review: {review.review}</p>
                                                      </div>
                                                  </div>
                                              ))}
                                          </>
                                      ) : (
                                        <>
                                        <div class="counter">
                                          <div class="row">
                                              <div class="col-12">
                                                  <div class="count-data text-center">
                                                      <h6 class="count h2" style={{ fontSize: 25}}>No Reviews Yet</h6>
                                                  </div>
                                              </div>
                                          </div>
                                      </div>
                                      </>
                                      )}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
};

export default ProfilePage;
