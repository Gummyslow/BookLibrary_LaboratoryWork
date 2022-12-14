from Laborator7.Repository.book_repository import BookRepository
from Laborator7.Repository.customer_repository import CustomerRepository


class RentRepository:
    def __init__(self, book_repository: BookRepository, customer_repository: CustomerRepository):
        self.__all_rents = {}
        self.__book_repository = book_repository
        self.__customer_repository = customer_repository

    def rent_book(self, rent):
        if self.__find_by_id(rent.get_id_rent()) is not None:
            raise ValueError("Duplicate rent id!")
        if self.__book_repository.find_book_by_id(rent.get_id_book()) is None:
            raise ValueError("There's no book with this id!")
        if self.__customer_repository.find_customer_by_id(rent.get_id_customer()) is None:
            raise ValueError("There's no customer with this id!")
        if self.__book_repository.find_book_by_availability(rent.get_id_book(), 'Unavailable') is not None:
            raise ValueError("The book you are trying to rent isn't available!")
        if self.__customer_repository.find_customer_by_owned(rent.get_id_customer(), 'Owns') is not None:
            raise ValueError("This customer already rented a book. He needs to return it so he can rent more")
        self.__all_rents[rent.get_id_rent()] = rent  # This ads the rent to the list of rents
        self.__customer_repository.update_own_rent(
            rent.get_id_customer())  # schimba parametrul own: Lacks -> Owns (daca da rent la o carte)
        self.__book_repository.update_availability_rent(
            rent.get_id_book())  # schimba parametrul availability: Available -> Unavailable
        self.__book_repository.book_rent_count(rent.get_id_book())
        self.__customer_repository.customer_rent_count(rent.get_id_customer())


    def return_book(self, rent):
        if self.__find_by_id(rent.get_id_rent()) is not None:
            raise ValueError("Duplicate rent id!")
        if self.__book_repository.find_book_by_id(rent.get_id_book()) is None:
            raise ValueError("There is no book with this id!")
        if self.__customer_repository.find_customer_by_id(rent.get_id_customer()) is None:
            raise ValueError("There is no customer with this id!")
        if self.__book_repository.find_book_by_availability(rent.get_id_book(), 'Available'):
            raise ValueError("You can't return a book that isn't rented!")
        if self.__customer_repository.find_customer_by_owned(rent.get_id_customer(), 'Lacks'):
             raise ValueError("This customer has no book rented, so he can't return one!")
        if self.verify_return(rent.get_id_book(), rent.get_id_customer()) is False: #verific daca customerul acesta, a inchiriat cartea
            raise ValueError("This customer can't return this book, because he dosen't own it!")
        self.__all_rents[rent.get_id_rent()] = rent
        self.__customer_repository.update_own_return(
            rent.get_id_customer())  # schimba parametrul own: Owns -> Lacks (daca da rent la o carte)
        self.__book_repository.update_availability_return(
            rent.get_id_book())  # schimba parametrul availability: Unavailable -> Available

    def most_popular(self, number):
        top = int(*number)
        lista2 = []
        lista = self.__book_repository.sort_by_popularity()
        for i in range(top):
            lista2.append(lista[i])
        return lista2

    def __find_by_id(self, id_rent):
        return self.__all_rents.get(id_rent, None)

    def find_all_rents(self):
        return list(self.__all_rents.values())

    def verify_return(self, id_book, id_customer):
        for entity in self.__all_rents:
            if self.__all_rents[entity].get_id_book() == id_book and self.__all_rents[entity].get_id_customer() == id_customer and self.__all_rents[entity].get_type() == 'Rent':
                return True
        return False

