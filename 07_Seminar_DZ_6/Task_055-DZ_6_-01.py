# ==============================================================================================
# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b),
# возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
# Ввод чисел продолжается до ввода пустой строки.
''' Входные данные: 36 12 144 18	 Выходные данные: 6 '''
# ==============================================================================================


from functools import reduce
import math

list_1 = []
# блок ввода чисел, до ввода пустой строки
while True:
    n = input('Введите число (отдельно на каждой строке): ')
    if n == '':
        break
    else:
        list_1.append(int(n))
print(list_1)


# Первый вариант
print('Первый вариант')
print('Наибольший общий делитель для введенных чисел равен:', math.gcd(*list_1))


# Второй вариант
print()
print('Второй вариант')

NOD = reduce(lambda a, b: math.gcd(a, b), list_1)
print('Наибольший общий делитель для введенных чисел равен:', NOD)


# reduce(function, iterable[, initializer])
# Функция reduce() модуля functools кумулятивно применяет функцию function
# к элементам итерируемой iterable последовательности, сводя её к единственному значению.
