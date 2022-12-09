# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

# *Пример:*

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import os

os.system("cls||clear")


user_list = [1, 5, 2, 3, 4, 6, 1, 7]

new_list = list(user_list)
new_list.sort()
new_set = set(new_list)
net_list = list(new_set)
new_int = int("".join(str(i) for i in net_list))


for i in range(10, new_int):
    new_i = list(map(int, str(i)))
    for j in range(0,len(new_i)):
        if j == len(new_i)-1:
            print(i)
            break
        if new_i[j] < new_i[j+1] and new_i[j] in user_list and new_i[j+1] in user_list and \
                user_list.index(new_i[j]) < user_list.index(new_i[j+1]):
                continue
        else:
            break
