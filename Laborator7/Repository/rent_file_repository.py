from Laborator7.Domain.rent_domain import Rent
from Laborator7.Repository.rent_repository import RentRepository

class RentFileRepository(RentRepository):
    def __init__(self, file_name, book_repository, customer_repository):
        super().__init__(book_repository, customer_repository)
        self.__file_name = file_name
        self.read_from_file()

    def rent_book(self, rent):
        super().rent_book(rent)
        self.write_in_file()

    def return_book(self, rent):
        super().return_book(rent)
        self.write_in_file()

    def most_popular(self, number):
        super().most_popular(number)
        self.write_in_file()


    def read_from_file(self):
        try:
            f = open(self.__file_name, 'r')
            line = f.readline().strip('\n')
            while line != '':
                list_of_attributes = line.split(',')
                id_rent = int(list_of_attributes[0])
                id_book = int(list_of_attributes[1])
                id_customer = int(list_of_attributes[2])
                type = list_of_attributes[3]
                rent = Rent(id_rent, id_book, id_customer, type)
                if type == 'Rent':
                    super().rent_book(rent)
                elif type == 'Return':
                    super().return_book(rent)
                line = f.readline().strip('\n')
            f.close()
        except IOError:
            print('An error occurred while trying to open the file' + self.__file_name)

    def write_in_file(self):
        try:
            f = open(self.__file_name, 'w')
            all_rents = super().find_all_rents()
            for rent in all_rents:
                id_rent = rent.get_id_rent()
                id_book = rent.get_id_book()
                id_customer = rent.get_id_customer()
                type = rent.get_type()
                f.write(f'{id_rent},{id_book},{id_customer},{type}\n')
            f.close()
        except IOError:
            print('An error occurred while trying to open the file' + self.__file_name)