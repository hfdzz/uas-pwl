// Kode ini tidak difungsikan, melainkan hanya sekedar tempat melempar kode yang tidak terpakai
import React from 'react';
import '../App.css';
import Footer from '../components/global/Footer';
import Navigasi from '../components/global/Navigasi';
import styled from 'styled-components';

const ProfileContainer = styled.div`
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: left;
`;

const ProfileImage = styled.img`
  border-radius: 100%;
  width: 250px;
  height: 200px;
  margin-bottom: 10px;
`;

const EditButton = styled.button`
  background-color: #3498db;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
`;

const handleEditClick = () => {
  alert('Edit button clicked!');
};

const UserProfile = () => {
  const user = {
    name: 'John Doe',
    email: 'john.doe@crazy.com',
    location: 'Bandar Lampung, Indonesia',
    password: '*****',
    profileImage: 'dog.jpg', // Replace with your image file name
  };

  return (
    <div className="App">
        <Navigasi/>
        
        <ProfileContainer>
            <ProfileImage src={process.env.PUBLIC_URL + '/' + user.profileImage} alt="Profile" />
            <h2>User Profile</h2>
            <p><strong>Name:</strong> {user.name}</p>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Location:</strong> {user.location}</p>
            <p><strong>Password:</strong> {user.password}</p>
            <EditButton onClick={handleEditClick}>Edit</EditButton>
        </ProfileContainer>
    
        <Footer/>
    </div>
  );
}

export default UserProfile;


import React, { useState } from 'react';
import './Keranjang.css';

const ShoppingCart = () => {
  const [cart, setCart] = useState([]);
  const [products] = useState([
    { id: 1, name: 'Product 1', price: 10 },
    { id: 2, name: 'Product 2', price: 20 },
    { id: 3, name: 'Product 3', price: 30 },
  ]);

  const addToCart = (product) => {
    setCart([...cart, product]);
  };

  const removeFromCart = (productId) => {
    const updatedCart = cart.filter(item => item.id !== productId);
    setCart(updatedCart);
  };

  const calculateTotal = () => {
    return cart.reduce((total, item) => total + item.price, 0);
  };

  return (
    <div className="shopping-cart">
      <h2>Shopping Cart</h2>
      <div className="products">
        {products.map(product => (
          <div className="product" key={product.id}>
            <span>{product.name} - ${product.price}</span>
            <button onClick={() => addToCart(product)}>Add to Cart</button>
          </div>
        ))}
      </div>
      <div className="cart">
        <h3>Cart</h3>
        <ul>
          {cart.map(item => (
            <li key={item.id}>
              {item.name} - ${item.price}{' '}
              <button onClick={() => removeFromCart(item.id)}>Remove</button>
            </li>
          ))}
        </ul>
        <p>Total: ${calculateTotal()}</p>
      </div>
    </div>
  );
};

export default ShoppingCart;
