def show_data() -> None:
    with open ('book.txt', 'r', encoding='utf-8') as f:
       
        x = list(enumerate(f,1))
        print (f'\n{x}')

def add_data() -> None:
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open ('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n {fio} | {tel_number}')


# поиск информации состоит из двух функций, так удобней.

def find_data() -> None:
    data = input("Введите данные для поиска: ")              #запрашиваем данные
    with open ('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()                                  # получаем информацию и читаем её
    print('Результаты поиска: ')
    print(search(tel_book, data))

def search(book: str, info: str) -> str:     # функция принимает базу данных (tel_book) и параметры поиска (data)
    # находит в строке записи по определенному критерию поиска
    book = book.split('\n')   # разделяем базу данных (т.к. она одна строка) на список через разделитель
    return '\n'. join([post for post in book if info in post])  # генератором строк формируем список из тех элементов, которые подошли по поиску

def edited(text:str) -> str:
    
    fio = input("Введите ФИО: ")
    num = input ("Введите номер телефона: ")
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(num) == 0:
        num = text.split(' | ')[1]
    return f'{fio} | {num}'