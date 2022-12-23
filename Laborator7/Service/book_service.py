from Laborator7.Domain.book_domain import Book
from Laborator7.Repository.book_repository import BookRepository

class BookService:
    def __init__(self, book_repository: BookRepository):
        self.__book_repository = book_repository

    def get_all_books(self):
        return self.__book_repository.find_all_books()

    def add_book(self, id, title, author, publisher, year, description, availability, rents):
        book = Book(id, title, author, publisher, year, description, availability, rents)
        return self.__book_repository.add_book(book)

    def update_book(self, id, new_title, new_author, new_publisher, new_year, new_description,availability,rents): #We can only update a book's caracteristics
        new_book = Book(id, new_title, new_author, new_publisher, new_year, new_description,availability,rents)
        return self.__book_repository.update_book(new_book)

    def search_book(self, id, title, author, publisher, year, description):
        search_book = Book(id, title, author, publisher, year, description)
        return self.__book_repository.search_book(search_book)

    def sort_book_title(self):
        return self.__book_repository.sort_book_title()

    def delete_by_id_book(self, id):
        self.__book_repository.delete_book(id)

