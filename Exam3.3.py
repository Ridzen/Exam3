# ______________________________________3__________________________________________
# Создайте класс Rectangle с длиной и шириной. И методы для получения площади и периметра.
# Также проперти метод для получения полной информации про прямоугольник.
# Используйте инкапсуляцию для длины и ширины.

class Rectangle:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def perimeter(self):
        return 2 * (self.__a + self.__b)

    @property
    def square(self):
        return self.__a * self.__b


rect = Rectangle(3, 4)
print(rect.square)
print(rect.perimeter)
