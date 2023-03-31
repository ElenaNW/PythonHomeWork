# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# import time

#  ПЕРВЫЙ ВАРИАНТ
# some_list = []
# number_n = int(input('Укажите количество элементов: '))
# for i in range(number_n):
#     some_list.append(int(input('Напишите число: ')))
# print(some_list)

# number_x = int(input('Введите искомое число: '))

# start = time.perf_counter()
# count = 0
# for i in some_list:
#     if i == number_x:
#         count +=1
# print(f"-> {count}")
# end = time.perf_counter()
# first_time = end-start
# print(first_time)

# # # ВТОРОЙ ВАРИАНТ
# some_list = []
# number_n = int(input('Укажите количество элементов: '))
# for i in range(number_n):
#     some_list.append(int(input('Напишите число: ')))
# print(some_list)

# number_x = int(input('Введите искомое число: '))

# start = time.perf_counter()
# print (some_list.count(number_x))
# end = time.perf_counter()
# second_time = end-start
# print(second_time)

# print(first_time/second_time)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

number_list = []
number_list_len = int(input('Введите длину списка: '))
for _ in range(number_list_len):
    number_list.append(int(input('Введите число: ')))
print(number_list)

for i in range(len(number_list)):
    for j in range(i+1, len(number_list)):
        if (number_list[j] < number_list[i]):
            x = number_list[i]
            number_list[i] = number_list[j]
            number_list[j] = x

number_x = int(input("Введите число: "))

res = 0
res2 = 0
flag = True

for i in number_list:
    if i > number_x:
        flag = False
        res += i
else:
    res = number_list[-1]
   
for el in number_list[-1::-1]:
   if el < number_x:
        flag = False
        res2 += el
else:
    res2 = number_list[0]
   
if number_x - res2 > res - number_x:
    print (res)
else:     
    print (res2)



# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12


# scrabble_dict = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1,
#                  "а": 1, "в": 1, "е": 1, "и": 1, "н": 1, "о": 1, "р": 1, "с": 1, "т": 1, 'd': 2, 'g': 2,
#                  "д": 2, "к": 2, "л": 2, "м": 2, "п": 2, "у": 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, "б": 3,
#                  "г": 3, "ё": 3, "ь": 3, "я": 3, "й": 4, "ы": 4, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
#                  'k': 5, "ж": 5, "з": 5, "х": 5, "ц": 5, "ч": 5, "ш": 8, "э": 8, "ю": 8, "j": 8, 'x': 8,
#                  'q': 10, 'z': 10, "ф": 10, "щ": 10, "ъ": 10}
# game_word = input("Напишите слово: ")
# sum = 0
# for el in game_word:
#     sum += scrabble_dict[el] 
# print(sum)