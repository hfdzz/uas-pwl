import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import Nav from './Nav'
import Sidebar from './Sidebar'

const Customers = () => {

  return (
    <div className='container-fluid bg-secondary min-vh-100'>
        <div className='row'>
            <div className='col-2 bg-white vh-100'>
                <Sidebar/>
            </div>
            <div className='col'>
            <Nav/>
        <div className='container-fluid'>
            <div className='row g-3 my-2'>
                <div className='col-md-3'>
                    <div className='p-3 bg-white shadow-sm d-flex justify-content-around align-items-center rounded'>
                        <div>
                            <h3 className='fs-2'>101</h3>
                            <p className='fs-5'>Users</p>
                        </div>
                        <i className='bi bi-cart-plus p-3 fs-1'></i>
                    </div>
                </div>
            </div>
        </div>
        <div>
        <table class="table caption-top bg-white rouded mt-2">
            <caption className='text-white fs-4'>Customers</caption>
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Email</th>
                <th scope="col">Password</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Mark@zrazy.com</td>
                <td>@mdo</td>
                </tr>
                <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Jacob@Lazy.com</td>
                <td>@fat</td>
                </tr>
                <tr>
                <th scope="row">3</th>
                <td>Larry</td>
                <td>Larry@cuit.com</td>
                <td>@twitter</td>
                </tr>
            </tbody>
            </table>
        </div>
            </div>
        </div>
        
    </div>
  );
};

export default Customers;
