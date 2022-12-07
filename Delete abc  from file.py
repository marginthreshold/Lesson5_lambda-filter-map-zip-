# Напишите программу, удаляющую из файла все слова, содержащие "abc".
# Very funny animal Abcodog wolking through the dabcopark road

import os

os.system("cls||clear")

with open("file contains abc.txt") as file:
    list_from_file = list(file.read().split())

new_list = list(filter(lambda x: not "abc" in x.lower(), list_from_file))
clear_text = " ".join(new_list)

with open("file contains abc.txt", "w") as file:
    file.write(clear_text)
