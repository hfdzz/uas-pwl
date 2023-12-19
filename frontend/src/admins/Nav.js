import React from 'react'
import "bootstrap/js/dist/dropdown"

export default function Nav() {
  return (
    <nav className='navbar navbar-expand-sm navbar-dark bg-transparent'>
        <a className='navbar-brand bi bi-justify-left fs-4'></a>
        <button className='navbar-toggle d-lg-none' type='button' data-bs-toggle='collapse'></button>
        <div className='collapse navbar-collapse' id='collapsibleNavId'>
            <ul className='navbar-nav ms-auto mt-2 mt-lg-0'>
                <li className='nav-item dropdown'>
                    <a className='nav-link dropdown-toggle' href='#' id='dropdownId' data-bs-toggle='dropdown' aria-haspopup="true" aria-expanded="false">
                        Leroy
                    </a>
                    <div className='dropdown-menu' aria-labelledby='dropdownId'>
                        <a className='dropdown-item' href='#'>Profile</a>
                        <a className='dropdown-item' href='#'>Logout</a>
                    </div>
                </li>
            </ul>
        </div>
    </nav>
  )
}
