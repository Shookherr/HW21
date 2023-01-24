# Обобщённый абстрактный класс "хранилище"
from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def add(self, name: str, amount: int) -> None:  # увеличивает запас items
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:  # уменьшает запас items
        pass

    @abstractmethod
    def get_free_space(self) -> int:  # возврат количества свободных мест
        pass

    # @abstractmethod
    # def get_items(self):                                # возврат содержания склада в словаре {товар: количество}
    #     pass

    @abstractmethod
    def get_unique_items_count(self):  # возврат количества уникальных товаров
        pass
