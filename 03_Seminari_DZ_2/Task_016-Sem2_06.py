# =======================================================================
# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой
# =======================================================================


s = input('введите букавы: ')
s1 = input('ведите букавы: ')

# первый вариант
print('Первый вариант')
print(s.count(s1))


# второй вариант
print('Второй вариант')
string = 'cccchjkccc'
find = 'cc'
# print(string.count(find))
count = 0
i = 0
while i < len(string):
    if string[i:i + len(find)] == find:
        count += 1
        i += len(find)
    else:
        i += 1
print(count)
