class Entity:

    def __init__(self, id_entity):
        self.__id_entity = id_entity

    def get_id_entity(self):
        return self.__id_entity

    def set_id_entity(self, id_entity):
        self.__id_entity = id_entity

    def __str__(self):
        return "ID: " + str(self.get_id_entity()) + "\n"