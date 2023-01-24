# Класс "Склад"
from typing import Dict

from entity.base_storage import Store


class Store(Store):
    def __init__(self, items: Dict[str, int], capacity: int = 100):  # конструктор с дефолтной ёмкостью 100
        super().__init__(items, capacity)  # базовый Storage
