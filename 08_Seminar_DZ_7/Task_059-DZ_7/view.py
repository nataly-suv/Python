

def start_menu():
    print('Выберите необходимое действие!')
    print('вы хотите открыть: файл txt - 1; файл csv - 2')
    return int(input('введите цифру: '))



def export_menu():
    print('Выберите необходимое действие!')
    print('вы хотите экспортировать: в файл txt - 1; в файл csv - 2')
    return int(input('введите цифру: '))



def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))