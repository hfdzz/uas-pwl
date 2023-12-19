import React from 'react'
import Navigasi from '../components/global/Navigasi'
import Footer from '../components/global/Footer'
import "../App.css"
import profileIcon from '../components/image/dog.jpg';
import './Profile.css';

export default function Profile() {
  return (
    <div>
      <div className='App'><Navigasi/></div>
      <div className='upc'>
        <div className='gradiant'></div>
        <div className='profile-down'>
          <img src={profileIcon} alt=''/>
          <div className='profile-title'>Sugar Smith</div>
          <div className='profile-description'>
            Hello im Sugar Smith, Im always accompany my friend Leroy
          </div>
          <div className='profile-button'><a href='http://localhost:3000/profile'>Edit</a></div>
        </div>
      </div>
        
      <div className='App'><Footer/></div>
    </div>
  )
}
