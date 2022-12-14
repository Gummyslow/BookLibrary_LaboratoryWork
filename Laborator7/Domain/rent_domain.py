import itertools


class Rent:
    def __init__(self, id_rent, id_book, id_customer, type):
        self.__id_rent = id_rent
        self.id_book = id_book
        self.id_customer = id_customer
        self.__type = type

    def get_id_rent(self):
        return self.__id_rent

    def get_id_customer(self):
        return self.id_customer

    def get_id_book(self):
        return self.id_book

    def get_type(self):
        return  self.__type

    def set_id_rent(self, id_rent):
        self.__id_rent = id_rent

    def set_id_customer(self, id_customer):
        self.id_customer = id_customer

    def set_id_book(self, id_book):
        self.id_book = id_book

    def set_type(self, type):
        self.__type = type

    def __str__(self):
        return f'{self.__type} id: {self.__id_rent}, Book Id: {self.id_book}, Customer Id: {self.id_customer}'

    def __repr__(self):
        return f'{self.__type} id: {self.__id_rent}, Book Id: {self.id_book}, Customer Id: {self.id_customer}'
