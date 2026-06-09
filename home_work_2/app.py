from flask import Flask
from db import *
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from flask import request

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

@app.route('/books', methods=["GET"])
def get_titles():
    titles = session.query(Library).all()
    result = [{"title": book.book_title} for book in titles]
    return jsonify(result)

@app.route('/authors', methods=["GET"])
def get_authors():
    authors = session.query(Library).all()
    result = [{"author": book.author} for book in authors]
    return jsonify(result)


@app.route('/book', methods=["POST"])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    new_book = Library(book_title=title, author=author)

    session.add(new_book)
    session.commit()
    return jsonify({"id": new_book.id, "title": new_book.book_title, "author": new_book.author}), 201

@app.route('/book/<id>', methods=["GET"])
def find_book(id):
    book = session.query(Library).filter_by(id=id).first()
    return jsonify({"title": book.book_title, "author": book.author})

@app.route('/author/<id>', methods=["GET"])
def find_author(id):
    book = session.query(Library).filter_by(id=id).first()
    return jsonify({"author": book.author, "title": book.book_title})

if __name__ == '__main__':
    app.run(debug=True)
