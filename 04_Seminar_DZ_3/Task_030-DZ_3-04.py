# ===================================================
# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное
# ===================================================


number = int(input('Введите число: '))
number_2 = number
number_3 = number

# Первый вариант
list = []
while number > 0:
    list.append(number % 2)
    number = number // 2

list = list[::-1]
print(*list, sep='')


# Второй вариант
string = ''
while number_2 > 0:
    string = str(number_2 % 2) + string
    number_2 = number_2 // 2

print(string)


# Третий вариант
print(f"{number_3:b}")
