# ==============================================================
# Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# ==============================================================

# Чтобы найти НОК нескольких натуральных чисел, надо разложить эти числа на простые множители,
# затем взять из этих разложений каждый простой множитель с наибольшим показателем степени
# и перемножить эти множители между собой.
# 99 = 3 · 3 · 11 = 3^2 · 11,
# 54 = 2 · 3 · 3 · 3 = 2 · 3^3
# 2 · 3^3 · 11 = 594.

import math

x = int(input('Введите число:'))
y = int(input('Введите число:'))

x_2 = x  # для второго варианта решения
y_2 = y  # для второго варианта решения

# Первый варинат
d = 2
list_x = []
while d**2 <= x:
    if x % d == 0:
        list_x.append(d)
        x = x // d
    else:
        d = d+1
list_x.append(x)

d = 2
list_y = []
while d**2 <= y:
    if y % d == 0:
        list_y.append(d)
        y = y // d
    else:
        d = d+1
list_y.append(y)

print(list_x)
print(list_y)

res = []
for i in list_x:
    if i not in res:
        if i not in list_y:
            res.extend([i] * list_x.count(i))
        else:
            res.extend(max([i] * list_x.count(i),
                           [i] * list_y.count(i)))
for i in list_y:
    if i not in res:
        res.extend([i] * list_y.count(i))
print(res)

nok = 1
for i in range(len(res)):
    nok = nok*res[i]

print(nok)

# Второй вариант

print((x_2 * y_2) // math.gcd(x_2, y_2))
