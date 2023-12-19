import './Kategori.css';
import ayatcinta from './image/ayat-cinta.jpg';
import bawang from './image/bawang.jpg';
import beethoven from './image/beethoven.jpg';
import jungle from './image/jungle.jpg';
import lotr from './image/lotr.jpg';
import sangpemimpi from './image/sang-pemimpi.jpg';

import { getAllProduk } from '../backend-api/produkAPI';

export default function Kategori() {

    const booksData = [
        { id: 1, image: ayatcinta, title: 'Ayat-Ayat Cinta', author: 'Habiburrahman El Shirazy', price: 200000,  },
        { id: 2, image: bawang, title: 'Bawang Merah dan Putih', author: '-', price: 50000 },
        { id: 3, image: beethoven, title: 'Beethoven', author: 'Beethoven', price: 190000 },
        { id: 4, image: jungle, title: 'The Jungle', author: 'Rudyard Kipling', price: 300000 },
        { id: 5, image: lotr, title: 'The Lord of The Rings', author: 'J.R.R. Tolkien', price: 250000 },
        { id: 6, image: sangpemimpi, title: 'Sang Pemimpi', author: 'Andrea Hirata', price: 150000 },
        // Add more books as needed
    ];

    

    const Book = ({ title, author, price, image }) => (
        <div className="book">
            <img src={image} alt={title} style={{ width: '200px', height: '250px' }}/>
            <h3>{title}</h3>
            <p>Author: {author}</p>
            <p>Price: Rp.{price}</p>
            <button className='detail-button'>Details</button>
            <button className='cart-button'>Add to Cart</button>
        </div>
    );

    return(
        <section id="categories" className="App-section">
            <h2>Product Categories</h2>
            <div className="Product-category">
                <h1>Fantasy</h1>
                <section>
                    <div className="books-container">
                        {booksData.map((book) => (
                        <Book key={book.id} {...book} />
                        ))}
                    </div>
                </section>
            </div>
            <div className="Product-category">
                <h1>Novel</h1>
                <section>
                    <div className="books-container">
                        {booksData.map((book) => (
                        <Book key={book.id} {...book} />
                        ))}
                    </div>
                </section>
            </div>
        </section>
    );
}