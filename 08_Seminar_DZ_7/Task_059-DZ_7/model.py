import csv
from re import S


def csv_data_open():      # открытие файла csv
    with open("08_Seminar_DZ_7/Task_059-DZ_7/csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res


def txt_data_open():     # открытие файла txt
    with open("08_Seminar_DZ_7/Task_059-DZ_7/txt_data.txt", "rt", encoding='utf-8') as file:
        file_txt = file.read()
        # print(file_txt)
    return file_txt


def export_txt_txt(file_txt):    # экспорт из txt в txt
    with open("08_Seminar_DZ_7/Task_059-DZ_7/txt-txt_data_out.txt", "w", encoding='utf-8') as txt_txt_data_out:
        txt_txt_data_out.write(file_txt)


def export_txt_csv(file_txt):    # экспорт из txt в csv
    file_txt = file_txt.replace(' ', ';')
    with open("08_Seminar_DZ_7/Task_059-DZ_7/txt-csv_data_out.csv", "w", encoding='utf-8') as txt_csv_data_out:
        txt_csv_data_out.write(file_txt)


def export_csv_csv():     # экспорт из csv в csv
    with open('08_Seminar_DZ_7/Task_059-DZ_7/csv_data.csv', encoding="utf8") as csvfile, open('08_Seminar_DZ_7/Task_059-DZ_7/csv-csv_data_out.csv', 'w', encoding="utf8", newline='') as f:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(f, delimiter=';')
        for row in reader:
            writer.writerow(row)


def export_csv_txt():     # экспорт из csv в txt
    list_csv = csv_data_open()
    for i in list_csv:
        s = ' '.join(i)
        with open("08_Seminar_DZ_7/Task_059-DZ_7/csv-txt_data_out.txt", "a", encoding='utf-8') as f:
            f.writelines(s + '\n')
