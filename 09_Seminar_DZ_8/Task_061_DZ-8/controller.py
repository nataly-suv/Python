# =======================================
# СВЯЗЬ model и view
# =======================================
import model
import view


def run():
    start = view.start_menu()
    if start == 1:
        file_csv = model.csv_data_open()
        view.show_file(file_csv)
        point = view.export_menu()
        if point == 1: model.export_csv_csv()
    elif start == 2:
        in_info = view.add_info()
        point= view.change_menu ()
        if point == 1: model.add_info(in_info)
        elif point == 2: model.add_info_new(in_info)
    elif start == 3:
        index = view.delete()
        point= view.change_menu ()
        if point == 1: model.del_info(index)
        elif point == 2: model.del_info_new(index)
    elif start == 4:
        index, tel = view.change_tel()
        point= view.change_menu ()
        if point == 1: model.update_info(index, tel)
        elif point == 2: model.update_info_new(index, tel)
        


# run()
