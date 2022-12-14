#GENERAL REPOSITORY ON ENTITIES
class Repository:

    def __init__(self):
        self.__all_entities = {}

    def get_all(self):
        '''
        Metoda care returneaza lista de entitati
        :return:
        '''
        return list(self.__all_entities.values())

    def add_entity(self, entity):
        if self.__find_by_id(entity.get_id()) is not None:
            raise KeyError('Duplicate id!')
        else:
            self.__all_entities[entity.get_id()] = entity

    def update_entity(self, new_entity):
        if self.__find_by_id(new_entity.get_id()) is None:
            raise KeyError("There's no entity with this id! ")
        self.__all_entities[new_entity.get_id()] = new_entity

    def delete_by_id_entity(self, id_entity):
        if self.__find_by_id(*id_entity) is None:
            raise KeyError("There's no entity with this id! ")
        self.__all_entities.pop(*id_entity)

    def __find_by_id(self, id_rent):
        return self.__all_entities.get(id_rent, None)