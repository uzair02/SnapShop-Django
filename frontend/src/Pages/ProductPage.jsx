import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Products from '../components/Products/Products';

const ProductPage = () => {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/get_products/');
      setProducts(response.data);
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  useEffect(() => {
    // Fetch products when the component mounts
    fetchProducts();
  }, []);

  return (
    <div>
      <Products products={products} />
    </div>
  );
};

export default ProductPage;