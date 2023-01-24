# Класс "Магазин"
from typing import Dict

from entity.base_storage import Store


class Shop(Store):
    def __init__(self, items: Dict[str, int], capacity: int = 20):  # конструктор с дефолтной ёмкостью 20
        super().__init__(items, capacity)  # базовый Storage

    def add(self, name: str, amount: int):  # модификация метода add
        if self.get_unique_items_count() >= 5:
            return 2  # raise TooManyDifferentProducts

        super().add(name, amount)  # модификация базового
