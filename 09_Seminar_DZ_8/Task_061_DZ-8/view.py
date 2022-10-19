# =======================================
# ЮРЕЗ ИНТЕРФЕЙС
# =======================================

def out_red(text):
    print("\033[31m {}\033[0m" .format(text))

def out_yellow(text):
    print("\033[33m {}\033[0m" .format(text))


def start_menu():
    out_yellow('Выберите необходимое действие!')
    print('1 - показать все')
    print('2 - добавить запись')
    print('3 - удалить запись')
    print('4 - изменить телефон')
    return int(input('Введите цифру: '))



def add_info():   # 2 - добавление информации
    out_yellow('Введите ФИО и тел через пробел')
    in_info = input().split()
    return in_info



def delete():   # 3 - удаление информации
    out_yellow('Введите индекс для удаления')
    return int(input())


def change_tel():  # 4 - изменить телефон
    out_yellow('Введите индекс для изменения и новый телефон, через энтер')
    return int(input()), input()



def change_menu ():     # что делать с изменениями? сохранить в текущем или создать новый
    out_yellow('Выберите необходимое действие!')
    out_red('Вы хотите: ')
    print ('1 - сохранить изменеия в текущем файле')
    print ('2 - экспортирвать в новый csv файл')
    return int(input('введите цифру: '))


def export_menu():     # что делать с показанной базой?
    out_yellow('Выберите необходимое действие!')
    out_red('Вы хотите: ')
    print ('1 - пересохранить файл в новый файл csv')
    print ('2 - выйти')
    return int(input('введите цифру: '))



def show_file(file_csv):   # красивы вывод базы
    for i, row in enumerate(file_csv):
        print(i, ' '.join(row))

