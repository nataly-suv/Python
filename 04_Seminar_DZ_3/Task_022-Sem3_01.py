# ======================================================================================
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# ======================================================================================

# Первый варинат

print('Первый варинат')
list1_1 = [4, 1, 2, 2, 3, 3, 5]
list1_2 = []
for i in list1_1:
    if list1_1.count(i) == 1:
        list1_2.append(i)
print(*list1_2)


# Второй варинат

print('Второй варинат')
list2_1 = [int(i) for i in ((input("Введите значения через пробел "))).split()]
print(list2_1)
list2_2 = []
count = 0
for i in list2_1:
    for j in list2_1:
        if i == j:
            count += 1
    if count == 1:
        list2_2.append(i)
    count = 0
print(list2_2)


# Третий варинат

print('Третий варинат')
# ist = [int(i) for i in input("Введите числа через пробел: ").split()]
List3 = list(map(int, input("Введите числа через пробел: ").split()))
for i in List3:
    if List3.count(i) == 1:
        print(i, end=' ')
