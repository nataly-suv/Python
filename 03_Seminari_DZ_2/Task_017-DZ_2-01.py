# =====================================================
# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:  1) 6782 -> 23   2) 0,56 -> 11
# =====================================================

input_number = float(input('Введите вещественное число: '))
input_string = str(input_number)
length_string = len(input_string)
index_point = input_string.index('.')

number = int(input_number*10**(length_string-index_point-1))
sum = 0

for i in range(length_string-1):
    sum = sum + number % 10
    number = number//10

print(sum)
