# ==============================================================
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов
# ==============================================================


with open("DZ_4_5-1.txt", "r") as file_1:
    file_1 = file_1.read()
with open("DZ_4_5-2.txt", "r") as file_2:
    file_2 = file_2.read()

print()
print('Первый многочлен', file_1)
print('Второй многочлен', file_2)
print()

for i in file_1:                   # Вычисляю степень первого многочлена
    stepen_1 = file_1.count('+')


for i in file_2:                   # Вычисляю степень второго многочлена
    stepen_2 = file_2.count('+')

print('Степень первого многочлена', stepen_1)
print('Степень второго многочлена', stepen_2)
print()

file_1 = file_1.replace('+', ' ')   # заменяю + на пробел
file_1 = file_1.split()             # делаю из строки список строк

file_2 = file_2.replace('+', ' ')   # заменяю + на пробел
file_2 = file_2.split()             # делаю из строки список строк


list_1 = []
list_2 = []

for i in file_1:                    # перевожу список строк в список чисел
    list_1.append(int(i[0]))        # беру 0-ой индекс в первой строке и перевожу в int

for i in file_2:                    # перевожу список строк в список чисел
    list_2.append(int(i[0]))        # беру 0-ой индекс в первой строке и перевожу в int


# блок для приведения списков чисел к одной длине 
if stepen_1 > stepen_2: 
    for j in range(stepen_1 - stepen_2):
        list_2.insert(j, 0)
else:
    for j in range(stepen_2 - stepen_1):
        list_1.insert(j, 0)

print('Коэффициенты для первого многочлена', list_1)
print('Коэффициенты для второго многочлена', list_2)
print()

list_res = []      # список для суммы коэффициентов 
for i in range(len(list_1)):
    list_res.append(str(list_1[i]+list_2[i]))  # складываю коэффициенты и сразу перевожу в str

print('Итоговые коэффициенты', list_res)

# блок для формирования итого многочлена 
res = ''
for i in range(len(list_res)):
    if i < len(list_res)-2:
        stepen = str(len(list_res)-1-i)
        res = res+list_res[i]+'*x^'+stepen+' + '
    elif len(list_res)-3 < i < len(list_res)-1:
        res = res+list_res[i]+'*x + '
    else:
        res = res+list_res[i] + ' = 0'

print()
print('Сумма многочленов: ', res)
print()

