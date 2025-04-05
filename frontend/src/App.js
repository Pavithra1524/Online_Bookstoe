import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [books, setBooks] = useState([]);
  const [cart, setCart] = useState([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    axios.get("http://localhost:5000/books").then(res => setBooks(res.data));
  }, []);

  const searchBooks = () => {
    axios.get(`http://localhost:5000/books/search?q=${query}`).then(res => setBooks(res.data));
  };

  const addToCart = (book) => {
    axios.post("http://localhost:5000/cart", book);
    setCart([...cart, book]);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>📚 BookStoreApp</h1>

      <input
        type="text"
        placeholder="Search books..."
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <button onClick={searchBooks}>Search</button>

      <h2>Books</h2>
      {books.map(book => (
        <div key={book.id} style={{ marginBottom: 10 }}>
          <b>{book.title}</b> by {book.author} ({book.category})
          <button onClick={() => addToCart(book)} style={{ marginLeft: 10 }}>Add to Cart</button>
        </div>
      ))}

      <h2>🛒 Cart ({cart.length})</h2>
      {cart.map((b, i) => <div key={i}>{b.title}</div>)}
    </div>
  );
}

export default App;
