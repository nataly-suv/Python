# ====================================================================
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# ====================================================================

import math

list = [float(i) for i in ((input("Введите значения через пробел "))).split()]
print('Исходный список', list)
print()

# ищем самую длинную дробную часть
count = 0
for i in range(len(list)):
    # пример обрезки строки по нужному элемнету s = 'text text: one two three'   >>> s[s.find(":") + 1:]   ответ ' one two three'
    len_element = len(str(list[i])[str(list[i]).find(".")+1:])
    if len_element > count:
        count = len_element
print('Кол-во цифр для округления:', count)

# взяла абсолютные значения. Т.к. поняла ,что именно это  нужно в задании
list_output = []
for i in range(len(list)):
    list_output.append(round(math.fabs(list[i])-math.fabs(int(list[i])), count))
    #                         беру по модулю      int - беру целую часть  округляю
print('Список с дробными частями', list_output)
a = max(list_output)-min(list_output)
print('Разница между мах и мин значением дробной части:', a)
print()


# ВОПРОС!!!!!!!!!!! Как можно вытащить дробную часть после разложения?
list_output_modf = []
for i in range(len(list)):
    list_output_modf.append(math.modf(list[i]))  # math.modf - делит число на целю и дробную части
print(list_output_modf)


# # оставила для себя )
# x = max(list)-min(list)
# print(x)
