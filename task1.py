from typing import Any
# TODO Написать 3 класса с документацией и аннотацией типов
class Table:
    """
    Класс описывает модель стола.
    """
    def __init__(self, height: int, material: str):
        """
        Инициализация экземпляра класса.

        :param height: Высота стола
        :param material: Материал стола

        :raise ValueError: Если высота стола отрицательная или нулевая

        Примеры:
        >>> table = Table(10, "Wood")
        """
        if not isinstance(height, int):
            raise TypeError("Высота должна быть типа int")
        if height <= 0:
            raise ValueError("Высота должна быть натуральным числом.")
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        self.height = height
        self.material = material

    def change_material(self, material: str) -> None:
        '''
        Метод меняет древесину стола.

        :param material: Новый материал стола

        Примеры:
        >>> table = Table(10, "Wood")
        >>> table.change_material("Bedrock")
        '''
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        ...

    def change_height(self, height: int) -> None:
        '''
        Метод меняет высоту стола.

        :param height: Новая высота стола

        :raise ValueError: Если новая высота стола отрицательная или нулевая

        Примеры:
        >>> table = Table(10, "Wood")
        >>> table.change_height(5)
        '''
        if not isinstance(height, int):
            raise TypeError("Высота должна быть типа int")
        if height <= 0:
            raise ValueError("Высота должна быть натуральным числом.")
        ...

class Ball:
    """
    Класс описывает модель двумерного мяча.
    """
    def __init__(self, x: float, y: float, radius: float):
        '''
        Инициализая экземпляра класса.

        :param x: Координата x
        :param y: Координата y
        :param radius: Радиус мяча

        :raise ValueError: Если радиус отрицательный или нулевой

        Примеры:
        >>> ball = Ball(-1.25, 2.25, 0.2)
        '''
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Координаты x и y должны быть типа int или float")
        self.x = x
        self.y = y

        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def get_coordinates(self) -> tuple:
        '''
        Метод возвращает координаты мяча x и y в виде кортежа из 2 элементов.

        Примеры:
        >>> ball = Ball(-1.25, 2.25, 0.2)
        >>> ball.get_coordinates()
        '''
        ...

    def move(self, dx: float, dy: float) -> None:
        '''
        Метод меняет координаты x и y на заданные значения.

        :param dx: Изменение координаты x
        :param dy: Изменение координаты y

        Примеры:
        >>> ball = Ball(-1.25, 2.25, 0.2)
        >>> ball.move(0.2, -0.25)
        '''
        if not isinstance(dx, (float, int)) or not isinstance(dy, (float, int)):
            raise TypeError("Изменение координат должно быть в виде int или float")
        ...

class Stack:
    """
    Класс описывает модель стека.
    """
    def __init__(self):
        """
        Инициализация экземпляра класса.

        Примеры:
        >>> stack = Stack()
        """
        self.items = []

    def is_empty(self) -> bool:
        """
        Метод проверяет является ли стек пустым.

        :return: Является ли стек пустым

        Примеры:
        >>> stack = Stack()
        >>> stack.is_empty()
        """
        ...

    def push(self, item: Any):
        """
        Метод добавляет элемент на вершину стека.

        :param item: Добавляемый элемент

        Примеры:
        >>> stack = Stack()
        >>> stack.push(10)
        """
        ...

    def pop(self) -> Any:
        """
        Удаляет из стека элемент с вершины и возвращает его.

        :return: Элемент с вершины стека

        :raise IndexError: Если стек пуст

        Примеры:
        >>> stack = Stack()
        >>> stack.push(10)
        >>> a = stack.pop()
        """
        if self.is_empty():
            raise IndexError("Стек пуст")
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
