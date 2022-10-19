# =======================================
# АЛГОРИТМ
# =======================================

import csv



def csv_data_open():      # открытие файла csv и переформатирование в list
    with open("09_Seminar_DZ_8/Task_061_DZ-8/csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        file_csv = list(file_csv)
    return file_csv



def add_info(list):  # 2- добавление информации
    with open("09_Seminar_DZ_8/Task_061_DZ-8/csv_data.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)


def del_info(index):  # 3 - удаление информации
    list_csv = csv_data_open()
    del list_csv[index]
    with open("09_Seminar_DZ_8/Task_061_DZ-8/csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def update_info(index, tel):  # 4 - изменить телефон
    list_csv = csv_data_open()
    list_csv[index][3] = tel
    with open("09_Seminar_DZ_8/Task_061_DZ-8/csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def export_csv_csv():     # экспорт из csv в csv
    with open('09_Seminar_DZ_8/Task_061_DZ-8/csv_data.csv', encoding="utf8") as csvfile, open('09_Seminar_DZ_8/Task_061_DZ-8/csv-csv_data_out.csv', 'w', encoding="utf8", newline='') as f:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(f, delimiter=';')
        for row in reader:
            writer.writerow(row)


def add_info_new(list):  # 2- добавление информации в новый файл
    export_csv_csv()
    with open("09_Seminar_DZ_8/Task_061_DZ-8/csv-csv_data_out.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)


def del_info_new(index):  # 3 - удаление информации с перезаписью в новый файл
    export_csv_csv()
    list_csv = csv_data_open()
    del list_csv[index]
    with open("09_Seminar_DZ_8/Task_061_DZ-8/csv-csv_data_out.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)



def update_info_new(index, tel):  # 4 - изменить телефон с перезаписью в новый файл
    export_csv_csv()
    list_csv = csv_data_open()
    list_csv[index][3] = tel
    with open("09_Seminar_DZ_8/Task_061_DZ-8/csv-csv_data_out.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)