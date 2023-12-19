import React, { useState } from 'react';
import './Keranjang.css';
import '../App.css';
import lotr from '../components/image/lotr.jpg';
import ayatCinta from '../components/image/ayat-cinta.jpg';
import bawang from '../components/image/bawang.jpg';
import Navigasi from '../components/global/Navigasi';
import Footer from '../components/global/Footer';

const ShoppingCart = () => {
  const [cart, setCart] = useState([]);
  const [products] = useState([
    { id: 1, name: 'The Lord of The Rings', image: lotr, price: 300000 },
    { id: 2, name: 'Ayat-Ayat Cinta', image: ayatCinta, price: 210000 },
    { id: 3, name: 'Bawang Merah dan Putih', image: bawang, price: 100000 },
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
    <div>
      <div className='App'><Navigasi/></div>
      <div className='shopping-cart'>
        <h2>Shopping Cart</h2>
        <div className="products">
          {products.map(product => (
            <div className="product" key={product.id}>
              <span><img src={product.image} alt={""} style={{ width: '150px', height: '180px' }}/> {product.name} - Rp {product.price}</span>
              <button onClick={() => addToCart(product)}>+</button>
            </div>
          ))}
        </div>
        <div className="cart">
          <h3>Cart</h3>
          <ul>
            {cart.map(item => (
              <li key={item.id}>
                {item.name} = Rp {item.price}{' '}
                <button onClick={() => removeFromCart(item.id)}>Remove</button>
              </li>
            ))}
          </ul>
          <p>Total: Rp {calculateTotal()}</p>
          <button>Pay</button>
        </div>
      </div>
      

      <div className='App'><Footer/></div>
    </div>
  );
};

export default ShoppingCart;
