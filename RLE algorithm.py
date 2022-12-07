# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaasssdddwwwwwwwwwwwweeeffffffc -> 4a3s3d12w3e6f1c
# 4a3s3d12w3e6f1c-> aaaasssdddwwwwwwwwwwwweeeffffffc

import os

os.system("cls||clear")

with open("RLE input long.txt") as file:
    list_char = list(file.read())

count_char = 1
new_list = []

for i in range(1, len(list_char)):
    if list_char[i] == list_char[i-1]:
        count_char += 1
    else:
        new_list.append(count_char)
        new_list.append(list_char[i-1])
        count_char = 1

new_list.append(count_char)
new_list.append(list_char[i])

new = "".join(map(str, new_list))

with open("RLE output short.txt", "w") as file:
    file.write(new)


with open("RLE input short.txt") as file:
    list_char = file.read()

long_name = ""
count = ""

for i in list_char:
    if i.isdigit():
        count += i
    else:
        long_name += i*int(count)
        count = ""

with open("RLE output long.txt", "w") as file:
    file.write(long_name)
