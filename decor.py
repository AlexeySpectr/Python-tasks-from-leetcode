import pandas as pd
a=[1,43,65,4,60]
print(pd.Series(a))

# Декоратор — это паттерн проектирования (design pattern) в Python, а также функция второго уровня, то есть принимающая другие функции в качестве переменных и возвращающая их.
# И в сам декоратор, и в функцию-обёртку можно передать и позиционные, и именованные аргументы — args и kwargs соответственно.
# Декораторы работают не только с функциями, но и с классами и методами.
# Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её 
# функциональности без непосредственного изменения её кода. 
def deco_upper(func):
    def wrapper(*arg):
        print('there')
        func(*arg)
    return wrapper

@deco_upper
def foo():
    print('1')
foo()




def deco(func):
    pr=3
    def wrapper(*arg):
        # print('variables',*arg)
        x=[pr*i for i in arg]
        return func(*x)
    return wrapper

@deco
def fo(a,b):
    print(a,b)
fo(2,5)


def dec(multiplier):
    def inner(func):
        def wrapper(*args):
            x = [multiplier * i for i in args]
            g=func(*x)
            return g
        return wrapper
    return inner

@dec(10)
def f(a, b):
    print(a, b)

f(2, 5)