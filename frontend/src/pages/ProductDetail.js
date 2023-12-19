import React from 'react';
import '.././App.css';
import './ProductDetail.css';
import DetailsThumb from '../components/produkDetail/Details';
import lotr from '../components/image/lotr.jpg';
import Navigasi from '../components/global/Navigasi';
import Footer from '../components/global/Footer';

class ProductDetails extends React.Component{

  state = {
    products: [
      {
        "_id": "1",
        "title": "The Lord of The Rings",
        "src": [
            lotr,
          ],
        "content": "Author : J.R.R Tolkien",
        "description": "The Lord of the Rings adalah seri film berisi tiga film petualangan fantasi yang disutradarai Peter Jackson. Film tersebut berdasarkan novel The Lord of the Rings oleh J. R. R. Tolkien",
        "price": 250000,

        "count": 1
      }
    ],
    index: 0
  };

  myRef = React.createRef();

  handleTab = index =>{
    this.setState({index: index})
    const images = this.myRef.current.children;
    for(let i=0; i<images.length; i++){
      images[i].className = images[i].className.replace("active", "");
    }
    images[index].className = "active";
  };

  componentDidMount(){
    const {index} = this.state;
    this.myRef.current.children[index].className = "active";
  }

  render(){
    const {products, index} = this.state;
    return(
      <div >
        <div className='App'><Navigasi/></div>
        <div className="productDetails">
        {
          products.map(item =>(
            <div className="details" key={item._id}>
              <div className="big-img">
                <img src={item.src[index]} alt=""/>
              </div>

              <div className="box">
                <div className="row">
                  <h2>{item.title}</h2>
                  <span>Rp.{item.price}</span>
                </div>
   

                <p>{item.description}</p>
                <p>{item.content}</p>

                <DetailsThumb images={item.src} tab={this.handleTab} myRef={this.myRef} />
                <button className="cart">Add to cart</button>

              </div>
            </div>
          ))
        }
        </div>

        <div className='App'><Footer/></div>

      </div>
    );
  };
}

export default ProductDetails;
