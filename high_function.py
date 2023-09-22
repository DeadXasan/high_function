# Задача 1:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# --------------------------------------------------------------------------------------------------------------------

# Функция для подсчета количества гласных букв в строке
# def count_vowels(s):
#     vowels = "AEIOUaeiou"  # Гласные буквы
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

# # Ввод стихотворения Винни-Пуха
# poem = input("Введите стихотворение Винни-Пуха: ")

# # Разделяем стихотворение на фразы, разделенные пробелами
# phrases = poem.split()

# # Проверяем ритм в каждой фразе
# rhyme_ok = True
# for phrase in phrases:
#     # Разделяем фразу на слова, разделенные дефисами
#     words = phrase.split("-")
    
#     # Получаем количество гласных букв в первом слове
#     vowels_count = count_vowels(words[0])
    
#     # Сравниваем количество гласных букв в каждом слове фразы
#     for word in words:
#         if count_vowels(word) != vowels_count:
#             rhyme_ok = False
#             break

# # Вывод результата
# if rhyme_ok:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")


# --------------------------------------------------------------------------------------------------------------------

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
#            Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
#            Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    # Создаем таблицу и заполняем ее значениями, используя указанную операцию
    table = [[operation(row, col) for col in range(1, num_columns + 1)] for row in range(1, num_rows + 1)]
    
    # Определяем максимальную длину значения в таблице для выравнивания вывода
    max_length = len(str(max(max(table))))
    
    # Выводим таблицу
    for row in table:
        for value in row:
            # Выравниваем значение по ширине и выводим его
            print(f"{value:>{max_length}}", end=" ")
        print()  # Переходим на следующую строку после завершения текущей

# Пример использования:
# Функция умножения двух аргументов
def multiply(row, col):
    return row * col

print("Таблица умножения:")
print_operation_table(multiply, 9, 9)
