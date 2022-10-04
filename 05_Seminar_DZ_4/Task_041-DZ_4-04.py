# ==============================================================
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# ==============================================================

import random

k = int(input('Введите степень k многочлена: '))

list = []
for i in range(k+1):
    list.append(int(random.random()*100))

print(list)

res = ''

for i in range(len(list)):
    if i < len(list)-2:
        if list[i] != 0:
            temp = str(list[i])
            stepen = str(len(list)-1-i)
            res = res+temp+'*x^'+stepen+' + '
    elif len(list)-3 < i < len(list)-1:
        if list[i] != 0:
            res = res+str(list[i])+'*x + '
    else:
        if list[i] != 0:
            res = res+str(list[i]) + ' = 0'
        else:
            res = res+'= 0'

print(res)

with open("DZ_4.txt", "w") as file:
    file.write(res)
