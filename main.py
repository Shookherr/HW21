# Домашняя работа №21 Шумихин Алексей, 24.01.23
from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import CourierError, RequestError

# Класс "Склад"
store_items = {
    'печенька': 25,
    'собачка': 25,
    'ёлка': 25,
    'пончик': 3,
    'зонт': 5,
    'ноутбук': 1
}
# Заполнение склада через setter
store = Store(items={})     # экземпляр store
store.items = store_items

# Класс "Магазин"
shop_items = {
    'печенька': 2,
    'собачка': 2,
    'ёлка': 2,
    'зонт': 1,
    'пончик': 1
}
# Заполнение магазина через атрибут класса
shop = Shop(items=shop_items)

# Привязка класса к названию хранилища - dict()
storages = {
    'магазин': shop,
    'склад': store
}


def main():
    print('\nHello!')

    while True:
        # Содержимое хранилищ - вывод содержимого
        for storage_name in storages:
            print(f'\nВ {storage_name}е хранится:\n')
            for item in storages[storage_name].items:  # через getter
                print(f'{item}: {storages[storage_name].items[item]}')

        # Ввод от пользователя
        while True:
            from_ = input('\nОткуда забирать товар? (М - магазин, С - склад, Й - окончание работы): ').lower()
            if from_ in ('q', 'й'):
                print('\nBye.')
                exit()
            if from_ == 'м':
                from_ = 'магазин'
            elif from_ == 'с':
                from_ = 'склад'
            else:
                print('Неправильный ввод, проверьте RUS регистр')
                continue
            break

        if from_ == 'магазин':
            to_ = 'склад'
            fr_om = 'из'
            t_o = 'на'
        else:
            to_ = 'магазин'
            fr_om = 'со'
            t_o = 'в'

        while True:
            name = input('Наименование товара: ')
            if name not in storages[from_].items.keys():
                print('Неправильный ввод')
                continue
            break

        numb = int(input('Количество товара: '))

        print(f'Доставить {numb} {name} {fr_om} {from_}а {t_o} {to_}\n')
        user_input = f'Доставить {numb} {name} {fr_om} {from_} {t_o} {to_}'

        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(f'{error.message}. Try again')
            continue

        # доставка
        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            if not courier.move(): # не доставлено
                courier.cancel()  # вернуть товар
        except CourierError as error:
            print(error.message)


if __name__ == '__main__':
    main()
