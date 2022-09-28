# ============================================================================
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]
#  (например, [-3, -2, 1, 0, 1, 2, 3].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# ============================================================================

N = int(input('Введите число N: '))
list = []
# создаю список от -N до N
for i in range(-N, N+1):
    list.append(i)
print(list)


# первый вариант. Для 2-х индексов
print()
print('Первый вариант. Для 2-х индексов')
with open("readme.txt", "rt") as file:
    x = int(file.readline())
    y = int(file.readline())
    print('1-ый индекс:', x, '  2-ой индекс:', y)
for i in list:
    mult = list[x]*list[y]
print('Произведение равно: ', mult)

# второй вариант. универсальный
print()
print('Второй вариант')
list_file = []

with open("readme.txt", "rt") as file:    # открываю файл и записываю его как строку в text
    text = file.read()
# print(text)   # печать строки
# print(type(text))  # проверяла, что это строка

for i in text:
    list_file.append(i)  # Переписала строку в список
print('Список типа str c энтерами: ', list_file)
print('Длина строки ', len(list_file))

for i in list_file:
    # удалила в списке \n' !!! файл обязательно должен заканчиваться \n' Почему?
    list_file.remove('\n')
print('Список типа str: ', list_file)

for i in range(len(list_file)):
    list_file[i] = int(list_file[i])  # перевела список в тип int
print('Список типа int: ', list_file)

mult_2 = 1  # временная переменная
if list_file[-1] > (N*2+1):
    print('нельзя произвести умножение')
else:
    for i in range(len(list_file)):
        z = list_file[i]
        mult_2 = mult_2*list[z]
print('Произведение равно: ', mult_2)
