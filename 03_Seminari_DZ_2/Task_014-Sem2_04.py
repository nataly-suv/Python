#======================================================================
# Напишите программу, которая проверяет пятизначное число на палиндром
#======================================================================

input_number = input('Введите число: ')

# первый вариант
print('Первый вариант')
if input_number[:2] == input_number[:2:-1]:
    print('палиндром')
else:
    print('не палиндром')

# второй вариант
print('Второй вариант')
number = str(input_number)
palindrome = True
for i in range(len(number) // 2):
    if number[i] != number[-i-1]:
        palindrome = False
        break
if palindrome:
    print('Палиндром')
else:
    print('Не палиндром')
