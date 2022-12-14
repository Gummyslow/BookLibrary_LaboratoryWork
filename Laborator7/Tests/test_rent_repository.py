import unittest
from Laborator7.Repository.rent_repository import *
from Laborator7.Domain.rent_domain import Rent

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.__rent_repository = BookRepository()

    def tearDown(self) -> None:
        pass

    def test_rent_book(self):
        pass

    def test_return_book(self):
        pass

    def test

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
