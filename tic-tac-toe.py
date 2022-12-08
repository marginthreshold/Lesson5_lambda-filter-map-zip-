# 3 Создайте программу для игры в "Крестики-нолики".
# Вариант интерфейса:
#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9

import os

os.system("cls||clear")

start_list = list(range(1, 10))
check_list = list(range(1, 10))

print("Игрок1 ходит X, Игрок2 ходит 0\n")
gamer1 = "Игрок1"
gamer2 = "Игрок2"


def game_filed(list):
    print(f"    {list[0]} | {list[1]} | {list[2]}\n   ___________\n\
    {list[3]} | {list[4]} | {list[5]}\n   ___________\n\
    {list[6]} | {list[7]} | {list[8]}\n")


def win(list):
    if list[0] == list[1] == list[2] or \
            list[3] == list[4] == list[5] or \
            list[6] == list[7] == list[8] or \
            list[0] == list[3] == list[6] or \
            list[1] == list[4] == list[7] or \
            list[2] == list[5] == list[8] or \
            list[1] == list[4] == list[8] or \
            list[2] == list[4] == list[6]:
            return 1


def draw(list):
    if list == []:
        return 1

game_filed(start_list)

for i in range(0,9):
    gamer1_turn = int(input("\n Игрок1, введите номер поля для X: "))
    while gamer1_turn not in check_list:
        gamer1_turn = int(
            input("\n Такие номера уже заняты, Игрок1, введите номер поля для X: "))

    start_list[gamer1_turn-1] = "X"
    check_list.remove(gamer1_turn)

    game_filed(start_list)

    if win(start_list):
        print("Победил Игрок1 ")
        break 

    if draw(check_list):
        print("Ничья")
        break


    gamer2_turn = int(input("\n Игрок2, введите номер поля для 0: "))
    while gamer2_turn not in check_list:
        gamer2_turn = int(
            input("\n Такие номера уже заняты, Игрок2, введите номер поля для 0: "))

    start_list[gamer2_turn-1] = "0"
    check_list.remove(gamer2_turn)

    game_filed(start_list)

    if win(start_list):
        print("Победил Игрок2 ")
        break
        

    if draw(check_list):
        print("Ничья")
        break
        

        
