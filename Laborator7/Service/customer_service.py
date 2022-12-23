from Laborator7.Domain.customer_domain import Customer
from Laborator7.Repository.customer_repository import CustomerRepository
from Laborator7.Repository.customer_file_repository import CustomerFileRepository


class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.__customer_repository = customer_repository

    def get_all_customers(self):
        return self.__customer_repository.find_all_customers()

    def add_customer(self, id, first_name, last_name, cnp, own, rents):
        customer = Customer(id, first_name, last_name, cnp, own, rents)
        return self.__customer_repository.add_customer(customer)

    def update_customer(self, id, new_first_name, new_last_name, new_cnp, own, rents): #parametrul own nu e pus, daca nu merge programul, trebuie sa-l pun
        new_customer = Customer(id, new_first_name, new_last_name, new_cnp, own, rents)
        return self.__customer_repository.update_customer(new_customer)

    def sort_customer_first_name(self):
        return self.__customer_repository.sort_customer_first_name()

    def sort_customer_rents(self):
        return self.__customer_repository.sort_customer_rents()

    def most_active(self):
        return self.__customer_repository.most_active_20()

    def search_customer(self, id, first_name, last_name, cnp): #parametrul own nu e pus, daca nu merge programul, trebuie sa-l pun
        customer = Customer(id, first_name, last_name, cnp)
        return self.__customer_repository.search_customer(customer)

    def delete_by_id_customer(self, id):
        self.__customer_repository.delete_customer(id)
