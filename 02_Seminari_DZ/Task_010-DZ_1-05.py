# =============================================================
# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве
# =============================================================

import math

x_1 = int(input('Введите координату Х1:'))
y_1 = int(input('Введите координату Y1:'))
x_2 = int(input('Введите координату Х2:'))
y_2 = int(input('Введите координату Y2:'))

l = round((math.sqrt((x_1-x_2)**2+(y_1-y_2)**2)), 3)
print(f'Расстояние между точками равно: {l}')
