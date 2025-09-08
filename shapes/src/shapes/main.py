from abc import ABC, abstractmethod
import math

# Создаем абстрактный базовый класс
class Shape(ABC):

# Создаем абстрактный метод, которвый обязательно должен быть реализован в классах-наследниках
    @abstractmethod
    def area_calc(self):
        pass

# Создаем класс, описывающий окружность
class  Circle(Shape):
    
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise Exception('Окружность должна быть задана вещественным числом')
        if radius <= 0:
            raise Exception('Окружность должна быть задана положительным числом больше 0')
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    def area_calc(self):
        return round(math.pi * self._radius ** 2, 2)
    
    def __str__(self):
        return f"Circle({self._radius})"

# Создаем класс, описывающий треугольник
class  Triangle(Shape):
    
    def __init__(self, a, b, c):
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise Exception('Треугольник должен быть задан 3-мя сторонами, которые задаются вещественными числами')
        if not all(x>0 for x in (a, b, c)):
            raise Exception('Сторона треугольника должна быть задана положительным числом больше 0')
        if (a + b) <= c or (a + c) <= b or (b + c) <= a:
            raise Exception('Треугольника с заданными сторонами не существует')
        self._a = a
        self._b = b
        self._c = c
        self._type = ''
        if math.isclose(a**2, b**2+c**2, rel_tol=1e-9) or \
            math.isclose(b**2, a**2+c**2, rel_tol=1e-9) or \
            math.isclose(с**2, a**2+b**2, rel_tol=1e-9):
            self._type = 'right'
            print('Заданный треугольник является прямоугольным')
    
    @property
    def sides(self):
        return (self._a, self._b, self._c)

    def area_calc(self):
        if self._type == 'right':
            if self._a > self._b and self._a > self._c:
                return round(0.5*self._b*self._c, 2)
            elif self._b > self._c and self._b > self._a:
                return round(0.5*self._a*self._c, 2)
            else:
                return round(0.5*self._a*self._b, 2)
        p = (self._a + self._b + self._c) / 2
        return round((p*(p-self._a)*(p-self._b)*(p-self._c))**0.5, 2)