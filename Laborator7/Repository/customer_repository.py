class CustomerRepository:
    def __init__(self):
        self.__all_customers = {}

    def add_customer(self, customer):
        if self.find_customer_by_id(customer.get_id()) is not None:
            raise KeyError('Duplicate id!')
        else:
            self.__all_customers[customer.get_id()] = customer

    def update_own_rent(self, id_customer):  # daca dai rent la o carte
        if self.find_customer_by_id(id_customer) is None:
            raise KeyError("There's no customer with this id! ")
        if self.__all_customers[id_customer].get_own() != 'Lacks':
            raise ValueError("This customer already has rented a book")
        self.__all_customers[id_customer].set_own('Owns')

    def update_own_return(self, id_customer):
        if self.find_customer_by_id(id_customer) is None:
            raise KeyError("There's no customer with this id!")
        if self.__all_customers[id_customer].get_own() != 'Owns':
            raise ValueError("This cusomer already has rented a book")
        self.__all_customers[id_customer].set_own('Lacks')

    def number_of_customers(self):
        number = int(len(self.__all_customers))
        return number

    def find_all_customers(self):
        return list(self.__all_customers.values())

    def find_customer_by_id(self, id):
        return self.__all_customers.get(id, None)

    def find_customer_by_owned(self, id_customer, owns):
        for customers in self.__all_customers:
            if self.__all_customers[customers].get_id() == id_customer:
                if self.__all_customers[customers].get_own() == owns:
                    return self.__all_customers[customers]
                else:
                    return None

    def customer_rent_count(self, id_customer):
        if self.find_customer_by_id(id_customer) is None:
            raise ValueError("There's no customer with this id!")
        rento = int(self.__all_customers[id_customer].get_customer_rents())
        self.__all_customers[id_customer].set_customer_rents(rento + 1)

    def update_customer(self, new_customer):
        if self.find_customer_by_id(new_customer.get_id()) is None:
            raise KeyError("There's no customer with this id! ")
        self.__all_customers[new_customer.get_id()] = new_customer

    def sort_customer_first_name(self):
        return sorted(self.__all_customers.values(), key=lambda x: x.get_first_name())

    def sort_customer_rents(self):
        return sorted(self.__all_customers.values(), key=lambda x: x.get_customer_rents(), reverse=True)

    def most_active_20(self):
        lista1 = []
        percent = 0.2  # 20%
        num = self.number_of_customers()
        number = int(percent * num)
        lista = self.sort_customer_rents()
        for i in range(number):
            lista1.append(lista[i])
        return lista1

    def search_customer(self, customer):
        search_list = []
        if customer.get_first_name() != '-' and customer.get_last_name() != '-' and customer.get_cnp() != '-':
            for customers in self.__all_customers:
                if self.__all_customers[customers].get_first_name() == customer.get_first_name() and \
                        self.__all_customers[customers].get_last_name() == customer.get_last_name() and \
                        self.__all_customers[customers].get_cnp() == customer.get_cnp():
                    search_list.append(self.__all_customers[customers])
            return search_list
        if customer.get_first_name() != '-' and customer.get_last_name() != '-':
            for customers in self.__all_customers:
                if self.__all_customers[customers].get_first_name() == customer.get_first_name() and \
                        self.__all_customers[customers].get_last_name() == customer.get_last_name():
                    search_list.append(self.__all_customers[customers])
            return search_list
        if customer.get_first_name() != '-':
            for customers in self.__all_customers:
                if self.__all_customers[customers].get_first_name() == customer.get_first_name():
                    search_list.append(self.__all_customers[customers])
            return search_list
        if customer.get_last_name() != '-':  # nu imi baga in lista si nu stiu de ce
            for customers in self.__all_customers:
                if self.__all_customers[customers] == customer.get_last_name():
                    search_list.append(self.__all_customers[customers])
            return search_list
        elif customer.get_cnp() != '-':
            for customers in self.__all_customers:  # nu imi baga in lista si nu stiu de ce
                if self.__all_customers[customers] == customer.get_cnp():
                    search_list.append(self.__all_customers[customers])
            return search_list

    def delete_by_id_customer(self, id_customer):
        id_customer = int(*id_customer)
        if self.find_customer_by_id(id_customer) is None:
            raise KeyError("There's no customer with this id! ")
        self.__all_customers.pop(id_customer)
