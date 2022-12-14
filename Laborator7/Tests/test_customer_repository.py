import unittest
from Laborator7.Repository.customer_repository import *
from Laborator7.Domain.customer_domain import Customer

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self) -> None:
        self.__customer_repository = CustomerRepository()

if __name__ == '__main__':
    unittest.main()
