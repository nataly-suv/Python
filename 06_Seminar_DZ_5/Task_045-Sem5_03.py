# =============================================================================================
# Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков
# и определяет, можно ли из этих отрезков составить треугольник.
# =============================================================================================

a = int(input())
b = int(input())
c = int(input())



def triangle(a, b, c):
    flag = False
    if (a+b) > c and (a+c) > b and (c+b) > a:
        flag = True
    return 'yes' if flag else 'no'


print(triangle(a, b, c))



# def triangle(a, b, c):
#     return ("Это не треугольник", "Это треугольник")[(a + b > c) and (a + c > b) and (b + c > a)]

# print(triangle(int(input()), int(input()), int(input())))
