import unittest
from unittest import TestCase
from Laborator7.Repository.customer_repository import *
from Laborator7.Domain.customer_domain import Customer
from Laborator7.Service.customer_service import CustomerService
class TestCustomer(TestCase):
    def setUp(self):
        self.customer = Customer(1,'Stefan','Lupu',5030220330235,'Lacks',0)

    def test_id(self):
        self.assertTrue(self.customer.get_id() == 1, "Customer id should be '1'!")
        self.customer.set_id(2)
        self.assertTrue(self.customer.get_id() == 2, "Customer id should be '2'!")

    def test_first_name(self):
        self.assertTrue(self.customer.get_first_name() == 'Stefan', "Customer first name should be 'Stefan'!")
        self.customer.set_first_name('Bogdan')
        self.assertTrue(self.customer.get_first_name() == 'Bogdan', "Customer first name should be 'Bogdan'!")

    def test_last_name(self):
        self.assertTrue(self.customer.get_last_name() == 'Lupu', "Customer last name should be 'Lupu'!")
        self.customer.set_last_name('Andreius')
        self.assertTrue(self.customer.get_last_name() == 'Andreius', "Customer last name should be 'Andreius'!")

    def test_cnp(self):
        self.assertTrue(self.customer.get_cnp() == 5030220330235, "Customer cnp should be '5030220330235'!")
        self.customer.set_cnp(3)
        self.assertTrue(self.customer.get_cnp() == 3, "Customer cnp should be '3'!")

    def test_own(self):
        self.assertTrue(self.customer.get_own() == 'Lacks', "Customer own should be 'Lacks'!")
        self.customer.set_own('Owns')
        self.assertTrue(self.customer.get_own() == 'Owns', "Customer own should be 'Owns'!")

    def test_rents(self):
        self.assertTrue(self.customer.get_customer_rents() == 0, "Customer rents should be '0'!")
        self.customer.set_customer_rents(1)
        self.assertTrue(self.customer.get_customer_rents() == 1, "Customer rents should be '1'!")

    def test_str(self):
        self.assertTrue(self.customer.__str__() == f'Customer: {self.customer.get_id()}, first name: {self.customer.get_first_name()}, last name: {self.customer.get_last_name()}, cnp: {self.customer.get_cnp()}, Book: {self.customer.get_own()}, Books rented: {self.customer.get_customer_rents()}')

    def test_repr(self):
        self.assertTrue(self.customer.__repr__() == f'Customer: {self.customer.get_id()}, first name: {self.customer.get_first_name()}, last name: {self.customer.get_last_name()}, cnp: {self.customer.get_cnp()}, Book: {self.customer.get_own()}, Books rented: {self.customer.get_customer_rents()}')

    def tearDown(self) -> None:
        pass

class TestCustomerRepository(TestCase):

    def setUp(self):
        self.customer_repository = CustomerRepository()
        self.all_customers = [self.customer_repository.add_customer(Customer(1,'Stefan','Lupu',5030220330235,'Lacks',0)), self.customer_repository.add_customer(Customer(2,'Robert','Micutaru',50301230330205,'Owns',0))]

    def test_add_customer(self):
        self.customer_repository.add_customer(Customer(3,'Robert','Burlacu',5030820330215, 'Lacks', 0))
        self.customer_repository.add_customer(Customer(2,'Stefan','Lupu',5030220330235,'Lacks',0))
        self.assertTrue(len(self.all_customers) == 3, 'The list should contain 3 customers!')
        self.assertTrue(self.all_customers[2].get_id() == 3, "Customer id should be '3'!")

    def test_update_customer(self):
        self.customer_repository.update_customer(Customer(1,'Robert','Burlacu',5030820330215, 'Lacks', 0))
        self.assertTrue(len(self.all_customers) == 3, 'The list should contain 3 customers!')
        self.assertTrue(self.all_customers[0].get_id() == 1, "Customer id should be '1'!")
        self.assertTrue(self.all_customers[0].get_first_name() == 'Robert', "Customer's first name should've been 'Robert'!")

    def test_delete_customer(self):
        self.customer_repository.delete_by_id_customer(1)
        self.assertTrue(self.all_customers[0].get_id() == 2, "Customer id should be '2'!")
        self.assertTrue(self.all_customers[0].get_first_name() == 'Robert', "Customer's first name should've been 'Robert'!")

    def test_update_own(self):
        self.customer_repository.update_own_rent(1)
        self.assertTrue(self.all_customers[0].get_own() == 'Owns', "Customer's own should've been 'Owns'!")
        self.customer_repository.update_own_return(1)
        self.assertTrue(self.all_customers[0].get_own() == 'Lacks', "Customer's own should've been 'Lacks'!")

    def test_customer_rent_count(self):
        self.customer_repository.customer_rent_count(1)
        self.assertTrue(self.all_customers[0].get_rents() == 1, "Customer's rents should've been '1'!")

    def tearDown(self) -> None:
        pass

class TestCustomerService(TestCase):
    def setUp(self):
        self.customer_repository = CustomerRepository()
        self.customer_service = CustomerService(self.customer_repository)
        self.all_customers = [self.customer_service.add_customer(1,'Stefan','Lupu',5030220330235,'Lacks',0), self.customer_service.add_customer(2,'Robert','Micutaru',50301230330205,'Owns',0)]

    def test_add_customer_serv(self):
        self.customer_service.add_customer(3,'Robert','Burlacu',5030820330215,'Owns',0)
        self.assertTrue(len(self.all_customers) == 3, "There should be 3 customers!")
        self.assertTrue(self.all_customers[2].get_id() == 3, "Customer's id should be '3'!")

    def tearDown(self) -> None:
        pass