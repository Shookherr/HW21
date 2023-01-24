# Базовый класс "Хранилище" - для классов "Склад" и "Магазин"
from typing import Dict

from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughProduct


class Store(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> int:  # добавление товара
        if self.get_free_space() < amount:
            return 1

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount  # если такого нет
        return 0

    def remove(self, name: str, amount: int) -> None:  # удаление (перемещение) товара
        if self.__items[name] < amount or name not in self.__items:  # есть, и в нужном количестве
            raise NotEnoughProduct

        self.__items[name] -= amount

        if self.__items[name] == 0:
            self.__items.pop(name)  # метод pop - удаление элемента списка

    def get_free_space(self) -> int:  # проверка свободного места
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):  # количество элементов словаря
        return len(self.__items)

    @property  # getter
    def items(self):
        return self.__items

    @items.setter  # setter
    def items(self, new_data):
        self.__items = new_data
