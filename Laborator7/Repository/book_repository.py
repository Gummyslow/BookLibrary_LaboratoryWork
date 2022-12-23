class BookRepository:
    def __init__(self):
        self.__all_books = {}

    def add_book(self, book):
        if self.find_book_by_id(book.get_id()) is not None:
            raise ValueError('Duplicate id')
        self.__all_books[book.get_id()] = book

    def find_all_books(self):
        return list(self.__all_books.values())

    def find_book_by_id(self, id):
        return self.__all_books.get(id, None)

    def find_book_by_availability(self, id_book, availability):
        for books in self.__all_books:
            if self.__all_books[books].get_id() == id_book:
                if self.__all_books[books].get_availability() == availability:
                    return self.__all_books[books]
                else:
                    return None

    def update_book(self, new_book):
        if self.find_book_by_id(new_book.get_id()) is None:
            raise KeyError("There's no customer with this id! ")
        self.__all_books[new_book.get_id()] = new_book

    def update_availability_rent(self, id_book):
        if self.find_book_by_id(id_book) is None:
            raise KeyError("There's no book with this id!")
        if self.__all_books[id_book].get_availability() != 'Available':
            raise ValueError("This book isn't available right now!")
        self.__all_books[id_book].set_availability('Unavailable')

    def update_availability_return(self, id_book):
        if self.find_book_by_id(id_book) is None:
            raise KeyError("There's no book with this id!")
        if self.__all_books[id_book].get_availability() != 'Unavailable':
            raise ValueError("This book was never rented in the first place, so nobody can return it!")
        self.__all_books[id_book].set_availability('Available')

    def book_rent_count(self, id_book):
        if self.find_book_by_id(id_book) is None:
            raise KeyError("There's no book with this id!")
        rento = int(self.__all_books[id_book].get_book_rents())
        self.__all_books[id_book].set_book_rents(rento + 1)

    def sort_by_popularity(self):
        lista = list(self.__all_books.values())
        return sorted(lista, key=lambda x: x.get_book_rents(), reverse=True)

    def sort_book_title(self):
        return sorted(self.__all_books.values(), key=lambda x: x.get_title())

    def search_book(self, book):
        # todo: search in functie de availabilitys
        search_list = []
        if book.get_title() != '-' and book.get_author() != '-' and book.get_publisher() != '-':
            for books in self.__all_books:
                if self.__all_books[books].get_title() == book.get_title() and self.__all_books[
                    books].get_author() == book.get_author() and self.__all_books[
                    books].get_publisher() == book.get_publisher():
                    search_list.append(self.__all_books[books])
            return search_list
        if book.get_title() != '-' and book.get_author() != '-':
            for books in self.__all_books:
                if self.__all_books[books].get_title() == book.get_title() and self.__all_books[
                    books].get_author() == book.get_author():
                    search_list.append(self.__all_books[books])
            return search_list
        if book.get_title() != '-' and book.get_publisher() != '-':
            for books in self.__all_books:
                if self.__all_books[books].get_title() == book.get_title() and self.__all_books[
                    books].get_publisher() == book.get_publisher():
                    search_list.append(self.__all_books[books])
            return search_list  # pana aici merge
        if book.get_author() != '-' and book.get_publisher() != '-':
            for books in self.__all_books:
                if self.__all_books[books].get_author() == book.get_author() and self.__all_books[
                    books].get_publisher() == book.get_publisher:
                    search_list.append(self.__all_books[books])
            return search_list
        if book.get_title() != '-':
            for books in self.__all_books:
                if self.__all_books[books].get_title() == book.get_title:
                    search_list.append(self.__all_books[books])
            return search_list
        if book.get_author() != '-':
            for books in self.__all_books:
                if self.__all_books[books].get_author == book.get_author():
                    search_list.append(self.__all_books[books])
            return search_list
        if book.get_publisher() != '-':
            for books in self.__all_books:
                if self.__all_books[books].get_publisher() == book.get_publisher():
                    search_list.append(self.__all_books[books])
            return search_list

    def delete_by_id_book(self, id_book):
        id_book = int(*id_book)
        if self.find_book_by_id(id_book) is None:
            raise KeyError("There's no book with this id! ")
        self.__all_books.pop(id_book)
