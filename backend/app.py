from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho", "category": "Fiction"},
    {"id": 2, "title": "Sapiens", "author": "Yuval Noah Harari", "category": "History"},
    {"id": 3, "title": "Clean Code", "author": "Robert C. Martin", "category": "Programming"},
]

cart = []

@app.route("/books", methods=["GET"])
def get_books():
    category = request.args.get("category")
    if category:
        filtered = [b for b in books if b["category"].lower() == category.lower()]
        return jsonify(filtered)
    return jsonify(books)

@app.route("/books/search", methods=["GET"])
def search_books():
    query = request.args.get("q", "").lower()
    result = [b for b in books if query in b["title"].lower() or query in b["author"].lower()]
    return jsonify(result)

@app.route("/cart", methods=["GET", "POST", "DELETE"])
def manage_cart():
    if request.method == "GET":
        return jsonify(cart)
    elif request.method == "POST":
        book = request.json
        cart.append(book)
        return jsonify({"message": "Added to cart"})
    elif request.method == "DELETE":
        cart.clear()
        return jsonify({"message": "Cart cleared"})

@app.route("/admin/books", methods=["POST"])
def add_book():
    new_book = request.json
    new_book["id"] = len(books) + 1
    books.append(new_book)
    return jsonify({"message": "Book added"})

@app.route("/admin/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Book deleted"})

if __name__ == "__main__":
    app.run(debug=True)
