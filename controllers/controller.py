from flask import render_template, request, redirect
from app import app
from models.books_class import Books
from models.books_list import *

@app.route("/books")
def index():
    return render_template('index.html', title='Home', books=books)

@app.route("/books", methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Books(title,author,genre)
    add_new_book(new_book)
    return render_template('index.html', title='Home', books=books)

@app.route('/books/<index>')
def single_book(index):
    return render_template('book.html', title="Book", book=books[int(index)])

# @app.route('/books', methods=['POST'])
# def remove_book():
#     title = request.form['title']
#     author = request.form['author']
#     genre = request.form['genre']
#     book_to_remove = Books(title,author,genre)
#     remove_book(book_to_remove)
#     return render_template('index.html', title='Home', books=books)

@app.route('/books/delete/<index>', methods=['POST'])
def delete_book(index):
    remove_book(index)
    return render_template('index.html', title="Home", book=books)