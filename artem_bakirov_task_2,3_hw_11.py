# Задание 2
def my_reduce(func, iterable):
    """func это функция, к которой последовательно применяется каждый
    элемент из iterable - func = add, iterable = list1"""
    return a


def add(a, b):  # функция,которую складывает элементы из iterable
    return a + b


list_1 = [7, 6, 4, 10, 20]
a = list_1[0]
for i in range(1, len(list_1)):  # Пробегаемся по нашему списку и складывем его значения
    b = list_1[i]
    a = add(a, b)

print(my_reduce(add, list_1))  # add функция которая помледовательно складывает элементы из list_1


# Задание 3
def func_tester():  # функция которая тестирует правильность подсчета my_reduce
    assert my_reduce(add, list_1) == 47, "Answer should be 47"


func_tester()
