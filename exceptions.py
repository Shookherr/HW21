class BaseError(Exception):
    message = 'Неожиданная ошибка'


class RequestError(BaseError):
    message = 'Ошибка обработки запроса'


class CourierError(BaseError):
    message = 'Ошибка доставки'


class NotEnoughSpace(CourierError):
    message = 'Недостаточно места на складе'


class NotEnoughProduct(CourierError):
    message = 'Не хватает на складе, попробуйте заказать меньше'


class TooManyDifferentProducts(CourierError):
    message = 'Недостаточно места, попробуйте что-то другое'


class InvalidRequest(RequestError):
    message = 'Неправильный запрос. Попробуйте снова'


class InvalidStorageName(RequestError):
    message = 'Выбран несуществующий склад'
