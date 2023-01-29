from models.books_class import Books

book_1 = Books("Lord of the Rings", "J R R Tolken", "Fantasy")
book_2 = Books("The Expanse", "James S A Corey", "Sci-Fi")
book_3 = Books("Shadow and Bone", "Leigh Bardugo", "Fantasy")

books = [book_1,book_2,book_3]

def add_new_book(new_book):
    books.append(new_book)

def remove_book(index):
    del books[int(index)]

# def remove_book(book_title):
#     book_to_remove = None
#     for book in books:
#         if books == book_title:
#             book_to_remove = book
#             break

#     books.remove(book_to_remove)