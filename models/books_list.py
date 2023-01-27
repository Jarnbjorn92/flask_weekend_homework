from models.books_class import Books

book_1 = Books("Lord of the Rings", "J R R Tolken", "Fantasy")
book_2 = Books("The Expanse", "James S A Corey", "Sci-Fi")
book_3 = Books("Shadow and Bone", "Leigh Bardugo", "Fantasy")

books = [book_1,book_2,book_3]

def add_new_book(new_book):
    books.append(new_book)