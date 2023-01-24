from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.request import Request
from exceptions import NotEnoughSpace, TooManyDifferentProducts


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request
        self.bad_add = 0        # неприёмка товара

        if request.departure in storages:
            self.__from = storages[request.departure]

        if request.destination in storages:
            self.__to = storages[request.destination]

    def move(self):
        name_prod = self.__request.product
        numb = self.__request.amount
        # отгрузка
        self.__from.remove(name=name_prod, amount=numb)
        # квитанция
        print(f'Курьер забрал {numb} {name_prod} из {self.__request.departure}')
        # доставка
        self.bad_add = self.__to.add(name=name_prod, amount=numb)
        if self.bad_add != 0:
            return False
        # квитанция
        print(f'Курьер доставил {numb} {name_prod} в {self.__request.destination}')
        return True

    # отмена доставки
    def cancel(self):
        self.__from.add(name=self.__request.product, amount=self.__request.amount)  # надо бы тоже проверять
        # квитанция
        print(f'Курьер вернул {self.__request.amount} {self.__request.product} в {self.__request.departure}')
        if self.bad_add == 1:
            raise NotEnoughSpace
        elif self.bad_add == 2:
            raise TooManyDifferentProducts

