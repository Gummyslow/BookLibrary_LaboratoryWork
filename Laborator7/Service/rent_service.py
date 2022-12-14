from Laborator7.Domain.rent_domain import Rent
from Laborator7.Repository.rent_repository import RentRepository
from Laborator7.Repository.book_repository import BookRepository
from Laborator7.Repository.customer_repository import CustomerRepository


class RentService:
    def __init__(self, rent_repository: RentRepository, book_repository: BookRepository,
                 customer_repository: CustomerRepository):
        self.__rent_repository = rent_repository
        self.__book_repository = book_repository
        self.__customer_repository = customer_repository

    def get_all_rents(self):
        return self.__rent_repository.find_all_rents()

    def rent_book(self, id_rent, id_book, id_customer, type):
        rent = Rent(id_rent, id_book, id_customer, type)
        return self.__rent_repository.rent_book(rent)

    def return_book(self, id_rent, id_book, id_customer, type):
        rent = Rent(id_rent, id_book, id_customer, type)
        return self.__rent_repository.return_book(rent)

    def most_popular(self, number):
        return self.__rent_repository.most_popular(number)
