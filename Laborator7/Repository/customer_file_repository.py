from Laborator7.Domain.customer_domain import Customer
from Laborator7.Repository.customer_repository import CustomerRepository

class CustomerFileRepository(CustomerRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.read_from_file()

    def add_customer(self, customer):
        super().add_customer(customer)
        self.write_in_file()

    def update_customer(self, new_customer):
        super().update_customer(new_customer)
        self.write_in_file()

    def delete_customer(self, id_customer):
        super().delete_by_id_customer(id_customer)
        self.write_in_file()

    def read_from_file(self):
        try:
            f = open(self.__file_name, 'r')
            line = f.readline().strip('\n')
            while line != '':
                list_of_attributes = line.split(',')
                id_customer = int(list_of_attributes[0])
                first_name = list_of_attributes[1]
                last_name = list_of_attributes[2]
                cnp = int(list_of_attributes[3])
                own = 'Lacks'
                rents = 0
                customer = Customer(id_customer, first_name, last_name, cnp, own, rents)
                super().add_customer(customer)
                line = f.readline().strip("\n")
            f.close()
        except IOError:
            print('An error occurred while trying to open the file' + self.__file_name)

    def write_in_file(self):
        try:
            f = open(self.__file_name, 'w')
            all_customers = super().find_all_customers()
            for customer in all_customers:
                id = customer.get_id()
                first_name = customer.get_first_name()
                last_name = customer.get_last_name()
                cnp = customer.get_cnp()
                f.write(f'{id},{first_name},{last_name},{cnp}\n')
            f.close()
        except  IOError:
            print('An error occurred while trying to open the file' + self.__file_name)
