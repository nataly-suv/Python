# ==================================================================
# Даны два целых числа A и В, A>B.
# Выведите все нечётные числа от A до B включительно,
# в порядке убывания. В этой задаче можно обойтись без инструкции if.
# ==================================================================

# первый вариант 
print('Первый вариант')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
b = b + (b + 1) % 2  # приводим к нечетному числу
k = []
for i in range(b, a + 1, 2):
    k.append(i)
k = k[:: -1]  # разворот списка
print(*k) # * - убирает скобки, запятые


# второй вариант
print('Второй вариант')
for i in range(a - (a + 1) % 2, b - 1, -2):
    print(i, end=' ')