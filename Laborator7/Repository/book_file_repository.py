from Laborator7.Domain.book_domain import Book
from Laborator7.Repository.book_repository import BookRepository


class BookFileRepository(BookRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.read_from_file()

    def add_book(self, book):
        super().add_book(book)
        self.write_in_file()

    def update_book(self, new_book):
        super().update_book(new_book)
        self.write_in_file()

    def delete_book(self, id_book):
        super().delete_by_id_book(id_book)
        self.write_in_file()

    def read_from_file(self):
        try:
            f = open(self.__file_name, 'r')
            line = f.readline().strip('\n')
            while line != '':
                # pos = line.find(' ')
                # cmd = line[:pos]
                # list_of_attributes = line[pos + 1:]
                list_of_attributes = line.split(',')
                id_book = int(list_of_attributes[0])
                title = list_of_attributes[1]
                author = list_of_attributes[2]
                publisher = list_of_attributes[3]
                year = int(list_of_attributes[4])
                description = (list_of_attributes[5])
                availability = 'Available'
                rents = 0
                book = Book(id_book, title, author, publisher, year, description, availability, rents)
                super().add_book(book)
                line = f.readline().strip("\n")
            f.close()
        except IOError:
            print('An error occurred while trying to open the file' + self.__file_name)

    def write_in_file(self):
        try:
            f = open(self.__file_name, 'w')
            all_books = super().find_all_books()
            for book in all_books:
                id_book = book.get_id()
                title = book.get_title()
                author = book.get_author()
                publisher = book.get_publisher()
                year = book.get_year()
                description = book.get_description()
                f.write(f'{id_book},{title},{author},{publisher},{year},{description}\n')
            f.close()
        except  IOError:
            print('An error occurred while trying to open the file' + self.__file_name)