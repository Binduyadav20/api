from flask import Flask, jsonify, request, send_from_directory
import json

app = Flask(__name__)


def load_books():
    with open('books.json', 'r') as file:
        return json.load(file)


def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')


@app.route('/api/books', methods=['GET'])
def get_books():
    books = load_books()
    return jsonify(books)


@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json
    books = load_books()
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)
