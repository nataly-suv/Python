# ====================================================================================================
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# ====================================================================================================

import re

''' БЛОК КОДИРОВАНИЯ ИСХОДНОГО ФАЙЛА '''

with open("06_Seminar_DZ_5/text-in.txt", "rt") as file:  # открытие файла на чтение
    text_in = file.readline()
print('Отрытый файл сожержит: ', text_in)
print('Длина этого файла: ',len(text_in))

count = 1 # счетчик дял подсчета одинаковых элементов

string_out = '' # пустая строк, куда будем записывать кодированный файл

for i in range(len(text_in)-1):
    if text_in[i] == text_in[i+1]:
        count = count+1
    elif text_in[i] != text_in[i+1]:
        string_out = string_out+str(count)+str(text_in[i]) 
        # Если элемент i и i+1 не равны, то в строку заносим значение счеткика и сам элемент
        count = 1 # сбрасываем счетчик 
        i = i+1
if text_in[-2] == text_in[-1]: 
    # если i и i+1 равны в конце строки, то нужно записать в строку последнее занчение счетчика и элемент
    string_out = string_out+str(count)+str(text_in[i])
else:
    string_out = string_out+'1'+str(text_in[-1]) # для случая, когда последний элемент в одном количестве 


print('Кодированный текст', string_out)

# запись кодированното текста во внешний файл
with open("06_Seminar_DZ_5/text-out.txt", "w") as file_out:
    file_out.write(string_out)

print()

''' БЛОК ДЕШИФРОВКИ '''

with open("06_Seminar_DZ_5/text-out.txt", "rt") as file_recode:
    file_recode = file_recode.readline()

file_number_str = re.findall('[0-9]+', file_recode) # сделали импорт re и вытащили в список, числа в этой строке

file_number_int = [int(i) for i in file_number_str] # перевод списка строк в список чисел

list_leter = [] # пустой список, для сбора элементов для дешефровки

# 1) 12W1B12W3B24W1B14W
# 2) ['12', '1', '12', '3', '24', '1', '14']
# 3) ['W', 'B', 'W', 'B', 'W', 'B', 'W']

count = 0
for number in file_number_str:
    count = count+len(number) 
    # пропускаем в исходной строке позиции, равные длине элемента (т.е. 12 - пропускаем 2 позиции b и переходим к букве W)
    list_leter.append(file_recode[count])  # добавляем элемент в список
    count = count+1 # переходим на новую позицию

strint_record=''  # пустая строка для дешефровки

for i in range(len(file_number_int)):
    strint_record=strint_record+list_leter[i]*file_number_int[i] 


print('Файл для дешефровки', file_recode)
print('Список строк с числами',file_number_str)
print('Список строк с буквами',list_leter)
print('Итоговый, дешефрованный текст',strint_record)








# # Заимствованный вариант
# def encode(s):

#     encoding = "" # сохраняет выходную строку

#     i = 0
#     while i < len(s):
#         # подсчитывает количество вхождений символа в индексе `i`
#         count = 1

#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1

#         # добавляет к результату текущий символ и его количество
#         encoding += str(count) + s[i]
#         i = i + 1

#     return encoding


# if __name__ == '__main__':

#     s = 'ABBCCCD'
#     print(encode(s))
