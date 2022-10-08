# =====================================================
# Создайте программу для игры в ""Крестики-нолики"".
# =====================================================

list = [[1, ' | ', 2, ' | ', 3], [
    4, ' | ', 5, ' | ', 6], [7, ' | ', 8, ' | ', 9]]

flag = False


def pechat():
    for row in list:
        for elem in row:
            print(elem, end=' ')
        print()
        print('-------------')


def igrok_1_x():
    x = int(input('Игрок - х. Ващ ход. Ввдеите номер позиции: '))
    if x == 1:
        list[0][0] = 'x'
    if x == 2:
        list[0][2] = 'x'
    if x == 3:
        list[0][4] = 'x'
    if x == 4:
        list[1][0] = 'x'
    if x == 5:
        list[1][2] = 'x'
    if x == 6:
        list[1][4] = 'x'
    if x == 7:
        list[2][0] = 'x'
    if x == 8:
        list[2][2] = 'x'
    if x == 9:
        list[2][4] = 'x'
    return x


def igrok_2_o():
    x = int(input('Игрок - о. Ваш ход. Ввдеите номер позиции: '))
    if x == 1:
        list[0][0] = 'o'
    if x == 2:
        list[0][2] = 'o'
    if x == 3:
        list[0][4] = 'o'
    if x == 4:
        list[1][0] = 'o'
    if x == 5:
        list[1][2] = 'o'
    if x == 6:
        list[1][4] = 'o'
    if x == 7:
        list[2][0] = 'o'
    if x == 8:
        list[2][2] = 'o'
    if x == 9:
        list[2][4] = 'o'
    return x


def proverka(flag):
    if (list[0][0] == list[0][2] == list[0][4] or list[1][0] == list[1][2] == list[1][4] or list[2][0] == list[2][2] == list[2][4]
        or list[0][0] == list[1][0] == list[2][0] or list[0][2] == list[1][2] == list[2][2] or list[0][4] == list[1][4] == list[2][4]
            or list[0][0] == list[1][2] == list[2][4] or list[0][4] == list[1][2] == list[2][0]):
        print('Ура!!! Вы победили')
        flag = True
    return flag


pechat()

count = 0

while count < 9:
    count += 1
    igrok_1_x()
    pechat()
    if proverka(flag) == True:
        break

    count += 1
    igrok_2_o()
    pechat()
    if proverka(flag) == True:
        break

    count += 1
    igrok_1_x()
    pechat()
    if proverka(flag) == True:
        break

    count += 1
    igrok_2_o()
    pechat()
    if proverka(flag) == True:
        break

    count += 1
    igrok_1_x()
    pechat()
    if proverka(flag) == True:
        break

    count += 1
    igrok_2_o()
    pechat()
    if proverka(flag) == True:
        break

    count += 1
    igrok_1_x()
    pechat()
    if proverka(flag) == True:
        break

    count += 1
    igrok_2_o()
    pechat()
    if proverka(flag) == True:
        break

    count += 1
    igrok_1_x()
    pechat()
    if proverka(flag) == True:
        break
