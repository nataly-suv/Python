# =============================================================================================
# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] , [1, 2, 3, 4, 6, 7], [1, 3, 4, 6, 7] и т.д.
# =============================================================================================

list = [1, 5, 2, 3, 4, 6, 1, 7]
list_res = []
list_res.append(list[0])



list = [1, 5, 2, 3, 4, 6, 1, 7]
list_res = []
for j in range(1, len(list)):
    list_temp = [list[0]]
    for i in range(j, len(list)):
        if list[i] > list_temp[-1]:
            list_temp.append(list[i])
    list_res.append(list_temp)
print(list_res)






# def filt(lst):
#     '''Функция для удаления чисел, выбивающихся из последовательности'''
#     start, end = lst[0], lst[-1]
#     res = [start]
#     for i in range(1, len(lst) - 1):
#         if start < lst[i] < end:
#             if res[-1] < lst[i]:
#                 res.append(lst[i])
#     return res + [end]


# sp = [1, 5, 2, 3, 4, 6, 1, 7]
# res = []
# for i in range(len(sp)):
#     for j in range(i, len(sp)):
#         if sp[j] > sp[i]:
#             res1 = sp[i:j + 1]
#             res.append(filt(res1))
#             res.append([sp[i], sp[j]])
# set_res = []
# for el in res:
#     if el not in set_res:
#         print(el)
#         set_res.append(el)
