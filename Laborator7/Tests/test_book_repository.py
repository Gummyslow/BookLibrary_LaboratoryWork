from unittest import TestCase
from Laborator7.Domain.book_domain import Book
from Laborator7.Repository.book_repository import BookRepository
from Laborator7.Service.book_service import BookService


class TestBook(TestCase):
    def setUp(self):
        self.book = Book(1,'Harap-Alb','Creanga','Ioda',1877,'ugaugauga')
