from typing import Tuple, Any

from Laborator7.Service.customer_service import CustomerService
from Laborator7.Service.book_service import BookService
from Laborator7.Service.rent_service import RentService


class Console:
    def __init__(self, customer_service: CustomerService, book_service: BookService, rent_service: RentService):
        self.__customer_service = customer_service
        self.__book_service = book_service
        self.__rent_service = rent_service

    def ui_add_book(self, *args):
        try:
            id, title, author, publisher, year, description = args
            rents = 0
            self.__book_service.add_book(id, title, author, publisher, year, description,
                                         'Available',
                                         rents)  # when adding a book, it will become automatically *on stock*
        except ValueError:
            print('Duplicate id!')
        except KeyError as ke:
            print(ke)

    def ui_add_customer(self, *args):
        try:
            id, first_name, last_name, cnp = args
            rents = 0
            self.__customer_service.add_customer(id, first_name, last_name, cnp, 'Lacks', rents)
        except ValueError:
            print('Duplicate id!')
        except KeyError as ke:
            print(ke)

    def ui_update_book(self, *args):
        try:
            id, new_title, new_author, new_publisher, new_year, new_description = args
            rents = 0
            id = int(id)
            self.__book_service.update_book(id, new_title, new_author, new_publisher, new_year, new_description, 'Available', rents)
        except KeyError as ke:
            print(ke)

    def ui_update_customer(self, *args):
        try:
            id, new_first_name, new_last_name, new_cnp = args
            id = int(id)
            rents = 0
            self.__customer_service.update_customer(id, new_first_name, new_last_name, new_cnp, 'Lacks', rents)
        except KeyError as ke:
            print(ke)

    def ui_delete_book(self, *args):
        try:
            id = args
            self.__book_service.delete_by_id_book(id)
        except KeyError as ke:
            print(ke)

    def ui_delete_customer(self, *args):
        try:
            id = args
            self.__customer_service.delete_by_id_customer(id),
        except KeyError as ke:
            print(ke)

    def ui_search_book(self, *args):
        try:
            title, author, publisher = args
            print(self.__book_service.search_book(None, title, author, publisher, None, None))
        except KeyError as ke:
            print(ke)

    def ui_search_customer(self, *args):
        '''

        :param args:
        :return:
        '''
        try:
            search_list = []
            first_name, last_name, cnp = args
            search_list = self.__customer_service.search_customer(None, first_name, last_name, cnp)
            print(search_list)
        except KeyError as ke:
            print(ke)

    def ui_rent_book(self, *args):
        try:
            id_rent, id_book, id_customer = args
            self.__rent_service.rent_book(id_rent, id_book, id_customer, 'Rent')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

    def ui_return_book(self, *args):
        try:
            id_rent, id_book, id_customer = args
            self.__rent_service.return_book(id_rent, id_book, id_customer, 'Return')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

    def ui_most_popular(self, *args):
        try:
            number = args
            print(self.__rent_service.most_popular(number))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)

    def ui_sort_book_title(self):
        try:
            print(self.__book_service.sort_book_title())
        except ValueError as ve:
            print(ve)

    def ui_sort_customer_first_name(self):
        try:
            print(self.__customer_service.sort_customer_first_name())
        except ValueError as ve:
            print(ve)

    def ui_sort_customer_rents(self):
        try:
            print(self.__customer_service.sort_customer_rents())
        except ValueError as ve:
            print(ve)

    def ui_most_active(self):
        print(self.__customer_service.most_active())

    def ui_get_all_books(self):
        for entity in self.__book_service.get_all_books():
            print(entity)

    def ui_get_all_customers(self):
        for entity in self.__customer_service.get_all_customers():
            print(entity)

    def ui_get_all_rents(self):
        for entity in self.__rent_service.get_all_rents():
            print(entity)

    def print_options(self):
        print('add_book: This command helps you to add a book to the list of books \n'
              'add_customer: This command helps you to add a customer to the list of customers \n'
              'update_book: This command helps you to update an existent book (id,new_title,new_author,new_publisher,new_year,new_description)\n'
              'update_customer: This command helps you to update an existent customer (id,new_first_name,new_last_name,new_cnp)\n'
              'delete_book: This command will remove a specific book from the list \n'
              'delete_customer: This command will remove a specific customer from the list \n'
              'search_customer: This command will search a specific customer in the list of customers \n'
              'search_book: This command will search a specific book in the list of books \n'
              'rent_book: This command will help a customer rent a book (id_book,id_customer)\n'
              'return_book: This command will help a customer to return a rented book (id_book,id_customer)\n'
              'most_popular: This command will show you the top X of the most popular books at this moment \n'
              'sort_book_title: This command will sort the books in alphabetical order of their titles \n'
              'sort_customer_first_name: This command will show you the customers, sorted by their first name\n'
              'sort_customer_rents: This command will show you the customers, sorted by the number of rented books\n'
              'most_active: This command will return you a list with the most 20% active customers\n'
              'get_all_books: This command will print all books that are in the library \n'
              'get_all_customers: This command will print all customers that are registered in the library \n'
              'get_all_rents: This command will print the history of rents that were registered\n'
              'x: This command will close the program')

    def read_commands(self):
        line = input('Select the command you want to do: ')
        pos = line.find(' ')
        if pos == -1:
            return line, []
        cmd = line[:pos]
        args = line[pos + 1:]
        args = args.split(',')
        args = [s.strip() for s in args]
        return cmd, args

    def run_menu(self):
        all_books = []
        all_customers = []
        book_options = {'add_book': self.ui_add_book, 'update_book': self.ui_update_book,
                        'delete_book': self.ui_delete_book,
                        'search_book': self.ui_search_book, 'sort_book_title': self.ui_sort_book_title,
                        'get_all_books': self.ui_get_all_books
                        }
        customer_options = {'add_customer': self.ui_add_customer, 'update_customer': self.ui_update_customer,
                            'delete_customer': self.ui_delete_customer,
                            'search_customer': self.ui_search_customer,
                            'sort_customer_first_name': self.ui_sort_customer_first_name,
                            'sort_customer_rents': self.ui_sort_customer_rents, 'most_active': self.ui_most_active,
                            'get_all_customers': self.ui_get_all_customers}

        rent_options = {'rent_book': self.ui_rent_book, 'return_book': self.ui_return_book,
                        'get_all_rents': self.ui_get_all_rents, 'most_popular': self.ui_most_popular}
        while True:
            self.print_options()
            try:
                cmd, args = self.read_commands()
                if cmd == 'x':
                    break
                for index in range(len(list(book_options.keys()))):
                    if cmd == list(book_options.keys())[index]:
                        book_options[cmd](*args)
                for index in range(len(list(customer_options.keys()))):
                    if cmd == list(customer_options.keys())[index]:
                        customer_options[cmd](*args)
                for index in range(len(rent_options.keys())):
                    if cmd == list(rent_options.keys())[index]:
                        rent_options[cmd](*args)
            except KeyError as ke:
                print('Option not yet implemented', ke)
