from Laborator7.Repository.customer_file_repository import CustomerFileRepository
from Laborator7.Repository.book_file_repository import BookFileRepository
from Laborator7.Repository.rent_file_repository import RentFileRepository
from Laborator7.Service.customer_service import CustomerService
from Laborator7.Service.book_service import BookService
from Laborator7.Service.rent_service import RentService
from Ui.Console.console import Console


def main1():
    book_repository = BookFileRepository("Files\Books.txt")
    book_service = BookService(book_repository)
    customer_repository = CustomerFileRepository('Files\Customers.txt')
    customer_service = CustomerService(customer_repository)
    rent_repository = RentFileRepository('Files\Rents.txt', book_repository, customer_repository)
    rent_service = RentService(rent_repository, book_repository, customer_repository)
    console = Console(customer_service, book_service, rent_service)

    console.run_menu()


if __name__ == '__main__':
    main1()
