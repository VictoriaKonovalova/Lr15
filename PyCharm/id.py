#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает
эту строку в список чисел и возвращает их сумму. Определите декоратор для этой функции,
который имеет один параметр start – начальное значение суммы. Примените декоратор
со значением start=5 к функции и вызовите декорированную функцию. Результат
отобразите на экране.
"""


def decorator(start=0):
    def wrapper(func):
        def inner(*args):
            print(f"Начальное значение: {start}")
            print(f"Оборачиваемая функция: {func}")
            string = args[0]
            lst = string.split()
            lst = lst[start:]
            start_string = " ".join(lst)
            return_sum = func(start_string)
            print("Выходим из обёртки")
            return return_sum

        return inner

    return wrapper


@decorator(start=5)
def str_summary(string):
    a = [int(s) for s in string.split()]
    summa = sum(elem for elem in a)
    return summa


if __name__ == "__main__":
    strr = input("Enter the str numbers: ")
    print(f"The sum is: {str_summary(strr)}")
