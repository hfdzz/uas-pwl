import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Beranda from './pages/Beranda';
import Profile from './pages/Profile';
import ProductDetail from './pages/ProductDetail';
import Keranjang from './pages/Keranjang';
import Login from './pages/Login';
import Signin from './pages/Signin';
import Payment from './pages/Payment';
import Admin from './admins/Admin';
import Customers from './admins/Customers';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Beranda/>}></Route>
        <Route path="/profile" element={<Profile/>}></Route>
        <Route path="/productDetail" element={<ProductDetail/>}></Route>
        <Route path="/cart" element={<Keranjang/>}></Route>
        <Route path="/login" element={<Login/>}></Route>
        <Route path="/signin" element={<Signin/>}></Route>
        <Route path="/payment" element={<Payment/>}></Route>
        <Route path="/admin" element={<Admin/>}></Route>
        <Route path="/customers" element={<Customers/>}></Route>
      </Routes>
    </Router>
  );
}

export default App;