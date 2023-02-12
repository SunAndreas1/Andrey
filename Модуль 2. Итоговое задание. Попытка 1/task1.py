import doctest


class Bicycle:

    def __init__(self, name: str, price: int, material: str, speed: float):
        """
        Создание и подготовка к работе объекта "Велосипед"
        :param name: Название велосипеда
        :param price: Цена одного велосипеда
        :param material: Материал рамы велосипеда
        :param speed: Скорость велосипеда
        Примеры:
         >>> bicycle = Bicycle("SX-400", 5000, "aluminum", 30)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть str")
        self.name = name
        if not isinstance(material, str):
            raise TypeError("Материал должен быть str")
        self.material = material
        if not isinstance(speed, int):
            raise TypeError("Скорость должна быть int")
        if speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self.speed = speed

        self._price = price    # Цену товара может изменить только продавец. Без его разрешения цену менять нельзя.

    @property
    def prop_price(self) -> int:
        return self._price

    @prop_price.setter
    def prop_price(self, price: int) -> None:
        if not isinstance(price, int):
            raise TypeError("Цена должна быть int")
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self._price = price

    def __str__(self):
        return f"Велосипед {self.name}. Цена {self._price}. Материал {self.material}. Скорость {self.speed} км/ч"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self._price!r}, material={self.material!r}, " \
               f"speed={self.speed})"

    def your_rest(self, money: int) -> None:
        """
        Функция которая проверяет достаточно ли средств для покупки велосипеда. Если средств хватает, рассчитывает сдачу
        Также учитываем другие товары, которые можно докупить в магазине: бутылку воды, звонок и т.д.
        :param money: Сумма денег, которую имеет покупатель
        :return: Можно ли купить велосивед?
        Примеры:
        >>> bicycle = Bicycle("SX-400", 5000, "aluminum", 30)
        >>> bicycle.your_rest(7000)
        Можно купить велосипед, Ваша сдача будет: 1650 рублей
        """
        if not isinstance(money, int):
            raise TypeError("Сумма денег должна быть int")
        if money <= 0:
            raise ValueError("Сумма денег должна быть положительным числом")

        dict_ = {"Bottle": 50, "Clarc": 300}
        rest = money - (self._price + sum(dict_.values()))
        if rest > 0:
            print("Можно купить велосипед, Ваша сдача будет:", rest, "рублей")
        elif rest == 0:
            print("Можно купить велосипед")
        else:
            print("Для покупки велосипеда необходимо ещё", rest * (-1), "рублей")

    def material_of_bicycle(self, weight: (int, float)) -> str:
        """
        Функция которая определяет вес велосипеда в зависимости от материала рамы.
        Если рама изготовлена из карбона - она легче алюминиевой в 2 раза.
        :param weight: Вес велосипеда
        :return: Сколько весит велосипед?
        Примеры:
        >>> bicycle = Bicycle("SX-400", 5000, "aluminum", 30)
        >>> bicycle.material_of_bicycle(30)
        Масса велосипеда 30 кг
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть str или float")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")

        if self.material == 'aluminum':
            print("Масса велосипеда", weight, "кг")
        elif self.material == 'carbon':
            print("Масса велосипеда", weight * 0.5, "кг")
        else:
            return "Такого материала не существует"

    def length(self, time: (int, float)) -> (int, float):
        """
        Функция которая определяет расстояние, которое проехал велосипедист.
        :param time: Время пути велосипедиста (в часах)
        :return: Сколько километров проехал велосипедист?
        Примеры:
        >>> bicycle = Bicycle("SX-400", 5000, "aluminum", 30)
        >>> bicycle.length(2)
        Длинна пути равна 60 км
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время должно быть str или float")
        if time <= 0:
            raise ValueError("Время должна быть положительным числом")

        length = time * self.speed
        print("Длинна пути равна", length, "км")


class MountainBicycle(Bicycle):
    def __init__(self, number_of_gears: int, name=None, price=None, material=None, speed=None):
        """
        Создание и подготовка к работе дочернего класса "Горный велосипед"
        :param number_of_gears: Количество передач
        Примеры:
        >>> bicycle = MountainBicycle(14, "SX-400", 5000, "aluminum", 30)
        """
        super().__init__(name, price, material, speed)
        if not isinstance(number_of_gears, int):
            raise TypeError("Количество передач должно быть типа int")
        if 21 < number_of_gears <= 0:
            raise ValueError("Количество передач должно быть положительным числом и не превышать 21")
        if number_of_gears % 7 != 0:
            raise ValueError("Количество передач должно быть кратно 7")
        self.number_of_gears = number_of_gears

    def __str__(self):
        return f"Велосипед {self.name}. Цена {self._price}. Материал {self.material}. Скорость {self.speed} км/ч. " \
               f"Количество передач {self.number_of_gears}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self._price!r}, material={self.material!r}, " \
               f"speed={self.speed}), gears={self.number_of_gears})"

    def length(self, time: float) -> (int, float):
        """
        Функция которая определяет расстояние, которое проехал велосипедист.
        Чем больше передач встроено в велосипед, тем легче велосипедисту будет ехать,
        поэтому больше расстояние, которое проедет велосипедист.
        :param time: Время пути велосипедиста (в часах)
        :return: Сколько километров проехал велосипедист?
        Примеры:
        >>> bicycle = MountainBicycle(14, "SX-400", 5000, "aluminum", 30)
        >>> bicycle.length(1)
        Длинна пути равна 36.0 км
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время должно быть str или float")
        if time <= 0:
            raise ValueError("Время должна быть положительным числом")

        if self.number_of_gears == 7:
            length = time * self.speed
        elif self.number_of_gears == 14:
            length = time * self.speed * 1.2
        else:
            length = time * self.speed * 1.4
        print("Длинна пути равна", length, "км")


class RaceBicycle(Bicycle):
    """
    Создание и подготовка к работе дочернего класса "Гоночный велосипед".
    Конструктор базового класс наследуем, так как нет возможности его расширить
    Примеры:
    >>> bicycle = RaceBicycle("SX-400", 5000, "aluminum", 60)
    """

    def length(self, time: float) -> (int, float):
        """
        Функция которая определяет расстояние, которое проехал велосипедист.
        Рама из алюминия в 2 раза тяжелее рамы из карбона, поэтому будет тяжелее ехать.
        Значит расстояние, которое проедалеет велосипедист в 2 раза меньше.
        :param time: Время пути велосипедиста (в часах)
        :return: Сколько километров проехал велосипедист?
        Примеры:
        >>> bicycle = RaceBicycle("SX-400", 5000, "aluminum", 60)
        >>> bicycle.length(6)
        Длинна пути равна 216.0 км
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время должно быть str или float")
        if time <= 0:
            raise ValueError("Время должна быть положительным числом")

        if self.material == 'aluminum':
            length = time * self.speed * 0.6
        else:
            length = time * self.speed * 1.2
        print("Длинна пути равна", length, "км")


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
