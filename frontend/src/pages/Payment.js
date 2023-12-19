// src/components/PaymentForm.js
import React, { useState } from 'react';
import Footer from '../components/global/Footer';
import Navigasi from '../components/global/Navigasi';
import './Payment.css';
import '../App.css';

const PaymentForm = () => {
  const [cardNumber, setCardNumber] = useState('');
  const [expiryDate, setExpiryDate] = useState('');
  const [cvc, setCvc] = useState('');

  const handlePayment = () => {
    // Add logic to handle payment (integrate with your payment gateway)
    console.log('Processing payment...');
  };

  return (
    <div>
        <div className='App'><Navigasi/></div>
        <div className='container'>
            <h2>Payment Information</h2>
            <form>
                <label>
                Card Number:
                <input
                    type="text"
                    value={cardNumber}
                    onChange={(e) => setCardNumber(e.target.value)}
                />
                </label>
                <br />
                <label>
                Expiry Date:
                <input
                    type="text"
                    value={expiryDate}
                    onChange={(e) => setExpiryDate(e.target.value)}
                />
                </label>
                <br />
                <label>
                    CVC:
                    <input type="text" value={cvc} onChange={(e) => setCvc(e.target.value)} />
                </label>
                <br />
                <button type="button" onClick={handlePayment}>
                    Process Payment
                </button>
            </form>
        </div>

        <div className='App'><Footer/></div>
    </div>
  );
};

export default PaymentForm;
