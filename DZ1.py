# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трёхзначное число: "))
digit1 = int(number/100)
digit2 = int(number/10 % 10)
digit3 = int(number % 10)
summa = digit1+digit2 + digit3
print(f"{number} -> {summa} ({digit1} + {digit2} + {digit3})")
