import React, { useState } from 'react';

export default function Search() {
    const [searchQuery, setSearchQuery] = useState('');

        const handleSearchChange = (event) => {
        setSearchQuery(event.target.value);
    };
    
    return(
        <section id="search" className="App-section">
          <h2>Search Products</h2>
          <div className="search-container">
            <input
              type="text"
              placeholder="Enter your search query"
              value={searchQuery}
              onChange={handleSearchChange}
            />
            <button onClick={() => alert(`Search for: ${searchQuery}`)}>
              Search
            </button>
          </div>
        </section>
    );
}