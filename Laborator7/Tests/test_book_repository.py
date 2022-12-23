from unittest import TestCase
from Laborator7.Domain.book_domain import Book
from Laborator7.Repository.book_repository import *
from Laborator7.Service.book_service import BookService


class TestBook(TestCase):
    def setUp(self):
        self.book = Book(1, 'Harap-Alb', 'Creanga', 'Ioda', 1877, 'ugaugauga', 'Available', 0)

    def test_id(self):
        self.assertTrue(self.book.get_id() == 1, "Book id should be 1!")
        self.book.set_id(101)
        self.assertTrue(self.book.get_id() == 101, "Book id should be 101!")

    def test_title(self):
        self.assertTrue(self.book.get_title() == 'Harap-Alb', "Book's title should be 'Harap-Alb'!")
        self.book.set_title('Moara cu noroc')
        self.assertTrue(self.book.get_title() == 'Moara cu noroc', "Book's title should be 'Moara cu noroc'!")

    def test_author(self):
        self.assertTrue(self.book.get_author() == 'Creanga', "Book's author should be 'Creanga'!")
        self.book.set_author('Rebreanu')
        self.assertTrue(self.book.get_author() == 'Rebreanu', "Book's author should be 'Rebreanu'!")

    def test_publisher(self):
        self.assertTrue(self.book.get_publisher() == 'Ioda', "Book's publisher should be 'Ioda'!")
        self.book.set_publisher('Peste')
        self.assertTrue(self.book.get_publisher() == 'Peste', "Book's publisher should be 'Peste'!")

    def test_year(self):
        self.assertTrue(self.book.get_year() == 1877, "Book's year should be '1877'!")
        self.book.set_year(2003)
        self.assertTrue(self.book.get_year() == 2003, "Book's year should be '2003'!")

    def test_description(self):
        self.assertTrue(self.book.get_description() == 'ugaugauga', "Book's description should be 'ugaugauga'!")
        self.book.set_description('asdfghjkl')
        self.assertTrue(self.book.get_description() == 'asdfghjkl', "Book's description should be 'asdfghjkl'!")

    def test_book_availability(self):
        self.assertTrue(self.book.get_availability() == 'Available', "Book's availability should be 'Available'!")
        self.book.set_availability('Unavailable')
        self.assertTrue(self.book.get_availability() == 'Unavailable', "Book's availability should be 'Unavailable'!")

    def test_book_rents(self):
        self.assertTrue(self.book.get_book_rents() == 0, "Book's rents should be '0'!")
        self.book.set_book_rents(20)
        self.assertTrue(self.book.get_book_rents() == 20, "Book's rents should be '20'!")

    def test_str(self):
        self.assertTrue(
            self.book.__str__() == f'Book {self.book.get_id()}, title: {self.book.get_title()}, author: {self.book.get_author()}, publisher: {self.book.get_publisher()}, year: {self.book.get_year()}, description: {self.book.get_description()}, availability: {self.book.get_availability()},  Rents: {self.book.get_book_rents()}')

    def test_repr(self):
        self.assertTrue(
            self.book.__repr__() == f'Book {self.book.get_id()}, title: {self.book.get_title()}, author: {self.book.get_author()}, publisher: {self.book.get_publisher()}, year: {self.book.get_year()}, description: {self.book.get_description()}, availability: {self.book.get_availability()},  Rents: {self.book.get_book_rents()}')

    def tearDown(self) -> None:
        pass


class TestBookService(TestCase):
    def setUp(self):
        self.book_repository = BookRepository()
        self.book_service = BookService(self.book_repository)

    def test_add_book(self):
        all_books = []
        all_books.append(self.book_service.add_book(1, 'Harap-Alb', 'Creanga', 'Ioda', 1877, 'ugaugauga', 'Available', 0))
        self.assertTrue(len(all_books) == 1, "There should be '1' book!")
        self.assertTrue(all_books[0].get_id() == 1, "Book's id should be '1'!")

    def test_update_book(self):
        all_books = []
        all_books.append(self.book_service.add_book(1, 'Harap-Alb', 'Creanga', 'Ioda', 1877, 'ugaugauga', 'Available', 0))
        self.book_service.update_book(1,'Enigma','Petrescu','Jizmund',1264,'rwgwefc', 'Available', 0)
        self.assertTrue(all_books[0].get_id() == 1, 'Book id shoul be 1!')
        self.assertTrue(all_books[0].get_title() == 'Enigma', "Book's title should've been 'Enigma'!")

    def test_delete_book(self):
        all_books = []
        all_books.append(self.book_service.add_book(1, 'Harap-Alb', 'Creanga', 'Ioda', 1877, 'ugaugauga', 'Available', 0))
        self.book_service.delete_by_id_book(1)
        self.assertTrue(len(all_books) == 0, 'List should have 0 elements!')
    def tearDown(self) -> None:
        pass
