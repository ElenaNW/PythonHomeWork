# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трёхзначное число: "))
digit1 = int(number/100)
digit2 = int(number/10 % 10)
digit3 = int(number % 10)
summa = digit1+digit2 + digit3
print(f"{number} -> {summa} ({digit1} + {digit2} + {digit3})")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

allChildren = int(input("Напишите, сколько журавликов сделали дети "))
third = int(allChildren/3)
Kate = int(allChildren-third)
boy = int(third/2)
print(f"{allChildren} -> {Kate}, {boy}, {boy}")


# Задача 6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

number = int(input("Введите номер своего билета: "))
part1 = int(number/1000)
part2 = int(number % 1000)
digit1Part1 = int(part1/100)
digit2Part1 = int(part1/10 % 10)
digit3Part1 = int(part1 % 10)
summaPart1 = digit1Part1 + digit2Part1 + digit3Part1
digit1Part2 = int(part2/100)
digit2Part2 = int(part2/10 % 10)
digit3Part2 = int(part2 % 10)
summaPart2 = digit1Part2 + digit2Part2 + digit3Part2
if (summaPart1 == summaPart2):
    print(f"{number} -> yes")
else:
    print(f"{number} -> no")


# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

numberN = int(input("Введите длину шоколадки (в дольках): "))
numberM = int(input("Введите ширину шоколадки (в дольках): "))
numberK = int(input("Укажите количество долек, которое нужно отломить: "))
if (numberK % numberN == 0 or numberK % numberM ==0) and numberK < (numberN*numberM):
    print("yes")
else:
    print("no")
