import React from 'react'
import Nav from "./Nav"

export default function () {
  return (
    <div className='px-3'>
        <Nav/>
        <div className='container-fluid'>
            <div className='row g-3 my-2'>
                <div className='col-md-3'>
                    <div className='p-3 bg-white shadow-sm d-flex justify-content-around align-items-center rounded'>
                        <div>
                            <h3 className='fs-2'>101</h3>
                            <p className='fs-5'>Fantasy</p>
                        </div>
                        <i className='bi bi-cart-plus p-3 fs-1'></i>
                    </div>
                </div>
                <div className='col-md-3'>
                    <div className='p-3 bg-white shadow-sm d-flex justify-content-around align-items-center rounded'>
                        <div>
                            <h3 className='fs-2'>100</h3>
                            <p className='fs-5'>Novels</p>
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
                <th scope="col">First</th>
                <th scope="col">Last</th>
                <th scope="col">Handle</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
                </tr>
                <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
                </tr>
                <tr>
                <th scope="row">3</th>
                <td>Larry</td>
                <td>the Bird</td>
                <td>@twitter</td>
                </tr>
            </tbody>
            </table>
        </div>
    </div>
  )
}
