# ==================================================================
# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81  (основание -3 в степенях 0, 1, 2, 3, 4)
# ==================================================================

n = int(input('введите число N: '))
for i in range(n):
    result = (-3)**i
    print(result, end=" ")
