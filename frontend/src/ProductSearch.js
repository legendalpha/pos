import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ProductSearch() {
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState([]);

    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    }

    useEffect(() => {
      const fetchData = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/api/products/`);
            console.log("Response Data:", response.data);
            setSearchResults(response.data.results);
        } catch (error) {
            console.error("Error fetching products:", error);
            // Optionally: Set an error state to display a message to the user
        }
    };
    

        fetchData();
    }, [searchTerm]); 

    return (
    <div>
      <input type="text" value={searchTerm} onChange={handleSearchChange} placeholder="Search products" />
      {searchResults ? ( // Check if searchResults exists
        <ul>
          {searchResults.map((product) => (
            <li key={product.id}>{product.name} - ${product.price}</li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>   // Display a loading message  
      )} 
    </div>
  );
}

export default ProductSearch;
