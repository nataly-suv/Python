# =============================================================================================
# Напишите программу, которая подсчитает и выведет
# сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.
# =============================================================================================


nums = [i for i in range(10, 100)]
res = sum(map(lambda x: x**2, filter(lambda x: not x % 9, nums)))
print(res)