import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

// Function to extract domain from a URL
const getDomainFromUrl = (url) => {
  try {
    const { hostname } = new URL(url);
    return hostname;
  } catch (error) {
    console.error('Error extracting domain:', error);
    return url;
  }
};

const Products = ({ products }) => {

  const token = localStorage.getItem("authTokens")
  let userId = null;

  if (token){
    const decoded = jwtDecode(token) 
    userId = decoded.user_id
  } 

  const [scrapedProducts, setScrapedProducts] = useState([]);
  const [wishlist, setWishlist] = useState([]);

  useEffect(() => {
    // Fetch scraped products when the component mounts
    fetchScrapedProducts();
  }, []);

  const fetchScrapedProducts = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/get_scraped_products/');
      setScrapedProducts(response.data);
    } catch (error) {
      console.error('Error fetching scraped products:', error);
    }
  };

  const fetchWishlist = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/mark/get_wishlist/');
      setWishlist(response.data);
    } catch (error) {
      console.error('Error fetching wishlist:', error);
    }
  };

  const handleReview = (productId) => {
    console.log("Product ID:", productId); // Log the productId
    // Redirect to review form page with product ID
    window.location.href = `/ReviewForm/${productId}`;
  };

  const handleToggleWishlist = async (productId) => {
    try {
      if (wishlist.some(item => item.product === productId)) {
        // If the product is already in the wishlist, remove it
        await axios.delete(`http://127.0.0.1:8000/mark/remove_from_wishlist/${productId}/`);
        setWishlist(prevWishlist => prevWishlist.filter(item => item.product !== productId));
        alert('Product removed from wishlist successfully!');
      } else {
        // If the product is not in the wishlist, add it
        const requestData = {
          user: userId,
          product: productId,
        };
        await axios.post('http://127.0.0.1:8000/mark/add_to_wishlist/', requestData);
        setWishlist(prevWishlist => [...prevWishlist, requestData]);
        // alert('Product added to wishlist successfully!');
      }
    } catch (error) {
      console.error('Error toggling wishlist:', error);
      // alert('Failed to toggle wishlist!');
    }
  };

  return (
    <div className="container py-3">
      <div className="container my-3 py-3">
        <div className="row">
          <div className="col-12">
            <h2 className="display-7 text-center text-2xl font-weight-bolder py-2">Websites</h2>
            <hr />
          </div>
        </div>
      </div>

      <div className="row">
        {products.map((product, index) => (
          <div className="col-md-6 col-lg-4 mb-4" key={index}>
            <div className="border rounded p-3">
              <h5 className="fw-bold text-center" style={{ height: "3rem", overflow: "hidden", textOverflow: "ellipsis" }}>{product.description}</h5>
              <p className="mb-2 text-center">
                <a href={product.link} style={{ fontSize: "17x" }} className="text-primary text-decoration-none" target="_blank" rel="noopener noreferrer">
                  {getDomainFromUrl(product.link)}
                </a>
              </p>
              {token !== null && (
                <div className="d-flex justify-content-center align-items-center">
                  <div className="btn-group">
                    <button
                      className="btn btn-primary"
                      style={{ backgroundColor: "#f7b030", color: "#fff", marginLeft: "auto",  borderColor: "#f7b030" }}
                      onClick={() => handleReview(product.id)}
                    >
                      Review
                    </button>
                    <button
                      className={`btn ${wishlist.some(item => item.product === product.id) ? 'btn-danger' : 'btn-secondary'}`}
                      style={{ backgroundColor: "#eb423f", color: "#fff", marginLeft: "auto",  borderColor: "#eb423f" }}
                      onClick={() => handleToggleWishlist(product.id)}
                    >
                      {wishlist.some(item => item.product === product.id) ? (
                        <i className="fas fa-heart"></i>
                      ) : (
                        <i className="far fa-heart"></i>
                      )}
                      {' '}
                      {wishlist.some(item => item.product === product.id) ? 'Remove from Wishlist' : 'Add to Wishlist'}
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      <div className="container my-3 py-3">
        <div className="row">
          <div className="col-12">
            <h2 className="display-7 text-center text-2xl font-weight-bolder">Products with Price</h2>
            <hr />
          </div>
        </div>
      </div>

      <div className="row">
        {scrapedProducts.map((product, index) => (
          <div className="col-md-6 col-lg-4 mb-4" key={index}>
            <div className="border rounded p-3" style={{ height: "147px"}}>
              <h5 className="fw-bold text-center" style={{ height: "3rem", overflow: "hidden", textOverflow: "ellipsis" }}>{product.title}</h5>
              <p className="mb-1 text-center" style={{ fontSize: '1.07rem' }}>{product.price}</p>
              <p className="mb-1 text-center">
                <a href={product.link} className="text-primary text-decoration-none" target="_blank" rel="noopener noreferrer">
                  {getDomainFromUrl(product.link)}
                </a>
              </p>
            </div>
          </div>
        ))}
      </div>

    </div>
  );
};

export default Products;
