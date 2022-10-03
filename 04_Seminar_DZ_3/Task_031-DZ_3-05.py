# ================================================
# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов
# для 8: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# ================================================


number = int(input('Введите число: '))

list_positiv = []
list_positiv.append(1)
list_positiv.append(1)

for i in range(2, number):
    list_positiv.append(list_positiv[i-2]+list_positiv[i-1])
# print(list_positiv)

list_negativ = []
for i in range(len(list_positiv)):
    if i % 2 != 0:
        list_negativ.append(list_positiv[i]*-1)
    else:
        list_negativ.append(list_positiv[i])

list_negativ = list_negativ[::-1]
list_negativ.append(0)
# print(list_negativ)

print(list_negativ+list_positiv)





# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# data = list(fibonacci(10))
# print(data)
