# 2 Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint
import random
import os

os.system("cls||clear")

game_sweets = 60
start_turn = randint(0, 1)
game_end = 10
game_phrase = ("глупый человечешка", "проиграешь",
               "ну же, только один разок =)) ", "кожаный мешок не умеет играть", "я забочусь о твоем здоровье")
print(f"В борьбе за человечество осталось {game_sweets} конфет")

if not start_turn:
    print("Вселенную захватили машины!")
else:
    print("Есть шанс у человечества!")


def play(sweets, turn, the_end, phrase):
    while sweets >= 0:
        if not turn:
            if sweets % (the_end+1) ==0:
                start = the_end
            else:
                start = sweets % (the_end+1)
            sweets = sweets-start
            print(f"Терминатор уничтожил {start}, осталось {sweets} конфет")
            print(random.choice(phrase))
            end = int(input(f"Введите число от 1 до {the_end}: "))
            while end < 1 or end > the_end:
                end = int(
                    input(f"Введено неправильное число. Введите число от 1 до {the_end}: "))
            sweets = sweets-end
            print(f"Осталось {sweets} конфет")
        else:
            if sweets <= the_end:
                the_end = sweets
            start = int(input(f"Введите число от 1 до {the_end}: "))
            while start < 1 or start > the_end:
                start = int(
                    input(f"Введено неправильное число. Введите число от 1 до {the_end}: "))
            sweets = sweets-start
            if sweets == 0:
                print("Победа человечества, Джон Коннор, ты ли это?")
                break
            if sweets <= the_end:
                print(f"Скайнет выиграл, уничтожив последние {sweets} конфеты")
                break
            if sweets % (the_end+1) ==0:
                end = randint(1, the_end-1)
            else:
                end = sweets % (the_end+1)
            sweets = sweets-end
            print(f"Терминатор выбрал число {end}, осталось {sweets} конфет")
            print(random.choice(phrase))
        if sweets <= the_end and not turn:
            print(f"Скайнет выиграл, уничтожив последние {sweets} конфеты")
            break


play(game_sweets, start_turn, game_end, game_phrase)
