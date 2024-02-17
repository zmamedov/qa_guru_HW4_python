import math
import random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = "Привет, {name}! Тебе {age} лет.".format(name=name, age=age)

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = (a + b) * 2

    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b

    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = math.pi * r ** 2

    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2 * math.pi * r

    assert length == 144.51326206513048

def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создайте список
    x1 = random.randint(1, 100)
    x2 = random.randint(1, 100)
    x3 = random.randint(1, 100)
    x4 = random.randint(1, 100)
    x5 = random.randint(1, 100)
    x6 = random.randint(1, 100)
    x7 = random.randint(1, 100)
    x8 = random.randint(1, 100)
    x9 = random.randint(1, 100)
    x10 = random.randint(1, 100)
    l = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
    l.sort()

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))

def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l = list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
