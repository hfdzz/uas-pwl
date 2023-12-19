import React from 'react';
import '../App.css';
import Footer from '../components/global/Footer';
import Navigasi from '../components/global/Navigasi';
import Search from '../components/global/Search';
import Header from '../components/global/Header';
import Kategori from '../components/Kategori';

function Beranda() {

  return (
    <div className="App">
      <Navigasi/>

      <Header/>

      <Search/>

      <Kategori/>

      <Footer/>
    </div>
  );
}

export default Beranda;
