######## Customer ########

class Customer:
    def __init__(self, id, first_name, last_name, cnp, own, rents):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cnp = cnp
        self.__own = own  #retine daca customerul are sau nu o carte inchiriata
        self.__rents = rents #retine numarul de carti inchiriate de o persoana

    def get_id(self):
        return self.__id

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

    def get_cnp(self):
        return self.__cnp

    def get_own(self):
        return self.__own

    def get_customer_rents(self):
        return self.__rents

    def set_id(self, id):
        self.__id = id

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def set_own(self, own):
        self.__own = own

    def set_customer_rents(self, rents):
        self.__rents = rents

    def __str__(self):
        return f'Customer: {self.__id}, first name: {self.__first_name}, last name: {self.__last_name}, cnp: {self.__cnp}, Book: {self.__own}, Books rented: {self.__rents}'

    def __repr__(self):
        return f'Customer: {self.__id}, first name: {self.__first_name}, last name: {self.__last_name}, cnp: {self.__cnp}, Book: {self.__own}, Books rented:{self.__rents}'
