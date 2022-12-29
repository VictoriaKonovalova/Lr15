#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def higher_order(func):
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    return func


def wrapper_function():
    def hello_world():
        print('Hello world!')

    hello_world()


def hello_world():
    print('Hello world!')


if __name__ == "__main__":
    print(type(hello_world))


    class Hello:
        pass


    print(type(Hello))
    print(type(10))
    hello = hello_world
    hello()
    wrapper_function()
    print(higher_order(hello_world))
