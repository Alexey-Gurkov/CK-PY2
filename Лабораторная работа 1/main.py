import doctest


class BluetoothHeadphones:
    def __init__(self, name: str, sensitivity: int, battery_capacity: int):
        """
        Создание и подготовка к работе Объекта "Стакан"

        :param name: Название наушников
        :param sensitivity: Чувствительность наушников
        :param battery_capacity: Емкость аккумулятора

        Пример:
        >>> bluetoothHeadphones = BluetoothHeadphones("Honor AM61", 98, 137)
        """
        if not isinstance(name, str):
            raise TypeError("Название наушников состоит из типа данных - строка")
        self.name = name

        if not isinstance(sensitivity, int):
            raise TypeError("Чувствительность наушников должна быть целым числом")
        if sensitivity <= 0:
            raise ValueError("Чувствительность наушником должна быть положительны числом")
        self.sensitivity = sensitivity

        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость аккумулятора должна быть целым числом")
        if battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительныи числом")
        self.battery_capacity = battery_capacity

    def charge(self) -> bool:
        """
        Функция, которая проверяет, заряжаются ли наушники
        """
        ...

    def turn_on(self) -> None:
        """
        Функция, которая включает наушники
        """
        ...


class Car:
    def __init__(self, name_car: str, colour_car: str, car_power: int, ):
        """
        Создание и подготовка к работе объекта "Машина"

        :param name_car: название машины
        :param colour_car: цвет машины
        :param car_power: мощность машины

        Пример:
        >>> car = Car("BMW", "Чёрный", 235)
        """
        if not isinstance(name_car, str):
            raise TypeError("Название машины состоит из типа данных - строка")
        self.name_car = name_car

        if not isinstance(colour_car, str):
            raise TypeError("Цвет машины состоит из типа данных - строка")
        self.colour_car = colour_car

        if not isinstance(car_power, int):
            raise TypeError("Мощность машины должна быть целым числом")
        if car_power <= 0:
            raise ValueError("Мощность машины должна быть положительны числом")
        self.car_power = car_power

    def open_doors(self) -> None:
        """
        Открытие двери
        """
        ...

    def start_moving(self) -> None:
        """
        Начало движение машины
        """
        ...

    def steering_wheel_turn(self) -> None:
        """
        Поворот рулевого колеса в ту или иную сторону
        """
        ...


class Pen:
    def __init__(self, color_pen: str, pen_body_material: str, letter_line_thickness: float):
        """
         Создание и подготовка к работе объекта "Шариковая ручка"

        :param color_pen: цвет ручки
        :param pen_body_material: материал корпуса ручки
        :param letter_line_thickness: Толщина линии письма

        Пример:
        >>> pen = Pen("Красный", "Пластик", 1.6)
        """
        if not isinstance(color_pen, str):
            raise TypeError("Цвет ручки - тип данных строка")
        self.color_pen = color_pen

        if not isinstance(pen_body_material, str):
            raise TypeError("Материал корпуса ручки - типа данных строка")
        self.pen_body_material = pen_body_material

        if not isinstance(letter_line_thickness, float):
            raise TypeError("Толщина линии письма - точное число вещественного типа данных float")
        self.letter_line_thickness = letter_line_thickness

    def replacing_rod_in_pen(self) -> None:
        """
        Замена стержня в ручке
        """
        ...

    def open_pen(self) -> None:
        """
        Открытие ручки, снятие колпочка
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
