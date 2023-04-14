# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# ///// ПЕРВОЕ РЕНШЕНИЕ
# def arithm_progres(first_element, number_d, count_of_elements):
#     arithm_progres_list = []
#     for i in range(1, count_of_elements):
#         all_numbers = first_element+ (number_d - 1)*number_d
#         arithm_progres_list.append(all_numbers)
#         print(arithm_progres_list)
#         first_element = all_numbers
#         all_numbers = all_numbers+1
        
#     return arithm_progres_list


# arithm_progres_list = []
# print(arithm_progres(int(input("Введите первый элемент a1: ")),int(input("Введите разность d: ")),int(input("Введите количество элементов n: "))))

# /////ВТОРОЕ РЕШЕНИЕ
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)



# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] # или рандомный ввод
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)