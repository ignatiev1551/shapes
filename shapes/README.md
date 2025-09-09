# Geometry Shapes Calculator

Простая библиотека для вычисления площади геометрических фигур.

## Возможности

- Вычисление площади круга по радиусу
- Вычисление площади треугольника по трем сторонам
- Автоматическое определение прямоугольного треугольника
- Валидация входных параметров

## Установка

- Клонируем проект
git clone https://github.com/ignatiev1551/shapes.git
- Переходим в папку
cd shapes/shapes
- Устанавливаем и активируем виртуальное окружение
python -m venv venv && \
source venv/bin/activate
- Устанавливаем пакет 
pip install . 

## Использование

```python
from shapes import Circle, Triangle

# Создание круга
circle = Circle(5)
print(f"Area: {circle.area_calc()}")  # Area: 78.54

# Создание треугольника
triangle = Triangle(3, 4, 5)
print(f"Area: {triangle.area_calc()}")  # Area: 6.0
print(f"Is right triangle: {triangle.is_right}")  # Is right triangle: True