# =====================================================
# Реализуйте алгоритм перемешивания списка
# (метод random.shuffle использовать нельзя,
# но другие методы из библиотеки random - можно).
# =====================================================

import random

list = [12, 55, 63, 89, 41, 58, 34]
print('Исходный список: ', list)

# первый вариант
list_random = []
while list:
    num = random.choice(list)
    list_random.append(num)
    list.remove(num)
print('Перемешанный список (вар 1) ', list_random)


# второй варинат
list_2 = [12, 55, 63, 89, 41, 58, 34]
list_random_2 = []
flag = True
i = 0
while i < len(list_2):
    num = random.choice(list_2)
    if num not in list_random_2:
        list_random_2.append(num)
        i = i + 1
print('Перемешанный список (вар 2) ', list_random_2)

# третий вариант
list_3 = [12, 55, 63, 89, 41, 58, 34]
list_random_3 = []
num = 0
a = False
for i in range(len(list_3)):
    while a == False:
        num = random.choice(list_3)
        if (num) not in (list_random_3):
            list_random_3.append(num)
            a == True
            break
print('Перемешанный список (вар 3) ', list_random_3)
