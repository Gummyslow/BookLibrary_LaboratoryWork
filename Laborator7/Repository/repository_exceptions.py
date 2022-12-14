class RepositoryException(Exception):

    def __init__(self, mesaj):
        self.__mesaj = mesaj

    def __str__(self):
        return self.__mesaj


class DuplicateIDException(RepositoryException):

    def __init__(self, mesaj):
        super().__init__(mesaj)


class InexistentIDException(RepositoryException):

    def __init__(self, mesaj):
        super().__init__(mesaj)
