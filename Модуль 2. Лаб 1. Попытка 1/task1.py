# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Basket:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """
        Создание и подготовка к работе объекта "Корзина"
        :param capacity_volume: Количество продуктов, которые можно положить в корзину (макимум)
        :param occupied_volume: Количество продуктов, которые уже лежат в корзине
        Примеры:
        >>> glass = Basket(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, int):
            raise TypeError("Объем корзины должен быть типа int")
        if capacity_volume <= 0:
            raise ValueError("Объем корзины должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, int):
            raise TypeError("Количество продуктов в корзине должно быть int")
        if occupied_volume < 0:
            raise ValueError("Количество продуктов не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_basket(self) -> bool:
        """
        Функция которая проверяет является ли корзина пустой
        :return: Является ли корзина пустой?
        Примеры:
        >>> basket = Basket(500, 0)
        >>> basket.is_empty_basket()
        True
        """
        return self.occupied_volume == 0

    def add_water_to_basket(self, product: int) -> None:
        """
        Добавление воды в стакан.
        :param product: Объем добавляемой жидкости
        :raise ValueError: Если количество дабовляемых продуктов превышает свободное место в корзине, то вызываем ошибку
        Примеры:
        >>> basket = Basket(500, 0)
        >>> basket.add_water_to_basket(200)
        """
        if not isinstance(product, int):
            raise TypeError("Количество добавляемых продуктов в корзине должно быть int")
        if product < 0:
            raise ValueError("Количество продуктов не может быть отрицательным числом")
        self.occupied_volume += product

    def remove_product_from_basket(self, estimate_product: float) -> None:
        """
        Извлечение воды из стакана.
        :param estimate_product: Количество извлекаемых продуктов
        :raise ValueError: Если количество извлекаемых продуктов превышает количество продуктов в корзине,
        то возвращается ошибка.
        :return: Количество извлекаемых продуктов
        Примеры:
        >>> basket = Basket(5, 5)
        >>> basket.remove_product_from_basket(2)
        """
        if not isinstance(estimate_product, (int, float)):
            raise TypeError("Количество убираемых продуктов в корзине должно быть int")
        if estimate_product < 0:
            raise ValueError("Количество продуктов не может быть отрицательным числом")
        self.occupied_volume -= estimate_product


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class Ellipse:
    def __init__(self, count_a: (int, float), count_b: (int, float)):
        """
        Создание и подготовка к работе объекта "Корзина"
        :param count_a: Один из радиусов эллипса
        :param count_b: Один из радиусов эллипса
        Примеры:
        >>> ellipse = Ellipse(6, 10)  # инициализация экземпляра класса
        """
        if not isinstance(count_a, (int, float)):
            raise TypeError("Знаение радиуса должно быть типа int или float")
        if count_a <= 0:
            raise ValueError("Знаение радиуса должно быть положительным числом")
        self.count_a = count_a

        if not isinstance(count_b, (int, float)):
            raise TypeError("Знаение радиуса должно быть типа int или float")
        if count_b <= 0:
            raise ValueError("Знаение радиуса должно быть положительным числом")
        self.count_b = count_b

    def area(self) -> float:
        """
        Метод считает площадь эллипса через формулу A*B*π.
        :return: Площадь эллипса
        Примеры:
        >>> ellipse = Ellipse(5, 6)
        >>> ellipse.area()
        94.2
        """
        return self.count_a * self.count_b * 3.14

    def perimeter(self) -> float:
        """
        Метод считает периметр эллипса через формулу (A+B)*π.
        :return: Периметр эллипса
        Примеры:
        >>> ellipse = Ellipse(5, 6)
        >>> ellipse.perimeter()
        34.54
        """
        return (self.count_a + self.count_b) * 3.14

    def ellipse_in_circle(self, radius) -> str:
        """
        Функция которая проверяет поместится ли эллипс в круг
        :return: Поместится ли эллипс в круг?
        Примеры:
        >>> ellipse = Ellipse(5, 6)
        >>> ellipse.ellipse_in_circle(10)
        'Поместится'
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Знаение радиуса должно быть типа int или float")
        if radius <= 0:
            raise ValueError("Знаение радиуса должно быть положительным числом")

        if self.count_b <= radius:
            return "Поместится"
        else:
            return "Не поместится"


class Car:
    def __init__(self, length: (int, float), speed: (int, float), length_before_stop: (int, float)):
        """
        Создание и подготовка к работе объекта "Корзина"
        :param length: Длина пути, в километрах
        :param speed: Постоянная скорость автомобиля, в часах
        :param length_before_stop: Расстояние, которое сможет преодалеть автомобиль не запрявляясь
        Примеры:
        >>> car = Car(240, 60, 200)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина пути должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина пути должна быть положительным числом")
        self.length = length

        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self.speed = speed

        if not isinstance(length_before_stop, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if length_before_stop <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        self.length_before_stop = length_before_stop

    def time(self) -> (int, float):
        """
        Метод считает время, затраченное на дорогу.
        :return: Количество часов
        Примеры:
        >>> car = Car(240, 60, 200)
        >>> car.time()
        4.0
        """
        return self.length / self.speed

    def stop(self) -> str:
        """
        Достаточно ли бензина для поездки???
        :return: Периметр эллипса
        Примеры:
        >>> car = Car(500, 60, 200)
        >>> car.stop()
        'Бензина не хватит'
        """

        if self.length_before_stop > self.length:
            return "Заправляться нет необходимости"
        else:
            return "Бензина не хватит"

    def petrol(self, price_for_petrol: (int, float), money: (int, float)) -> tuple:
        """
        Функция которая проверяет достаточно ли денег для покупки бензина
        :param price_for_petrol: Цена за полный бак
        :param money: Сколько денег у нас с собой
        :return: Достаточно ли денег взяли с собой, если нет, то сколько нужно ещё взять?
        Примеры:
        >>> car = Car(400, 20, 100)
        >>> car.petrol(1000, 5000)
        """
        if not isinstance(price_for_petrol, (int, float)):
            raise TypeError("Цена за бензин должна быть типа int или float")
        if price_for_petrol <= 0:
            raise ValueError("Цена за бензин должна быть положительным числом")

        if not isinstance(money, (int, float)):
            raise TypeError("Сумма денег должна быть типа int или float")
        if money <= 0:
            raise ValueError("Сумма денег должна быть положительным числом")

        rest_ = (self.length_before_stop / self.length) * price_for_petrol
        if rest_ < 0:
            return "Необходимо", rest_ * (-1), "рублей"
        else:
            return "Остаток", rest_, "рублей"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
