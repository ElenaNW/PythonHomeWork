# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# ПЕРВОЕ РЕШЕНИЕ ЗАДАЧИ С МОНЕТКАМИ (БЕЗ ЦИКЛА)
# count = int(input("Введите количество монеток: "))
# first_side = int(input("Сколько монеток лежит гербом вверх? "))
# second_side = count - first_side
# min = 0
# if second_side < first_side:
#     min = second_side
# else:
#     min = first_side
# print(min)

# ВТОРОЕ РЕШЕНИЕ ЗАДАЧИ С МОНЕТКАМИ
# count = int(input("Введите количество монеток: "))  # решение через цикл for
# first_side = 0                                      
# second_side = 0
# for i in range(count):                               
#     x = input()                                # можно писать орёл или другое значение, 
#     if x == "орёл":                            # программа прибавляет к орлу или другому значению счет +1
#         first_side += 1
#     else:
#         second_side += 1
# if first_side < second_side:                   # сравниваем, какая сторона встречалась реже, её и выводим в принт
#     print (first_side)
# else:
#     print (second_side)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# summa = int(input("сумма: "))
# multiplication = int(input("произведение: "))
# for i in range(summa):
#     for j in range(multiplication):
#         if summa == i + j and multiplication == i * j:
#             print(i, j)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# ПЕРВОЕ РЕШЕНИЕ ЗАДАЧИ 14
# n = int(input("Введите число: "))
# step = 0
# for i in range(n):
#     if 2**i <= n:
#         step = 2**i
#         print (step)

# ВТОРОЕ РЕШЕНИЕ ЗАДАЧИ 14
# n = int(input("Введите число: "))
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1
