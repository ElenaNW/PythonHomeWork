# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# и сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: если символ встречается 1 раз, он остается без изменений;
# если символ повторяется более 1 раза, к нему добавляется количество повторений.

# def rle(some_str): 
#     letter_list = [] 
#     some_str += ' '
#     temp_letter = some_str[0] 
#     count = 1 
#     for index in range(1, len(some_str)): 
#         if some_str[index] == temp_letter: 
#             count += 1
#         else:    
#             if count == 1:
#                 letter_list.append(f'{temp_letter}') 
#             else:
#                 letter_list.append(f'{temp_letter}{count}') 
#             count = 1 
#             temp_letter = some_str[index] 
#     print(*letter_list, sep='') 

# rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')


# Сгруппировать слова по общим буквам:
# Sample input: ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output[["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]


def common_letters(input_list): 
    some_dict = {}
    for word in input_list:
        if (frozenset(word), len(word)) not in some_dict:
            some_dict[(frozenset(word), len(word))] = [word]
        else:
            some_dict[(frozenset(word), len(word))].append(word)
    result_list = []
    for value in some_dict.values():
        result_list.append(value)
    return result_list

print (common_letters(["eat", "tea", "tan", "ate", "nat", 'bat']))
