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

@app.route("/books")
def get_books():
    return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)
