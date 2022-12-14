######## Book ########

class Book:
    def __init__(self, id, title, author, publisher, year, description, availability, rents):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year
        self.__description = description
        self.__availability = availability  # retine availabilityul cartii respective
        self.__rents = rents # retine de cate ori a fost inchiriata cartea

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def get_year(self):
        return self.__year

    def get_description(self):
        return self.__description

    def get_availability(self):
        return self.__availability

    def get_book_rents(self):
        return self.__rents

    def set_id(self, id):
        self.__id = id

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_year(self, year):
        self.__year = year

    def set_description(self, description):
        self.__description = description

    def set_availability(self, availability):
        self.__availability = availability

    def set_book_rents(self, rents):
        self.__rents = rents

    def __str__(self):
        return f'Book {self.__id}, title: {self.__title}, author: {self.__author}, publisher: {self.__publisher}, year: {self.__year}, description: {self.__description}, availability: {self.__availability},  Rents: {self.__rents}'

    def __repr__(self):
        return f'Book {self.__id}, title: {self.__title}, author: {self.__author}, publisher: {self.__publisher}, year: {self.__year}, description: {self.__description}, availability: {self.__availability}, Rents: {self.__rents}'
