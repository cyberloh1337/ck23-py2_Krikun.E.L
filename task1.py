from math import pi
if __name__ == "__main__":
    # Write your solution here
    class Shape:
        """Базовый класс для геометрических фигур"""

        def __init__(self, color: str):
            """Инициализация экземпляра класса. Color сделан непубличным для избежания ошибок"""
            self.color = color

        @property
        def color(self) -> str:
            return self._color

        @color.setter
        def color(self, value: str):
            if not isinstance(value, str):
                raise TypeError("Color should be str type")
            self._color = value

        def __str__(self) -> str:
            """Возвращает строковое представление фигуры."""
            return f"A {self.color} shape"

        def __repr__(self) -> str:
            """Возвращает печатное представление фигуры."""
            return f"{self.__class__.__name__}(color='{self.color}')"


    class Rectangle(Shape):
        """Класс, представляющий прямоугольник."""

        def __init__(self, color: str, width: float, height: float):
            """Инициализация экземпляра прямоугольника."""
            super().__init__(color)
            self.width = width
            self.height = height

        @property
        def width(self) -> float:
            return self._width

        @width.setter
        def width(self, value: float):
            if not isinstance(value, (int, float)):
                raise TypeError("Width should be int or float type")
            if value <= 0:
                raise ValueError("Width should be positive")
            self._width = value

        @property
        def height(self) -> float:
            return self._height

        @height.setter
        def height(self, value: float):
            if not isinstance(value, (int, float)):
                raise TypeError("Height should be int or float type")
            if value <= 0:
                raise ValueError("Height should be positive")
            self._height = value

        def area(self) -> float:
            """Вычисление площади прямоугольника."""
            return self.width * self.height

        def perimeter(self) -> float:
            """Вычисление периметра прямоугольника."""
            return 2 * (self.width + self.height)

        def __str__(self) -> str:
            """Возвращает строковое представление прямоугольника.
            Метод перегружен для добавления дополнительной информации"""
            return f"A {self.color} rectangle with width {self.width} and height {self.height}"

        def __repr__(self) -> str:
            """Возвращает печатное представление прямоугольника.
             Метод перегружен для добавления дополнительной информации"""
            return f"{self.__class__.__name__}(color='{self.color}', width={self.width}, height={self.height})"


    class Circle(Shape):
        """Класс, представляющий круг."""

        def __init__(self, color: str, radius: float):
            """Инициализация экземпляра круга."""
            super().__init__(color)
            self.radius = radius

        @property
        def radius(self) -> float:
            return self._radius

        @radius.setter
        def radius(self, value: float):
            if not isinstance(value, (int, float)):
                raise TypeError("Radius should be int or float type")
            if value <= 0:
                raise ValueError("Radius should be positive")
            self._radius = value

        def area(self) -> float:
            """Вычисление площади круга."""
            return pi * self.radius ** 2

        def perimeter(self) -> float:
            """Вычисление длины окружности круга."""
            return 2 * pi * self.radius

        def __str__(self) -> str:
            """Возвращает строковое представление круга.
            Метод перегружен для добавления дополнительной информации"""
            return f"A {self.color} circle with radius {self.radius}"

        def __repr__(self) -> str:
            """Возвращает печатное представление круга.
            Метод перегружен для добавления дополнительной информации"""
            return f"{self.__class__.__name__}(color='{self.color}', radius={self.radius})"